# 🌎 Currency Converter API

REST API for currency conversion, built using FastAPI, integrating an external service for updated exchange rates.

---

## 📖 Project Overview

The **Currency Converter API** project was developed to allow fast and easy value conversion between different currencies, ensuring the persistence of all completed transactions.

### 🎯 Purpose
- Perform currency conversions using updated rates.
- Record a history of user transactions.
- Provide endpoints to query past transactions.

### ✨ Features
- Integration with external exchange rate API ([exchangeratesapi.io](https://exchangeratesapi.io/)).
- Persistence of all transactions in a database.
- Endpoints for conversion and transaction listing.
- Mandatory validation to ensure **EUR** is one of the currencies.
- Automated unit and integration tests.
- CI/CD configured with GitHub Actions.

---

## 🛠️ How to Run the Application Locally

### 1. Clone the repository
```bash
git https://github.com/marcosbertolline/currency-converter.git
cd your-repository
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn app.main:app --reload
```

Access the interactive documentation at:
```
http://localhost:8000/docs
```

---

## 🌐 Online Deployment

The project is hosted on **Render**.

Access the API at:
```
https://currency-converter-api-a1y3.onrender.com
```

Interactive Swagger documentation:
```
https://currency-converter-api-a1y3.onrender.com/docs
```