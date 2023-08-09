import os

def search_folder(directory, search_term):
    found_items = []
    for root, dirs, files in os.walk(directory):
        for item in files + dirs:
            if search_term.lower() in item.lower():
                found_items.append(os.path.join(root, item))
    return found_items

if __name__ == "__main__":
    search_directory = input("Enter the directory path to search: ")
    search_term = input("Enter the search term: ")
    search_results = search_folder(search_directory, search_term)

    if not search_results:
        print("No items found.")
    else:
        print("Search Results:")
        for item in search_results:
            if ".zip" in item:
                print(search_directory,item)
            else:
                print(item)
