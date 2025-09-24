# Vibeosys Product API

A standalone FastAPI application for managing products with MySQL as the backend.  

---

## Features

- List products with pagination (10 per page)  
- Get product information by ID  
- Add new products  
- Update existing products  
- SQLAlchemy ORM with Pydantic validation  

---

## Project Structure



---

## Prerequisites

- Python 3.11+  
- MySQL Server  
- Git (optional)  

---

## Setup Instructions

1. **Clone the repository**  
```bash
git clone <https://github.com/Yashtapkir2913/vibeosys-assignment.git>
cd vibeosys-assignment

python3 -m venv venv
venv\Scripts\activate        

pip install -r requirements.txt

DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
DB_NAME=vibeosys

CREATE DATABASE vibeosys;

uvicorn main:app --reload

