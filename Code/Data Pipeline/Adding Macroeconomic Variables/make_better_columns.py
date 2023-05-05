import pandas as pd

def main():
    new_df = pd.DataFrame()
    old_df = pd.read_pickle('master+about+location+co_entry.pkl')


    # Primary Stuff
    new_df["id"] = old_df["id"]
    new_df["name"] = old_df["name_y"]
    # Make it a datetime object, where the current form is dd.mm.yyyy
    new_df['founded'] = pd.to_datetime(old_df['registry_date'], format='%d.%m.%Y')
    new_df["canton"] = old_df["canton"]
    new_df["city"] = old_df["seat"]
    new_df["zip"] = old_df["plz_city"].str.extract(r'(\d{4})')
    new_df["address"] = old_df["address_y"]
    new_df["legal_form"] = old_df["legal_form"]
    new_df["industry"] = old_df["industry"]
    new_df["size"] = old_df["employees_total"]
    new_df["employees"] = old_df["employees_on_linkedin"]
    new_df["followers"] = old_df["followers"]


    # Secondary Stuff
    new_df["status"] = old_df["status"]
    new_df["auditor"] = old_df["auditor"]
    new_df["purpose"] = old_df["purpose"]
    new_df["keywords"] = old_df["specialties"]
    new_df["keyword"] = old_df["keyword"]
    new_df["name_linekdin"] = old_df["name_x"]
    new_df["short_description_linkedin"] = old_df["description"]
    new_df["long_description_linkedin"] = old_df["long_description"]
    new_df["linkedin_url"] = old_df["linkedin_url"]
    new_df["employees_list"] = old_df["employees_link"]
    new_df["website"] = old_df["website_link"]

    # ID's
    new_df["uid"] = old_df["uid"]
    new_df["ch_id"] = old_df["ch_id"]
    new_df["ehra_id"] = old_df["ehra_id"]

    # Remove all data without a founded date
    new_df = new_df[new_df["founded"].notnull()]

    # If the website = "https://null", set it to NaN
    new_df["website"] = new_df["website"].replace("https://null", pd.np.nan)

    # Save
    new_df.to_pickle('data_analysis.pkl')
    new_df.to_csv('data_analysis.csv')
    print(new_df)
    print(new_df.describe())

if __name__ == '__main__':
    main()

