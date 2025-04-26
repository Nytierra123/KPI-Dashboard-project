# kpi_data_generator.py

import pandas as pd
import random
from datetime import datetime, timedelta

#  generate fake sales, operations, marketing data
def generate_kpi_data(num_rows=100):
    today = datetime.today()
    data = {
        'Date': [today - timedelta(days=i) for i in range(num_rows)],
        'Sales_Amount': [round(random.uniform(500, 5000), 2) for _ in range(num_rows)],
        'Operations_Cost': [round(random.uniform(200, 2000), 2) for _ in range(num_rows)],
        'Marketing_Spend': [round(random.uniform(100, 1000), 2) for _ in range(num_rows)],
        'New_Customers': [random.randint(5, 50) for _ in range(num_rows)],
        'Customer_Churn_Rate': [round(random.uniform(0.01, 0.2), 2) for _ in range(num_rows)]
    }
    df = pd.DataFrame(data)
    return df

# Generate the dataset
kpi_df = generate_kpi_data(180)  # Generate data for 6 months

# Save it as CSV
kpi_df.to_csv('kpi_data.csv', index=False)

print("✅ KPI data generated and saved to 'kpi_data.csv'. Ready for Power BI!")
