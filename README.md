# PokerProject
A temporary repository to store a python poker project

This project was one of the first projects I ever did in python. It uses an object-oriented programming system to store card items, which each contain the properties that one might know in a common playing card, such as the value and color. All face cards are given a value based on their worth, for example a Queen card would have a value of 12. This can be easily calculated by knowing the order of face cards: Jack, Queen, King, Ace. When stated, the program will deal four hands. These hands are displayed in a sort of chart. It then takes each individual hand, and by using custom written algorithm, determines the value of that hand. The values are calculated by finding the best poker hand rankings in that hand. These values are then compared with the rankings of the three other hands present. If there is a hand with the clear winning value, then the program will automatically display the winning hand as well as the name of the hand type. If there seems to be a tie, the algorithm will go through the list of values in that hand, comparing each card with the tying hands, until a verdict is reached. This will once again display as a new image. 
