

# 🚀 Crypto API – Vetty Backend Assignment

A modular Flask backend application integrating with the CoinGecko API to fetch cryptocurrency data.  
Includes JWT authentication, pagination, meta endpoints, service-layer architecture, and unit tests.

---

## 📂 Project Structure

```

crypto-api/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── **init**.py
│
├── routes/
│   ├── routes_coins.py
│   ├── routes_meta.py
│   ├── auth.py
│   └── **init**.py
│
├── services/
│   └── coingecko_client.py
│
└── tests/
├── test_routes.py
├── test_security.py
└── **init**.py

```

---

## 🔧 Tech Stack

- Python 3  
- Flask  
- PyJWT  
- Requests  
- unittest (Flask Test Client)

---

## 🚀 How to Run the Project

### 1️⃣ Create Virtual Environment
```

python -m venv venv

```

Activate:

Windows:
```

.\venv\Scripts\activate

```

Mac/Linux:
```

source venv/bin/activate

```

---

### 2️⃣ Install Dependencies
```

pip install -r requirements.txt

```

---

### 3️⃣ Run App
```

python app.py

```

App runs at:
```

[http://127.0.0.1:5000](http://127.0.0.1:5000)

```

---

## 🔐 JWT Authentication

### Get Token
```

GET /token

````

Response:
```json
{
  "token": "your_jwt_token_here"
}
````

Use this token with:

Postman → Authorization → Bearer Token

---

## 📘 API Endpoints

### 🔹 Health Check

```
GET /meta/health
```

### 🔹 API Version

```
GET /meta/version
```

### 🔹 List Coins (Protected)

```
GET /coins?page_num=1&per_page=10
```

### 🔹 Get Coin by ID

```
GET /coins/<coin_id>
```

Example:

```
GET /coins/bitcoin
```

---

## 🧪 Running Tests

```
python -m unittest discover -s tests
```

Covers:

* JWT token generation
* Invalid/missing token cases
* Route response validation

---



## 📄 Author

**Abhishek Kumar**
Vetty Backend Assignment – 2025




