import pandas as pd
import random
from datetime import datetime, timedelta
import os

# -------------------------
# 0️⃣ Create folders if not exist
# -------------------------
if not os.path.exists('data'):
    os.makedirs('data')

# -------------------------
# 1️⃣ Dataset setup
# -------------------------
num_rows = 3000
teams = ['Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Delhi Capitals', 'Rajasthan Royals',
         'Sunrisers Hyderabad', 'Punjab Kings']
venues = ['Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Delhi', 'Hyderabad', 'Jaipur', 'Pune']
players = [f'Player_{i}' for i in range(1, 101)]

start_date = datetime(2008, 4, 1)
dates = [start_date + timedelta(days=random.randint(0, 6300)) for _ in range(num_rows)]

# -------------------------
# 2️⃣ Generate dataset
# -------------------------
data = {
    'MatchID': [f'MATCH{str(i).zfill(4)}' for i in range(1, num_rows+1)],
    'Date': [d.strftime('%Y-%m-%d') for d in dates],
    'Season': [d.year for d in dates],
    'Venue': [random.choice(venues) for _ in range(num_rows)],
    'Team1': [random.choice(teams) for _ in range(num_rows)],
    'Team2': [random.choice(teams) for _ in range(num_rows)],
    'Winner': [random.choice(teams) for _ in range(num_rows)],
    'Margin': [random.randint(1,50) for _ in range(num_rows)],
    'MarginType': [random.choice(['runs','wickets']) for _ in range(num_rows)],
    'PlayerOfMatch': [random.choice(players) for _ in range(num_rows)],
    'RunsTeam1': [random.randint(80,250) for _ in range(num_rows)],
    'RunsTeam2': [random.randint(80,250) for _ in range(num_rows)],
    'WicketsTeam1': [random.randint(0,10) for _ in range(num_rows)],
    'WicketsTeam2': [random.randint(0,10) for _ in range(num_rows)],
}

df_ipl = pd.DataFrame(data)

# -------------------------
# 3️⃣ Save CSV
# -------------------------
df_ipl.to_csv('data/ipl_matches.csv', index=False)
print("✅ IPL dataset created: data/ipl_matches.csv")
