Here is a **clean, professional, GitHub-ready README documentation** for your API — tailored for your ALX capstone and everything you’ve implemented so far.

You can copy-paste this directly into:

```
README.md
```

---

# 🚚 Dispatch Delivery Matching API

A backend REST API that connects sellers (senders) with dispatch riders for last-mile delivery. Built with Django and Django REST Framework, this system allows senders to create delivery requests and riders to accept and complete them.

---

## 📌 Features

### 🔐 Authentication & Authorization

* JWT authentication (register, login, token refresh)
* Custom user model
* Role-based access control (Sender / Rider)
* Protected endpoints

---

### 👤 Sender Capabilities

* Create delivery requests
* View own deliveries
* View delivery details
* Cancel pending deliveries

---

### 🚴 Rider Capabilities

* View available deliveries
* Accept deliveries
* View assigned deliveries
* Update delivery status
* Toggle availability status

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* SimpleJWT (JWT Authentication)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Server

```bash
python manage.py runserver
```

API Base URL:

```
http://127.0.0.1:8000/api/
```

---

## 🔐 Authentication Endpoints

### Register User

```
POST /api/auth/register/
```

Body:

```json
{
  "name": "Victor",
  "email": "victor@example.com",
  "password": "StrongPass123",
  "role": "sender"
}
```

---

### Login User

```
POST /api/auth/login/
```

Response:

```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

---

### Refresh Token

```
POST /api/auth/token/refresh/
```

Body:

```json
{
  "refresh": "your_refresh_token"
}
```

---

### Get Current User

```
GET /api/auth/me/
Authorization: Bearer <access_token>
```

---

## 📦 Sender Endpoints

### Create Delivery

```
POST /api/deliveries/
Authorization: Bearer <sender_token>
```

Body:

```json
{
  "pickup_address": "Ikeja",
  "delivery_address": "Lekki",
  "package_description": "Electronics",
  "receiver_name": "John Doe",
  "receiver_phone": "08012345678",
  "delivery_fee": 3000
}
```

---

### View My Deliveries

```
GET /api/deliveries/my/
Authorization: Bearer <sender_token>
```

---

### View Delivery Details

```
GET /api/deliveries/{id}/
Authorization: Bearer <sender_token>
```

---

### Cancel Delivery

```
DELETE /api/deliveries/{id}/cancel/
Authorization: Bearer <sender_token>
```

Only pending deliveries can be cancelled.

---

## 🚴 Rider Endpoints

### View Available Deliveries

```
GET /api/deliveries/available/
Authorization: Bearer <rider_token>
```

Shows deliveries not yet accepted.

---

### Accept Delivery

```
POST /api/deliveries/{id}/accept/
Authorization: Bearer <rider_token>
```

Assigns rider to delivery.

---

### View My Assigned Deliveries

```
GET /api/deliveries/rider/my-deliveries/
Authorization: Bearer <rider_token>
```

---

### Update Delivery Status

```
PATCH /api/deliveries/{id}/status/
Authorization: Bearer <rider_token>
```

Body:

```json
{
  "status": "picked_up"
}
```

Allowed statuses:

* picked_up
* delivered

---

### Update Rider Availability

```
PATCH /api/deliveries/rider/availability/
Authorization: Bearer <rider_token>
```

Body:

```json
{
  "availability_status": "available"
}
```

Available values:

* available
* busy
* offline

---

## 📦 Delivery Status Flow

```
pending → accepted → picked_up → delivered
           ↘ cancelled
```

---

## 🔐 Authentication Header Format

All protected endpoints require:

```
Authorization: Bearer <access_token>
```

---

## ❌ Error Responses

Typical HTTP status codes:

| Code | Meaning                        |
| ---- | ------------------------------ |
| 400  | Bad request / validation error |
| 401  | Unauthorized                   |
| 403  | Forbidden (wrong role)         |
| 404  | Resource not found             |

---

## 🧪 Testing

You can test the API using:

* Postman
* Insomnia
* cURL
* Swagger (if enabled)

---

## 🚀 Future Improvements

* Location-based rider matching
* Real-time tracking
* Rating system
* Push notifications
* Payment integration
* Admin dashboard

---

## 👨‍💻 Author

ALX Capstone Project — Dispatch Delivery Matching System

