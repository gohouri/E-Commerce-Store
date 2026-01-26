# Overview

As a software engineer seeking to expand my web development skills, I built this E-Commerce Store web application to understand how dynamic web frameworks process requests, interact with databases, and generate HTML content on the server side. This project allowed me to explore the Model-View-Template (MVT) architecture pattern and learn how to create interactive, data-driven web applications.

This web app is a fully functional e-commerce store built with Django. It features product browsing, searching, filtering, a shopping cart system, and a checkout process. All content is dynamically generated based on database records and user interactions.

To run the application:
1. Open a terminal in the project directory
2. Run `python manage.py runserver`
3. Open your browser and navigate to `http://127.0.0.1:8000/`

My purpose for creating this software was to gain hands-on experience with server-side web development, understand how frameworks like Django handle HTTP requests and responses, and learn how to integrate a database into a web application for persistent data storage.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

**Home Page (`/`)**: The main landing page displays all products in a responsive grid layout. Users can search for products by name or description using the search bar, filter products by category using a dropdown menu, and filter by price range. The product cards, search results, and filter options are all dynamically generated from the database. Clicking on a product navigates to its detail page, and clicking "Add to Cart" adds the item to the shopping cart.

**Product Detail Page (`/product/<id>/`)**: This page shows comprehensive information about a single product including its image, name, description, price, stock availability, and category. Related products from the same category are dynamically displayed at the bottom. Users can add the product to their cart or navigate back to the home page. The entire page content is generated based on the product ID in the URL.

**Shopping Cart Page (`/cart/`)**: Displays all items the user has added to their cart. Each cart item shows the product image, name, price, quantity selector, and subtotal. Users can update quantities or remove items, with the cart total recalculating dynamically. The page transitions to checkout when the user clicks "Proceed to Checkout" or back to shopping via the "Continue Shopping" button.

**Checkout Page (`/checkout/`)**: Presents a form for users to enter their contact, shipping, and payment information. An order summary sidebar displays all cart items and the total cost. Upon form submission, the cart is cleared and the user receives a confirmation message before being redirected to the home page.

# Development Environment

**Tools Used:**
- Visual Studio Code as the code editor
- Git for version control
- Django development server for local testing
- SQLite Browser (optional) for database inspection

**Programming Language and Libraries:**
- Python 3.x
- Django 6.0 - Web framework providing URL routing, template rendering, ORM, and admin interface
- SQLite - Built-in database for storing products, categories, and cart items

# Useful Websites

* [Django Official Documentation](https://docs.djangoproject.com/)
* [Django Tutorial - Writing Your First Django App](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
* [W3Schools Django Tutorial](https://www.w3schools.com/django/)
* [MDN Web Docs - Django Introduction](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
* [Real Python - Django Tutorials](https://realpython.com/tutorials/django/)

# Future Work

* Add user authentication and registration system for personalized shopping experiences
* Implement order history so users can track their past purchases
* Add product reviews and ratings functionality
* Integrate a real payment gateway (Stripe or PayPal) for secure transactions
* Add product image upload capability instead of using URLs
* Implement inventory management to automatically update stock after purchases
* Add email notifications for order confirmations
* Create an admin dashboard with sales analytics and reports
