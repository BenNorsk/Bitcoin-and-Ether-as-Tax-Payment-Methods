import pandas as pd

def get_p_value_for_cutoff(cutoff, mspe_df):
    # Select the rows where cutoff
    mspe_df = mspe_df[mspe_df["cutoff"] == cutoff]
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

def add_minimal_p_value():
    mspe_df = pd.read_csv(f'case_0/rspes.csv')
    minimal_p_df = pd.DataFrame(columns=["cutoff", "p_value", "case"])
    for cutoff in mspe_df["cutoff"].unique():
        # Select only the mspe df for the cutoff
        df = mspe_df[mspe_df["cutoff"] == cutoff]
        minimal_p_value = (1 / len(df["canton"].unique()))
        minimal_p_df = minimal_p_df.append({"cutoff": cutoff, "p_value": minimal_p_value, "case": "min_p_value"}, ignore_index=True)
    return minimal_p_df
    

def make_p_value_df():
    master_df = pd.DataFrame(columns=["cutoff", "p_value", "case"])
    for i in range(0,5):
        mspe_df = pd.read_csv(f'case_{i}/rspes.csv')
        mspe_df["MSPE_ratio"] = mspe_df["RSPE_ratio"]
        p_value_df = create_a_p_value_df(mspe_df)
        p_value_df["case"] = i
        master_df = master_df.append(p_value_df, ignore_index=True)
    master_df = master_df.append(add_minimal_p_value(), ignore_index=True)
    return master_df

p_value_df = make_p_value_df()
#p_value_df.to_csv("p_values.csv", index=False)
