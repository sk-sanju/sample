import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def sea_level_predictor():
    # 1. Import the data
    df = pd.read_csv('epa-sea-level.csv')
    
    # 2. Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # 3. Line of best fit (all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    sea_levels_all = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_all, color='red', label='Best Fit (All Data)')

    # 4. Line of best fit (from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    sea_levels_recent = [slope_recent * year + intercept_recent for year in years_extended]
    plt.plot(years_extended, sea_levels_recent, color='green', label='Best Fit (2000 Onwards)')

    # 5. Formatting the plot
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # 6. Save and display the plot
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    plt.show()