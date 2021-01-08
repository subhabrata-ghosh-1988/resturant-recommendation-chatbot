## intent:greet
- hello
- hi
- hey
- hi there
- good morning
- good evening
- gud afternoon
- hello bot
- hi robot
- wassup
- whats up buddy
- hello thr
- hey whatsup
- hola
- hi thr

## intent:affirm
- yo
- yes
- yep
- yeah
- ok
- sure thanks
- sure
- fine
- y ok
- yes k
- ohhk
- okido
- why not
- sounds good
- sure thing
- gr8 man
- sure bot
- great
- gr8
- hey thats great
- yes plz
- ys please

## intent:affirm_email
- yes. Please send it to [ahbcdj@dkj.com](email)
- send it to [xyz@yahoo.co.in](email)
- ok e-mail is [xyz@abcd.edu](email)
- [dfkjvflnv233@gmail.co.uk](email)
- [somagi.112233@mit.edu.co.us] is the email
- why not :) send it to [gabrux32@iit-delhi.com](email)
- sounds gr8, email me on [cdmk7dfnvk_231@rediffmail.com](email)
- mail is [909e3_o328e832@msn.co.jp](email)
- gr8 send me the details on [8899@hotmail.com](email)
- [abcd-398@482.co.us](email)
- [a@b.com](email)
- yes. [A@b.com](email)
- [abcd.283190@mit.edu](email)
- yes send it to [a-x@nl.edu](email)
- [fal2email@rdx.fr](email)
- [9@10.com](email)
- ys send it to [a123@234.co.sg](email)
- yes please send it to [anushaa_vemuri@rediffmail.com](email)
- [subhabrata.ghosh@gmail.com](email)
- yes send it to [subhabrata_ghosh@rediffmail.com](email)
- send to [anushaa_vemuri@rediffmail.com](email)

## intent:negative
- no
- nah
- no, thanks
- let it be
- no. thanks
- no its ok
- i dont want it
- i am not interested
- no fine thank you
- no fine
- no thnx
- thanks but not interested
- no thanks
- no thx
- nope

## intent:goodbye
- tata
- take care
- ok thnx
- thnx
- thanks
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye

## intent:restaurant_search_no_entity
- i'm looking for a place to eat
- I want to grab lunch
- get me a dinner spot
- search for restaurants
- show me some restaurants
- find me a good restaurant near me
- find me a fast food corner
- I am looking a place for dinner
- show me options for lunch
- get me family dining locations
- where can I dine
- place for quick byte
- lunch
- dinner
- something to eat
- get me places to eat
- i am searching for food
- food
- restaurant
- restaurant near me
- show me places to eat
- find me good rest
- I'm hungry
- hungry good restaurant
- find me god restaurants

## intent:location_only
- in [Delhi](location)
- south [delhi](location)
- [colaba](location)
- anywhere in [pune](location)
- at [kolkata](location)
- [mumbai](location)
- [new york](location)
- near me
- my city
- in my locality
- my neighbourhood
- ok try in [illahabad]{"entity": "location", "value": "Allahabad"}
- not far away from my location
- within 10 min walking distance
- within 5 km radius
- max 10 min drive
- try [prayagraj]{"entity": "location", "value": "Allahabad"}
- [ajmer](location)
- [b'lore](location)
- [delhi](location)
- [calcutta]{"entity": "location", "value": "Kolkata"}
- in [shimla](location)
- south [b'lore]{"entity": "location", "value": "bangalore"}
- [bokaro steel city](location)
- [bengaluru](location)
- [b'lore]{"entity": "location", "value": "bangalore"}
- [bengaluru]{"entity": "location", "value": "Bangalore"}
- [rajahmundry](location)
- [salem](location)
- [calcutta](location)
- [kalkatta](location)
- [bombay](location)
- [Mumbai](location)
- ok find it in [Moradabad](location)
- [chennai](location)
- [bombay]{"entity": "location", "value": "Mumbai"}
- bomba

## intent:restaurant_search_location
- I am looking for some restaurants in [dilli]}{"entity":"location", "value":"Delhi"}.
- I am looking for some restaurants in [banaras](location)
- anywhere in the [west](location)
- Oh, sorry, in [Italy](location)
- can you please change it to [noida](location)
- please change location to [new jersey](location)
- I am looking for some restaurants in [Mumbai](location)
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [amritsar](location)
- please find me a restaurant in [ahmedabad](location)
- can you suggest some good restaurants in [rishikesh](location)
- find me good restaurants in [Chandigarh](location)

## intent:restaurant_search_cuisine
- show me [chinese](cuisine) restaurants
- i am looking for an [indian](cuisine) spot
- I am looking for [asian fusion](cuisine) food
- [American](cuisine)
- [Chinese](cuisine)
- [Italian](cuisine)
- [Mexican](cuisine)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [chinese](cuisine){"entity": "cuisine", "value": "Chinese"}
- I am looking for [mexican indian fusion](cuisine)
- can you find me a [chinese]{"entity": "cuisine", "value": "Chinese"} restaurant
- [Tandoori]{"entity": "cuisine", "value": "North Indian"} food
- restaurants where I can get good [Tandoori]{"entity": "cuisine", "value": "North Indian"} food
- where can I find good [Dosa]{"entity": "cuisine", "value": "South Indian"}?
- I want to eat [Idly]{"entity": "cuisine", "value": "South Indian"}
- find me a [mexican]{"entity": "cuisine", "value": "Mexican"} restaurant

## intent:restaurant_search_budget
- show me good restaurants in range [100](budget_min)-[200](budget_max)
- find me restaurants for budget < [250](budget_max)
- get me list of restaurants near me, I have budget of [1,000]{"entity": "budget_max", "value": "1000"}
- restaurant within [400](budget_min)- [800](budget_max) budget Rs
- show me food options within [200](budget_min) -[400](budget_max) range
- list restaurants for budget of [700](budget_max)
- for approx [200](budget_min) to [600](budget_max) what restaurants can I go
- tell me food joints not costlier than [1000](budget_max) Rs
- get me good places to eat. budget no issue for me
- where can I go for candle light dinner? any price is Ok
- family dinner options? any budget is fine
- find family restaurant budget [900](budget_max)
- food junction price [300](budget_max)
- i'm hungry suggest sm hotels.  i have  [100](budget_min)-[200](budget_max) rs
- food near me Lesser than Rs. [300](budget_max)
- Rs. [300](budget_min) to [700](budget_max) budget retaurant options
- find me a restaurant in budget of [300](budget_min) -[600](budget_max) rs
- find me restaurant in budget of [500](budget_min)- [1000](budget_max)
- show me restaurants for budget [600](budget_max)
- suggest some good family dinner options. budget no concern
- suggest sm good family dinner option. budget no issue
- Rs. [300](budget_min) to [700](budget_max)
- Lesser than Rs. [300](budget_max)
- More than [700](budget_min)

## intent:restaurant_search_location_cuisine
- show me [chines]{"entity": "cuisine", "value": "Chinese"} restaurants in [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- [central](location) location [indian](cuisine) restaurant
- please find me [chinese](cuisine) food spots in [delhi](location)
- get me good [italian](cuisine) lunch corners in [bangalore](location)
- what are best [south india](cuisine) spots in [Mysore](location)
- show [american](cuisine) restaurant in [south bombay]{"entity": "location", "value": "Mumbai"}
- what are great [italian](cuisine) family dinner options in downtown [mumbai](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- suggest me good [american](cuisine) restaurants in [chandigarh](location)
- find me good [japanese](cuisine) restaurant in [noida](location)
- please find me [egyptian](cuisine) restaurant in [chennai](location)
- find me good [italian]{"entity": "cuisine", "value": "Italian"} restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- [chinese]{"entity": "cuisine", "value": "Chinese"} restaurant in [delhi]{"entity": "location", "value": "Delhi"}
- hello find me [chinese]{"entity": "cuisine", "value": "Chinese"} restarant in [jaipur]{"entity": "location", "value": "Jaipur"}
- find me [ameriacn]{"entity": "cuisine", "value": "American"} restaurants in [delhi]{"entity": "location", "value": "Delhi"}
- i'm hungry. looking out for some good [chinese]{"entity": "cuisine", "value": "Chinese"} restaurants in [chandigarh](location)

## intent:restaurant_search_location_budget
- can you find a table in [Chennai](location) in [300](budget_min)-[700](budget_max) price range for 3 people?
- show me restaurants in [Rishikesh](location). budget [eight hundred] {"entity": "budget_max", "value": "800"} for 2 person.
- what restaurants would fit my budget of [200](budget_max) rs in [Allahabad](location)?
- get me dinner options in [noida](location) for 4 people. budget more than [1000](budget_min)
- show me family dining options for 3 in range [600](budget_min) to [1000](budget_max) in [jaipur]{"entity": "location", "value": "Jaipur"}

## intent:restaurant_search_cuisine_budget
- for budget [999](budget_max) rs show me [chines]{"entity": "cuisine", "value": "Chinese"} restaurants
- show me a [mexican](cuisine) place for price <[750](budget_max)
- Get me [indian](cuisine) restaurant for 2 persons in less than [1,200]{"entity": "budget_max", "value": "1200"}
- get me good [italian](cuisine) lunch corners. any budget
- what are best [south india](cuisine) spots. no budget limit
- what are great [italian](cuisine) family dinner options for rs [101](budget_min)-[1111](budget_max)
- find me good [italian]{"entity": "cuisine", "value": "Italian"} restaurants in budget [600](budget_max)

## intent:restaurant_search
- can you book a table in [Chennai](location) in a [475](budget_min)-[759](budget_max) price range with [spanish](cuisine) food for four people
- get me [north indian](cuisine) cuisine restaurants in [vijaywada](location) within [six hundred]{"entity": "budget_max", "value": "600"} rs
- get me [italian]{"entity": "cuisine", "value": "Italian"} resta in [hyderabad](location) within [786](budget_max) budget

## intent:out_of_scope
- vnfneron lkdnlen

## synonym: Allahabad
- illahabad
- prayagraj
- allahabad
- alahabad

## synonym:1000
- 1,000
- thousand
- one thousand
- 1 thousand

## synonym:1200
- 1,200
- 2 thousand
- two thousand

## synonym:300
- 399
- three hundred
- 3 hundred

## synonym:500
- five hundred
- 5 hundred

## synonym:600
- six hundred
- 6 hundred

## synonym:700
- seven hundred
- 7 hundred

## synonym:800
- eight hundred
- 8 hundreds
- eight hundreds
- 8 hundrd

## synonym:American
- ameriacn
- American
- american
- usa

## synonym:Bangalore
- b'lore
- bengaluru
- Bengaluru
- bangalore
- bangalor

## synonym:Chinese
- chinese
- chines
- Chinese
- Chines

## synonym:Delhi
- New Delhi
- delhi
- delli
- new deli
- new delhi

## synonym:Italian
- italian
- Italian

## synonym:Jaipur
- jaipur

## synonym:Kolkata
- calcutta
- Calcutta
- kalkatta
- kolkata

## synonym:Mexican
- mexican
- Mexican
- mexico

## synonym:Mumbai
- south bombay
- bombay
- mumbai
- bom
- m'bai

## synonym:Nagpur
- nagpur

## synonym:North Indian
- Tandoori
- tandoori
- north indian

## synonym:South Indian
- Dosa
- Idly
- Sambar
- Idaly
- South Indian
- south indian

## regex:email
- ^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,3}|\.([a-zA-Z]{2,3}))$

## regex:greet
- he[l]+[o]+
- hey[^\s]*
