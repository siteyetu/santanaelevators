from flask import Blueprint
from .api import  *


ecommerce_app = Blueprint("ecommerce_app", __name__)


shoppage_view = ShopPageAPI.as_view('shoppage_api')

ecommerce_app.add_url_rule('/shop', 
	view_func=shoppage_view, 
	methods=['POST','GET'])



productpage_view = ProductPageAPI.as_view('shoppage_api')

ecommerce_app.add_url_rule('/shop/product/<productId>', 
	view_func=shoppage_view, 
	methods=['POST','GET'])\



shoppingcartpage_view = ShoppingCartPageAPI.as_view('shoppingcartpage_api')

ecommerce_app.add_url_rule('/shoppingcart', 
	view_func=shoppingcartpage_view, 
	methods=['POST','GET'])



checkoutpage_view = CheckoutPageAPI.as_view('checkoutpage_api')

ecommerce_app.add_url_rule('/checkout', 
	view_func=checkoutpage_view, 
	methods=['POST','GET'])



invoicepage_view = InvoicePageAPI.as_view('invoicepage_api')

ecommerce_app.add_url_rule('/invoice', 
	view_func=invoicepage_view, 
	methods=['POST','GET'])