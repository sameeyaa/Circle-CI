import scipy.stats
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

months = np.array([5,10,15,20,25,30,35])
sales = np.array([50,100,150,200,250,300])

slope,intercept,r_value,p_value, std_err = stats.linegress(months, sales)

best_fit_line = slope*months + intercept

plt.scatter(months, sales, color = 'blue', label = 'Sales')
plt.plot(months, best_fit_line_color = 'pink', label = 'Line of Best fit')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales with Regression')
plt.legend()
plt.show()