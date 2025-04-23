import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def medical_data_visualizer():
    # 1. Import the data
    df = pd.read_csv('medical_examination.csv')

    # 2. Add overweight column
    df['bmi'] = df['weight'] / (df['height'] / 100) ** 2  # BMI = weight / height^2 (in meters)
    df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0)

    # 3. Normalize cholesterol and glucose columns
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    # 4. Draw the categorical plot
    # Prepare the data for the categorical plot
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 5. Create the catplot
    g = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count')
    g.set_axis_labels("Variable", "Count")
    g.set_titles("Cardio = {col_name}")
    fig = g.fig
    fig.tight_layout()

    # 6. Draw the heatmap
    # Clean the data for the heatmap
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                (df['height'] >= df['height'].quantile(0.025)) & 
                (df['height'] <= df['height'].quantile(0.975)) & 
                (df['weight'] >= df['weight'].quantile(0.025)) & 
                (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle of the correlation matrix
    mask = np.triu(corr)

    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", cbar_kws={'shrink': .8})

    # 7. Display the plot
    plt.show()
