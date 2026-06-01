#!/usr/bin/env python
# coding: utf-8

# ![Logo.png](attachment:c9188f9f-cd30-4e98-bacc-726ee45a48e9.png)

# # Python Programming for Real World Data Analytics and GUI Development
# ## SOFT40161 - Introduction to Computer Programming
# ### Submission of the Coursework
# 
# ## Name: Pratham Amit Shah
# ## NTU ID: N1364759
# 
# <font  color= 'red'> **The Full description of the Coursework is here -** </font>
# <a href="https://now.ntu.ac.uk/d2l/le/content/1110621/viewContent/14307207/View">SOFT40161-Coursework (Click here)</a>
# 
# ## Start your answer here-
# <font  color= 'green'> **GitHub Link to access your activity.** </font>
# 
# Please add your Link here: <a href="https://olympus.ntu.ac.uk/N1364759/N1364759_coursework.git">https://olympus.ntu.ac.uk/N1364759/N1364759_coursework.git</a>

# # Section 1: Control Structures (12 marks)
# 

# # *Introduction* : **Daily Water Intake & Hydration Patterns Dataset**

# Hydration is essential for maintaining good health and physical performance, and daily water intake can be influenced by factors such as age, body weight, activity level, and weather conditions. This coursework analyses a hydration dataset using Python to explore how these variables relate to an individual’s hydration level
# 
# Python libraries are used to perform basic data analysis and visualisation, enabling the identification of patterns and relationships. The coursework aims to demonstrate effective data handling, analysis, and interpretation skills while drawing meaningful conclusions from real-world data.
# 
# Dataset is taken from-: https://www.kaggle.com/datasets/sonalshinde123/daily-water-intake-and-hydration-patterns-dataset

# In[91]:


get_ipython().system('pip install --user pandoc nbconvert[webpdf] --quiet')
# Importing the library Pandas
import pandas as pd

# Reading the dataset 
df = pd.read_csv('dataset.csv')

#Understanding the concept of data by printing first five inputs
df.head()


# In[92]:


# Displaying dataset columns
print(df.columns)


# In[93]:


# Knowing dataset information
df.info()


# # Classifying the Risk based on Hydration Level 

# ## Assigning and Updating Hydration Risk Categories
# 
# Before execution, a new column named **Hydration Risk** is created and assigned a default value of *"Major Risk"* for all records. It establishes a baseline risk level for individuals regardless of their daily water intake.
# 
# Conditional indexing is then applied to update hydration risk levels based on water consumption. Records with a daily water intake of **3.0 liters or more** are reclassified as *"Moderate Risk"*, while values of **4.0 liters or more** are further upgraded to *"Minimal Risk"*.

# In[94]:


# Assign default hydration risk as Major Risk for all records
df["Hydration Risk"] = "Major Risk"

# Update hydration risk to Moderate Risk for intake 3.0 liters or more
df.loc[df["Daily Water Intake (liters)"] >= 3.0, "Hydration Risk"] = "Moderate Risk"

# Update hydration risk to Minimal Risk for intake 4.0 liters or more
df.loc[df["Daily Water Intake (liters)"] >= 4.0, "Hydration Risk"] = "Minimal Risk"

# Display first five records of daily intake and assigned hydration risk
df[["Daily Water Intake (liters)", "Hydration Risk"]].head()


# 
# After execution, a subset of the DataFrame displaying **Daily Water Intake (liters)** alongside the newly assigned **Hydration Risk** is shown using the 'head()` method.
# It allows verification that the risk categories have been applied correctly.
# Output confirms that hydration risk levels have been correctly assigned based on the specified water intake thresholds.

# # calculating average water intake by level of performance

# Purpose of the code is to analyse average daily water intake for each physical activity level. Unique activity categories are extracted from the dataset, and a loop is used to calculate mean water intake for individuals within each activity group. Results are formatted for readability and prepared for display.

# In[95]:


# Extract unique physical activity levels from dataset
Performance_levels = df["Physical Activity Level"].unique()

 # Loop through each activity level to calculate average intake
for level in Performance_levels:
    # Compute mean daily water intake for current activity level
    approx_intake = df[df["Physical Activity Level"] == level]["Daily Water Intake (liters)"].mean()

    # Display activity level with corresponding average water intake
    print(f"{level} activity average intake: {approx_intake:.2f} liters")


# Output displays average daily water intake values for each physical activity level, rounded to two decimal places. Each line shows an activity category followed by its corresponding mean intake in liters, allowing easy comparison between different activity levels.

# # Identifying Unique Dehydration Values Using Conditional Iteration
# 

# ### *Code is designed to identify individuals at risk of dehydration under hot weather conditions. It checks each row of the dataset to find cases where daily water intake is less than 2.0 liters and weather is recorded as "Hot," and counts how many such cases exist*.

# In[96]:


# Initialize counter for dehydration cases under hot weather
count = 0

# Loop through each row of dataset to check conditions
for index, row in df.iterrows():
   # Check if daily intake is below 2.0 liters and weather is hot
   if row["Daily Water Intake (liters)"] < 2.0 and row["Weather"] == "Hot":
       # Increment counter for each matching dehydration case
       count += 1

# Display total count of individuals at risk of dehydration under hot conditions
print('Total number of dehydration unique values',count)


# ### *Output provides total number of dehydration risk cases under hot weather. Printed value represents count of unique records where water intake is insufficient in hot conditions*.
# 

# # Weather Column Analysis

# ### Code calculates average daily water intake for each unique weather condition in the dataset. It iterates through all weather categories, creates a subset of records for each condition, and computes mean water intake when records exist. Purpose is to analyse how environmental factors influence hydration levels.

# In[97]:


# Loop through each unique weather condition
for weather in df["Weather"].unique():
   # Filter dataset for current weather condition
   subset = df[df["Weather"] == weather]
   # Ensure subset is not empty
   if len(subset) > 0:
       # Print mean daily water intake for current weather
       print(f"{weather} weather average intake: {subset['Daily Water Intake (liters)'].mean():.2f}")


# ### Output displays average daily water intake for each weather condition, rounded to two decimal places. Each line shows a weather type followed by its corresponding mean intake, allowing comparison of hydration across different environmental conditions.
# 

# # Hydration Level Classification

# ### Code assigns a hydration status to each individual based on daily water intake and weather conditions. A new column **Hydration Output** is created, where `0` indicates poor hydration and `1` indicates good hydration. For hot weather, intake of 3.0 liters or more is classified as good, while for other weather conditions, 2.5 liters or more qualifies. Iteration over each row applies conditional logic to update hydration status accordingly.
# 

# In[98]:


# Initialize hydration status column: 0 = Poor, 1 = Good
df["Hydration Output"] = 0   

# Loop through each row of dataset to assign hydration status
for index, row in df.iterrows():
    # Check if weather condition is hot
    if row["Weather"] == "Hot":
        # Assign Good status if intake is 3.0 liters or more in hot weather
        if row["Daily Water Intake (liters)"] >= 3.0:
            df.at[index, "Hydration Output"] = 1
    else:
        # Assign Good status if intake is 2.5 liters or more
        if row["Daily Water Intake (liters)"] >= 2.5:
            df.at[index, "Hydration Output"] = 1
# Extract first few values of hydration status for verification
_checksum = df["Hydration Output"].head()

 # Display sample of hydration output values
_checksum


# ### Output shows first few values of **Hydration Output** column for verification. Each entry indicates whether hydration status is poor (`0`) or good (`1`) based on defined intake thresholds and weather conditions.
# 

# # Section 2: Functions and Modules (16 marks)  

# # Importing required Modules

# In[99]:


# Import NumPy library for numerical computations and array operations
import numpy as np

# Import Matplotlib pyplot module for creating plots and visualisations
import matplotlib.pyplot as plt


# # Function to Estimate Average Daily Water Intake
# 

# ### Code defines a function to calculate average daily water intake from the dataset. Column **Daily Water Intake (liters)** is extracted, and NumPy's `mean` function computes the average value. Function can be applied to the DataFrame to obtain a single numerical estimate of typical hydration levels.
# 

# In[100]:


# Import NumPy library for numerical operations and calculating mean
import numpy as np
# Define function to compute average daily water intake
def calculate_average_intake(df):
     # Extract daily water intake column from dataset
    water_intake= df['Daily Water Intake (liters)']
    # Calculate mean value of daily water intake
    mean = np.mean(water_intake)
    # Return computed average intake
    return mean

# Call function to obtain average daily water intake for entire dataset
calculate_average_intake(df)


# ### Output displays a single numeric value representing mean daily water intake across all individuals in the dataset. Value provides an overall estimate of general hydration for analysis or comparison purposes.
# 

# # Function on finding the low hydration unique values from dataset

# ### Dataset includes information on daily water intake, hydration level, physical activity, and weather. Code defines a function that filters the DataFrame to return only records where **Hydration Level** is `'Poor'`, allowing identification of individuals at risk due to low hydration.
# 

# In[101]:


# Define function to filter records with poor hydration
def find_low_hydration(df):
    # Return subset of dataset where Hydration Level is 'Poor'
    return df[df['Hydration Level'] == 'Poor']

# Call function to extract all individuals with poor hydration
find_low_hydration(df)


# ### Code filters dataset to return only records where hydration level is `'Poor'`. It checks **Hydration Level** column for this condition and outputs a subset containing all matching rows for further analysis.
# 

# # Function on finding hydration level by activity level

# ### Dataset contains individual records of daily water intake, hydration level, physical activity, and weather conditions. Code defines a function that calculates average daily water intake for each **Physical Activity Level**. Grouping is performed on activity categories, and mean intake is computed for each group.
# 

# In[102]:


# Define function to calculate average water intake by physical activity level
def intake_by_activity(df):
    
    # Group dataset by activity level and compute mean daily intake for each group
    return df.groupby('Physical Activity Level')['Daily Water Intake (liters)'].mean()

 # Call function to obtain average water intake for all physical activity categories
intake_by_activity(df)


# ### Output displays average water intake values for each physical activity category. Result allows comparison of hydration patterns across different activity levels and highlights how activity influences water consumption.
# 

# # Function to visualise the water intake 

# ### Dataset contains individual records including daily water intake, hydration level, physical activity, and weather conditions. Code performs multiple analyses: calculates overall average water intake, extracts records with poor hydration, and computes average intake grouped by physical activity level to examine patterns and trends in hydration.
# 

# In[103]:


# Create dataset using predefined function
# df = create_dataset()

# Calculate and display average daily water intake
print("Average Water Intake:", calculate_average_intake(df))

# Display records where hydration level is poor
print("\nLow Hydration Records:")
print(find_low_hydration(df))

# Display average water intake grouped by physical activity level
print("\nWater Intake by Activity Level:")
print(intake_by_activity(df))


# ### Output displays overall mean daily water intake, a subset of records where hydration is poor, and average water intake values for each physical activity category. Results provide insights into general hydration, identify individuals at risk, and show how activity level influences water consumption.
# 

# ### Code Dataset includes individual daily water intake records. Code defines a simple function to classify hydration as "Good" or "Poor" based on water consumption. Function is applied to each record to create a new column **Hydration_Result** for easy identification of hydration status.
# 

# In[104]:


# Define function to classify hydration based on daily water intake
def hydration_simple(water):
    # Assign "Good" if intake is 3 liters or more
    if water >= 3:
        return "Good"
    # Assign "Poor" if intake is less than 3 liters
    else:
        return "Poor"

# calling the function
df["Hydration_Result"] = df["Daily Water Intake (liters)"].apply(hydration_simple)

# Display first five rows including new Hydration_Result column
df.head()


# ### Output displays first few records of dataset including **Hydration_Result**. Each entry shows whether an individual's hydration is classified as "Good" or "Poor" based on daily water intake, enabling quick assessment of hydration levels.
# 

# # Function to Classify Hydration Based on Weather, Activity, and Water Intake
# ### Dataset contains individual daily water intake, weather, and physical activity information. Code defines a function to classify hydration as "Good" or "Poor" based on combined conditions of weather, activity level, and water intake. Function is applied to each record to create **Hydration_Result** column for detailed analysis.
# 
# 

# In[105]:


# Define function to classify hydration based on weather, activity level, and water intake
def hydration_weather_activity(weather, activity, water):
    # For hot weather or high physical activity
    if weather == "Hot" or activity == "High":
    # Assign "Good" if intake is 3.5 liters or more
        if water >= 3.5:
            return "Good"
        else:
         # Assign "Poor" if intake is less than 3.5 liters
            return "Poor"
         # For other weather and activity conditions
    else:
     # Assign "Good" if intake is 2.5 liters or more
        if water >= 2.5:
            return "Good"
        else:
        # Assign "Poor" if intake is less than 2.5 liters
            return "Poor"

# Apply function to each row of dataset to determine hydration result considering weather and activity
df["Hydration_Result"] = df.apply(
    lambda row: hydration_weather_activity(
        row["Weather"],
        row["Physical Activity Level"],
        row["Daily Water Intake (liters)"]
    ),
    axis=1
)

# Display first five rows including updated Hydration_Result column
df.head()


# ### Output displays first few records of dataset with **Hydration_Result**. Each row indicates whether hydration status is "Good" or "Poor" considering both environmental conditions and activity level, providing a more accurate assessment of hydration.
# 

# # Section 3: Data Handling with Pandas (16 marks)  

# # Bar Chart of Daily Water Intake by Age
# ### Dataset includes individual records of Age and Daily Water Intake. Code defines a function to create a bar chart showing water intake for each age. Visualization allows easy comparison of hydration patterns across different age groups.
# 

# In[106]:


# Import Matplotlib pyplot module for creating visualizations
import matplotlib.pyplot as plt

# Define function to plot daily water intake by age
def plot_water_intake(df):
# Create bar chart with Age on x-axis and Daily Water Intake on y-axis
    plt.bar(df['Age'], df['Daily Water Intake (liters)'])
 # Label x-axis as Age  
    plt.xlabel('Age')

 # Label y-axis as Water Intake (liters)
    plt.ylabel('Water Intake (liters)')
 # Add title to chart
    plt.title('Daily Water Intake by Age')
 # Display the plot
    plt.show()

# Call function to generate and display bar chart
plot_water_intake(df)


# ### Output displays a bar chart with Age on x-axis and Daily Water Intake (liters) on y-axis. Each bar represents an individual's water intake, providing a visual understanding of how hydration varies with age.
# 

# # Handling Missing Values and Data Cleaning
# 
# ### Dataset contains missing values in various columns, including Daily Water Intake and Weight. Code identifies missing values, removes rows with missing water intake, and fills missing weight values with the median to ensure dataset is clean for analysis.
# 

# In[107]:


# Check for missing values in each column
missing_val = df.isnull().sum()
# Display number of missing values for each column
print("Missing values per column:\n", missing_val)

# Remove records where Daily Water Intake is missing
df_clean = df.dropna(subset=['Daily Water Intake (liters)'])

# Fill missing Weight values with median weight
median_weigt = df_clean['Weight (kg)'].median()

 # Replace NaN values in Weight with median
df_clean['Weight (kg)'] = df_clean['Weight (kg)'].fillna(median_weigt)


# ### Output displays count of missing values per column. After cleaning, dataset has no missing values in Daily Water Intake, and all missing Weight entries are replaced with median, making data suitable for accurate analysis.
# 

# # Identifying and Removing Duplicate Records
# 
# ### Dataset may contain duplicate records after cleaning. Code counts total duplicates and removes them to maintain data integrity, ensuring each individual record is unique for analysis.
# 

# In[108]:


# Check duplicates count
duplic_count = df_clean.duplicated().sum()
print(f"Number of duplicate rows: {duplic_count}")

# Remove duplicates
df_clean = df_clean.drop_duplicates()


# ### Output displays number of duplicate rows before removal. After execution, dataset contains only unique records, preventing duplication errors in analysis or visualizations.

# # Average Daily Water Intake Analysis by Gender
# 
# ### Code Dataset contains individual records with Gender and Daily Water Intake. Code groups data by gender and calculates average daily water intake for each group to analyse hydration patterns between males and females.

# In[109]:


# Average Daily Water Intake by Gender
avg_water_by_gen = df_clean.groupby('Gender')['Daily Water Intake (liters)'].mean()
print("Average Daily Water Intake by Gender:\n", avg_water_by_gen)


# ### Output displays mean daily water intake for each gender. Results allow comparison of hydration levels between males and females, highlighting potential differences in water consumption.
# 

# # Average Daily Water Intake Analysis by Weather Condition
# ### Dataset contains records of daily water intake and weather conditions. Code groups data by weather type and calculates average water intake for each category to analyse how environmental factors influence hydration.
# 

# In[110]:


# Average Water Intake by Weather
avg_by_weather = df_clean.groupby('Weather')['Daily Water Intake (liters)'].mean()
print("\nAverage Daily Water Intake by Weather:\n", avg_by_weather)


# ### Output displays mean daily water intake for each weather condition. Results provide insights into how different weather environments affect hydration levels across individuals.
# 

# # Count of Hydration Levels Across Physical Activity Levels
# 
# ### Dataset contains Hydration Level and Physical Activity Level for individuals. Code groups data by activity level and counts occurrences of each hydration category to analyse how activity influences hydration patterns.
# 

# In[111]:


# Count of Hydration Levels by Physical Activity Level
hydration_num = df_clean.groupby('Physical Activity Level')['Hydration Level'].value_counts()
print("\nHydration Level counts by Physical Activity Level:\n", hydration_num)


# ### Output shows count of each hydration level for every physical activity category. Results highlight the distribution of poor, moderate, and good hydration among different activity levels.
# 

# # Identifying Individuals with Low Daily Water Intake (<2.5 liters)
# 
# ### Dataset contains daily water intake records for individuals. Code filters and identifies records where intake is below 2.5 liters to analyse at-risk individuals with low hydration.
# 

# In[112]:


# Filter individuals with daily water intake less than 2.5 liters
low_water_count = df_clean[df_clean["Daily Water Intake (liters)"] < 2.5]
print(f"Number of individuals with water intake < 2.5 liters: {len(low_water_count)}")
low_water_count.head()


# ### Output displays total number of individuals consuming less than 2.5 liters daily and shows a sample of these records. Results help focus on hydration intervention or further analysis for low-intake individuals.
# 

# # Filtering Dataset for Female Individuals
# 
# ### Code Dataset contains gender information for individuals. Code filters records to include only females, enabling gender-specific analysis of hydration and related patterns.
# 

# In[113]:


# Filter for females only
females = df_clean[df_clean["Gender"] == "Female"]
print(f"Number of females: {len(females)}")
females.head()


# ### Output displays total number of female individuals and shows a sample of their records. Results allow focused examination of hydration and water intake among females.
# 

# # Filtering Individuals Aged 30–50
# 
# ### Dataset contains Age information for all individuals. Code filters records to include only those aged 30 to 50 to analyse hydration patterns within this age group.
# 

# In[114]:


# People aged between 30 and 50
age_30_50 = df_clean[(df_clean["Age"] >= 30) & (df_clean["Age"] <= 50)]
print(f"Number of people aged between 30 and 50: {len(age_30_50)}")
age_30_50.head()


# ### Output displays total number of individuals aged 30–50 and shows a sample of their records. Results help focus on hydration and water intake analysis for middle-aged adults.
# 

# # Section 4: Data Visualization (16 marks)  

# # Histogram of Daily Water Intake Distribution
# ### Code Purpose
# 
# Dataset contains daily water intake values for individuals. Code creates a histogram to visualize distribution of daily water consumption, showing how frequently different intake levels occur across the dataset.
# 

# In[115]:


# Import Matplotlib for plotting
import matplotlib.pyplot as plt
# Import Seaborn for advanced visualization
import seaborn as sns

plt.figure(figsize=(8,5))
# Plot histogram with 10 bins and teal color
sns.histplot(df_clean["Daily Water Intake (liters)"], bins=10,color="teal")
 # Add title to histogram
plt.title("Distribution of Daily Water Intake", fontsize=14)
# Label x-axis
plt.xlabel("Daily Water Intake (liters)", fontsize=12)
# Label y-axis
plt.ylabel("Frequency", fontsize=12)
# Add light grid lines for readability
plt.grid(True, linestyle='--', alpha=0.5)
# Display the plot
plt.show()


# ### Outcome
# 
# Output displays a histogram with daily water intake on x-axis and frequency on y-axis. Visualization highlights common intake ranges, patterns, and potential outliers in hydration among individuals.
# 

# # Multi-Plot Visualization of Hydration Patterns and Water Intake
# ### Dataset contains daily water intake, hydration levels, gender, weather, and physical activity information. Code creates a 2x2 subplot figure to visualize:  
# 
# 1. Count of people by hydration level (horizontal bar plot).  
# 2. Average water intake grouped by gender (bar plot).  
# 3. Distribution of water intake across weather conditions (box plot).  
# 4. Hydration level distribution across physical activity levels (count plot).  
# 
# Visualizations help identify patterns, relationships, and differences across various factors affecting hydration.
# 

# In[116]:


import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure with 2 rows x 2 columns of subplots
fig, axes = plt.subplots(2, 2, figsize=(14,10))

# 1️⃣ Horizontal Bar Plot: Count of people by Hydration Level
hydra_counts = df_clean['Hydration Level'].value_counts()
axes[0,0].barh(hydra_counts.index, hydra_counts.values, color='#8BE820')
axes[0,0].set_title("Count of People by Hydration Level", fontsize=12)
axes[0,0].set_xlabel("Number of People")
axes[0,0].set_ylabel("Hydration Level")
axes[0,0].grid(True, linestyle='--', alpha=0.5)

# 2️⃣ Bar Plot: Average Water Intake by Gender
avg_water_by_gender = df_clean.groupby("Gender")["Daily Water Intake (liters)"].mean().reset_index()
sns.barplot(data=avg_water_by_gender, x="Gender", y="Daily Water Intake (liters)", palette="pastel", ax=axes[0,1])
axes[0,1].set_title("Average Water Intake by Gender", fontsize=12)
axes[0,1].set_ylabel("Average Water Intake (liters)")
axes[0,1].set_xlabel("Gender")

# 3️⃣ Box Plot: Water Intake by Weather
sns.boxplot(x="Weather", y="Daily Water Intake (liters)", data=df_clean, palette="Set2", ax=axes[1,0])
axes[1,0].set_title("Water Intake by Weather", fontsize=12)
axes[1,0].set_ylabel("Daily Water Intake (liters)")
axes[1,0].set_xlabel("Weather")

# 4️⃣ Count Plot: Hydration Level by Physical Activity
sns.countplot(data=df_clean, x="Physical Activity Level", hue="Hydration Level", palette="coolwarm", ax=axes[1,1])
axes[1,1].set_title("Hydration Level by Physical Activity", fontsize=12)
axes[1,1].set_ylabel("Count")
axes[1,1].set_xlabel("Physical Activity Level")
axes[1,1].legend(title="Hydration Level")

# Adjust layout for better spacing
plt.tight_layout()
plt.show()


# ### Outcome and Findings
# 
# - **Hydration Count:** Most individuals fall under moderate hydration; few are poorly hydrated.  
# - **Gender Comparison:** Average water intake between males and females shows slight variation; generally consistent.  
# - **Weather Influence:** Water intake tends to be higher in hot weather, as expected.  
# - **Physical Activity Impact:** High activity individuals show more "Good" hydration, while low activity often aligns with "Moderate" or "Poor" hydration.  
# 
# **Conclusion:** Hydration is influenced by both environmental factors (weather) and lifestyle factors (physical activity), with age and gender showing moderate effect. Visual analysis allows targeting at-risk individuals and highlights importance of sufficient water intake for health.
# 

# # Pie Charts for Categorical Variable Distributions
# ### Code Implementation
# 
# Dataset contains categorical variables including Gender, Hydration Level, Weather, and Physical Activity Level. Code creates a 2x2 subplot of pie charts to visualize distribution of each category, providing a clear view of population proportions across different factors.
# 

# In[117]:


import matplotlib.pyplot as plt

# Create 2x2 subplot
fig, axes = plt.subplots(2, 2, figsize=(12,12))

#  Pie Chart: Gender Distribution
gender_coun = df_clean['Gender'].value_counts()
axes[0,0].pie(gender_coun, labels=gender_coun.index, autopct="%1.1f%%", colors=["lightskyblue","lightcoral"])
axes[0,0].set_title("Gender Distribution", fontsize=14)

#  Pie Chart: Hydration Level Distribution
hydration_counts = df_clean['Hydration Level'].value_counts()
axes[0,1].pie(hydration_counts, labels=hydration_counts.index, autopct="%1.1f%%", colors=["lightgreen","orange","pink"])
axes[0,1].set_title("Hydration Level Distribution", fontsize=14)

#  Pie Chart: Weather Distribution
weather_counts = df_clean['Weather'].value_counts()
axes[1,0].pie(weather_counts, labels=weather_counts.index, autopct="%1.1f%%", colors=["gold","skyblue","lightgrey"])
axes[1,0].set_title("Weather Distribution", fontsize=14)

#  Pie Chart: Physical Activity Level Distribution
activity_counts = df_clean['Physical Activity Level'].value_counts()
axes[1,1].pie(activity_counts, labels=activity_counts.index, autopct="%1.1f%%", colors=["plum","salmon","lightgreen"])
axes[1,1].set_title("Physical Activity Level Distribution", fontsize=14)

# Adjust layout
plt.tight_layout()
plt.show()


# ### Outcome and Findings
# 
# - **Gender Distribution:** Displays proportion of males vs. females.  
# - **Hydration Level Distribution:** Shows percentage of individuals with Poor, Moderate, or Good hydration.  
# - **Weather Distribution:** Visualizes how many records fall under Hot, Mild, or Cold weather.  
# - **Physical Activity Distribution:** Indicates proportion of Low, Moderate, and High activity individuals.  
# 
# **Conclusion:** Pie charts provide a quick visual summary of dataset composition, highlighting dominant groups and helping identify demographic or lifestyle patterns that may influence hydration.
# 

# # Section 5: GUI Development (16 marks)  

# #  Interactive Hydration Data Explorer GUI using Tkinter and Matplotlib
# ### Implementation
# 
# GUI uses Tkinter to explore hydration dataset interactively. Users can select **Gender** and **Weather** from dropdowns. Upon selection, **summary statistics** of daily water intake are displayed. Hydration distribution is visualized with an **embedded pie chart** using Matplotlib. Buttons allow filtering data, plotting charts, resetting selections, and exiting the application. Code handles empty selections and dynamically updates chart and summary.
# 

# In[118]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create main window
root = tk.Tk()
root.title("Hydration Data Explorer")
root.geometry("600x600")
root.configure(bg="#e6f2e6")  # light green background

# Function to filter dataset based on selections
def filter_data():
    selected_gender = gender_var.get()
    selected_weather = weather_var.get()
    
    filtered_df = df_clean.copy()
    if selected_gender != "All":
        filtered_df = filtered_df[filtered_df["Gender"] == selected_gender]
    if selected_weather != "All":
        filtered_df = filtered_df[filtered_df["Weather"] == selected_weather]
    
    if len(filtered_df) > 0:
        summary = filtered_df["Daily Water Intake (liters)"].describe()
        summary_text.set(summary.to_string())
    else:
        summary_text.set("No data for this selection!")
    
    return filtered_df

# Function to plot hydration pie chart inside the GUI
def plot_hydration_pie():
    filtered_df = filter_data()
    if len(filtered_df) == 0:
        messagebox.showinfo("No Data", "No data to plot for this selection.")
        return
    
    hydration_counts = filtered_df["Hydration Level"].value_counts()
    
    # Clear previous chart if exists
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(4,4), facecolor="#e6f2e6")
    ax.pie(hydration_counts, labels=hydration_counts.index, autopct="%1.1f%%", colors=["#66c266", "#99e699", "#b3ffb3"])
    ax.set_title("Hydration Level Distribution", fontsize=12)
    
    # Embed figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to reset selections
def reset_selection():
    gender_dropdown.current(0)
    weather_dropdown.current(0)
    summary_text.set("")
    for widget in chart_frame.winfo_children():
        widget.destroy()

# Exit function
def exit_app():
    root.destroy()

# Labels and dropdowns
tk.Label(root, text="Select Gender:", bg="#e6f2e6", font=("Arial", 12)).pack(pady=5)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, state="readonly")
gender_dropdown['values'] = ["All"] + df_clean["Gender"].unique().tolist()
gender_dropdown.current(0)
gender_dropdown.pack(pady=5)

tk.Label(root, text="Select Weather:", bg="#e6f2e6", font=("Arial", 12)).pack(pady=5)
weather_var = tk.StringVar()
weather_dropdown = ttk.Combobox(root, textvariable=weather_var, state="readonly")
weather_dropdown['values'] = ["All"] + df_clean["Weather"].unique().tolist()
weather_dropdown.current(0)
weather_dropdown.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#e6f2e6")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Show Summary", command=filter_data, bg="#66c266", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Show Hydration Chart", command=plot_hydration_pie, bg="#339933", fg="white", width=15).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Reset", command=reset_selection, bg="#99e699", fg="white", width=15).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=exit_app, bg="#ff6666", fg="white", width=15).grid(row=1, column=1, padx=5, pady=5)

# Label to display summary statistics
summary_text = tk.StringVar()
summary_label = tk.Label(root, textvariable=summary_text, justify="left", bg="#e6f2e6", font=("Arial", 10))
summary_label.pack(pady=10)

# Frame to embed the matplotlib chart
chart_frame = tk.Frame(root, bg="#e6f2e6")
chart_frame.pack(pady=10)

# Run the GUI
root.mainloop()


# ### Findings
# 
# - GUI allows users to quickly analyze hydration patterns across gender and weather categories.  
# - Pie charts show proportion of Poor, Moderate, and Good hydration within selected subsets.  
# - Summary statistics provide mean, median, min, max, and quartiles of daily water intake for selected filters.  
# - Reset button clears selections and chart for fresh analysis.  
# 
# ### Conclusion
# 
# Interactive GUI enables non-technical users to explore hydration data efficiently. Visualization and summary statistics help identify at-risk individuals and trends across gender and environmental conditions. Tool demonstrates practical application of Python for data analysis and interactive reporting.
# 

# # Section 6: Conclusion: Version Control, Critical Appraisal, Documentation (24 marks)  

# ## Critical Appraisal of Hydration Dataset and Analysis
# 
# 1) Dataset includes structured numerical (Age, Weight, Daily Water Intake) and categorical (Gender, Weather, Physical Activity Level, Hydration Level) variables, allowing comprehensive analysis.  
# 2) Strengths of dataset include clarity of fields, sufficient numeric values for statistical calculations, and categorical labels for grouping and visualization.  
# 3) Limitations include **missing values**, **duplicate records**, and **unequal representation** in some categories (e.g., fewer high-activity individuals), which could bias results.  
# 4) Data cleaning, such as handling missing values, imputing median weights, and removing duplicates, improved reliability of analysis.  
# 5) Visualizations (bar plots, pie charts, boxplots) and summary statistics effectively revealed trends in water intake and hydration levels.  
# 6) Potential improvements include **increasing sample size**, ensuring balanced category representation, and collecting additional features (e.g., temperature in degrees, physical activity duration) to strengthen insights.  
# 7) Critical appraisal ensures findings are **interpreted cautiously**, highlighting dataset limitations and guiding responsible conclusions.  
# 

# ## Key Findings and Insights
# 
# 1) **Daily Water Intake Patterns:** Most individuals consume between 2.5–3.5 liters daily, with a few outliers below 2 liters, indicating potential dehydration risk.  
# 2) **Hydration Risk Levels:** Classification showed a significant proportion at **Major or Moderate Risk**, emphasizing need for increased daily water consumption in some groups.  
# 3) **Gender Differences:** On average, males consume slightly more water than females, but both show risk of inadequate intake in specific categories.  
# 4) **Impact of Physical Activity:** High-activity individuals generally require more water; analysis confirmed average intake rises with activity level.  
# 5) **Effect of Weather:** Hot weather correlates with higher water intake, yet some individuals still remain underhydrated, highlighting environmental impact on hydration behavior.  
# 6) **Age Group Insights:** Middle-aged adults (30–50 years) show moderate water consumption, while younger and older age groups vary more widely, suggesting targeted awareness campaigns.  
# 7) **Hydration Level Distribution:** Pie charts revealed that a notable portion of the population falls under **Poor or Moderate Hydration**, requiring attention to daily water consumption habits.  
# 8) **GUI Findings:** Interactive filters confirmed trends visually, allowing exploration of specific gender and weather subsets, enhancing understanding of subgroup hydration patterns.  
# 9) **Data Quality Observations:** Cleaning steps, including removing duplicates and handling missing values, improved reliability of analysis, but some imbalance in category representation remains.  
# 10) **Overall Insight:** Hydration patterns are influenced by gender, age, activity, and weather, highlighting the need for **personalized hydration recommendations** and targeted awareness initiatives.
# 

# ## Section 6: Conclusion
# 
# **Version Control:**  
# Maintaining code and dataset changes through version control systems, such as Git, enhances reproducibility and transparency. Every update to data cleaning, transformation, or visualization steps can be tracked with descriptive commit messages, allowing restoration of previous states and collaborative development without loss of work. Version control ensures that analytical workflows remain **robust, traceable, and manageable**.
# 
# **Critical Appraisal:**  
# Analysis of the hydration dataset highlighted important trends in water intake across **gender, age, weather, and physical activity levels**. The dataset’s structured numerical and categorical features facilitated clear statistical and visual exploration. Limitations, including **missing values, duplicate entries, and unequal representation of categories**, were addressed through cleaning and imputation strategies. Awareness of these limitations allowed **cautious interpretation** of results and guided decision-making in data preprocessing and visualization.
# 
# **Documentation:**  
# Comprehensive documentation was integrated using **inline comments, descriptive headings, and Markdown cells** explaining the purpose, functionality, and output of each code section. Well-documented code ensures **clarity, reproducibility, and ease of understanding** for both instructors and future collaborators.
# 
# **Overall Summary:**  
# Applying version control, performing critical appraisal, and maintaining clear documentation collectively strengthened the project. These practices guarantee a **structured, transparent, and reproducible analytical workflow**, enabling reliable insights into hydration patterns while demonstrating best practices in Python-based data analysis.
# 

# # References:
# 

# 
# ## Additional Python‑Related References
# 
#  Grus, J. (2019). *Data Science from Scratch: First Principles with Python*. O’Reilly Media.  
#    https://www.oreilly.com/library/view/data-science-from/9781492041122/
# 
#  Lutz, M. (2013). *Learning Python*. O’Reilly Media.  
#    https://learning-python.com/
# 
#  Python Software Foundation. *Python Documentation*.  
#    https://docs.python.org/3/
# 
# 
