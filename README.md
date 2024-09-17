
# Expense Tracker API

A simple RESTful API for tracking expenses. This API allows you to manage your expenses with CRUD operations and filter by category.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete expenses.
- **Filtering**: Filter expenses by category using query parameters.

## Installation

1. **Clone the Repository**


2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the Database**

   Run the application to create the SQLite database and tables:

   ```bash
   python app.py
   ```

   After running the script, you can stop the server.

## Usage

### Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will run at `http://127.0.0.1:5000/`.

### Endpoints

#### `GET /expenses`

Retrieve all expenses. Optionally, filter by category with the `?filter=` query parameter.

**Example Request:**

```bash
curl http://127.0.0.1:5000/expenses?filter=food
```

**Response:**

```json
[
    {
        "id": 1,
        "amount": 100.0,
        "category": "food",
        "description": "Grocery shopping"
    }
]
```

#### `POST /expenses`

Add a new expense.

**Example Request:**

```bash
curl -X POST http://127.0.0.1:5000/expenses -H "Content-Type: application/json" -d '{"amount": 50.0, "category": "transport", "description": "Bus fare"}'
```

**Response:**

```json
{
    "id": 2,
    "amount": 50.0,
    "category": "transport",
    "description": "Bus fare"
}
```

#### `PUT /expenses/<id>`

Update an existing expense by ID.

**Example Request:**

```bash
curl -X PUT http://127.0.0.1:5000/expenses/1 -H "Content-Type: application/json" -d '{"amount": 120.0, "description": "Updated description"}'
```

**Response:**

```json
{
    "id": 1,
    "amount": 120.0,
    "category": "food",
    "description": "Updated description"
}
```

#### `DELETE /expenses/<id>`

Delete an expense by ID.

**Example Request:**

```bash
curl -X DELETE http://127.0.0.1:5000/expenses/1
```

**Response:**

```json
{
    "message": "Expense deleted successfully"
}
```

### Running Tests

To run tests (if you add any), make sure to use a separate test database or configuration.

## Contributing

Feel free to fork the repository and submit pull requests. If you have any suggestions or improvements, open an issue or contribute directly.
