#whatever strings we have python go to google and give top 5 results from the google,bing,firefox
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import webbrowser

def google_search(query, num_results=5):
    try:
        # Perform the Google search and fetch top num_results results
        search_results = [result for result in search(query, num_results=num_results)]
        
        # Print the search results
        print(f"Top {num_results} search results from Google:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result}")
    except Exception as e:
        print("An error occurred during Google search:", e)

   

def bing_search(query, num_results=5):
    try:
        # Perform the Bing search
        url = f"https://www.bing.com/search?q={query}&count={num_results}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("li", class_="b_algo")
        print("\nTop 5 search results from Bing:")
        for i, result in enumerate(search_results[:num_results], start=1):
            link = result.find("a").get("href")
            print(f"{i}. {link}")
    except Exception as e:
        print("An error occurred during Bing search:", e)

def firefox_search(query,num_results=5):
    try:
        # Open Firefox browser with the search query
        url = f"https://www.firefox.com/search?q={query}&count={num_results}"
        webbrowser.get(url)  #need to work in this line after downloading firefox browser
        print("\nTop 5 search results from Firefox:")
    except Exception as e:
        print("An error occurred during Firefox search:", e)

if __name__ == "__main__":
    query = input("Enter your search query: ")
    google_search(query)
    bing_search(query)
    firefox_search(query)
