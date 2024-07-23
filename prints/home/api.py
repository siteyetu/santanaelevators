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
        homedict ["titlelongdesc"] = "Spannning East Africa currently expanding regionally into the continent, our global standard is shown in our client diversity and most of all quality of our work"
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
        homedict["projectcardslist"] = [{"cardtaglist":["residential","apartments"],"title":"Vraj Builders Limited","content":"Residential Apartments with 11 storeys in suburb area.","imagename":"vraj.png"},{"cardtaglist":["installation","power plant"],"title":"KenGen Gitaru Plant","content":"Lead technician working with Neputech Ltd on installion of 145 metres underground elevator to the turbines.","imagename":"kengen.png"},{"cardtaglist":["commercial","hotel"],"title":"Premier West Hotel","content":"Commercial residence with 2 unit 8 stops elevators.","imagename":"premierwest.png"},{"cardtaglist":["commercial","office"],"title":"Sanlam Towers","content":"Commercial space with 18 storeys.","imagename":"sanlamTowers.jpg"},{"cardtaglist":["residential","mixed"],"title":"Cytonn Ruaka","content":"Mixed residence with 477 housing units","imagename":"cytonnRuaka.jpeg"},{"cardtaglist":["residential","home"],"title":"Residential Home","content":"Residence with 3 stops elevators.","imagename":"residential.png"},{"cardtaglist":["commercial","education"],"title":"Kenyatta University Kisumu Campus","content":"Commercial residence with 9 stop.","imagename":"kuKisumu.jpeg"}]  
        homedict ["ecommercecardsintro"] = "Get latest products"
        homedict ["ecommercecardsintrofollow"] = "with integrated installation offers"
        homedict["ecommercecardslist"] = [{"cardtaglist": ["motherboards", "microcontrollers", "cpu"], "title": "Raspberry Microcontroller Motherboard", "content": "This new generation motherboard allows for compact installations with ease in data processing, upgrade management to smart software technologies", "imagename": "raspberry.jpeg"}, {"cardtaglist": ["elevators", "escalators", "installation"], "title": "Otis Elevators and Escalators", "content": "Otis offers a wide range of elevator and escalator solutions for residential, commercial, and industrial applications with seamless installation services.", "imagename": "otis.jpeg"}, {"cardtaglist": ["building automation", "sensors", "control systems"], "title": "Honeywell Building Automation", "content": "Honeywell's advanced building automation systems provide intelligent control and monitoring of HVAC, lighting, and security systems for optimal energy efficiency and occupant comfort.", "imagename": "honeywell.jpeg"}, {"cardtaglist": ["access control", "security", "smart locks"], "title": "SALTO Smart Access Control", "content": "SALTO's innovative access control solutions enable secure and convenient management of building entry points with keyless and mobile-based access options.", "imagename": "salto.jpeg"}, {"cardtaglist": ["fire protection", "fire alarms", "sprinklers"], "title": "Tyco Fire Protection Products", "content": "Tyco offers a comprehensive range of fire detection, suppression, and alarm systems to ensure the safety and compliance of commercial and industrial facilities.", "imagename": "tyco.jpeg"}, {"cardtaglist": ["lighting", "smart home", "automation"], "title": "Philips Hue Smart Lighting", "content": "Philips Hue offers a wide range of connected lighting solutions that allow for intelligent control and automation of indoor and outdoor lighting for homes and businesses.", "imagename": "philips.jpeg"}, {"cardtaglist": ["hvac", "thermostats", "energy efficiency"], "title": "Nest Thermostat", "content": "The Nest Thermostat is a smart, learning thermostat that helps you save energy and maintain optimal comfort in your home or office by intelligently adjusting temperature settings.", "imagename": "nest.jpeg"}, {"cardtaglist": ["security cameras", "surveillance", "smart home"], "title": "Arlo Pro Security Cameras", "content": "Arlo Pro offers a versatile range of wireless, weatherproof security cameras that provide reliable home and business monitoring with advanced features like motion detection and cloud storage.", "imagename": "arlo.jpeg"}, {"cardtaglist": ["smart plugs", "energy monitoring", "automation"], "title": "Kasa Smart Plugs", "content": "Kasa Smart Plugs enable you to control and monitor your home or office appliances remotely, as well as set schedules and timers for improved energy efficiency and convenience.", "imagename": "kasa.jpeg"}, {"cardtaglist": ["smart speakers", "voice assistants", "home automation"], "title": "Amazon Echo Dot", "content": "The Amazon Echo Dot is a compact and affordable smart speaker that allows you to voice control your smart home devices, play music, get information, and more using Alexa voice commands.", "imagename": "echodot.jpeg"}]
        homedict ["footer"] = "message"
        homedict ["footer"]={"message": "Elevators, Escalators, Microprocessors l... you name it"}
        homedict ["blogsintro"] = "Recommeded Tips"
        homedict ["blogsintrofollow"] = " and News Pieces"
        homedict["blogslist"] = [{"cardtaglist": ["elevators", "escalators", "installation"], "title": "Otis Elevators Unveil Next-Gen Intelligent Control Systems", "content": "Otis, the global leader in elevator and escalator solutions, has announced the launch of their latest intelligent control systems that optimize traffic flow, energy efficiency, and passenger experience in high-traffic commercial buildings.", "imagename": "otisNext.jpeg"}, {"cardtaglist": ["elevators", "accessibility", "disability"], "title": "Inclusive Elevator Design: Improving Access for All", "content": "Industry experts explore the latest advancements in elevator design that cater to the needs of passengers with disabilities, ensuring seamless vertical transportation and enhanced accessibility in modern buildings.", "imagename": "elevatorAccess.jpeg"}, {"cardtaglist": ["escalators", "safety", "maintenance"], "title": "Escalator Safety: Best Practices for Proper Maintenance", "content": "A technical review of the critical maintenance procedures and safety protocols that ensure the reliable and risk-free operation of escalators in high-traffic commercial and public settings.", "imagename": "elevatorSafety.jpg"}, {"cardtaglist": ["elevators", "smart technology", "energy efficiency"], "title": "Leveraging Smart Tech for Elevator Energy Savings", "content": "An in-depth analysis of how the integration of smart sensors, control systems, and regenerative braking technologies are driving significant energy efficiency improvements in modern elevator systems.", "imagename": "elevatorEnergy.jpeg"}, {"cardtaglist": ["elevators", "modernization", "retrofit"], "title": "Elevator Modernization: Breathe New Life into Aging Systems", "content": "Industry experts share insights on the benefits and best practices for modernizing older elevator installations, including upgrades to controls, safety features, and passenger experience.", "imagename": "elevatorRevitalize.jpeg"}, {"cardtaglist": ["escalators", "commercial", "airport"], "title": "Escalator Solutions for High-Traffic Commercial Spaces", "content": "A technical review of the specialized escalator systems designed to handle the heavy passenger loads and unique requirements of large-scale commercial facilities such as airports, shopping malls, and transportation hubs.", "imagename": "elevatorTraffic.jpeg"}, {"cardtaglist": ["elevators", "residential", "smart home"], "title": "Elevating the Smart Home: Integrated Elevator Solutions", "content": "An in-depth look at the emerging trend of seamlessly integrating elevators into smart home ecosystems, allowing for voice control, remote monitoring, and enhanced convenience for modern residential buildings.", "imagename": "smartHome.jpeg"}]
        #homedict ["blogslist"] = [{"title": "OSTEC unveil new PID with 2x processing times", "imagename": "recommended-1.jpg"}, {"title": "New Quantum Computer Reaches 1000 Qubits", "imagename": "recommended-2.jpg"}, {"title": "Climate Change Report Warns of Dire Consequences", "imagename": "recommended-3.jpg"}, {"title": "Breakthrough in Fusion Energy Research", "imagename": "recommended-4.jpg"}, {"title": "AI Assistants Gain Emotional Intelligence", "imagename": "recommended-5.jpg"}, {"title": "Augmented Reality Revolutionizes Gaming", "imagename": "recommended-6.jpg"}, {"title": "Personalized Medicine Advances with Genomic Sequencing", "imagename": "recommended-7.jpg"}, {"title": "Quantum Cryptography Ensures Unbreakable Data Security", "imagename": "recommended-8.jpg"}, {"title": "Sustainable Cities Emerge with Smart Urban Planning", "imagename": "recommended-9.jpg"}, {"title": "Robotic Exoskeletons Enhance Human Capabilities", "imagename": "recommended-10.jpg"}, {"title": "Advancements in Renewable Energy Storage", "imagename": "recommended-11.jpg"}, {"title": "Brain-Computer Interfaces Revolutionize Assistive Tech", "imagename": "recommended-12.jpg"}, {"title": "Breakthrough in Graphene-Based Electronics", "imagename": "recommended-13.jpg"}, {"title": "Sustainable Aviation Fuels Reduce Carbon Footprint", "imagename": "recommended-14.jpg"}, {"title": "Quantum Sensing Enables Revolutionary Measurements", "imagename": "recommended-15.jpg"}, {"title": "Advances in Gene Editing and Personalized Medicine", "imagename": "recommended-16.jpg"}, {"title": "Autonomous Vehicles Reshape Urban Transportation", "imagename": "recommended-17.jpg"}, {"title": "Blockchain Technology Transforms Financial Services", "imagename": "recommended-18.jpg"}, {"title": "Advancements in Wearable Technology and IoT", "imagename": "recommended-19.jpg"}, {"title": "Breakthroughs in Quantum Computing and Algorithms", "imagename": "recommended-20.jpg"}]
        homedict["madeby"] = { "intro" : "Neutrino Developers 2024 courtesy ", "name" : " Biokraft Systems Limited"}
        return render_template("home/index.html", homedict=homedict)
        

#    def post(self):
        #homepage params
 #       pass
