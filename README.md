# Azure Flask-style API — Hire Ziyaan Osman

This project is a **Python Azure Function** that simulates a mini Flask-style API using HTTP triggers. It returns a custom message when accessed through a web browser or a POST request.

## 🚀 What It Does

When deployed, this function listens for HTTP requests and responds with:

> "You should hire Ziyaan Osman, you won't regret it."

This is an example of using **Azure Functions** for serverless app development — great for lightweight, scalable APIs.

---

## 🛠️ Tech Stack

- Azure Functions (Python runtime)
- HTTP Trigger binding
- Azure Functions Core Tools (for local development)
- Python 3.10+

---

## 📂 Project Structure
azure-flask-api/
│
├── FlaskAPI/
│ ├── init.py # Contains the main function logic
│ └── function.json # Defines HTTP trigger route
│
├── host.json # Azure host config
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # (optional)


---

## 🧪 How to Run Locally

1. Install Azure Functions Core Tools:
   ```bash
   npm install -g azure-functions-core-tools@4 --unsafe-perm true
2. Start the local server:

   func start

3. Test it in browser or with curl:

   http://localhost:7071/api/FlaskAPI?name=Ziyaan

