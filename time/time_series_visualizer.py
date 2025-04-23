import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def time_series_visualizer():
    # 1. Import the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # 2. Clean the data by filtering out the top and bottom 2.5% of page views
    lower_percentile = df['page_views'].quantile(0.025)
    upper_percentile = df['page_views'].quantile(0.975)
    df_clean = df[(df['page_views'] >= lower_percentile) & (df['page_views'] <= upper_percentile)]

    # 3. Draw the line plot
    def draw_line_plot():
        plt.figure(figsize=(12, 6))
        plt.plot(df_clean.index, df_clean['page_views'], color='b', linewidth=1)
        plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
        plt.xlabel('Date')
        plt.ylabel('Page Views')
        plt.tight_layout()
        plt.savefig('line_plot.png')
        plt.show()

    # 4. Draw the bar plot
    def draw_bar_plot():
        # Group by year and month to calculate the average daily page views for each month
        df_clean['year'] = df_clean.index.year
        df_clean['month'] = df_clean.index.month
        monthly_avg = df_clean.groupby(['year', 'month'])['page_views'].mean().unstack()

        # Draw the bar plot
        monthly_avg.plot(kind='bar', figsize=(12, 6))
        plt.title('Average Daily Page Views for Each Month Grouped by Year')
        plt.xlabel('Years')
        plt.ylabel('Average Page Views')
        plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        plt.tight_layout()
        plt.savefig('bar_plot.png')
        plt.show()

    # 5. Draw the box plot
    def draw_box_plot():
        plt.figure(figsize=(12, 6))

        # Year-wise Box Plot (Trend)
        plt.subplot(1, 2, 1)
        sns.boxplot(x=df_clean.index.year, y=df_clean['page_views'])
        plt.title('Year-wise Box Plot (Trend)')
        plt.xlabel('Year')
        plt.ylabel('Page Views')

        # Month-wise Box Plot (Seasonality)
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df_clean.index.month, y=df_clean['page_views'])
        plt.title('Month-wise Box Plot (Seasonality)')
        plt.xlabel('Month')
        plt.ylabel('Page Views')
        plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

        plt.tight_layout()
        plt.savefig('box_plot.png')
        plt.show()

    # Call the functions to plot the graphs
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
