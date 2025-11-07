# IPL Performance Analytics

## Overview
Analyzed IPL match data to uncover insights about team performance, players, and venues. Provides interactive dashboards and actionable insights.

## Dataset
- **File:** `data/ipl_matches.csv`
- Columns: MatchID, Date, Season, Venue, Team1, Team2, Winner, Margin, MarginType, PlayerOfMatch, RunsTeam1, RunsTeam2, WicketsTeam1, WicketsTeam2
- ~3,000 matches from 2008 to 2025

## Key Analyses
- Total matches per team
- Wins per team
- Top 10 players of the match
- Venue-wise wins
- Season-wise performance trends

## Dashboards

**Python Dashboards (static charts):**
Saved in `dashboard/`:
- `total_matches_per_team.png`
- `total_wins_per_team.png`
- `top_players_of_match.png`
- `venue_wins_per_team.png`

**Power BI Dashboards (interactive):**
- Total Wins per Team (Bar)  
- Top 10 Players of the Match (Bar)  
- Venue-wise Wins (Stacked Bar)  
- Total Matches per Team (Column)  
- Runs Trend per Season (Line)  
*(Slicers: Season, Team, Venue)*

## Insights
Saved in `insights/README.md`:
- Most wins: [Team Name]
- Most matches played: [Team Name]
- Top player of the match: [Player Name]
- Venue with most matches: [Venue]

## Tech Stack
- Python (pandas, matplotlib, seaborn)
- Power BI
- CSV data handling
- Data cleaning & visualization
