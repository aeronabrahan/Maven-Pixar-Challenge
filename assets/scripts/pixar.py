# Updated script to fetch only Pixar movie posters from Wikipedia

import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

# Define Wikipedia Base URL
WIKI_BASE_URL = "https://en.wikipedia.org/wiki/"

# Define correct Wikipedia titles & release years
correct_titles = {
    "Toy Story": ("Toy_Story", 1995),
    "A Bug's Life": ("A_Bug%27s_Life", 1998),
    "Toy Story 2": ("Toy_Story_2", 1999),
    "Monsters, Inc.": ("Monsters,_Inc.", 2001),
    "Finding Nemo": ("Finding_Nemo", 2003),
    "The Incredibles": ("The_Incredibles", 2004),
    "Cars": ("Cars_(film)", 2006),
    "Ratatouille": ("Ratatouille_(film)", 2007),
    "WALL-E": ("WALL-E", 2008),
    "Up": ("Up_(2009_film)", 2009),
    "Toy Story 3": ("Toy_Story_3", 2010),
    "Cars 2": ("Cars_2", 2011),
    "Brave": ("Brave_(2012_film)", 2012),
    "Monsters University": ("Monsters_University", 2013),
    "Inside Out": ("Inside_Out_(2015_film)", 2015),
    "The Good Dinosaur": ("The_Good_Dinosaur", 2015),
    "Finding Dory": ("Finding_Dory", 2016),
    "Cars 3": ("Cars_3", 2017),
    "Coco": ("Coco_(2017_film)", 2017),
    "Incredibles 2": ("Incredibles_2", 2018),
    "Toy Story 4": ("Toy_Story_4", 2019),
    "Onward": ("Onward_(film)", 2020),
    "Soul": ("Soul_(2020_film)", 2020),
    "Luca": ("Luca_(2021_film)", 2021),
    "Turning Red": ("Turning_Red", 2022),
    "Lightyear": ("Lightyear_(film)", 2022),
    "Elemental": ("Elemental_(2023_film)", 2023),
    "Inside Out 2": ("Inside_Out_2", 2024),
}

# Function to extract movie poster URL from Wikipedia
def get_poster_url(wiki_title):
    try:
        response = requests.get(WIKI_BASE_URL + wiki_title, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        img_tag = soup.find("table", class_="infobox").find("img")
        return "https:" + img_tag["src"] if img_tag else None
    except Exception as e:
        print(f"❌ Error fetching poster for {wiki_title}: {e}")
        return None

# Fetch poster URLs dynamically
pixar_films = []
for title, (wiki_title, year) in correct_titles.items():
    print(f"🔎 Fetching poster for: {title} ({year})...")
    poster_url = get_poster_url(wiki_title)
    pixar_films.append({"Title": title, "Year": year, "Poster_URL": poster_url})
    
    # Adding a delay to avoid request blocks
    time.sleep(2)

# Convert to DataFrame and Save CSV Locally
df_pixar = pd.DataFrame(pixar_films)
csv_file_path = r"C:\Users\Aeron\Desktop\Aeron\0 Work\_Data Projects\Maven Analytics Challenge\Maven Pixar Challenge\datasets\pixar_posters.csv"
df_pixar.to_csv(csv_file_path, index=False)