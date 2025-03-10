Pixar Film Analytics: A Deep Dive into Box Office, Ratings & Legacy
Project Overview
This project explores the financial and critical success of Pixar films over the past three decades, leveraging data from multiple sources to analyze box office performance, audience vs. critic approval, and key storytelling trends.

✔ Live Dashboard Link: Pixar Film Analytics Dashboard



Table of Contents
Problem Statement
Objective
Strategic Goals
Key Questions
Data Source
Dashboard Design
Film Overview
Film Performance & Audience Impact
The Pixar Formula
Insights & Findings
Tools Used
Development Process
Codes Used
Analysis & Insights
Key Takeaways
Recommendations
Conclusion
Connect with Me
Feedback & Suggestions
Problem Statement
Over the years, Pixar has set industry benchmarks with its storytelling and animation, yet:

Not all Pixar films achieve the same level of box office success or critical acclaim.
Audience approval does not always match critic scores—why?
Some films achieve higher profitability despite lower budgets, while others underperform.
A data-driven approach is needed to understand what makes a Pixar film successful and how different factors influence financial returns and audience reception.

Objective
Strategic Goals
Identify key drivers of financial success in Pixar films.
Analyze the impact of audience vs. critic ratings on box office performance.
Detect trends over time to understand the evolution of Pixar’s storytelling and commercial performance.
Provide actionable insights on which factors contribute to a Pixar film’s success.
Key Questions
✅ What is the relationship between box office revenue and audience/critic ratings?
✅ Do higher production budgets always lead to greater box office success?
✅ How do sequels compare to original films in revenue and approval ratings?
✅ What are the top-performing Pixar films financially and critically?

Data Source
Box Office Revenue & Budget: Industry financial reports
Audience Ratings: IMDb, Rotten Tomatoes, Metacritic, CinemaScore
Film Metadata: Pixar film database (years, genres, key contributors)
Award Wins/Nominations: Academy Awards & nominations
Data was cleaned and processed using Python (Pandas) and imported into Power BI for visualization.

Dashboard Design
1️⃣ Film Overview
📌 Purpose: Provides a high-level summary of each Pixar film’s financial and critical performance.

✔ Key Metrics (KPI Cards):

Release Date
Runtime
Box Office Revenue
IMDb Rating
Rotten Tomatoes Score
Oscar Wins & Nominations
✔ Visuals:
🎬 Radar Chart: How does the film compare across all rating platforms?
📊 Line Chart: Box office trends over time

2️⃣ Film Performance & Audience Impact
📌 Purpose: Investigates the relationship between box office performance and audience vs. critic approval.

✔ Key Metrics (KPI Cards):

ROI Ratio
US & Canada Revenue %
International Revenue %
Breakeven Success Rate
✔ Visuals:
📊 Stacked Column & Line Chart: Do high-grossing films also have high audience approval?
📊 Critic vs. Audience Ratings Chart: Do audiences and critics agree on Pixar films?

3️⃣ The Pixar Formula
📌 Purpose: What patterns make a Pixar film successful?

✔ Visuals:
📊 Trend Line Chart: How have Pixar films evolved financially & critically?
📊 Box Office vs. Budget Comparison: Do bigger budgets guarantee success?
📊 Scatter Plot: Does audience approval predict financial performance?

Tools Used
Tool	Purpose
Power BI	Data visualization & dashboard
Python (Pandas)	Data processing & cleaning
GitHub	Version control & documentation
Development Process
1️⃣ Data Cleaning & Transformation: Standardized film titles, removed inconsistencies.
2️⃣ Exploratory Data Analysis (EDA): Identified patterns & trends.
3️⃣ Visualization in Power BI: Designed interactive insights for analysis.
4️⃣ Final Optimization: Ensured seamless storytelling & data flow.

Codes Used
python
Copy
Edit
# Checking for missing values in dataset
import pandas as pd  

df = pd.read_csv("pixar_films.csv")  
print(df.isnull().sum())  
dax
Copy
Edit
# Calculate IMDb Rating (Trend Measure)
_Avg_IMDb_Trend = AVERAGE(pixarfilms[IMDb_Score])

# Calculate Total Worldwide Revenue
_Total_Worldwide_Revenue = 
SUMX(
    VALUES(pixarfilms[film]),
    CALCULATE(SUM(pixarfilms[box_office_worldwide]))
)
Analysis & Insights
Key Takeaways
Box office revenue does NOT always correlate with critical scores. Some critically acclaimed films (Ratatouille, Coco) had lower revenue than expected.
Audience ratings (IMDb, CinemaScore) are better predictors of financial success than critic scores.
Bigger budgets do not always mean higher revenue—films like Inside Out outperformed some higher-budget sequels.
Sequels perform well financially but often have lower critic scores (Cars 2, Lightyear).
Recommendations
✅ Focus on strong storytelling rather than inflating production budgets.
✅ Leverage audience engagement to predict box office performance.
✅ Strategic sequel planning: Not all franchises need continued installments.

Conclusion
💡 The Pixar Formula: Successful films balance emotional storytelling, audience engagement, and controlled budgets—not just high production costs or critic approval. 🚀

Connect with Me
📂 GitHub: github.com/aeronabrahan
🔗 LinkedIn: linkedin.com/in/jagabrahan
📧 Email: aerongabrahan@gmail.com

Feedback & Suggestions
This is my entry for the Maven Pixar Challenge, and I’d love to hear your thoughts! If you have any suggestions for improving my analysis, feel free to connect and share your feedback.

This README.md is now professional, concise, and insight-driven while covering everything from problem statement to key findings. This will help showcase your work at a high level while making it easy for others to understand the impact of your analysis. 🚀
