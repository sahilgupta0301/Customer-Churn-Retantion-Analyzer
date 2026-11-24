# 1. Store customer data in a simple list of dictionaries
customers = [
    {"id": 101, "name": "Aarav Sharma", "plan": "Basic", "charge": 499, "days": 5, "status": "Active"},
    {"id": 102, "name": "Priya Verma", "plan": "Premium", "charge": 999, "days": 45, "status": "Churned"},
    {"id": 103, "name": "Rohan Gupta", "plan": "Standard", "charge": 799, "days": 32, "status": "Active"},
    {"id": 104, "name": "Sneha Singh", "plan": "Basic", "charge": 499, "days": 60, "status": "Churned"},
    {"id": 105, "name": "Vikram Patel", "plan": "Premium", "charge": 999, "days": 2, "status": "Active"},
    {"id": 106, "name": "Ananya Mishra", "plan": "Standard", "charge": 799, "days": 38, "status": "Active"},
    {"id": 107, "name": "Kabir Das", "plan": "Basic", "charge": 499, "days": 12, "status": "Active"},
    {"id": 108, "name": "Meera Joshi", "plan": "Premium", "charge": 999, "days": 50, "status": "Churned"},
]

# 2. Separate churned and at-risk customers
total = len(customers)
churned = [c for c in customers if c["status"] == "Churned"]
at_risk = [c for c in customers if c["status"] == "Active" and c["days"] > 30]

# 3. Calculate churn rate and total revenue lost
churn_rate = (len(churned) / total) * 100
lost_revenue = sum(c["charge"] for c in churned)

# 4. Print the report
print("=== CUSTOMER CHURN & RETENTION REPORT ===")
print(f"Total Customers : {total}")
print(f"Churned Count   : {len(churned)}")
print(f"Churn Rate      : {churn_rate:.1f}%")
print(f"Monthly Loss    : ₹{lost_revenue}\n")

print("--- High-Risk Active Customers (Inactive > 30 Days) ---")
for c in at_risk:
    print(f"ID {c['id']} | {c['name']} ({c['plan']}) - Inactive for {c['days']} days")