import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/Users/macbookair/Documents/Page-view-time-visualizer/freecodecamp-page-view-time-series-visualizer/fcc-forum-pageviews.csv', index_col="date", parse_dates=True)
print(df.head())

# Clean data with the top of 2.5% page views and the bottom of 2.5% page views
top_25 = df['value'].quantile(0.025)
bottom_25 = df['value'].quantile(0.975)
df = df[(df['value'] >= top_25) & (df['value'] <= bottom_25)]


def draw_line_plot():
    #1. Set Figure
    fig, ax = plt.subplots(figsize=(28, 12))

    #2. Set the Filtered Dataset
    ax.plot(df.index, df['value'], marker='o', color='r', linestyle='-', linewidth=2)

    #3. Set Figure Format
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=28, fontweight="bold")
    ax.set_xlabel('Date', fontsize=20)
    ax.set_ylabel('Page Views', fontsize=20)
    plt.xticks(rotation=45)

    #4. Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    #1. Copy data for monthly bar plot
    df_bar = pd.read_csv('/Users/macbookair/Documents/Page-view-time-visualizer/freecodecamp-page-view-time-series-visualizer/fcc-forum-pageviews.csv', parse_dates=["date"])
    print(df_bar)

    #2. Grouping Year and Month
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month

    #3. Calculate Average Page Views
    df_average = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    #4. Set Figure
    fig = df_average.plot(kind='bar', figsize=(14,10), legend=True).figure
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Average Page Views', fontsize=14)
    plt.title('Daily freeCodeCamp Forum Average Page Views 5/2016-12/2019', fontsize=16, fontweight="bold")
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], fontsize=12)

    #5. Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    #1. Prepare data for box plots 
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    #2. Set Figure
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6), sharey=True)

    #3. Create Boxplot by Year 
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette=['#EA638C', '#B33C86', '#190E4F', '#03012C'])
    axes[0].set_xlabel('Year', fontsize=12)
    axes[0].set_ylabel('Page Views', fontsize=12)
    axes[0].set_title('Year-wise Box Plot (Trend)', fontsize=14, fontweight='bold')

    #3. Create Boxplot by Month
    x_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=x_order, palette='coolwarm')
    axes[1].set_xlabel('Month', fontsize=12)
    axes[1].set_ylabel('Page Views', fontsize=12)
    axes[0].set_title('Month-wise Box Plot (Seasonality)', fontsize=14, fontweight='bold')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
