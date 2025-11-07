# HR-Attrition-Analytics Analysis & Dashboard
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12,6)

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
df = pd.read_csv('data/hr_attrition_data.csv')

# -------------------------
# 2️⃣ Basic Overview
# -------------------------
print(df.head())
print(df.info())
print(df.describe())

# Check nulls and duplicates
df = df.drop_duplicates()

# -------------------------
# 3️⃣ Attrition Analysis
# -------------------------
attrition_counts = df['Attrition'].value_counts()

plt.figure(figsize=(6,5))
sns.countplot(x='Attrition', data=df, palette='Set2')
plt.title('Attrition Count (Yes/No)')
plt.savefig('dashboard/attrition_count.png', bbox_inches='tight')
plt.show()

# Attrition by Department
plt.figure(figsize=(8,6))
sns.countplot(x='Department', hue='Attrition', data=df, palette='Set1')
plt.title('Attrition by Department')
plt.savefig('dashboard/attrition_department.png', bbox_inches='tight')
plt.show()

# Attrition by Job Role
plt.figure(figsize=(10,6))
sns.countplot(y='JobRole', hue='Attrition', data=df, palette='Set3')
plt.title('Attrition by Job Role')
plt.savefig('dashboard/attrition_jobrole.png', bbox_inches='tight')
plt.show()

# -------------------------
# 4️⃣ Numerical Analysis
# -------------------------
plt.figure(figsize=(8,6))
sns.boxplot(x='Attrition', y='Age', data=df, palette='Pastel1')
plt.title('Age Distribution by Attrition')
plt.savefig('dashboard/age_attrition.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='Attrition', y='YearsAtCompany', data=df, palette='Pastel2')
plt.title('Years at Company by Attrition')
plt.savefig('dashboard/years_attrition.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette='Pastel1')
plt.title('Monthly Income by Attrition')
plt.savefig('dashboard/income_attrition.png', bbox_inches='tight')
plt.show()

# -------------------------
# 5️⃣ Categorical Insights
# -------------------------
plt.figure(figsize=(6,5))
sns.countplot(x='OverTime', hue='Attrition', data=df, palette='coolwarm')
plt.title('OverTime vs Attrition')
plt.savefig('dashboard/overtime_attrition.png', bbox_inches='tight')
plt.show()

plt.figure(figsize=(6,5))
sns.countplot(x='Gender', hue='Attrition', data=df, palette='Set2')
plt.title('Gender vs Attrition')
plt.savefig('dashboard/gender_attrition.png', bbox_inches='tight')
plt.show()

# -------------------------
# 6️⃣ Polished Insights Summary
# -------------------------
# Calculate key metrics
dept_attrition = df.groupby('Department')['Attrition'].apply(lambda x: (x=='Yes').sum()).idxmax()
role_attrition = df.groupby('JobRole')['Attrition'].apply(lambda x: (x=='Yes').sum()).idxmax()
median_age_leave = df[df['Attrition']=='Yes']['Age'].median()
median_years_leave = df[df['Attrition']=='Yes']['YearsAtCompany'].median()
overtime_leave = df[df['Attrition']=='Yes']['OverTime'].value_counts().get('Yes', 0)
gender_leave = df[df['Attrition']=='Yes']['Gender'].value_counts().to_dict()

insights_text = f"""
# HR Attrition Insights - India

## Key Findings

1. **Total Attrition:** 
   - Yes: {attrition_counts.get('Yes',0)} employees
   - No: {attrition_counts.get('No',0)} employees

2. **Department Insights:**  
   - Highest attrition: {dept_attrition}

3. **Job Role Insights:**  
   - Highest attrition: {role_attrition}

4. **Age & Experience:**  
   - Median age of leaving employees: {median_age_leave} years  
   - Median years at company for leaving employees: {median_years_leave} years

5. **OverTime Impact:**  
   - Employees working overtime leaving: {overtime_leave} employees

6. **Gender Insights:**  
   - Attrition by gender: {gender_leave}

7. **Actionable Insight for HR:**  
   - Focus retention strategies on high-attrition departments, roles, and employees with overtime and mid-range experience.
"""

with open('insights/README.md', 'w') as f:
    f.write(insights_text)

print("✅ Dashboard charts saved in 'dashboard/' and polished insights written to 'insights/README.md'")
