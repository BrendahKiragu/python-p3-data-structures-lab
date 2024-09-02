spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# returns foods with a heat_level over 5. 
def get_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food["heat_level"] > 5] 
    return spiciest_food

# print_spicy_foods that returns all foods formatted with 🌶  emojis.
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emoji = '🌶' * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")
       
# print(print_spicy_foods(spicy_foods))

# returns the food that matches a cuisine.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)
    

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emoji = '🌶' * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")

def get_average_heat_level(spicy_foods):
    heat_levels =[food['heat_level'] for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
