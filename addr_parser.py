## ADDRESS PARSER 
## coded by Dezaida Malek
## for TM One Geomatics Application Developer Assignment

# ===== IMPORT NECESSARY LIBRARIES =====
import re
import nltk
from nltk import word_tokenize
import string
import numpy as np
from re import search, match

# ===== INITIALIZE =====

# initialize 'apt' as No 1-999
int_apt = np.arange(0, 999).tolist()
apt = [str(x) for x in int_apt]
apt = ['No {}'.format(d) for d in range(len(apt))]

# initialize 'city' with given city names
city = ["Kuala Terengganu", "Kuala Lumpur", "Kajang", "Bangi", "Damansara", "Petaling Jaya", "Puchong", "Subang Jaya", "Cyberjaya", "Putrajaya", "Mantin", "Kuching", "Seremban", 
"kuala terengganu", "kuala lumpur", "kajang", "bangi", "damansara", "petaling jaya", "puchong", "subang jaya", "cyberjaya", "putrajaya", "mantin", "kuching", "seremban"]

# initialize 'state' with given state names
state = ["Selangor", "Terengganu", "Pahang", "Kelantan", "Melaka", "Pulau Pinang", "Kedah", "Johor", "Perlis", "Sabah", "Sarawak", 
"selangor", "terengganu", "pahang", "kelantan", "melaka", "pulau pinang", "kedah", "johor", "perlis", "sabah", "sarawak"]

# initialize 'type_of_street' with given street types
type_of_street = ["Jalan", "Jln", "Lorong", "Persiaran", "jalan", "jln", "lorong", "persiaran"]

# initialize 'postcode' with no between 01000 to 98859
int_postcode = np.arange(1000, 98860).tolist()
postcode = [str(x) for x in int_postcode]  


# ===== FUNCTIONS =====

# func to remove punctuations
def remove_punct(text):
    text_nopunct = ''
    text_nopunct = re.sub('['+string.punctuation+']', '', text)
    return text_nopunct


# func to return all uncommon words 
def UncommonWords(A, B): 

	# count will contain all the word counts 
	count = {} 
	
	# insert words of string A to hash 
	for word in A.split(): 
		count[word] = count.get(word, 0) + 1
	
	# insert words of string B to hash 
	for word in B.split(): 
		count[word] = count.get(word, 0) + 1

	# return required list of words 
	return [word for word in count if count[word] == 1] 

# func to parse the address given
def parse(text):

    text_clean = remove_punct(text)
    # split input by comma
    addr_chunks = re.split(',+', text)

    apt_exist = ""
    street_exist = ""
    postcode_exist = ""
    state_exist = ""
    city_exist = ""

    # parse apt
    for w in range(len(apt)):
        if match(apt[w].lower(), text.lower()):
            apt_exist = apt[w]
           
    print("\nApt: " + apt_exist)

    # parse street
    for r in range(len(type_of_street)):
            for s in range(len(addr_chunks)):
                if type_of_street[r].lower() in addr_chunks[s].lower():
                    street_exist = addr_chunks[s]
                    street_exist = street_exist

    print('Street: ' + street_exist)

    # parse city
    for w in range(len(city)):
        if search(city[w], text):
            city_exist = city[w]

    print("City: " + city_exist)

    # parse state
    for w in range(len(state)):
        if search(state[w], text):
            state_exist = state[w]

    print("State: " + state_exist)

    # parse postcode
    for w in range(len(postcode)):
        if search(postcode[w], text):
            postcode_exist = postcode[w]
            if len(postcode_exist) < 5:
                postcode_exist = '0'+postcode_exist

    print("Postcode: " + postcode_exist)

    # put all parsed item in a list
    whole_addr = [apt_exist, state_exist, city_exist, postcode_exist, street_exist]
    
    # parse section 
    cleaned_addr = text_clean
    addr_str = ' '.join(whole_addr)
    sectt = UncommonWords(cleaned_addr.lower(), addr_str.lower())
    for i in sectt:
        print('Section: ' + i)

# func to main program
def mainprog():
    print("Please capitalize each word for better result.")
    text = input("Enter the address to parse: ")
    print("Parsing may take a while :)")
    parse(text)

# ===== START UP PROG =====
print("\nHi, Welcome to Address Parser!")
answer = input("Ready to parse an address? (y/n): ") 
if answer == "y": 
    mainprog()
    print('\nThank you!')
elif answer == "n": 
    print("Goodbye :)")
    exit 
else: 
    print("Please enter y or n.") 



