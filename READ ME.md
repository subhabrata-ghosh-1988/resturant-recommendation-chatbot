#### Author: Subhabrata Ghosh , Anusha Vemuri
-----------------------------------

#### Batch: MLC-18
-------------


Version/ Environment:
----------------------
Our Rasa bot is trained and tested in following environment:
1) Rasa 2.0.0
2) Rasa sdk 2.0.0
3) Python 3.7.0 (Windows) 
4) Tensorflow 2.3.2
5) en-core-web-md 2.2.5


Files which we have worked upon/modified:
-----------------------------------------
1) actions.py: We have implemented some custom actions for the chatbot.
	- **Introduced:**  
	    - ActionValidateLocation : This action validates if the current location falls under Tier1 & Tier2 cities in India.
	    - ActionValidateCuisine  : This action validates if the cuisines is supported for recommendations.our chatbot currently supports the following cuisines.
	        - Chinese
	        - Italian
	        - North Indian
	        - South Indian
	        - American
	        - Mexican
	    - ActionValidateBudget : This actions set the budget for the average of two people.
	    - ActionSendEmail : This method is used for sending email notifications to the users based on their selection
	- **Modified  :**  
	    - ActionSearchRestaurants: This action is used to call zomato api
2) domain.yml
	- Several new slots, actions and entities introduced - to meet assignment needs
3) zomatopy.py:
	- Updated method restaurant_search() to include additional Header parameter 'User-agent': 'curl/7.43.0'. This was done so that occassional errors from actual Zomato API such as http code 440/443/500 should not negatively impact our functionality.
4) search_restaurant.py:
	Our own wrapper over zomatopy.py to reduce un-necessary compexity in actions.py. Methods ActionSearchRestaurants() and ActionSendEmail() in actions.py makes use of the 3 methods in this new file. Methods in this file are:
	a) search_restaurant() : Retrieves 100 results for given input location, cuisine & budget range. It uses zomatopy internally
	b) get_top5(): Returns top 5 (or less) results from given set of results
	c) get_top10(): Returns 10 (or less) results from given set of results

5) config.yml:
	updated to make it compatibale with rasa 2.0.0.
	Please have a look at this [article](https://blog.rasa.com/migrating-your-rasa-1-x-assistant-to-rasa-2-0/)

6) data/nlu/nlu.md:
	Several new intents with multiple examples, synonyms added. 

7) data/stories/stories.md:
	Several stories included (incl. sample stories provided)

8) data/Locations:
	We have two files - Tier1.txt and Tier2.txt contains list of all Tier-1, Tier-2 cities provided in the assignment. Is used for validation of user inputs.For more details please have a look [here](https://en.wikipedia.org/wiki/Classification_of_Indian_cities)
