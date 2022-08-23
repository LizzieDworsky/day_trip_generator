import random
destinations_dictionary = {"option_one": "Lambeau Field", "option_two": "Levi's Stadium", "option_three": "Soldier Field", "option_four": "SoFi Stadium"}
restaurants_dictionary = {"option_one": "Taverne in the Sky", "option_two": "Alinea", "option_three": "Pho", "option_four": "Pacific Catch"}
transportation_dictionary = {"option_one": "boat", "option_two": "car", "option_three": "train", "option_four": "bicycle"}
entertainment_dictionary = {"option_one": "watch a football game", "option_two": "go on a hot air balloon ride", "option_three": "go to the beach", "option_four": "go on a boat tour"}
final_trip_dictionary = {"destination": "", "transportation": "", "restaurant": "", "entertainment": ""}

#lists and list selection function
# destinations = ["Lambeau Field", "Levi's Stadium", "Soldier Field", "SoFi Stadium"]
# restaurants = ["Taverne in the Sky", "Alinea", "Pho", "Pacific Catch"]
# transportation = ["boat", "car", "train", "bicycle"]
# entertainment = ["watch a football game", "go on a hot air balloon ride", "go to the beach", "go on a boat tour"]
# def randomly_select_from_lists (list):
#     random_selection = random.choice (list)
#     return random_selection

#selection function
def randomly_select_from_dictionaries(dictionary):
    random_selection = random.choice(list(dictionary.values()))
    return random_selection

#user preference function
def check_if_user_likes_choice (selected_variable, dict_name, dict_type):
    user_likes_option = input (f"The {dict_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    while user_likes_option == "n" or user_likes_option == "no":
        selected_variable = randomly_select_from_dictionaries (dict_name)
        user_likes_option = input (f"The {dict_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    return selected_variable

#function to run selection and user preference functions
def selection_and_confirmation (current_dict, dict_type):
    selection = randomly_select_from_dictionaries (current_dict)
    selection = check_if_user_likes_choice (selection, current_dict, dict_type)
    return selection


#destination
final_trip_dictionary["destination"] = selection_and_confirmation (destinations_dictionary, "destination")

#transportation
final_trip_dictionary["transportation"] = selection_and_confirmation (transportation_dictionary, "transportation")

#resturant
final_trip_dictionary["restaurant"] = selection_and_confirmation (restaurants_dictionary, "restaurant")

#entertainment
final_trip_dictionary["entertainment"] = selection_and_confirmation (entertainment_dictionary, "entertainment")

#final confirmation
final_confirmation = input (f"Congratulations! Your day trip has been generated! You will be taking a {final_trip_dictionary['transportation']} to {final_trip_dictionary['destination']}. While there you will {final_trip_dictionary['entertainment']} and eat at {final_trip_dictionary['restaurant']} restaurant for dinner! Does this sound good y/n? ")
while final_confirmation == "n":
    print ("We're sorry to hear this isn't what you wanted. Lets try again!")
    change_selection = input (f"Are you satisfied with {final_trip_dictionary['destination']}, y/n? ")
    if change_selection == "n" or change_selection == "no":
        final_trip_dictionary["destination"] = selection_and_confirmation (destinations_dictionary, "destination")
    change_selection = input (f"Are you satisfied with {final_trip_dictionary['transportation']}, y/n? ")
    if change_selection == "n" or change_selection == "no":
        final_trip_dictionary["transportation"] = selection_and_confirmation (transportation_dictionary, "transportation")
    change_selection = input (f"Are you satisfied with {final_trip_dictionary['restaurant']}, y/n? ")
    if change_selection == "n" or change_selection == "no":
        final_trip_dictionary["restaurant"] = selection_and_confirmation (restaurants_dictionary, "restaurant")
    change_selection = input (f"Are you satisfied with {final_trip_dictionary['entertainment']}, y/n? ")
    if change_selection == "n" or change_selection == "no":
        final_trip_dictionary["entertainment"] = selection_and_confirmation (entertainment_dictionary, "entertainment")
    final_confirmation = input (f"Congratulations! Your day trip has been generated! You will be taking a {final_trip_dictionary['transportation']} to {final_trip_dictionary['destination']}. While there you will {final_trip_dictionary['entertainment']} and eat at {final_trip_dictionary['restaurant']} restaurant for dinner! Does this sound good y/n? ")

print (f"Congratulations! We are so excited that you like your day trip selections! Here is your itinerary: You'll be travelling using a {final_trip_dictionary['transportation']} to {final_trip_dictionary['destination']}, while there you'll {final_trip_dictionary['entertainment']} and eat dinner at {final_trip_dictionary['restaurant']}. Hope you enjoy your time!")

# also, should wrap everything within a function and call that function.