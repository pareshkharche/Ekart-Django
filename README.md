# Ecommerce application
eKart is an e-commerce web application built using Python, Django, and Django Rest Framework. It features a modern, responsive design using HTML, CSS, and Bootstrap 5. The application includes user authentication with email confirmation and password reset functionalities, as well as payment integration via PayPal.

# Features
 User Authentication: Secure user registration, login, and logout.
 
 Email Confirmation: Users must confirm their email addresses to activate their accounts.
 
 Password Reset: Users can reset their passwords via email.
 
 Product Management: Admin can add, edit, and delete products.
 
 Shopping Cart: Users can add products to their cart and proceed to checkout.
 
 Payment Integration: Secure payment processing using PayPal.
 
 Responsive Design: Mobile-friendly layout using Bootstrap 5.
 
 RESTful API: Backend API built using Django Rest Framework for handling data operations.
 

Installation
Clone the repository

git clone https://github.com/yourusername/ekart.git

cd ekart

Create and activate a virtual environment


python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies


pip install -r requirements.txt

Apply migrations

python manage.py migrate

Run the development server


python manage.py runserver

Configuration

Email Settings: Update your email settings in settings.py for sending confirmation and reset emails.


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'your_email_host'

EMAIL_PORT = your_email_port

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your_email'

EMAIL_HOST_PASSWORD = 'your_email_password'

PayPal Settings: Update your PayPal settings in settings.py for payment processing.


PAYPAL_CLIENT_ID = 'your_paypal_client_id'

PAYPAL_CLIENT_SECRET = 'your_paypal_client_secret'

# Usage
Register and Confirm Email: Register a new user account and confirm your email address.

Browse Products: Browse the available products.

Add to Cart: Add desired products to your shopping cart.

Checkout: Proceed to checkout and pay using PayPal.

Reset Password: If needed, reset your password using the password reset feature.

# Screenshots
![1](https://github.com/pareshkharche/Ekart-Django/assets/80632983/edbc80f5-bdd6-4d3f-b33b-949ca8594486)
![2](https://github.com/pareshkharche/Ekart-Django/assets/80632983/add065a2-d72a-48bf-b2fe-e5b4d65bfb06)
![3](https://github.com/pareshkharche/Ekart-Django/assets/80632983/e96cb74e-1383-4262-91d3-ef676b6a2ea1)
![4](https://github.com/pareshkharche/Ekart-Django/assets/80632983/ba336dbb-88ea-4097-883c-923995ac4ed8)
![5](https://github.com/pareshkharche/Ekart-Django/assets/80632983/fb2832ac-5fec-43fa-be63-6f7f93bf6e69)
![Screenshot (2414)](https://github.com/pareshkharche/Ekart-Django/assets/80632983/2bce77a0-60c1-4cf3-ab58-0bcb4e68b0ca)
![Screenshot (2410)](https://github.com/pareshkharche/Ekart-Django/assets/80632983/88018f0c-5645-4b10-8648-987c10a34d65)
![6](https://github.com/pareshkharche/Ekart-Django/assets/80632983/b663b2e5-c750-4c4c-a607-83f03efc0ff3)
![7](https://github.com/pareshkharche/Ekart-Django/assets/80632983/4a192324-7b98-4cc5-8ef8-14d4b2bc68f8)
![8](https://github.com/pareshkharche/Ekart-Django/assets/80632983/c9f577c6-0a3e-4cc2-95a1-a73caa8ea35e)
![9](https://github.com/pareshkharche/Ekart-Django/assets/80632983/883c4352-4a8d-4452-88a0-5dd0f048a5b2)
![10](https://github.com/pareshkharche/Ekart-Django/assets/80632983/81456dfb-3f4a-4c31-bc2e-0cc0f45c8227)
