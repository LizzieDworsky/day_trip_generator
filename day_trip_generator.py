import random
destinations = ["Lambeau Field", "Levi's Stadium", "Soldier Field", "SoFi Stadium"]
resturants = ["Taverne in the Sky", "Alinea", "Pho", "Pacific Catch"]
transportation = ["boat", "car", "train", "bicycle"]
entertainment = ["watch a football game", "go on a hot air balloon ride", "go to the beach", "go on a boat tour"]

#selection function
def randomly_select_from_lists (list):
    random_selection = random.choice (list)
    return random_selection

#user preference function
def check_if_user_likes_choice (selected_variable, list_name, list_type):
    user_likes_option = input (f"The {list_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    while user_likes_option == "n" or user_likes_option == "no":
        selected_variable = randomly_select_from_lists (list_name)
        user_likes_option = input (f"The {list_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    return selected_variable

#function to run selection and user preference functions
def selection_and_confirmation (current_list):
    selection = randomly_select_from_lists (current_list)
    selection = check_if_user_likes_choice (selection, current_list, "destination")
    return selection

#destination
selected_destination = selection_and_confirmation (destinations)

#transportation
selected_transportation = selection_and_confirmation (transportation)

#resturant
selected_resturant = selection_and_confirmation (resturants)

#entertainment
selected_entertainment = selection_and_confirmation (entertainment)

#final confirmation
final_confirmation = input (f"Congratulations! Your day trip has been generated! You will be taking a {selected_transportation} to {selected_destination}. While there you will {selected_entertainment} and eat at {selected_resturant} resturant for dinner! Does this sound good y/n? ")
while final_confirmation == "n":
    print ("We're sorry to hear this isn't what you wanted. Lets try again!")
    selected_destination = selection_and_confirmation (destinations)
    selected_transportation = selection_and_confirmation (transportation)
    selected_resturant = selection_and_confirmation (resturants)
    selected_entertainment = selection_and_confirmation (entertainment)
    final_confirmation = input (f"Congratulations! Your day trip has been generated! You will be taking a {selected_transportation} to {selected_destination}. While there you will {selected_entertainment} and eat at {selected_resturant} resturant for dinner! Does this sound good y/n? ")

print (f"Congratulations! We are so excited that you like your day trip selections! Here is your itinerary: You'll be travelling using a {selected_transportation} to {selected_destination}, while there you'll {selected_entertainment} and eat dinner at {selected_resturant}. Hope you enjoy your time!")
