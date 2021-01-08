from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import ast
from search_restaurant import SearchRestaurant

from email.message import EmailMessage
import smtplib
global_restrnt_srch_res = []
d_email_rest=[]

from rasa_sdk.events import UserUtteranceReverted

class ActionValidateLocation(Action):
    """Revertible mapped action for action_validate_location"""
    def name(self):
        return "action_validate_location"

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        city_matched = False
        corr_city = ""
        f = open("data/lookup_location.txt", "r", encoding='latin1')
        for line in f.readlines():
            city = str(line.strip().lower())
            if city == str(loc).lower():
                 city_matched = True
                 corr_city = str(line.strip())
                
        if city_matched:
            return [SlotSet('valid_location',True), SlotSet('location',corr_city)]
        else:
            return [SlotSet('valid_location',False), SlotSet('location',None)]

class ActionValidateCuisine(Action):
    """Revertible mapped action for action_validate_cuisine"""
    def name(self):
        return "action_validate_cuisine"

    def run(self, dispatcher, tracker, domain):
        user_cuisine = tracker.get_slot('cuisine')
        cuisines_list=['American', 'Chinese', 'Italian', 'Mexican', 'North Indian', 'South Indian']
        if user_cuisine in cuisines_list:
            return [SlotSet('valid_cuisine',True), SlotSet('cuisine',user_cuisine)]
        else:
            dispatcher.utter_message("\n\nSorry, your cuisine is either incorrectly spelled or not yet supported. \n\n")
            return [SlotSet('valid_cuisine',False), SlotSet('cuisine',None)]

class ActionValidateBudget(Action):
    """Revertible mapped action for action_validate_budget"""
    def name(self):
        return "action_validate_budget"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot('budget_min') != None:
            budget_min = float(str(tracker.get_slot('budget_min')))
        else:
            budget_min = 0
        if tracker.get_slot('budget_max') != None:
            budget_max = float(str(tracker.get_slot('budget_max')))
        else:
            budget_max = 0
        if (budget_min == 0 and budget_max == 0):
            return [SlotSet('valid_budget',False), SlotSet('budget_min',None), SlotSet('budget_max',None) ]
        else:
            if (budget_min < budget_max <= 300):
                return [SlotSet('valid_budget',True), SlotSet('budget_min', 0), SlotSet('budget_max',299)]
            elif (budget_min <= 300 < budget_max <= 700) or (300 < budget_min < budget_max <= 700)  :
                return [SlotSet('valid_budget',True), SlotSet('budget_min', 300), SlotSet('budget_max',700)]
            elif (budget_min <= 700):
                return [SlotSet('valid_budget',True), SlotSet('budget_min', 701), SlotSet('budget_max',10000)]
            else: 
                return [SlotSet('valid_budget',False), SlotSet('budget_min',None), SlotSet('budget_max',None) ]
                    

class ActionSendEmail(Action):
    """Revertible mapped action for action_send_email"""
    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('email')
        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget_min = tracker.get_slot('budget_min')
        budget_max = tracker.get_slot('budget_max')
        
        sr = SearchRestaurant()
        global global_restrnt_srch_res
        res = sr.get_top10(global_restrnt_srch_res)
        
        d_email_subj = "Top " + str(len(res)) + " " + cuisine.capitalize() + " restaurants in " + loc.capitalize()
        
        if len(res) == 0:
            # Construct the email 'subject' and the contents.
            d_email_msg = "Hi there! \n Sorry, something went wrong and we could not get you your list \n Best regards, \n Foodie Bot" 
        else:
            d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
            count = 0
            for x in res:
                count+= 1
                d_email_msg = d_email_msg + "\n" + str(count) + ": " + x[0] + " in " + x[1] + " has been rated " + str(x[2]) + ". Avg budget here for 2 person = Rs. " + str(x[3])
        
        d_email_msg = d_email_msg+ "\nThanks, \nFoodie Team\n\n" 
        d_email_msg = d_email_msg+ "\n\n Developed by Subhabrata Ghosh and Anushaa Vemuri"   
        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("rasachatbot42020@gmail.com", "acodhdkkugyjgbrz")
        # Create the msg object
        msg = EmailMessage()
        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "Foodie Resturant Suggestions"
        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email
        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("Email sent. Please check.")
        return []
        


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("\n Searching for suitable restaurants ...")
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget_min = tracker.get_slot('budget_min')
        budget_max = tracker.get_slot('budget_max')
        sr = SearchRestaurant()
        global global_restrnt_srch_res
        global_restrnt_srch_res = sr.search_restaurant(loc, cuisine, budget_min, budget_max)
        res = sr.get_top5(global_restrnt_srch_res)
        response=""
        if len(res) == 0:
            response = "No restaurants found for your inquiry"
        else:
            response = "Following restaurants match your preferences: \n \n"
            count = 0
            for x in res:
                count+= 1
                response = response + "\n" + str(count) + ": " + x[0] + " in " + x[1] + " has been rated " + str(x[2])
        dispatcher.utter_message("-----"+response+"\n\n")
        return [SlotSet('location',loc)]