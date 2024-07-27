from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory, make_response

#from .models import *
import uuid, json, importlib
import json, time
import requests


from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory, make_response

#from .models import *
import uuid, json, importlib
import json, time
import requests

# response = requests.get(...)
# dictionary = json.loads(response.text)


# # Serializing json  
# json_object = json.dumps(dictionary)


#Time GMT +3
nowtime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()+10800))))


class ShopPageAPI(MethodView): 

    #get token from params
    #decrypt body and get message
    #verify signed text with body
    
#    decorators = [auth_required]

    


    # ALL PRODUCTS WITH FILTER
    def get(self):
        return render_template("ecommerce/shop.html")



class WishListPageAPI(MethodView): 
    
#    decorators = [auth_required]


    # USER PRODUCT WISHLIST RETRIEVAL
    def get(self, productid):
        return render_template("ecommerce/wishlist.html")


    # USER PRODUCT WISHLIST ADDITION
    def post(self, productid):
        return render_template("ecommerce/wishlist.html")



class ProductPageAPI(MethodView): 
    
#    decorators = [auth_required]


    # SINGLE PRODUCTS WITH GALLERY SLIDE, DESCRIPTION, WISHLIST
    def get(self):
        return render_template("ecommerce/product.html")






class ShoppingCartPageAPI(MethodView): 
    
#    decorators = [auth_required]


    # ShOPPING CART RETRIEVAL WHERE STATUS IS ALL OR CARTID
    def get(self, productid, status):
        return render_template("ecommerce/shoppingcart.html")

    # SHOPPING CART PRODUCT ADDITION OR REMOVAL OR SAVING
    def post(self,productid, status):
    	...



class CheckoutPageAPI(MethodView): 
    
#    decorators = [auth_required]

    # CART RETRIVAL FOR ADDRESS ADDITION
    def get(self, cartid):
        return render_template("ecommerce/checkout.html")

    # ADDRESS ADDITION AND PROCEEDING TO FULL INVOICE




class InvoicePageAPI(MethodView): 
    
#    decorators = [auth_required]

    # PAGE FOR TOTAL ITEMS AND PAYMENT METHOD SELECTION
    def get(self):
        return render_template("ecommerce/invoice.html")


     # PAYMENT METHOD OUTBOUND REQUEST WITH INVOICE ID, AMOUNT, PAYMENT TYPE, PAYER, PAYEE AND REF CODE 


