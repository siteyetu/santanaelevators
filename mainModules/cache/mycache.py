from flask import Flask, session, request, jsonify
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set up the cache
cache = SimpleCache()


user_id = session.get('user_id', None)


# Add the product to the user's cart in the cache
cart = cache.get(f'cart_{user_id}') or {}
cart[product_id] = cart.get(produc-t_id, 0) + 1
cache.set(f'cart_{user_id}', cart)



# Retrieve the user's cart from the cache
cart = cache.get(f'cart_{user_id}') or {}


# Remove the product from the user's cart in the cache
cart = cache.get(f'cart_{user_id}') or {}
if product_id in cart:
    del cart[product_id]
    cache.set(f'cart_{user_id}', cart)
