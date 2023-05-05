import pandas as pd

def main():
    # About data
    # 1. Read the data
    main_df = pd.read_pickle("main.pkl")
    location_df = pd.read_pickle("location.pkl")
    # Read the delete list (not_crypto_ids.txt)
    with open("not_crypto_ids.txt", "r") as f:
        delete_list = f.read()
    # Split the list
    delete_list = delete_list.split("\n")
    for e in delete_list:
        delete_list[delete_list.index(e)] = int(e)


    print(main_df)
    print(location_df)
    print(delete_list)

    # Merge the data on id
    df = pd.merge(location_df, main_df,  on="id")
    # Delete rows, where the name is a duplicate
    df = df.drop_duplicates(subset="name", keep="first")
    # Delete all rows, where the id is in the delete list
    df = df[~df["id"].isin(delete_list)]
    # Save the data
    print(df)
    # Save the data as CSV
    df.to_csv("master+about+location.csv", index=False)
    # Save the data as pickle
    df.to_pickle("master+about+location.pkl")

if __name__ == "__main__":
    main()