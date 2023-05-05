import pandas as pd

def main():
    df_companies = pd.read_pickle("master+about.pkl")
    print(df_companies)
    df_master = pd.read_pickle("master.pkl")
    print(df_master)
    # Make the id the index
    df_companies["id"] = df_companies.index
    # Make the index the id of the company
    df_master["id"] = df_master.index
    # Make an integer out of the id column
    df_master["id"] = df_master["id"].astype(int)
    df_companies["id"] = df_companies["id"].astype(int)
    # Drop the followers of the df_master
    df_master = df_master.drop(columns=['followers', "industry"])
    df_companies = df_companies.drop(columns=["name"])
    # Join the two dataframes on the id column
    print(df_master)
    print(df_companies)
    df = pd.merge(df_master, df_companies, on="id")
    # Save the dataframe
    df.to_pickle("main.pkl")
    df.to_csv("main.csv")
    print(df)

if __name__ == "__main__":
    main()

