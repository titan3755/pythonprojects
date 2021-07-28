import matplotlib as mpl
from matplotlib import pyplot as plt

years_x = [*range(1970, 2020, 10)]
condom_sales_y = [300000, 330000, 320000, 430000, 530000]

plt.plot(years_x, condom_sales_y)
plt.xlabel('Years')
plt.ylabel('Condom Sales')
plt.title('Condom sales vs Years')
plt.show()