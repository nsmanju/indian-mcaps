import pandas as pd
import matplotlib.pyplot as plt

# Data for 2023
data_2023 = {
    'Company': ['RIL', 'TCS', 'HDFCBk', 'Infosys', 'ICICI Bk', 'HUL', 'ITC', 'SBI', 'Bharti', 'HDFC'],
    'MarketCap (Lakh Crores)': [18.50, 12.00, 9.30, 5.50, 6.60, 6.30, 5.80, 5.30, 5.30, 5.10]
}

# Data for 2013
data_2013 = {
    'Company': ['RIL', 'TCS', 'HDFCBk', 'Infosys', 'ICICI Bk', 'HUL', 'ITC', 'SBI', 'Bharti', 'HDFC'],
    'MarketCap (Lakh Crores)': [2.90, 2.80, 1.85, 1.30, 1.32, 1.40, 2.90, 1.70, 1.60, 1.50]
}

# Convert data to Pandas data frames
df_2023 = pd.DataFrame(data_2023)
df_2013 = pd.DataFrame(data_2013)

# Plotting the data using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df_2023['Company'], df_2023['MarketCap (Lakh Crores)'], label='2023')
plt.plot(df_2013['Company'], df_2013['MarketCap (Lakh Crores)'], label='2013')
plt.xlabel('Company')
plt.ylabel('Market Cap (Lakh Crores)')
plt.title('Indian Stock Market - Top 10 Midcap Companies - 2023 vs 2013')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
py