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