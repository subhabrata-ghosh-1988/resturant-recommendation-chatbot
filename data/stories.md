## story_1
* greet
    - utter_greet
* restaurant_search_no_entity
    - utter_ask_location
* location_only{"location": "bengaluru"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_validate_budget
    - slot{"valid_budget" : true}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_email_option
* affirm_email{"email": "A@b.com"}
    - slot{"email": "A@b.com"}
    - action_send_email
    - utter_goodbye


## story_2
* greet
    - utter_greet
* restaurant_search_location{"location":"Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"valid_location": false}
    - slot{"location" : "None"}
    - utter_ask_location_again
* location_only{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Chinese"}
    - slot{"cuisine":"Chinese"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - action_validate_budget
    - slot{"valid_budget" : true}
    - slot{"budget_min": "700"}
    - slot{"budget_max": "10000"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
    - utter_email_option
* affirm_email{"email": "xyz-1123@rediffmail.com"}
    - slot{"email": "xyz-1123@rediffmail.com"}
    - action_send_email
    - utter_goodbye

## story_3
* greet
    - utter_greet
* restaurant_search_location{"location":"calcutta"}
    - slot{"location": "Kolkata"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot {"location" : "Kolkata"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget" : true}
    - slot{"budget_min": "0"}
    - slot{"budget_max": "300"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "_zxy123_@yahoo.com"}
    - slot{"email": "_zxy123_@yahoo.com"}
    - action_send_email
    - utter_goodbye

## story_4
* greet
    - utter_greet
* restaurant_search_no_entity
    - utter_ask_location
* location_only{"location": "near me"}
    - slot{"location": "near me"}
    - action_validate_location
    - slot{"valid_location": false}
    - slot{"location": "None"}
    - utter_ask_location_again
* location_only{"location": "nagpur"}
    - slot{"location": "Nagpur"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_validate_budget
    - slot{"valid_budget" : true}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_search_restaurants
    - slot{"location": "Nagpur"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "gg-pg@yahho.co.in"}
    - slot{"email": "gg-pg@yahho.co.in"}
    - action_send_email
    - utter_goodbye


## story_5
* greet
    - utter_greet
* restaurant_search_location_cuisine{"location":"Bokaro Steel City", "cuisine":"chines"}
    - slot{"location": "Bokaro Steel City"}
    - slot{"cuisine": "Chinese"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Bokaro Steel City"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget" : true}
    - slot{"budget_min": "0"}
    - slot{"budget_max": "300"}
    - action_search_restaurants
    - slot{"location": "Bokaro Steel City"}
    - utter_email_option
* negative
    - utter_goodbye

## story_6
* greet
    - utter_greet
* restaurant_search_location_budget{"location":"noida", "budget_max": "1000"}
    - slot{"location": "pune"}
    - slot{"budget_max": "1000"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Pune"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": "701"}
    - slot{"budget_max": "10000"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location":"Pune"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "a-b@google.com"}
    - slot{"email": "a-b@google.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_location_cuisine{"cuisine": "japanese", "location": "noida"}
    - slot{"cuisine": "japanese"}
    - slot{"location": "noida"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Noida"}
    - action_validate_cuisine
    - slot{"valid_cuisine": false}
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_email_option
* affirm_email{"email": "a-x@nl.edu"}
    - slot{"email": "a-x@nl.edu"}
    - action_send_email
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search_location_cuisine{"cuisine": "egyptian", "location": "chennai"}
    - slot{"cuisine": "egyptian"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Chennai"}
    - action_validate_cuisine
    - slot{"valid_cuisine": false}
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search_cuisine_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": "0"}
    - slot{"budget_max": "300"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_email_option
* negative
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "hyderabad", "budget_max": "500"}
    - slot{"budget_max": "500"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Hyderabad"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Italian"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "fal2email@rdx.fr"}
    - slot{"email": "fal2email@rdx.fr"}
    - action_send_email
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search_budget{"budget_min": "300", "budget_max": "600"}
    - slot{"budget_max": "600"}
    - slot{"budget_min": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - utter_ask_location
* location_only{"location": "rajahmundry"}
    - slot{"location": "rajahmundry"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Rajahmundry"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"location": "Rajahmundry"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "9@10.com"}
    - slot{"email": "9@10.com"}
    - action_send_email
    - utter_goodbye


## interactive_story_5
* restaurant_search_budget{"budget_max": "600"}
    - slot{"budget_max": "600"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": "300"}
    - slot{"budget_max": "700"}
    - utter_ask_location
* location_only{"location": "salem"}
    - slot{"location": "salem"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Salem"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"location": "Salem"}
    - utter_email_option
* negative
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
* restaurant_search_location_cuisine{"cuisine": "Italian", "location": "Delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_search_restaurants
    - utter_email_option
* affirm_email{"email": "a123@234.co.sg"}
    - slot{"email": "a123@234.co.sg"}
    - action_send_email
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search_location_cuisine{"cuisine": "Chinese", "location": "Delhi"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_email_option
* negative
    - utter_goodbye

## interactive_story_8
* restaurant_search_location{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"valid_location": false}
    - slot{"location": null}
    - utter_ask_location_again
* location_only{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Moradabad"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search_cuisine_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - action_search_restaurants
    - slot{"location": "Moradabad"}
    - utter_email_option
* negative
    - utter_goodbye

## interactive_story_9
* restaurant_search_location_cuisine{"cuisine": "Chinese", "location": "Jaipur"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Jaipur"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Jaipur"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - utter_email_option
* affirm_email{"email": "subhabrata_ghosh@rediffmail.com"}
    - slot{"email": "subhabrata_ghosh@rediffmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search_location{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Chandigarh"}
    - utter_ask_cuisine
* restaurant_search_cuisine{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search_cuisine_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "anushavemuri@gmail.com"}
    - slot{"email": "anushavemuri@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search_location_cuisine{"cuisine": "American", "location": "Delhi"}
    - slot{"cuisine": "American"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Delhi"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search_cuisine_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "anushavemuri@gmail.com"}
    - slot{"email": "anushavemuri@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search_location_cuisine{"cuisine": "Chinese", "location": "chandigarh"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Chandigarh"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search_cuisine_budget{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "anushavemuri@gmail.com"}
    - slot{"email": "anushavemuri@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_cuisine{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* location_only{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Chennai"}
    - utter_ask_budget
* restaurant_search_budget{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 701}
    - slot{"budget_max": 10000}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_email_option
* affirm_email{"email": "subhabrata_ghosh@rediffmail.com"}
    - slot{"email": "subhabrata_ghosh@rediffmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search_cuisine_budget{"cuisine": "Italian", "budget_max": "600"}
    - slot{"budget_max": "600"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"valid_cuisine": true}
    - slot{"cuisine": "Italian"}
    - action_validate_budget
    - slot{"valid_budget": true}
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - utter_ask_location
* location_only
    - utter_ask_location_again
* location_only{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"valid_location": true}
    - slot{"location": "Mumbai"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_email_option
* affirm
    - utter_ask_email
* affirm_email{"email": "subhabrata_ghosh@rediffmail.com"}
    - slot{"email": "subhabrata_ghosh@rediffmail.com"}
    - action_send_email
    - utter_goodbye
