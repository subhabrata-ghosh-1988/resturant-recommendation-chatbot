import zomatopy
import json
from operator import itemgetter

class SearchRestaurant:
    """Searches restaurants for given city name, cuisine and budget"""
    def name(self):
        return "search_restaurant"

    def search_restaurant(self, loc, cuisine, budget_min, budget_max):
        """
        Takes City name, cuisine & budget(budget_min, budget_max) as inputs.
        Returns a list (max 100) of Restaurants matching the input criteria.
        NOTE: This function makes use of Zomatopy library
        """
    
        config = {"user_key" : "6bb9a42fda572d73004199cdd94a6238"}
        zomato = zomatopy.initialize_app(config)
        
        cuisines_dict={'American': 1, 'Chinese':25, 'Italian':55, 'Mexican':73, 'North Indian':50, 'South Indian':85}
        
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        
        print(d1)
        
        search_res = []
        search_param_start = ["start=0", "start=20", "start=40", "start=60", "start=80"]
        for x in search_param_start:
            results=zomato.restaurant_search(x, lat, lon, str(cuisines_dict.get(cuisine)), 20)
            d = json.loads(results)
            print(d)
            for restaurant in d['restaurants']:
                temp=[]
                temp.append(restaurant['restaurant']['name'])
                temp.append(restaurant['restaurant']['location']['address'])
                rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                temp.append(rating)
                temp.append(restaurant['restaurant']['average_cost_for_two'])
                search_res.append(temp)
        
        print('search resturant '+str(budget_min))
        print('serach resturant '+str(budget_max))

        #From above search results, select only those that have avg cost for 2 persons between budget_min & budget_max
        final_res = [x for x in search_res if budget_min <= x[3] <= budget_max]
        
        # Sort the final results in Descending order of user's aggregate rating (rating 5 (high) --> 1(low))
        final_res.sort(key=itemgetter(2), reverse=True)
        
        return final_res


    #def get_top5 (self, loc, cuisine, budget_min, budget_max):
    def get_top5 (self, rest_list):
        """
        Takes a list of restaurants as input containint rest name, location, avg user rating & budget.
        Returns a list of top 5 Restaurants, sorted in descending order of avg user rating
        """
        #res = self.search_restaurant(loc, cuisine, budget_min, budget_max)
        res = rest_list
        if len(res)> 5:
            print(" top 5: 3 ")
            return res[:5]
        else:
            print(" top 5: 4 ")
            return res
        
    #def get_top10 (self, loc, cuisine, budget_min, budget_max):
    def get_top10 (self, rest_list):
        """
        Takes a list of restaurants as input containint rest name, location, avg user rating & budget.
        Returns a list of top 10 Restaurants, sorted in descending order of avg user rating
        """
        #res = self.search_restaurant(loc, cuisine, budget_min, budget_max)
        res= rest_list
        if len(res)> 10:
            return res[:10]
        else:
            return res

