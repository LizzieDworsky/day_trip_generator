import random
destinations = ["Lambeau Field", "Levi's Stadium", "Soldier Field", "SoFi Stadium"]
resturants = ["Taverne in the Sky", "Alinea", "Pho", "Pacific Catch"]
transportation = ["boat", "car", "train", "bicycle"]
entertainment = ["watch a football game", "hot air balloon ride", "go to the beach", "go on a boat tour"]

print (random.choice (destinations))
print (random.choice (resturants))
print (random.choice (transportation))
print (random.choice (entertainment))

#I want to write a function that will generate the random selection random.choice, 
# perhaps with the parameter of the lists? I'm not sure how that would look yet
#then call the function using variable names such as destination_selection = 



#selection function
def randomly_select_from_lists (list):
    random_selection = random.choice (list)
    return random_selection


selected_destination = randomly_select_from_lists (destinations)
print (selected_destination)



#need to create a function that checks if user likes selection or not
def check_if_user_likes_choice (selected_variable, list_type):
    user_likes_option = input (f"The {list_type} selected for you is {selected_variable}. Does this sound good? Enter y/n: ")
    if user_likes_option == "n" or user_likes_option == "no":
        user_likes_option = False
    if user_likes_option == "y" or user_likes_option == "yes":
        user_likes_option = True
    else:
        input (f"We're sorry there was an error. Does the {list_type} {selected_variable} sound good to you? Yes or no: ")

check_if_user_likes_choice (selected_destination, "destination")


#write a function that takes the boolean value and if T moves us forward, if F repeats. 
# Has to loop, while loop is probably the best option

#after repeating through all the lists double check that the user likes the selections, 
# have to be able to reselect if they do not

#if they like need to print the vacation out