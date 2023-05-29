import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
  plt.xticks([1850,1875,1900,1925,1950,1975,2000,2025,2050,2075])

    # Create first line of best fit
  slope, intercept, _, _, _ = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
  x_range = np.arange(df.Year.min(),2051,1)
  line_FullTime = slope * x_range + intercept
  plt.plot(x_range,line_FullTime, color ='red')
  

    # Create second line of best fit
  df2000 = df.copy()
  df2000 = df2000[df2000.Year > 1999]
  slope1,intercept1,_,_,_ = linregress(df2000['Year'],df2000['CSIRO Adjusted Sea Level'])
  x_2000 = np.arange(2000,2051,1)
  line_2000 = slope1 * x_2000 + intercept1
  plt.plot(x_2000,line_2000,color = 'blue')

    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()