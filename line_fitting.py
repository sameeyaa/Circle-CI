import scipy.stats
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

months = np.array([5,13,15,20,25,30,32,40,45,50,58,60])
sales = np.array([50,100,147,200,250,305,350,420,450,500,550,600])

slope,intercept,r_value,p_value, std_err = stats.linregress(months, sales)

line_of_best_fit = slope*months + intercept

plt.scatter(months, sales, color = 'blue', label = 'Sales')
plt.plot(months,line_of_best_fit, color = 'pink', label = 'Line of Best fit')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales with Regression')
plt.legend()
plt.show()
