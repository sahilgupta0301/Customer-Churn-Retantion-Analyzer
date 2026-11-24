# Customer Churn & Retention Analyzer

A lightweight Python analytics tool built to track subscription metrics, calculate customer churn rates, quantify monthly revenue loss, and identify high-risk inactive users for targeted retention campaigns.

## Key Features
- **Churn Rate Calculation:** Automatically computes the percentage of customers who have discontinued their subscriptions.
- **Revenue Loss Tracking:** Calculates total monthly recurring revenue (MRR) lost from churned accounts.
- **At-Risk Customer Detection:** Flags active subscribers who have been inactive for more than 30 days so businesses can proactively re-engage them.
- **Zero External Dependencies:** Built using pure Python data structures (`lists` and `dictionaries`) for fast, dependency-free execution.

## Project Structure
```text
Customer-Churn-Retention-Analyzer/
│
├── main.py       # Core script for churn calculation and report generation
└── README.md     # Project documentation
