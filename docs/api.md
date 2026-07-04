
# 📁 Project Structure

This structure follows a common organization for **FastAPI** applications, making the project easier to maintain, scale, and understand.

---

# 📂 Folder and File Responsibilities

| Folder/File     | Responsibility                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| **main.py**     | Entry point of the application. Initializes the FastAPI app, registers routers, and starts the server. |
| **routers/**    | Defines API endpoints and organizes routes by feature or resource.                                     |
| **models.py**   | Contains SQLAlchemy models that represent the database tables.                                         |
| **schemas.py**  | Defines Pydantic models used for request validation and API responses.                                 |
| **crud.py**     | Implements database operations such as Create, Read, Update, and Delete.                               |
| **database.py** | Configures the database connection, engine, and session management.                                    |
| **auth.py**     | Handles authentication, authorization, JWT tokens, and password hashing.                               |
| **templates/**  | Stores HTML templates rendered by Jinja2.                                                              |
| **static/**     | Contains static assets such as CSS, JavaScript, images, and fonts.                                     |
| **utils/**      | Stores reusable helper functions, utilities, and common logic shared across the project.               |
| **tests/**      | Contains automated tests for the application.                                                          |

---

# 🚀 Recommended Development Order

Follow this order to build the project incrementally.

* [ ] Create the project structure
* [ ] Configure the virtual environment
* [ ] Install dependencies
* [ ] Configure the database connection (`database.py`)
* [ ] Create the database models (`models.py`)
* [ ] Create the Pydantic schemas (`schemas.py`)
* [ ] Implement CRUD operations (`crud.py`)
* [ ] Build the API routes (`routers/`)
* [ ] Implement authentication (`auth.py`)
* [ ] Create the HTML templates (`templates/`)
* [ ] Add CSS, JavaScript, and images (`static/`)
* [ ] Write automated tests (`tests/`)
* [ ] Refactor and improve the code
* [ ] Update the documentation (`README.md`)
* [ ] Deploy the application
