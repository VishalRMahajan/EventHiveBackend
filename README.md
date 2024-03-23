
# EventHive Backend

EventHive Backend is the backend repository for [EventHive](https://github.com/VishalRMahajan/EventHive), a Python-native college event ticket booking and verification website. This repository contains the backend code, which is built using the FastAPI Python framework. FastAPI is used to create APIs for handling various backend functionalities, including user authentication, event management, ticketing, and more. The backend integrates with the PostgreSQL database for data storage, providing a robust and efficient solution for managing events and tickets.
## Project Structure

```bash
├── README.md
├── main.py              
├── cloudinary_setup.py  (This is to Setup Cloudinary)
├── requirements.txt
├── models
│   ├── __init__.py
│   ├── database.py      (Py scripts to create database/engine)            
│   └── models.py        (Models of all tables using sqlalchemy)
│
├── routes
│   ├── auth.py          ( /auth["/register,/login,/protected"] endpoint)
│   ├── fest.py          ( /fest["/add,/fetch,/all,/ticketprice"] endpoint)
│   └── profile.py       ( /profile["/me,/update,/getall"] endpoint)
│
└── templates
    └── pay.html         (Razorpay HTML file)
```



## API Reference

For detailed information about the API endpoints and usage, refer to the [API Reference](./API_REFERENCE.md) file.

## Run Locally

Clone the project

```bash
  git clone https://github.com/VishalRMahajan/EventHiveBackend
```

Go to the project directory

```bash
  cd EventHiveBackend
```

Install all the required Python packages for this project, run the following command:

```bash
   pip install -r requirements.txt
```

Run the following command to run the backend server:
```bash
  uvicorn main:app --reload --port [your_desired_port]

```






## Disclaimer

**Important:** Do not use ports 3000 or 8000  to run the FastAPI backend, as Reflex is already using these ports. Using these ports for FastAPI may result in conflicts and errors.
## Docs

For any queries, Refer following Docs:
- [FastAPI Docs](https://fastapi.tiangolo.com/)
