import urllib.request
from PIL import Image
from  main import response

def  print_all_icons():
    emojis = response.json()
    icon_names = emojis.keys()
    for i, icon_name in enumerate(icon_names):
        print(i,icon_name)
    return icon_names

def search_icons_by_keyword():
    icon_search = input("enter a search value: ")
    emojis = response.json()
    icon_names = [icon for icon in emojis.keys() if icon_search.lower() in icon.lower()]
    if len(icon_names) > 0:
        for i, icon_name in enumerate(icon_names):
            print(i,icon_name)
    else:
        print("not Found🤔")
    return icon_names

def display_icon(icon_list, icon_name):
    if icon_name in icon_list:
        urllib.request.urlretrieve(response.json()[icon_name], "img.png")
        img = Image.open("img.png")
        img.show()
    else:
        print("😔Icon name does not exist in list...")