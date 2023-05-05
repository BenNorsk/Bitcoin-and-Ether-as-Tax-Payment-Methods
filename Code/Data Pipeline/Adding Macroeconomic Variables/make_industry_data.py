import pandas as pd
import datetime

def add_days_column(companies_df):
    for index, row in companies_df.iterrows():
        year = row["founded"].year
        month = row["founded"].month
        day = row["founded"].day
        companies_df.at[index, "days"] = (datetime.datetime(year, month, day) - datetime.datetime(2016, 1, 31)).days 
    return companies_df

def get_last_day_of_month(month, year):
    months_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if (year == 2020 or year == 2016) and month == 2:
        return 29
    else:
        return months_day[month]

def create_industry_df(companies_df):
    industry_df = pd.DataFrame()
    for year in range(2016, 2023):
        for month in range(1, 13):
            for canton in ["ZG", "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "FR", "SO", "BS", "BL", "SH", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]:
                day = get_last_day_of_month(month, year)
                date = pd.to_datetime(f"{day}.{month}.{year}", format='%d.%m.%Y')
                days = (datetime.datetime(year, month, day) - datetime.datetime(2016, 1, 31)).days
                row = {"month": date, "days": days, "canton": canton}
                industry_df = industry_df.append(row, ignore_index=True)
    industry_df["companies"] = 0
    industry_df["Aktiengesellschaft"] = 0
    industry_df["Gesellschaft mit beschränkter Haftung"] = 0
    industry_df["Einzelunternehmen"] = 0
    industry_df["Kollektivgesellschaft"] = 0
    industry_df["Verein"] = 0
    industry_df["Stiftung"] = 0
    industry_df["Zweigniederlassung"] = 0
    industry_df["employees"] = 0
    industry_df["followers"] = 0
    for industry in companies_df["industry"].unique():
        industry_df[industry] = 0
    return industry_df

def add_previous_companies(industry_df, index, industries):
    if index == 0:
        return industry_df
    else:
        industry_df.at[index, "companies"] = industry_df.at[index - 1, "companies"]
        industry_df.at[index, "Aktiengesellschaft"] = industry_df.at[index - 1, "Aktiengesellschaft"]
        industry_df.at[index, "Gesellschaft mit beschränkter Haftung"] = industry_df.at[index - 1, "Gesellschaft mit beschränkter Haftung"]
        industry_df.at[index, "Einzelunternehmen"] = industry_df.at[index - 1, "Einzelunternehmen"]
        industry_df.at[index, "Kollektivgesellschaft"] = industry_df.at[index - 1, "Kollektivgesellschaft"]
        industry_df.at[index, "Verein"] = industry_df.at[index - 1, "Verein"]
        industry_df.at[index, "Stiftung"] = industry_df.at[index - 1, "Stiftung"]
        industry_df.at[index, "Zweigniederlassung"] = industry_df.at[index - 1, "Zweigniederlassung"]
        industry_df.at[index, "employees"] = industry_df.at[index - 1 , "employees"]
        industry_df.at[index, "followers"] = industry_df.at[index - 1, "followers"]
        for industry in industries:
            industry_df.at[index, industry] = industry_df.at[index - 1, industry]
        return industry_df

def add_companies(industry_df, index, companies_df, correct_canton):
    legal_forms = ["Aktiengesellschaft", "Gesellschaft mit beschränkter Haftung", "Einzelunternehmen", "Kollektivgesellschaft", "Verein", "Stiftung", "Zweigniederlassung"]
    industries = companies_df["industry"].unique()

    if index == 0:
        for industry in industries:
            industry_df.at[index, industry] = correct_canton[correct_canton["industry"] == industry].shape[0]
        industry_df.at[index, "companies"] = correct_canton.shape[0]
        for legal_form in legal_forms:
            industry_df.at[index, legal_form] = correct_canton[correct_canton["legal_form"] == legal_form].shape[0]
        industry_df.at[index, "employees"] = int(correct_canton["employees"].sum())
        industry_df.at[index, "followers"] = int(correct_canton["followers"].sum())
    else:
        industry_df.at[index, "companies"] = industry_df.at[index - 1, "companies"] + correct_canton.shape[0]
        industry_df.at[index, "employees"] = industry_df.at[index - 1, "employees"] + int(correct_canton["employees"].sum())
        industry_df.at[index, "followers"] = industry_df.at[index - 1, "followers"] + int(correct_canton["followers"].sum())
        for industry in industries:
            industry_df.at[index, industry] = industry_df.at[index - 1, industry] + correct_canton[correct_canton["industry"] == industry].shape[0]
        for legal_form in legal_forms:
            industry_df.at[index, legal_form] = industry_df.at[index - 1, legal_form] + correct_canton[correct_canton["legal_form"] == legal_form].shape[0]
    return industry_df

def add_companies2(industry_df, index, companies_df, correct_canton):
    legal_forms = ["Aktiengesellschaft", "Gesellschaft mit beschränkter Haftung", "Einzelunternehmen", "Kollektivgesellschaft", "Verein", "Stiftung", "Zweigniederlassung"]
    industries = companies_df["industry"].unique()
    industry_df.at[index, "employees"] = int(correct_canton["employees"].sum())
    industry_df.at[index, "followers"] = int(correct_canton["followers"].sum())
    industry_df.at[index, "companies"] = correct_canton.shape[0]
    for industry in industries:
            industry_df.at[index, industry] = correct_canton[correct_canton["industry"] == industry].shape[0]
    for legal_form in legal_forms:
        industry_df.at[index, legal_form] = correct_canton[correct_canton["legal_form"] == legal_form].shape[0]
    return industry_df

    

def fill_industry_df(industry_df, companies_df):
    for index, row in industry_df.iterrows():
        correct_dates = companies_df[companies_df["days"] <= row["days"]]
        correct_canton = correct_dates[correct_dates["canton"] == row["canton"]]
        if row["canton"] == "ZG":
            print(row["month"])
            print(correct_canton)
        industry_df = add_companies2(industry_df, index, companies_df, correct_canton)
    return industry_df

def main():
    companies_df = pd.read_pickle('data_analysis.pkl')
    companies_df = add_days_column(companies_df)
    industry_df = create_industry_df(companies_df)
    industry_df = fill_industry_df(industry_df, companies_df)
    print(industry_df)
    industry_df.to_pickle("industry_data.pkl")
    industry_df.to_csv("industry_data.csv")

if __name__ == "__main__":
    # main()

