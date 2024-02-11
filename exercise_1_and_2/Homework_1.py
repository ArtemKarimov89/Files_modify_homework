
import pprint


def get_sorted_cook_book():
    with open("recipes.txt", 'r', encoding='utf-8') as f:
        dishes_list = f.readlines()

    cook_book = {}
    index = 0
    current_dish = ""
    dict_keys_list = ['ingredient_name', "quantity", "measure"]

    for line in dishes_list:
        line = line.strip()
        if index == 0:
            current_dish = line
            cook_book[current_dish] = []
            # index += 1
            # continue
        # elif index == 1:
            # index += 1
            # continue
        elif line == "":
            index = 0
            continue
        elif index != 1:
            ingredients_list = cook_book.get(current_dish)
            dict_from_ingredients(line, ingredients_list, dict_keys_list)
        index += 1

    return cook_book


def dict_from_ingredients(current_line, ingredients_list, dict_keys_list):
    # new_ingredients_list = current_line.replace(" ", "").split("|")
    new_ingredients_list = current_line.split("|")
    for index, new_ingredient in enumerate(new_ingredients_list):
        new_ingredients_list[index] = new_ingredient.strip()

    ingredients_dict = dict(zip(dict_keys_list, new_ingredients_list))
    ingredients_list.append(ingredients_dict)


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_sorted_cook_book()
    shop_list = {}

    for dish in dishes:
        dish_ingredients = cook_book[dish]

        for ingredient in dish_ingredients:
            if ingredient['ingredient_name'] in shop_list.keys():
                ingredient_name = ingredient['ingredient_name']
                current_quantity = shop_list.get(ingredient_name)['quantity']
                shop_list[ingredient_name]['quantity'] = current_quantity + inc_quantity(ingredient, person_count)
                continue

            dict_ingredient = ingredient.copy()
            dict_ingredient['quantity'] = inc_quantity(ingredient, person_count)
            ingredient_name = dict_ingredient.pop('ingredient_name')
            shop_list[ingredient_name] = dict_ingredient

    return shop_list


def inc_quantity(current_dict, inc):
    current_quantity = current_dict.get('quantity')
    if current_quantity is None:
        current_quantity = 0
    new_quantity = int(current_quantity) * inc

    return new_quantity


cook_book = get_sorted_cook_book()
pprint.pprint(cook_book)

print('\n')

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Запеченный картофель'], 2)
pprint.pprint(shop_list)
