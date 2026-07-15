import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
df = pd.read_csv(r"C:\Users\Arav\Downloads\archive\bank_fraud.csv")
df = df.drop("fraud_type", axis=1)
df = df.drop_duplicates()

print("Dataset Shape:", df.shape)
print("Missing Values:", df.isna().sum().sum())
print("-" * 50)

# Overall statistics
total_trans = len(df)
total_fraud = df['is_fraud'].sum()
fraud_rate = (total_fraud / total_trans * 100)

print("\n📊 OVERALL STATISTICS")
print(f"Total Transactions: {total_trans:,}")
print(f"Fraudulent Transactions: {total_fraud:,}")
print(f"Fraud Rate: {fraud_rate:.2f}%\n")

# Helper function to create color palette (top in red, rest in gray)
def create_color_palette(n_bars, top_color='#E24B4A', rest_color='#A8A8A8'):
    """Create color list with top bar highlighted"""
    colors = [top_color] + [rest_color] * (n_bars - 1)
    return colors

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 1: FRAUD BY MERCHANT CATEGORY
# ═══════════════════════════════════════════════════════════════════

fraud_by_merchant = df[df['is_fraud'] == 1].groupby('merchant_category').size().reset_index(name='count')
fraud_by_merchant = fraud_by_merchant.sort_values('count', ascending=False)

print("\n ======= TOP 10 MERCHANT FRAUD =======")
print(fraud_by_merchant.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_merchant.head(10)))
sns.barplot(data=fraud_by_merchant.head(10), x='merchant_category', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Merchant Categories - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_merchant.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 2: FRAUD BY COUNTRY
# ═══════════════════════════════════════════════════════════════════

fraud_by_country = df[df['is_fraud'] == 1].groupby('country').size().reset_index(name='count')
fraud_by_country = fraud_by_country.sort_values('count', ascending=False)

print("\n ======= TOP 10 COUNTRIES WITH MOST FRAUD =======")
print(fraud_by_country.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_country.head(10)))
sns.barplot(data=fraud_by_country.head(10), x='country', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Countries - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_country.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 3: FRAUD BY CITY
# ═══════════════════════════════════════════════════════════════════

fraud_by_city = df[df['is_fraud'] == 1].groupby('city').size().reset_index(name='count')
fraud_by_city = fraud_by_city.sort_values('count', ascending=False)

print("\n ======= TOP 10 CITIES WITH MOST FRAUD =======")
print(fraud_by_city.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_city.head(10)))
sns.barplot(data=fraud_by_city.head(10), x='city', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Cities - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_city.png', dpi=150)
plt.show()

print("\n Analysis Complete! Charts saved.")

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 4: FRAUD BY Payment Method
# ═══════════════════════════════════════════════════════════════════

fraud_by_payment_method = df[df['is_fraud'] == 1].groupby('payment_method').size().reset_index(name='count')
fraud_by_payment_method = fraud_by_payment_method.sort_values('count', ascending=False)

print("\n ======= TOP 10 Payment Method FRAUD =======")
print(fraud_by_payment_method.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_payment_method.head(10)))
sns.barplot(data=fraud_by_payment_method.head(10), x='payment_method', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Payment Method - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_payment_method.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 5: FRAUD BY Customer Age
# ═══════════════════════════════════════════════════════════════════

fraud_by_customer_age = df[df['is_fraud'] == 1].groupby('customer_age').size().reset_index(name='count')
fraud_by_customer_age = fraud_by_customer_age.sort_values('count', ascending=False)

print("\n ======= TOP 10 Customer Age =======")
print(fraud_by_customer_age.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_customer_age.head(10)))
sns.barplot(data=fraud_by_customer_age.head(10), x='customer_age', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Customer Age - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_customer_age.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 6: FRAUD BY Device Type
# ═══════════════════════════════════════════════════════════════════

fraud_by_device_type = df[df['is_fraud'] == 1].groupby('device_type').size().reset_index(name='count')
fraud_by_device_type = fraud_by_device_type.sort_values('count', ascending=False)

print("\n ======= TOP 10 Devices WITH MOST FRAUD =======")
print(fraud_by_device_type.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_device_type.head(10)))
sns.barplot(data=fraud_by_device_type.head(10), x='device_type', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Devices - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_device_type.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 7: Finding User Account Balance 
# ═══════════════════════════════════════════════════════════════════

fraud_by_account_balance = df[df['is_fraud'] == 1].groupby('account_balance').size().reset_index(name='count')
fraud_by_account_balance = fraud_by_account_balance.sort_values('count', ascending=False)

print("\n ======= TOP 10 Account Balance =======")
print(fraud_by_account_balance.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_account_balance.head(10)))
sns.barplot(data=fraud_by_account_balance.head(10), x='account_balance', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top Account Balance - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_account_balance.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 8: Finding Distance of Transaction 
# ═══════════════════════════════════════════════════════════════════

fraud_by_distance_from_home_km = df[df['is_fraud'] == 1].groupby('distance_from_home_km').size().reset_index(name='count')
fraud_by_distance_from_home_km = fraud_by_distance_from_home_km.sort_values('count', ascending=False)

print("\n ======= TOP Distance of Transaction =======")
print(fraud_by_distance_from_home_km.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_distance_from_home_km.head(10)))
sns.barplot(data=fraud_by_distance_from_home_km.head(10), x='distance_from_home_km', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top Distance - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_distance_from_home_km.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 9: Finding User Transaction Time 
# ═══════════════════════════════════════════════════════════════════

fraud_by_transaction_time = df[df['is_fraud'] == 1].groupby('transaction_time').size().reset_index(name='count')
fraud_by_transaction_time = fraud_by_transaction_time.sort_values('count', ascending=False)

print("\n ======= TOP Transaction Time =======")
print(fraud_by_transaction_time.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_transaction_time.head(10)))
sns.barplot(data=fraud_by_transaction_time.head(10), x='transaction_time', y='count', palette=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top Transaction Time - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_transaction_time.png', dpi=150)
plt.show()

# ═══════════════════════════════════════════════════════════════════
# ANALYSIS 10: Finding User Pin Changed 
# ═══════════════════════════════════════════════════════════════════

fraud_by_pin_changed_recently = df[df['is_fraud'] == 1].groupby('pin_changed_recently').size().reset_index(name='count')
fraud_by_pin_changed_recently = fraud_by_pin_changed_recently.sort_values('count', ascending=False)

print("\n ======= Top User Pin Changed =======")
print(fraud_by_pin_changed_recently.head(10).to_string(index=False))

plt.figure(figsize=(10, 5))
colors = create_color_palette(len(fraud_by_pin_changed_recently.head(10)))
sns.barplot(data=fraud_by_pin_changed_recently.head(10), x='pin_changed_recently', y='count', palette=colors)
plt.xticks(rotation=0, ha='right')
plt.title('Pin Changed ? - Fraud Count', fontweight='bold')
plt.ylabel('Number of Frauds')
plt.tight_layout()
plt.savefig('fraud_by_pin_changed_recently.png', dpi=150)
plt.show()

print("\n All analyses complete! Charts saved with highlighted top categories.")

print("=================== result ===========================")

print("This bank fraud analysis identified several factors associated with fraudulent transactions. The results show that fraud is more common in countries such as the United States, India, and the United Kingdom, with fraudsters frequently targeting ATM withdrawals, jewelry purchases, and cryptocurrency exchanges. Fraudulent transactions are often conducted using credit or debit cards, through mobile devices, by younger customers, and during unusual hours such as late at night. To reduce fraud, banks should implement real-time AI-based fraud detection systems, multi-factor authentication (MFA), transaction monitoring, device verification, instant customer alerts, and risk-scoring mechanisms. Additionally, customer awareness programs and enhanced security checks for high-risk transactions can help prevent fraud and improve overall banking security.")