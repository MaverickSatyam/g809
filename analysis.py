import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'MRR_Growth': [5.41, 8.59, 12.54, 10.56]
}
df = pd.DataFrame(data)

# 2. Key Metrics
industry_target = 15
company_average = df['MRR_Growth'].mean()

# 3. Print Summary (for verification)
print(f"Company Average MRR Growth (2024): {company_average:.2f}%")
print(f"Industry Target: {industry_target:.2f}%")

# 4. Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='Quarter', y='MRR_Growth', data=df, palette='viridis')

# Add Target Line
plt.axhline(industry_target, color='red', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target}%)')

# Add Average Line
plt.axhline(company_average, color='black', linestyle='-', linewidth=1.5, label=f'Company Avg ({company_average:.2f}%)')

# Add Labels
for index, row in df.iterrows():
    plt.text(index, row.MRR_Growth + 0.5, f"{row.MRR_Growth:.2f}%", ha='center')

plt.title('2024 Quarterly MRR Growth vs. Industry Target', fontsize=16)
plt.xlabel('2024 Quarter')
plt.ylabel('MRR Growth Rate (%)')
plt.ylim(0, 18) # Set y-limit to better show the target gap
plt.legend()
plt.grid(axis='y', linestyle='dotted')
plt.savefig('mrr_growth_analysis.png') # Save the visualization
plt.show()

# Verification Email (as requested)
verification_email = "23f3003273@ds.study.iitm.ac.in"
# This variable is stored in the code for verification purposes.
