#create place for user input 
user_input =''
#create a list to store the value
input = []

#the while loop
while user_input.lower() =! 'done':
    #check if there is a value in the user_input
    if user_input:
        #store value in the list
        input.append(user_input)

    #promp fore new value
    user_input = input("Enter a new value, or done when done") 