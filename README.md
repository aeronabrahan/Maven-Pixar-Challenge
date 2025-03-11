# Maven Pixar Challenge: Analyzing Pixar's Legacy Through Data

---

## Project Overview
This project explores Pixar's cinematic legacy by analyzing key financial, critical, and audience-based metrics. By leveraging interactive visualizations in Power BI, this dashboard provides insights into Pixar’s box office success, storytelling patterns, and critical reception over the past 30 years. 

✔ Live Dashboard Link: [Pixar Data Analysis](https://app.powerbi.com/reportEmbed?reportId=b4b8537c-502f-42be-ae2f-33c5b1a65b01&autoAuth=true&ctid=254ba93e-1f6f-48f3-90e6-e2766664b477)

![Power BI Dashboard](assets/images/dashboard.gif)

---

- ## Table of Contents
- [Problem Statement](#problem-statement)
- [Objective](#objective)
  - [Strategic Goals](#strategic-goals)
  - [Challenges](#challenges)
  - [Ideal Solution](#ideal-solution)
- [User Story](#user-story)
- [Data Source](#data-source)
- [Dashboard Design](#dashboard-design)
  - [Film Overview](#film-overview)
  - [Film Performance & Audience Impact](#film-performance--audience-impacat)
  - [Pixar's Greatest Hits & Storytelling](#pixars-greatest-hits--storytelling)
  - [The Pixar Formula](#the-pixar-formula)
- [Tools Used](#tools-used)
- [Development Process](#development-process)
- [Codes Used](#codes-used)
- [Analysis & Insights](#analysis--insights)
  - [Key Insights](#key-insights)
  - [Recommendations](#recommendations)
- [Feedback & Suggestions](#feedback--suggestions)
- [Connect with Me](#connect-with-me)

---

## Problem Statement
Pixar has produced some of the most iconic animated films, but not all Pixar movies achieve both critical and commercial success. This project aims to answer key questions:
- Which Pixar films generated the highest box office revenue?
- How do critic and audience scores correlate with financial performance?
- What storytelling patterns contribute to Pixar's biggest hits?
- Which directors have the best track record based on audience reception and revenue?

A data-driven approach is required to identify patterns behind Pixar’s biggest successes and rare misses.

---

## Objective

### Strategic Goals
- Identify Pixar's highest-grossing films and analyze their success factors.  
- Compare audience ratings vs. critic scores to determine which is more influential.  
- Discover the storytelling patterns behind Pixar's most successful films.  
- Analyze the financial impact of sequels vs. original films.  

### Challenges
- Some critically acclaimed films did not perform well financially (WALL-E, Ratatouille).
- Some high-revenue films received mixed audience reception (Cars 2, Lightyear).
- Audience and critic scores often disagree—which metric is a better predictor of success?

### Ideal Solution
A Power BI dashboard that provides:
- Box office revenue trends across Pixar’s entire film catalog.
- Correlation analysis between critic/audience scores and financial success.
- A storytelling framework that defines Pixar’s winning formula.
- Best-performing Pixar directors based on revenue and audience ratings.

---

## User Story
“As a data-driven film analyst, I want to explore Pixar’s financial and critical success over the years so that I can identify patterns that contribute to a hit animated film.”

“Pixar films have shaped animation history, but not all movies achieve the same level of box office success. I want to understand the factors behind Pixar’s biggest hits, uncover hidden storytelling patterns, and analyze audience engagement trends.”

---

## Data Source
- Pixar Film Data (1995-2024): Includes financial performance, audience scores, and critic reviews.
- Pixar People Dataset: Director information linked to each film.
- Box Office & Ratings Data: Includes worldwide revenue, IMDb, Rotten Tomatoes, and Metacritic scores.
- Academy Awards Data: Tracks Pixar’s Oscar nominations and wins.

---

## Dashboard Design

### Film Overview
- Provides basic film details, including release date, genre, runtime, and key creators.
- Displays box office revenue, critic scores, and audience ratings for each film.

### Film Performance & Audience Impact
- Compares box office revenue with audience scores to determine which films were commercially and critically successful.
- ROI Analysis of each film’s profitability.
- Critic vs. Audience Ratings: Identifies discrepancies between critic and public reception.

### Pixar’s Greatest Hits & Storytelling
- Top-Grossing Pixar Films: Ranked by worldwide revenue.
- Best Pixar Directors: Ranked by average audience ratings and revenue.
- The Evolution of Pixar’s Legacy: Tracks box office trends over time.

### The Pixar Formula
- Heatmap Analysis: Identifies storytelling elements shared by Pixar’s most successful films.
- Quadrant Analysis: Classifies Pixar films into four categories based on box office performance and audience approval.
- Box Office vs. Budget Comparison: Evaluates the financial efficiency of Pixar films.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Power BI | Data visualization and interactive dashboard |
| Python (Pandas) | Data transformation and cleaning |
| SQL | Querying structured film data |
| GitHub | Version control and documentation |

---

## Development Process

1. Extract and clean data from multiple sources.
2. Merge and transform datasets to align financial and critical metrics.
3. Develop DAX measures to calculate performance indicators.
4. Build and format Power BI visuals for storytelling insights.
5. Ensure interactivity and drill-through functionality for deeper analysis.

---

## Codes Used

### logos.py
- For creating the pixar_logos.csv
```python
import pandas as pd
import urllib.parse  # For URL encoding

# ✅ Define the Base URL of Your GitHub Repository
GITHUB_BASE_URL = "https://raw.githubusercontent.com/aeronabrahan/Maven-Pixar-Challenge/main/assets/images/logos/"

# ✅ List of Pixar Films (Ensure These Match the Exact Image Filenames)
pixar_films = [
    "Toy Story", "A Bug's Life", "Toy Story 2", "Monsters, Inc.", "Finding Nemo", "The Incredibles",
    "Cars", "Ratatouille", "WALL-E", "Up", "Toy Story 3", "Cars 2", "Brave", "Monsters University",
    "Inside Out", "The Good Dinosaur", "Finding Dory", "Cars 3", "Coco", "Incredibles 2",
    "Toy Story 4", "Onward", "Soul", "Luca", "Turning Red", "Lightyear", "Elemental", "Inside Out 2"
]

# ✅ Function to Convert Film Titles to GitHub-Compatible URLs
def format_url(film_name):
    encoded_film_name = urllib.parse.quote(film_name)  # Convert spaces to %20
    return f"{GITHUB_BASE_URL}{encoded_film_name}.png"

# ✅ Generate Data for CSV
logo_data = [{"Film": film, "Logo URL": format_url(film)} for film in pixar_films]

# ✅ Convert to Pandas DataFrame
df_logos = pd.DataFrame(logo_data)

# ✅ Save to CSV
csv_file_path = r"C:\Users\Aeron\Desktop\Aeron\0 Work\_Data Projects\Maven Analytics Challenge\Maven Pixar Challenge\datasets\pixar_logos.csv"
df_logos.to_csv(csv_file_path, index=False, encoding="utf-8")

print(f"✅ Pixar Logos CSV Saved at: {csv_file_path}")
print(df_logos.head())  # Display sample output
```

### pixar.py
- For scraping the posters and saving as csv
```python
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
```
### dataprep.py
- For combining all dataset into pixarfilms.csv
```python
import pandas as pd
import os

# ✅ Define base file path
base_path = r"C:\Users\Aeron\Desktop\Aeron\0 Work\_Data Projects\Maven Analytics Challenge\Maven Pixar Challenge\datasets"

# ✅ Load datasets with UTF-8 encoding to prevent Unicode mismatches
pixar_films = pd.read_csv(os.path.join(base_path, "pixar_films.csv"), dtype=str, encoding="utf-8")
pixar_people = pd.read_csv(os.path.join(base_path, "pixar_people.csv"), dtype=str, encoding="utf-8")
public_response = pd.read_csv(os.path.join(base_path, "public_response.csv"), dtype=str, encoding="utf-8")
box_office = pd.read_csv(os.path.join(base_path, "box_office.csv"), dtype=str, encoding="utf-8")
academy = pd.read_csv(os.path.join(base_path, "academy.csv"), dtype=str, encoding="utf-8")
genres = pd.read_csv(os.path.join(base_path, "genres.csv"), dtype=str, encoding="utf-8")
pixar_posters = pd.read_csv(os.path.join(base_path, "pixar_posters.csv"), dtype=str, encoding="utf-8")
pixar_logos = pd.read_csv(os.path.join(base_path, "pixar_logos.csv"), dtype=str, encoding="utf-8")

# ✅ Store datasets in a dictionary for batch processing
datasets = {
    "pixar_films": pixar_films,
    "pixar_people": pixar_people,
    "public_response": public_response,
    "box_office": box_office,
    "academy": academy,
    "genres": genres,
    "pixar_posters": pixar_posters,
    "pixar_logos": pixar_logos,
}

# ✅ Standardizing column names (lowercase, no spaces)
for name, df in datasets.items():
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ✅ Standardizing film titles across datasets (strip spaces, **KEEP original case**)
for name, df in datasets.items():
    if "film" in df.columns:
        df["film"] = df["film"].str.strip()

# ✅ Fixing column inconsistencies
pixar_posters.rename(columns={"title": "film"}, inplace=True)
pixar_logos.rename(columns={"film": "film", "logo_url": "logo_url"}, inplace=True)

# ✅ Removing any leading/trailing spaces in film names before merging
for name, df in datasets.items():
    if "film" in df.columns:
        df["film"] = df["film"].str.strip()

# ✅ Handling missing values
box_office["budget"] = box_office["budget"].where(pd.notna(box_office["budget"]), None)  # ✅ Replacing NaN with NULL
public_response["cinema_score"] = public_response["cinema_score"].fillna("N/A")  # ✅ Fix for missing values

# ✅ Checking for duplicate film entries in the main dataset
duplicate_titles = pixar_films[pixar_films.duplicated(subset=["film"], keep=False)]
if not duplicate_titles.empty:
    print("\n⚠️ Warning: Duplicate film entries found. Removing duplicates.")
    pixar_films.drop_duplicates(subset=["film"], keep="first", inplace=True)

# ✅ Ensure all datasets have unique "film" values before merging
pixar_films.drop_duplicates(subset=["film"], keep="first", inplace=True)
pixar_posters.drop_duplicates(subset=["film"], keep="first", inplace=True)
pixar_logos.drop_duplicates(subset=["film"], keep="first", inplace=True)

# ✅ Convert to **lowercase only for merging** to prevent mismatches
pixar_films["film_lower"] = pixar_films["film"].str.lower()
pixar_posters["film_lower"] = pixar_posters["film"].str.lower()
pixar_logos["film_lower"] = pixar_logos["film"].str.lower()

# ✅ Merging all datasets using "film_lower" as the key
merged_df = (
    pixar_films
    .merge(box_office, on="film", how="left")
    .merge(public_response, on="film", how="left")
    .merge(academy, on="film", how="left")
    .merge(genres, on="film", how="left")
    .merge(pixar_posters, on="film_lower", how="left")  # ✅ Merge using lowercase
    .merge(pixar_logos, on="film_lower", how="left")  # ✅ Merge logos to add Logo URL
)

# ✅ If 'film' is missing, recover it from 'film_lower'
if "film" not in merged_df.columns and "film_lower" in merged_df.columns:
    merged_df["film"] = merged_df["film_lower"].str.title()

# ✅ Drop the temporary "film_lower" column if it exists
if "film_lower" in merged_df.columns:
    merged_df.drop(columns=["film_lower"], inplace=True)

# ✅ Drop any extra "_x" columns caused by merging
for col in merged_df.columns:
    if col.endswith("_x"):
        merged_df.drop(columns=[col], inplace=True)

# ✅ Ensuring missing poster URLs and years for A Bug’s Life & WALL-E are populated
films_to_fix = ["A Bug's Life", "WALL-E"]
for film in films_to_fix:
    poster_row = pixar_posters[pixar_posters["film"].str.lower() == film.lower()]

    if not poster_row.empty:
        if merged_df.loc[merged_df["film"].str.lower() == film.lower(), "poster_url"].isna().any():
            merged_df.loc[merged_df["film"].str.lower() == film.lower(), "poster_url"] = poster_row["poster_url"].values[0]
        if merged_df.loc[merged_df["film"].str.lower() == film.lower(), "year"].isna().any():
            merged_df.loc[merged_df["film"].str.lower() == film.lower(), "year"] = poster_row["year"].values[0]

# ✅ Reorder columns to make "film" the second column after "number"
if "number" in merged_df.columns and "film" in merged_df.columns:
    columns_order = ["number", "film"] + [col for col in merged_df.columns if col not in ["number", "film"]]
    merged_df = merged_df[columns_order]

# ✅ Save the cleaned dataset as "pixarfilms.csv"
output_path = os.path.join(base_path, "pixarfilms.csv")
merged_df.to_csv(output_path, index=False, encoding="utf-8")

print(f"\n✅ Data Cleaning & Merging Completed! File saved as: {output_path}")

# ✅ Display the first few rows of the cleaned dataset
print("\n🎬 Sample of Cleaned Data:")
print(merged_df.head())
```

---

## Analysis & Insights

### Key Insights
- Sequels generate revenue but do not always score well with audiences (e.g., Cars 2, Lightyear).
- Critic scores do not always predict box office success (Ratatouille, WALL-E).
- Pixar’s highest-grossing films often balance strong storytelling with emotional depth (Toy Story 3, Inside Out).
- The best Pixar directors have consistent audience approval and strong box office revenue.

### Recommendations
- Focus on original storytelling concepts rather than relying on sequels for box office success.
- Leverage audience engagement metrics to refine marketing strategies for future releases.
- Maintain Pixar’s core storytelling formula while innovating in new genres.

---

## Feedback & Suggestions
I’d love to hear your feedback and suggestions to improve this analysis. Feel free to reach out and share your insights!

---

## Connect with Me

- GitHub Profile: [github.com/aeronabrahan](https://github.com/aeronabrahan)
- LinkedIn Profile: [linkedin.com/in/jagabrahan](https://linkedin.com/in/jagabrahan)
- Email Address: [aerongabrahan@gmail.com](mailto:aerongabrahan@gmail.com)
