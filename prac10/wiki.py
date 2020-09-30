import wikipedia
def search_WIKIPEDIA():
    search_phrase=input("Enter search")
    print(wikipedia.summary(search_phrase))
    page=wikipedia.page(search_phrase)
    print("Page Title:", page.title)
    print("Page Content:", page.content)
    print("Page Image:", page.images[0])
    print("Page Link:", page.links[0])
    print("Page URl:",page.url)       

    search_phrase = input("Enter search: ")
    print("Thank you!")
search_WIKIPEDIA()