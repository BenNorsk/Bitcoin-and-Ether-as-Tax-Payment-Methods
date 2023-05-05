import pandas as pd


def get_p_value_for_cutoff(cutoff, mspe_df):
    # Select the rows where cutoff
    mspe_df = mspe_df[mspe_df["cutoff"] == cutoff]
    print(mspe_df)
    # Get the MSPE_ratio of the canton of ZG
    mspe_ratio_zg = mspe_df[mspe_df["canton"] == "ZG"]["MSPE_ratio"].values[0]
    # Calculate the total amount of cantons
    total_cantons = len(mspe_df["canton"].unique())
    # Calculate the amount of cantons with a higher MSPE_ratio than mspe_ratio_zg
    cantons_higher = len(mspe_df[mspe_df["MSPE_ratio"] >= mspe_ratio_zg]["canton"].unique())
    p = cantons_higher / total_cantons
    return p

def create_a_p_value_df(mspe_df):
    # Make an empty df named p_values
    p_values = pd.DataFrame(columns=["cutoff", "p_value"])
    # Iterate through all cutoffs
    for cutoff in mspe_df["cutoff"].unique():
        # Get the p_value for the cutoff
        p_value = get_p_value_for_cutoff(cutoff, mspe_df)
        # Append the p_value to the p_values df
        p_values = p_values.append({"cutoff": cutoff, "p_value": p_value}, ignore_index=True)
    # Round all values to 2 decimals
    p_values = p_values.round(2)
    return p_values



# Read in the data
df = pd.read_csv("mspes_no_cv.csv")
p_value_df = create_a_p_value_df(df)
p_value_df.to_csv("p_values_no_cv.csv", index=False)


