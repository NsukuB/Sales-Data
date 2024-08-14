

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [15000, 18000, 12000, 17000, 16000],
    'Product': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

product_sales = df.groupby('Product')['Sales'].sum()

product_sales.plot(kind='bar', title='Total Sales by Product')
plt.show()
