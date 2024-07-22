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
        homedict["projectcardslist"] = [{"cardtaglist":["residential","apartments"],"title":"Vraj Builders Limited","content":"Residential Apartments with 11 storeys in suburb area.","imagename":"featured-1.jpg"},{"cardtaglist":["installation","power plant"],"title":"KenGen Gitaru Plant","content":"Lead technician working with Neputech Ltd on installion of 145 metres underground elevator to the turbines.","imagename":"featured-2.jpg"},{"cardtaglist":["commercial","hotel"],"title":"Premier West Hotel","content":"Commercial residence with 2 unit 8 stops elevators.","imagename":"featured-3.jpg"},{"cardtaglist":["commercial","office"],"title":"Sanlam Towers","content":"Commercial space with 18 storeys.","imagename":"featured-4.jpg"},{"cardtaglist":["residential","mixed"],"title":"Cytonn Ruaka","content":"Mixed residence with 477 housing units","imagename":"featured-5.jpg"},{"cardtaglist":["residential","home"],"title":"Residential Home","content":"Residence with 3 stops elevators.","imagename":"featured-6.jpg"},{"cardtaglist":["commercial","education"],"title":"Kenyatta University Kisumu Campus","content":"Commercial residence with 9 stop.","imagename":"featured-7.jpg"}]  
        homedict ["ecommercecardsintro"] = "Get latest products"
        homedict ["ecommercecardsintrofollow"] = "with integrated installation offers"
        homedict["ecommercecardslist"] = [{"cardtaglist": ["motherboards", "microcontrollers", "cpu"], "title": "Raspberry Microcontroller Motherboard", "content": "This new generation motherboard allows for compact installations with ease in data processing, upgrade management to smart software technologies", "imagename": "recent-1.jpg"}, {"cardtaglist": ["elevators", "escalators", "installation"], "title": "Otis Elevators and Escalators", "content": "Otis offers a wide range of elevator and escalator solutions for residential, commercial, and industrial applications with seamless installation services.", "imagename": "recent-2.jpg"}, {"cardtaglist": ["building automation", "sensors", "control systems"], "title": "Honeywell Building Automation", "content": "Honeywell's advanced building automation systems provide intelligent control and monitoring of HVAC, lighting, and security systems for optimal energy efficiency and occupant comfort.", "imagename": "recent-3.jpg"}, {"cardtaglist": ["access control", "security", "smart locks"], "title": "SALTO Smart Access Control", "content": "SALTO's innovative access control solutions enable secure and convenient management of building entry points with keyless and mobile-based access options.", "imagename": "recent-4.jpg"}, {"cardtaglist": ["fire protection", "fire alarms", "sprinklers"], "title": "Tyco Fire Protection Products", "content": "Tyco offers a comprehensive range of fire detection, suppression, and alarm systems to ensure the safety and compliance of commercial and industrial facilities.", "imagename": "recent-5.jpg"}, {"cardtaglist": ["lighting", "smart home", "automation"], "title": "Philips Hue Smart Lighting", "content": "Philips Hue offers a wide range of connected lighting solutions that allow for intelligent control and automation of indoor and outdoor lighting for homes and businesses.", "imagename": "recent-6.jpg"}, {"cardtaglist": ["hvac", "thermostats", "energy efficiency"], "title": "Nest Thermostat", "content": "The Nest Thermostat is a smart, learning thermostat that helps you save energy and maintain optimal comfort in your home or office by intelligently adjusting temperature settings.", "imagename": "recent-7.jpg"}, {"cardtaglist": ["security cameras", "surveillance", "smart home"], "title": "Arlo Pro Security Cameras", "content": "Arlo Pro offers a versatile range of wireless, weatherproof security cameras that provide reliable home and business monitoring with advanced features like motion detection and cloud storage.", "imagename": "recent-8.jpg"}, {"cardtaglist": ["smart plugs", "energy monitoring", "automation"], "title": "Kasa Smart Plugs", "content": "Kasa Smart Plugs enable you to control and monitor your home or office appliances remotely, as well as set schedules and timers for improved energy efficiency and convenience.", "imagename": "recent-9.jpg"}, {"cardtaglist": ["smart speakers", "voice assistants", "home automation"], "title": "Amazon Echo Dot", "content": "The Amazon Echo Dot is a compact and affordable smart speaker that allows you to voice control your smart home devices, play music, get information, and more using Alexa voice commands.", "imagename": "recent-10.jpg"}]
        homedict ["footer"] = "message"
        homedict ["footer"]={"message": "Elevators, Escalators, Microprocessors l... you name it"}
        homedict ["blogsintro"] = "Recommeded Tips"
        homedict ["blogsintrofollow"] = " and News Pieces"
        homedict ["blogslist"] = [{"title": "OSTEC unveil new PID with 2x processing times", "imagename": "recommended-1.jpg"}, {"title": "New Quantum Computer Reaches 1000 Qubits", "imagename": "recommended-2.jpg"}, {"title": "Climate Change Report Warns of Dire Consequences", "imagename": "recommended-3.jpg"}, {"title": "Breakthrough in Fusion Energy Research", "imagename": "recommended-4.jpg"}, {"title": "AI Assistants Gain Emotional Intelligence", "imagename": "recommended-5.jpg"}, {"title": "Augmented Reality Revolutionizes Gaming", "imagename": "recommended-6.jpg"}, {"title": "Personalized Medicine Advances with Genomic Sequencing", "imagename": "recommended-7.jpg"}, {"title": "Quantum Cryptography Ensures Unbreakable Data Security", "imagename": "recommended-8.jpg"}, {"title": "Sustainable Cities Emerge with Smart Urban Planning", "imagename": "recommended-9.jpg"}, {"title": "Robotic Exoskeletons Enhance Human Capabilities", "imagename": "recommended-10.jpg"}, {"title": "Advancements in Renewable Energy Storage", "imagename": "recommended-11.jpg"}, {"title": "Brain-Computer Interfaces Revolutionize Assistive Tech", "imagename": "recommended-12.jpg"}, {"title": "Breakthrough in Graphene-Based Electronics", "imagename": "recommended-13.jpg"}, {"title": "Sustainable Aviation Fuels Reduce Carbon Footprint", "imagename": "recommended-14.jpg"}, {"title": "Quantum Sensing Enables Revolutionary Measurements", "imagename": "recommended-15.jpg"}, {"title": "Advances in Gene Editing and Personalized Medicine", "imagename": "recommended-16.jpg"}, {"title": "Autonomous Vehicles Reshape Urban Transportation", "imagename": "recommended-17.jpg"}, {"title": "Blockchain Technology Transforms Financial Services", "imagename": "recommended-18.jpg"}, {"title": "Advancements in Wearable Technology and IoT", "imagename": "recommended-19.jpg"}, {"title": "Breakthroughs in Quantum Computing and Algorithms", "imagename": "recommended-20.jpg"}]
        homedict["madeby"] = { "intro" : "Neutrino Developers 2024 courtesy", "name" : " Biokraft Systems Limited"}
        return render_template("home/index.html", homedict=homedict)
        

#    def post(self):
        #homepage params
 #       pass
