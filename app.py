from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for Expenses
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'description': self.description
        }

with app.app_context():
    db.create_all()


# GET /expenses - Get all expenses, with optional filter by category
@app.route('/expenses', methods=['GET'])
def get_expenses():
    category = request.args.get('filter')
    if category:
        expenses = Expense.query.filter_by(category=category).all()
    else:
        expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses])


# POST /expenses - Add a new expense
@app.route('/expenses', methods=['POST'])
def add_expense():
    if not request.json or 'amount' not in request.json or 'category' not in request.json:
        abort(400)

    new_expense = Expense(
        amount=request.json['amount'],
        category=request.json['category'],
        description=request.json.get('description', '')
    )
    db.session.add(new_expense)
    db.session.commit()

    return jsonify(new_expense.to_dict()), 201


# PUT /expenses/<id> - Update an existing expense
@app.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    expense = Expense.query.get_or_404(id)

    if not request.json:
        abort(400)

    expense.amount = request.json.get('amount', expense.amount)
    expense.category = request.json.get('category', expense.category)
    expense.description = request.json.get('description', expense.description)

    db.session.commit()
    return jsonify(expense.to_dict())


@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': f'The expense was deleted.'}), 200


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
