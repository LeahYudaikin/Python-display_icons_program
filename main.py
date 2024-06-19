import requests

import exceptions
import functions

response = requests.get("https://api.github.com/emojis")

def main():
    try:
        if response.status_code != 200:
            raise exceptions.status_error("❗ ")
        print("choice: 1.Print all icons, 2.Search icons by keyword")
        choice = int(input())
        if choice==1 or choice==2:
            if choice == 1:
                icon_list = functions.print_all_icons()
            elif choice == 2:
                icon_list = functions.search_icons_by_keyword()
            icon_name = input("✏️choose an icon_name: ")
            functions.display_icon(icon_list, icon_name)
        else:
            print("⚠️Must choose 1/2")
    except exceptions.status_error as e:
        print(e)

if __name__ == "__main__":
    main()