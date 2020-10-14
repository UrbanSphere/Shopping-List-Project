from recepies import *
from other import *

shopping_list = []
welcome_statement()
text = input()
recepies = text.split(', ')

spaghetti(recepies, shopping_list)
scrambled_eggs(recepies, shopping_list)
korean_fried_pork(recepies, shopping_list)
mascarpone_salomon(recepies, shopping_list)

neat_display(shopping_list)
