import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page config to make the layout wide
st.set_page_config(layout="wide")

# Load dataset
data = pd.read_csv('employee.csv')  # Pastikan untuk mengganti dengan jalur dataset Anda

# Existing visualizations (questions 1–10)

# 1. Comparison of Active and Exiting Employees
attrition_comparison = data['Attrition'].value_counts().reset_index()
attrition_comparison.columns = ['Attrition', 'Count']
fig1 = px.bar(attrition_comparison, 
              x='Attrition', 
              y='Count', 
              color='Attrition', 
              color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'}, 
              labels={'Attrition': 'Attrition Status', 'Count': 'Number of Employees'},
              title="Comparison of Active and Exiting Employees")

# 2. Employees Leaving by Gender
attrition_gender = data.groupby(['Gender', 'Attrition']).size().reset_index(name='Count')
fig2 = px.bar(attrition_gender, 
              x='Gender', 
              y='Count', 
              color='Attrition', 
              barmode='group', 
              color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'}, 
              labels={'Attrition': 'Attrition Status', 'Count': 'Count'},
              title="Employees Leaving by Gender")

# 3. Attrition by Business Travel
attrition_business_travel = data.groupby(['BusinessTravel', 'Attrition']).size().reset_index(name='Count')
fig3 = px.bar(attrition_business_travel, 
              x='BusinessTravel', 
              y='Count', 
              color='Attrition', 
              barmode='group', 
              color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'}, 
              labels={'Attrition': 'Attrition Status', 'Count': 'Count'},
              title="Attrition by Business Travel")

# 4. Effect of Distance From Home on Attrition (Yes and No)
fig_yes = px.histogram(data[data['Attrition'] == 'Yes'], 
                       x="DistanceFromHome", 
                       color="Attrition", 
                       barmode="overlay", 
                       color_discrete_map={"Yes": "#FF6347"},
                       title="Effect of Distance From Home on Attrition (Yes)", 
                       labels={"DistanceFromHome": "Distance From Home"})

fig_no = px.histogram(data[data['Attrition'] == 'No'], 
                      x="DistanceFromHome", 
                      color="Attrition", 
                      barmode="overlay", 
                      color_discrete_map={"No": "#4682B4"},
                      title="Effect of Distance From Home on Attrition (No)", 
                      labels={"DistanceFromHome": "Distance From Home"})

# 5. Attrition Comparison by Department
attrition_comparison_dept = data.groupby(['Department', 'Attrition']).size().reset_index(name='Count')
fig5 = px.bar(attrition_comparison_dept, 
              x='Department', 
              y='Count', 
              color='Attrition', 
              barmode='group', 
              title="Attrition Comparison by Department", 
              labels={"Count": "Number of Employees", "Department": "Department", "Attrition": "Attrition Status"},
              color_discrete_map={"Yes": "#FF6347", "No": "#4682B4"})

# 6. Attrition Count by Job Role
attrition_yes_count = data[data['Attrition'] == 'Yes'].groupby('JobRole').size().reset_index(name='Attrition Count')
fig6 = px.bar(attrition_yes_count, 
              x='Attrition Count', 
              y='JobRole', 
              orientation='h', 
              title='Attrition Count by Job Role',
              labels={'Attrition Count': 'Number of Attrition', 'JobRole': 'Job Role'})

# 7. Age Distribution by Attrition Status
fig7 = px.histogram(data, 
                    x='Age', 
                    color='Attrition', 
                    barmode='overlay', 
                    title='Age Distribution by Attrition Status',
                    labels={'Attrition': 'Attrition', 'Age': 'Age'},
                    color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'})

# 8. Monthly Income Distribution by Attrition Status
fig8 = px.histogram(data, 
                    x='MonthlyIncome', 
                    color='Attrition', 
                    barmode='overlay',
                    title="Monthly Income Distribution by Attrition Status",
                    labels={'Attrition': 'Attrition', 'MonthlyIncome': 'Monthly Income'},
                    color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'})

# 9. Relationship between Monthly Income and Hourly Rate by Attrition Status and Department
fig9 = px.scatter(data, 
                  x='MonthlyIncome', 
                  y='HourlyRate', 
                  color='Attrition', 
                  symbol='Department', 
                  title="Relationship between Monthly Income and Hourly Rate by Attrition Status and Department",
                  labels={'MonthlyIncome': 'Monthly Income', 'HourlyRate': 'Hourly Rate'})

# 10. Attrition Rate by Education Field
attrition_by_education = data.groupby(['EducationField', 'Attrition']).size().reset_index(name='Count')
attrition_by_education['Total'] = attrition_by_education.groupby('EducationField')['Count'].transform('sum')
attrition_by_education['AttritionRate'] = attrition_by_education['Count'] / attrition_by_education['Total']
attrition_yes_education = attrition_by_education[attrition_by_education['Attrition'] == 'Yes']
fig10 = px.bar(attrition_yes_education, 
               x='EducationField', 
               y='AttritionRate', 
               color='EducationField', 
               title='Attrition Rate by Education Field',
               labels={'AttritionRate': 'Attrition Rate', 'EducationField': 'Education Field'},
               color_discrete_map={
                   'Life Sciences': '#FF6347', 
                   'Other': '#4682B4', 
                   'Medical': '#FFD700', 
                   'Marketing': '#32CD32', 
                   'Technical Degree': '#8A2BE2', 
                   'Human Resources': '#FF4500'
               })

# 11. Attrition Rate by Overtime Status
attrition_overtime = data.groupby(['OverTime', 'Attrition']).size().reset_index(name='Count')
attrition_overtime['Total'] = attrition_overtime.groupby('OverTime')['Count'].transform('sum')
attrition_overtime['AttritionRate'] = attrition_overtime['Count'] / attrition_overtime['Total']
attrition_yes_overtime = attrition_overtime[attrition_overtime['Attrition'] == 'Yes']
fig11 = px.bar(attrition_yes_overtime, 
               x='OverTime', 
               y='AttritionRate', 
               color='OverTime', 
               title='Attrition Rate by Overtime Status',
               labels={'AttritionRate': 'Attrition Rate', 'OverTime': 'Overtime Status'},
               color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'})

# 12. Attrition Rate by Work-Life Balance
work_life_attrition_rate = data.groupby('WorkLifeBalance')['Attrition'].value_counts(normalize=True).unstack().fillna(0)
work_life_attrition_rate = work_life_attrition_rate['Yes']
fig12 = px.bar(work_life_attrition_rate,
               x=work_life_attrition_rate.index,
               y=work_life_attrition_rate.values,
               labels={'x': 'Work Life Balance', 'y': 'Attrition Rate'},
               title="Attrition Rate by Work-Life Balance")

# 13. Attrition Based on Overtime
overtime_attrition = data.groupby(['OverTime', 'Attrition']).size().reset_index(name='Count')
fig13 = px.bar(overtime_attrition,
               x='OverTime',
               y='Count',
               color='Attrition',
               title="Attrition Based on Overtime",
               labels={'OverTime': 'Overtime', 'Attrition': 'Attrition', 'Count': 'Count'},
               color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'},
               barmode='group')

# 14. Attrition Rate by Environment Satisfaction
env_satisfaction_attrition_rate = data.groupby('EnvironmentSatisfaction')['Attrition'].value_counts(normalize=True).unstack().fillna(0)
env_satisfaction_attrition_rate = env_satisfaction_attrition_rate['Yes']
fig14 = px.bar(env_satisfaction_attrition_rate,
               x=env_satisfaction_attrition_rate.index,
               y=env_satisfaction_attrition_rate.values,
               labels={'x': 'Environment Satisfaction', 'y': 'Attrition Rate'},
               title="Attrition Rate by Environment Satisfaction")

# 15. Attrition Rate by Job Satisfaction
job_satisfaction_attrition_rate = data.groupby('JobSatisfaction')['Attrition'].value_counts(normalize=True).unstack().fillna(0)
job_satisfaction_attrition_rate = job_satisfaction_attrition_rate['Yes']
fig15 = px.bar(job_satisfaction_attrition_rate,
               x=job_satisfaction_attrition_rate.index,
               y=job_satisfaction_attrition_rate.values,
               labels={'x': 'Job Satisfaction', 'y': 'Attrition Rate'},
               title="Attrition Rate by Job Satisfaction")

# 16. distribution of years of experience for employees who left (Attrition = 'Yes') and stayed (Attrition = 'No')
fig = px.histogram(data, 
                   x='YearsAtCompany', 
                   color='Attrition', 
                   barmode='overlay',
                   title="Distribution of Work Experience by Attrition",
                   labels={'YearsAtCompany': 'Years at Company', 'Attrition': 'Attrition'},
                   color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'},
                   nbins=15,  # You can adjust the number of bins
                   histfunc='count')

# 17. Attrition Comparison by Work Experience (Total Working Years)
attrition_comparison = data.groupby(['TotalWorkingYears', 'Attrition']).size().unstack().fillna(0)

# Creating a line plot to show attrition comparison by work experience
fig = px.line(attrition_comparison,
              x=attrition_comparison.index,
              y=['Yes', 'No'],
              labels={'TotalWorkingYears': 'Total Working Years', 'value': 'Count'},
              title="Attrition Comparison by Work Experience (Total Working Years)",
              markers=True)

# 18. Attrition Count by Education Level
attrition_counts_education = data.groupby('Education')['Attrition'].value_counts().unstack().fillna(0)

# Create a bar plot with separate bars for each 'Yes' and 'No' attrition status
fig = px.bar(attrition_counts_education,
             x=attrition_counts_education.index,
             y=['Yes', 'No'],
             labels={'Education': 'Education Level', 'value': 'Count', 'variable': 'Attrition'},
             title="Attrition Count by Education Level",
             color='variable',
             color_discrete_map={'Yes': '#FF6347', 'No': '#4682B4'},
             barmode='group')  # Grouped bars instead of stacked


# Create a sidebar with the questions
question = st.sidebar.selectbox("Choose a question to visualize", [
    "Comparison of Active and Exiting Employees",
    "Employees Leaving by Gender",
    "Attrition by Business Travel",
    "Effect of Distance From Home on Attrition (Yes and No)",
    "Attrition Comparison by Department",
    "Attrition Count by Job Role",
    "Age Distribution by Attrition Status",
    "Monthly Income Distribution by Attrition Status",
    "Relationship between Monthly Income and Hourly Rate by Attrition Status and Department",
    "Attrition Rate by Education Field",
    "Attrition Rate by Overtime Status",
    "Attrition Rate by Work-Life Balance",
    "Attrition Based on Overtime",
    "Attrition Rate by Environment Satisfaction",
    "Attrition Rate by Job Satisfaction",
    "Distribution of Work Experience by Attrition",
    "Attrition Comparison by Work Experience (Total Working Years)",
    "Attrition Count by Education Level"
])

# Show the appropriate plot based on the user's selection
if question == "Comparison of Active and Exiting Employees":
    st.plotly_chart(fig1)
elif question == "Employees Leaving by Gender":
    st.plotly_chart(fig2)
elif question == "Attrition by Business Travel":
    st.plotly_chart(fig3)
elif question == "Effect of Distance From Home on Attrition (Yes and No)":
    st.plotly_chart(fig_yes)
    st.plotly_chart(fig_no)
elif question == "Attrition Comparison by Department":
    st.plotly_chart(fig5)
elif question == "Attrition Count by Job Role":
    st.plotly_chart(fig6)
elif question == "Age Distribution by Attrition Status":
    st.plotly_chart(fig7)
elif question == "Monthly Income Distribution by Attrition Status":
    st.plotly_chart(fig8)
elif question == "Relationship between Monthly Income and Hourly Rate by Attrition Status and Department":
    st.plotly_chart(fig9)
elif question == "Attrition Rate by Education Field":
    st.plotly_chart(fig10)
elif question == "Attrition Rate by Overtime Status":
    st.plotly_chart(fig11)
elif question == "Attrition Rate by Work-Life Balance":
    st.plotly_chart(fig12)
elif question == "Attrition Based on Overtime":
    st.plotly_chart(fig13)
elif question == "Attrition Rate by Environment Satisfaction":
    st.plotly_chart(fig14)
elif question == "Attrition Rate by Job Satisfaction":
    st.plotly_chart(fig15)
elif question == "Distribution of Work Experience by Attrition":
    st.plotly_chart(fig)
elif question == "Attrition Comparison by Work Experience (Total Working Years)":
    st.plotly_chart(fig)
elif question == "Attrition Count by Education Level":
    st.plotly_chart(fig)
