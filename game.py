#Welcome users to the game
print("Welcome to Saba's Sparkly Crystal Ball!")
name = input("What's your name? ")
print(f"Hello, {name}! You can ask me any question about your future and I'll tell you the true answer.")
print("But beware: you might not like what I have to say.")
decision = input("Would you like to continue? Type Yes or No: ")

#if statement, if yes, next prompt; if no, say goodbye
if decision == "Yes":
    print("You are a brave soul.")
    print("Alright. I'm ready for your question.")
    input("What do you want to know? ") 
    print("Do you want me to A) tell you the real truth or B) go easy on you?")
    decision2 = input("Type A or B. ")
    
elif decision == "No":
    print("Thanks for nothing.")
    print("Goodbye!") #end code somehow?
    exit()

else:
    print("Error")
    exit()

#Change set of questions depending on answer above
if decision2 == "A":
    print("Thank you for letting me know. I need a little more information:")
    input("What is your favorite color? ")
    print("Hmm...")
    input("What month were you born in? ")
    print("Okay...")
    input("What time is it right now? ")

elif decision2 == "B":
    print("Thank you for letting me know. I need a little more information:")
    input("How old are you? ")
    print("Hmm...")
    input("How do you feel right now? ")
    print("Okay...")
    print("What is your credit card number? ")
    input("Just kidding. What is your zodiac sign? ")
    print()

else:
    print("Error")
    exit()

#Tell users you need more information
print("I just need one more piece of information.")
numberpick = int(input("Pick a number from 1 to 5. "))
print("My answer is...")

#Make list of fortune teller options and provide answer
if numberpick == 1:
    print("Yes. 100%. It's going to happen.")
elif numberpick == 2:
    print("Okay so awkward but I actually forgot your question. Could you try again?")
elif numberpick == 3:
    print("Sorry dude. It's a no.")
elif numberpick == 4:
    print("I love gatekeeping. So I'm actually not going to tell you.")
elif numberpick == 5:
    print("Depends on how you carry out this moment. Your life depends on it. Good luck.")
else:
    print("Error")
    exit()


