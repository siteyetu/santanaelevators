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


class HomePageAPI(MethodView): 

    #get token from params
    #decrypt body and get message
    #verify signed text with body
    
#    decorators = [auth_required]


    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()

    


    # HOMEPAGE USER
    def get(self):
    	homedict = {}
    	homedict ["title"] = "Santana Elevators"
    	homedict ["titleshortdesc"] = "We install, upgrade, maintain and provide latest elvator products"
    	homedict ["titlelongdesc"] = "Spannning East Africa currently expandibg regionally into the continent, our global standard is shown in our client diversity and most of all quality of our work"
    	homedict ["menu1"] = "Projects"
    	homedict ["menu2"] = "Ecommerce"
    	homedict ["menu3"] = "Blog"
    	homedict ["search"] = "Search"
    	homedict ["searchtext"] = "What are you lookinng for?"
    	homedict ["intro"] = "We're Santana Elevators"
    	homedict ["introfollow"] = "We got much in store for you"
    	homedict ["newslettertext"] = "Get the email newsletter and unlock access to members-only content and updates "
    	homedict ["projectcardsintro"] = "Catch up with our"
    	homedict ["projectcardsintrofollow"] = "latest projects"
    	homedict ["projectcardslist"]  = [{
    	"cardtaglist" : ["office","tower"],
    	"title" : "Jinja Heights Tower Block",
    	"content" : "The 12500sq ft area is served by our escalators and elevators both for client and their clientele's needs",
    	"imagename" : "featured-1.jpg"
    	}]
    	homedict ["ecommercecardsintro"] = "Get latest products"
    	homedict ["ecommercecardsintrofollow"] = "with integrated installation offers"
    	homedict ["ecommercecardslist"] = [{
    	"cardtaglist" : ["motherboards","microcontrollers","cpu"],
    	"title" : "Raspberry Microcontroller Motherboard",
    	"content" : "This nnew generation motherbaord allows for compact installations with ease inn data processing, upgrade management to smart software technologies",
    	"imagename" : "recent-1.jpg"
    	}]
    	homedict ["footer"] = "message"
        
    	homedict ["footer"]={"message": "Elevators, Escalators, Microprocessors l... you name it"}
    	homedict ["blogsintro"] = "Recommeded Tips"
    	homedict ["blogsintrofollow"] = " and News Pieces"
    	homedict ["blogslist"] = [{
    	"title" : "OSTEC unveil new PID with 2x processing times",
    	"imagename" : "recommended-1.jpg"
    	}]
    	homedict["madeby"]={"intro":"Made by ","name":"Neutrino Developers"}
    	return render_template("home/index.html", homedict=homedict)
        

#    def post(self):
        #homepage params
 #       pass
