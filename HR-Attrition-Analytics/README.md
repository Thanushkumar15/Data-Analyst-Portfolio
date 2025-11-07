# HR Attrition Analytics

## Overview
Analyzed HR data to identify patterns leading to employee attrition and help improve retention strategies.

## Dataset
- **File:** `data/hr_attrition.csv`
- Columns include EmployeeID, Age, Department, JobRole, MonthlyIncome, Attrition, PerformanceRating, etc.
- ~3,000 employee records

## Key Analyses
- Attrition rate per department
- Monthly income vs attrition
- Performance rating analysis
- Correlation between satisfaction, tenure, and attrition

## Dashboards

**Python Dashboards (static charts):**
Saved in `dashboard/`:
- `attrition_by_department.png`
- `income_vs_attrition.png`
- `performance_analysis.png`

**Power BI Dashboards (interactive):**
- Attrition per Department (Donut/Pie)
- Income vs Attrition (Scatter)
- Performance vs Attrition (Column)
- Attrition by Job Role (Bar)  
*(Slicers: Department, Job Role, Age Range)*

## Insights
Saved in `insights/README.md`:
- Departments with highest attrition identified
- Key factors influencing attrition highlighted
- Recommendations for HR interventions

## Tech Stack
- Python (pandas, matplotlib, seaborn)
- Power BI
- CSV data handling
- Data cleaning & visualization
