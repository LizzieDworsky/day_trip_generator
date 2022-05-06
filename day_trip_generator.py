import random
destinations = ["Lambeau Field", "Levi's Stadium", "Soldier Field", "SoFi Stadium"]
resturants = ["Taverne in the Sky", "Alinea", "Pho", "Pacific Catch"]
transportation = ["boat", "car", "train", "bicycle"]
entertainment = ["to watch a football game", "go on a hot air balloon ride", "go to the beach", "go on a boat tour"]

#selection function
def randomly_select_from_lists (list):
    random_selection = random.choice (list)
    return random_selection

#user preference function
def check_if_user_likes_choice (selected_variable, list_name, list_type):
    user_likes_option = input (f"The {list_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    while user_likes_option == "n":
        selected_variable = randomly_select_from_lists (list_name)
        user_likes_option = input (f"The {list_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    return selected_variable

#destination
selected_destination = randomly_select_from_lists (destinations)
selected_destination = check_if_user_likes_choice (selected_destination, destinations, "destination")

#transportation
selected_transportation = randomly_select_from_lists (transportation)
selected_transportation = check_if_user_likes_choice (selected_transportation, transportation, "transportation")

#resturant
selected_resturant = randomly_select_from_lists (resturants)
selected_resturant = check_if_user_likes_choice (selected_resturant, resturants, "resturant")

#entertainment
selected_entertainment = randomly_select_from_lists (entertainment)
selected_entertainment = check_if_user_likes_choice (selected_entertainment, entertainment, "entertainment")

print (selected_destination)
print (selected_transportation)
print (selected_resturant)
print (selected_entertainment)

    #if user_likes_option == "n" or user_likes_option == "no":
    #    user_likes_option = False
    #    return user_likes_option
    #elif user_likes_option == "y" or user_likes_option == "yes":
    #    user_likes_option = True
    #    return user_likes_option
    #else:
    #    input (f"We're sorry there was an error. Does the {list_type} {selected_variable} sound good to you? Yes or no: ")
        #needs more added, deadends here


#in progress below




#confirmed user likes this, now I need to store that value and proceed to asking about the additional values


#write a function that takes the boolean value and if T moves us forward, if F repeats. 
# Has to loop, while loop is probably the best option


        
#while loop if == no

#after repeating through all the lists double check that the user likes the selections, 
# have to be able to reselect if they do not

#if they like need to print the vacation out