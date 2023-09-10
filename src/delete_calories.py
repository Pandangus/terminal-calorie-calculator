import os
import time
import re
from utility_functions.return_to_main_menu import return_to_main_menu
from list_total_calories import list_total_calories


def delete_calories(ingredients_list, total_calories):
    try:
        menu_header = "DELETE CALORIES\n---------------"
        time.sleep(0.25)
        os.system("clear")
        print("\nYou selected delete calories.")
        time.sleep(0.25)

        while True:
            delete_type_input = (
                input(
                    f"\n{menu_header}\n\nplease enter: delete [e]ntry from current calories, or, delete [f]ile from previously saved files (enter 'x' to return to main menu):\n\n-> "
                )
                .strip()
                .lower()
            )
            
            if delete_type_input == "x":
                return (return_to_main_menu())
            
            elif delete_type_input == "e":
                os.system('clear')
                if not list_total_calories(ingredients_list):
                    return None

                delete_user_input = (
                    input(f"\nPlease enter name of ingredient to remove\n\n-> ").strip().lower()
                )
                item_deleted = False

                for entry in ingredients_list:
                    if delete_user_input.lower() in entry:
                        ingredients_list.remove(entry)
                        total_calories -= int(re.search(r"\d+", entry).group())
                        os.system("clear")
                        print(f"\nsuccess! {delete_user_input} removed from ingredient list")
                        item_deleted = True
                        time.sleep(0.25)
                        print("\nreturning to main menu")
                        return (ingredients_list, total_calories)

                if not item_deleted:
                    os.system("clear")
                    print(
                        f"\n{delete_user_input} returned no matches. Nothing was deleted from ingredients list."
                    )
                    time.sleep(0.25)
                    print("\nreturning to main menu")
                    return None
            
            elif delete_type_input == "f":
                pass

            else:
                os.system('clear')
                print("invalid input")

    except ValueError as e:
        print(f"\ndelete_calories - ValueError: {e}")

    except TypeError as e:
        print(f"\ndelete_calories - TypeError: {e}")

    except Exception as e:
        print(f"\nudelete_calories - an unexpected error occurred: {e}")
