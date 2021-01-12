Author: Subhabrata Ghosh , Anush Vemuri
-----------------------------------

Batch: MLC-18
-------------


Version/ Environment:
----------------------
Our Rasa bot is trained and tested in following environment:
1) Rasa 1.10.2
2) Rasa sdk 1.10.3
3) Python 3.7.0 (Windows) 
4) Tensorflow 2.1.3
5) en-core-web-md 2.1.0


Files which we have worked upon/modified:
-----------------------------------------
1) actions.py:
	Introduced: ActionValidateLocation, ActionValidateCuisine, ActionValidateBudget, ActionSendEmail
	Modified: ActionSearchRestaurants
2) domain.yml
	Several new slots, actions and entities introduced - to meet assignment needs
3) zomatopy.py:
	Updated method restaurant_search() to include additional Header parameter 'User-agent': 'curl/7.43.0'. This was done so that occassional errors from actual Zomato API such as http code 440/443/500 should not negatively impact our functionality.
4) search_restaurant.py:
	Our own wrapper over zomatopy.py to reduce un-necessary compexity in actions.py. Methods ActionSearchRestaurants() and ActionSendEmail() in actions.py makes use of the 3 methods in this new file. Methods in this file are:
	a) search_restaurant() : Retrieves 100 results for given input location, cuisine & budget range. It uses zomatopy internally
	b) get_top5(): Returns top 5 (or less) results from given set of results
	c) get_top10(): Returns 10 (or less) results from given set of results

5) config.yml:
	updated to include FallbackPolicy

6) data/nlu.md:
	Several new intents with multiple examples, synonyms added. 

7) data/stories.md:
	Several stories included (incl. sample stories provided)

8) data/location.txt:
	Contains list of all Tier-1, Tier-2 cities provided in the assignment. Is used for validation of user inputs.
