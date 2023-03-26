GRAM = 100


def get_recipe_price(prices: dict[str,float], optionals: list[str] = [], **ingredients) -> float:
    """
     this function calculates the price of the recipe
    :param prices: dictionary of prices of ingredients
    :param optionals: list of optional ingredients that are not needed
    :param ingredients: dictionary of ingredients and their weights
    :return: the price of the recipe
    """
    wanted_list = [price for price in prices if price not in optionals]
    return sum([((prices[ingredient] * ingredients[ingredient]) / GRAM) for ingredient in wanted_list if
                ingredient in ingredients])


# ================== MAIN ==================
if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))
