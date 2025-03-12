# 🛒 E-Cart - Django E-Commerce Website

E-Cart is a feature-rich e-commerce web application built using Django. It provides a seamless shopping experience with user authentication, product management, cart functionality, and payment integration.

## 🚀 Features
- 🛍️ User authentication (Signup, Login, Logout)
- 📦 Product listing & detailed product pages
- 🛒 Add to cart & manage cart items
- 💳 Secure payment integration (Razorpay/PayPal/Stripe)
- 📜 Order history & invoice generation
- 🔍 Product search & filtering
- 🌟 User-friendly UI with responsive design

## 🏗️ Tech Stack
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL / PostgreSQL / SQLite
- **Payment Gateway:** Razorpay / PayPal / Stripe

## 🎯 Installation Guide
### Step 1: Clone the Repository
git clone https://github.com/yourusername/e-cart.git
cd e-cart

### Step 2: Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Configure Database
Update settings.py with database credentials.
Run migrations:
python manage.py migrate

### Step 5: Create Superuser (Admin Panel)
python manage.py createsuperuser

### Step 6: Run the Server
python manage.py runserver
Visit: http://127.0.0.1:8000
