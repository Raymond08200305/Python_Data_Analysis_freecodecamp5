import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Create first line of best fit
    result = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    slope = result.slope
    intercept = result.intercept
    predicted_2050 = slope * 2050 + intercept

    # Create second line of best fit
    fit = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    future_years = range(1880, 2051)
    future_levels = [fit.slope * y + fit.intercept
                    for y in future_years]
    plt.plot(future_years, future_levels)

    recent = df[df["Year"] >= 2000]
    fit_recent = linregress(recent["Year"],
                            recent["CSIRO Adjusted Sea Level"])
    recent_years = range(2000, 2051)
    recent_levels = [fit_recent.slope*y + fit_recent.intercept
                    for y in recent_years]
    plt.plot(recent_years, recent_levels)
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.xticks(range(1850, 2076, 25))
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()