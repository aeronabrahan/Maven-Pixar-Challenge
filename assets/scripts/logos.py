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
