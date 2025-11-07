# IPL-Performance-Analytics Analysis & Dashboard
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------
# 0️⃣ Folders Setup
# -------------------------
if not os.path.exists('dashboard'):
    os.makedirs('dashboard')

if not os.path.exists('insights'):
    os.makedirs('insights')

# -------------------------
# 1️⃣ Load dataset
# -------------------------
df = pd.read_csv('data/ipl_matches.csv')

# Ensure 'Date' is datetime
df['Date'] = pd.to_datetime(df['Date'])

# -------------------------
# 2️⃣ Quick overview
# -------------------------
print(df.head())
print(df.info())
print(df.describe())

# -------------------------
# 3️⃣ Total Matches per Team
# -------------------------
teams = df['Team1'].tolist() + df['Team2'].tolist()
team_matches = pd.Series(teams).value_counts()

plt.figure(figsize=(10,6))
sns.barplot(x=team_matches.index, y=team_matches.values, palette='Blues_d')
plt.title('Total Matches Played per Team')
plt.xticks(rotation=45)
plt.savefig('dashboard/total_matches_per_team.png', bbox_inches='tight')
plt.show()

# -------------------------
# 4️⃣ Wins per Team
# -------------------------
wins = df['Winner'].value_counts()

plt.figure(figsize=(10,6))
sns.barplot(x=wins.index, y=wins.values, palette='Greens_d')
plt.title('Total Wins per Team')
plt.xticks(rotation=45)
plt.savefig('dashboard/total_wins_per_team.png', bbox_inches='tight')
plt.show()

# -------------------------
# 5️⃣ Top Players of the Match
# -------------------------
top_players = df['PlayerOfMatch'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_players.values, y=top_players.index, palette='viridis')
plt.title('Top 10 Players of the Match Awards')
plt.savefig('dashboard/top_players_of_match.png', bbox_inches='tight')
plt.show()

# -------------------------
# 6️⃣ Venue-wise Wins
# -------------------------
venue_wins = df.groupby('Venue')['Winner'].value_counts().unstack().fillna(0)

venue_wins.plot(kind='bar', stacked=True, figsize=(12,6), colormap='tab20')
plt.title('Venue-wise Wins per Team')
plt.xlabel('Venue')
plt.ylabel('Wins')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dashboard/venue_wins_per_team.png')
plt.show()

# -------------------------
# 7️⃣ Polished Insights Summary
# -------------------------
most_wins_team = wins.idxmax()
most_matches_team = team_matches.idxmax()
top_player = top_players.idxmax()
top_venue = df['Venue'].value_counts().idxmax()

insights_text = f"""
# IPL Performance Analytics - Insights

## Key Findings

1. **Most Wins:** {most_wins_team}  
2. **Most Matches Played:** {most_matches_team}  
3. **Top Player of the Match:** {top_player}  
4. **Venue with Most Matches:** {top_venue}  

## Actionable Insights:

- Focus marketing and fan engagement on top-performing teams.  
- Identify venues that host more matches for operational planning.  
- Highlight star players in promotions and content for higher engagement.
"""

with open('insights/README.md', 'w') as f:
    f.write(insights_text)

print("✅ Dashboard charts saved in 'dashboard/' and insights written to 'insights/README.md'")
