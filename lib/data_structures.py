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
    return [food['name'] for food in spicy_foods]
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        # Extracting the necessary information
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        
        # Create a string of chili pepper emojis based on the heat level
        heat_emojis = '🌶' * heat_level
        
        # Format and print the string
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # Return None if no matching cuisine is found


def print_spiciest_foods(spicy_foods):
    # Filter the list to include only foods with heat_level greater than 5
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    
    for food in spiciest_foods:
        # Extracting necessary information
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        
        # Create a string of chili pepper emojis based on the heat level
        heat_emojis = '🌶' * heat_level
        
        # Print the formatted string
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")
    

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0  # Return 0 if the list is empty to avoid division by zero

    # Calculate the total heat level
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    
    # Count the number of spicy foods
    number_of_foods = len(spicy_foods)
    
    # Compute the average heat level and return it as an integer
    return total_heat_level // number_of_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

