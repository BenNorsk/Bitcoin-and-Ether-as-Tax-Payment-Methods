import pandas as pd

df = pd.read_pickle('industry_data.pkl')

# Make a new col called "Other legal forms", which is the sum of all the other legal forms
df['other legal forms'] = df['Einzelunternehmen'] + df['Kollektivgesellschaft'] + df['Verein'] + df['Stiftung'] + df['Zweigniederlassung']
df["AG's"] = df["Aktiengesellschaft"]
df["GmbH's"] = df["Gesellschaft mit beschränkter Haftung"]

# Make a new col Share of AG's
df["share of AG's"] = df["AG's"] / df["companies"]
df["share of GmbH's"] = df["GmbH's"] / df["companies"]

# Drop the old cols
# df = df.drop(["Einzelunternehmen", "Kollektivgesellschaft", "Verein", "Stiftung", "Zweigniederlassung", "Aktiengesellschaft", "Gesellschaft mit beschränkter Haftung"], axis=1)


# Make a new col "Financial sector"
all_cols = df.columns
# Remove these cols from all_cols (month	days	canton	companies	Aktiengesellschaft	Gesellschaft mit beschränkter Haftung	Einzelunternehmen	Kollektivgesellschaft	Verein	Stiftung	Zweigniederlassung	employees	followers)
all_cols = all_cols.drop(["month", "days", "canton", "companies", "Aktiengesellschaft", "Gesellschaft mit beschränkter Haftung", "Einzelunternehmen", "Kollektivgesellschaft", "Verein", "Stiftung", "Zweigniederlassung", "employees", "followers", "share of AG's", "share of GmbH's", "other legal forms", "AG's", "GmbH's"])
# Define these as IT cols:
# IT Services and IT Consulting
# Software Development
# Information Technology & Services
# Technology, Information and Internet
# Computer Networking Products
# Computer and Network Security
# Data Security Software Products
# Computer Games
financial_cols = ["Financial Services", "Venture Capital and Private Equity Principals", "Investment Management", "Capital Markets", "Banking", "Fundraising"]
it_cols = ["IT Services and IT Consulting", "Software Development", "Information Technology & Services", "Technology, Information and Internet", "Computer Networking Products", "Computer and Network Security", "Data Security Software Products", "Computer Games"]
rest_cols = all_cols.drop(financial_cols).drop(it_cols)
df["financial sector"] = df[financial_cols].sum(axis=1)
df["IT sector"] = df[it_cols].sum(axis=1)
df["other sectors"] = df[rest_cols].sum(axis=1)

# Make a new col "Share of financial sector"
df["share of financial sector"] = df["financial sector"] / df["companies"]
df["share of IT sector"] = df["IT sector"] / df["companies"]

# Drop the old cols
df = df.drop(all_cols, axis=1)
# Drop the cols = Aktiengesellschaft	Gesellschaft mit beschr√§nkter Haftung	Einzelunternehmen	Kollektivgesellschaft	Verein	Stiftung	Zweigniederlassung
df = df.drop(["Aktiengesellschaft", "Gesellschaft mit beschränkter Haftung", "Einzelunternehmen", "Kollektivgesellschaft", "Verein", "Stiftung", "Zweigniederlassung"], axis=1)

# Save the df
df.to_pickle('smart_industry_data.pkl')
df.to_csv('smart_industry_data.csv')