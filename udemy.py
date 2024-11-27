# from rich.jupyter import display
#
# word_list = ['serial', 'movie', 'studio']
#
# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
#
# placeholder = ""
# word_lenght = len(chosen_word)
# for position in range(word_lenght):
#     placeholder += "_"
# print(placeholder)
#
# guess = input('Guess a letter: ').lower()
# print(guess)
#
# display =  ""
#
# for  letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"
#
# print(display)
#
# lives = [1,2,3,4,5,6]
# if guess ==0:
#     lives -=1
#     if lives==0:
#         game_over = True
#         print("You lose.")
# if "_" not in display:
#     game_over=True
#     print("You win.")
#
#     print(stages[lives])


# def life_in_years(age):
#     print("You are", age, "years old")
#
# life_in_years(47)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with("Ziza", "Caucasian")

