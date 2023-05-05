import pandas as pd
from make_similarity_table import make_comparison_for_one_case, add_value

def one_cutoff_table(c):
    agg_df = pd.DataFrame()
    for i in range(0, 5):
        synth_file = f'automatise/case_{i}/controlled_for_taxes/ZG/{c}_synth_ZG.csv'
        weights_file = f'automatise/case_{i}/controlled_for_taxes/ZG/{c}_weights.csv'
        df = make_comparison_for_one_case(synth_file, weights_file)
        # Add the synth_ZG column to the df
        df['case_{}'.format(i)] = df['synth_ZG']
        
        # Append the df to the aggregated dataframe
        agg_df = pd.concat([agg_df, df], axis=1)

    # Delete columns with the name "synth_ZG"
    agg_df = agg_df.loc[:,~agg_df.columns.duplicated()]

    # Delete colunn with the name "synth_ZG"
    agg_df = agg_df.drop(columns=['synth_ZG'])

    # Set the field at case_0 to "-" and variable == "taxes", "working_population", "share of financial sector", "share of IT sector" to "-"
    agg_df.loc[(agg_df['variables'] == "taxes") & (agg_df['case_0'] == agg_df['case_0']), 'case_0'] = "-"
    agg_df.loc[(agg_df['variables'] == "working_population") & (agg_df['case_0'] == agg_df['case_0']), 'case_0'] = "-"
    agg_df.loc[(agg_df['variables'] == "share of financial sector") & (agg_df['case_0'] == agg_df['case_0']), 'case_0'] = "-"
    agg_df.loc[(agg_df['variables'] == "share of IT sector") & (agg_df['case_0'] == agg_df['case_0']), 'case_0'] = "-"
    # Set the field at case_1 to "-" and variable == "working_population", "share of financial sector", "share of IT sector" to "-"
    agg_df.loc[(agg_df['variables'] == "working_population") & (agg_df['case_1'] == agg_df['case_1']), 'case_1'] = "-"
    agg_df.loc[(agg_df['variables'] == "share of financial sector") & (agg_df['case_1'] == agg_df['case_1']), 'case_1'] = "-"
    agg_df.loc[(agg_df['variables'] == "share of IT sector") & (agg_df['case_1'] == agg_df['case_1']), 'case_1'] = "-"
    # Set the field at case_2 to "-" and variable == "share of financial sector", "share of IT sector" to "-"
    agg_df.loc[(agg_df['variables'] == "share of financial sector") & (agg_df['case_2'] == agg_df['case_2']), 'case_2'] = "-"
    agg_df.loc[(agg_df['variables'] == "share of IT sector") & (agg_df['case_2'] == agg_df['case_2']), 'case_2'] = "-"
    # Set the field at case_3 to "-" and variable == "share of IT sector" to "-"
    agg_df.loc[(agg_df['variables'] == "share of IT sector") & (agg_df['case_3'] == agg_df['case_3']), 'case_3'] = "-"

    
    # Set the index = 1 where the variable == "taxes"
    agg_df.loc[(agg_df['variables'] == "companies"), 'index'] = 0
    agg_df.loc[(agg_df['variables'] == "taxes"), 'index'] = 1
    # Set the index = 2 where the variable == "working_population"
    agg_df.loc[(agg_df['variables'] == "working_population"), 'index'] = 2
    # Set the index = 3 where the variable == "share of financial sector"
    agg_df.loc[(agg_df['variables'] == "share of financial sector"), 'index'] = 3
    # Set the index = 4 where the variable == "share of IT sector"
    agg_df.loc[(agg_df['variables'] == "share of IT sector"), 'index'] = 4

    # Rename the columns
    cols = {
        "case_0": "synth. ZG ($C_{0}$)",
        "case_1": "synth. ZG ($C_{1}$)",
        "case_2": "synth. ZG ($C_{2}$)",
        "case_3": "synth. ZG ($C_{3}$)",
        "case_4": "synth. ZG ($C_{4}$)"
    }
    # Rename the values in the variable column
    agg_df['variables'] = agg_df['variables'].replace({
        "companies": "$A_{" + str(c) + "}(\\bar{Y}_{2020})$",
        "taxes": "$A_{" + str(c) + "}(\\bar{x}_{TX_{2020}})$",
        "working_population": "$A_{" + str(c) + "}(\\bar{x}_{WP_{2020}})$",
        "share of financial sector": "$A_{" + str(c) + "}(\\bar{x}_{f_{2020}})$",
        "share of IT sector": "$A_{" + str(c) + "}(\\bar{x}_{IT_{2020}})$"
    })
    agg_df = agg_df.rename(columns=cols)


    # Rename the canton to index
    agg_df = agg_df.rename(columns={"canton": "index"})
    # Replace the
    # Order the dataframe by the index
    agg_df = agg_df.sort_values(by=['index'], ascending=True)

    # Remove the index column called "canton"
    agg_df = agg_df.drop(columns=['index'])


    # Drop the canton column
    print(agg_df)
    return agg_df


cutoffs_df = pd.DataFrame()
for c in range(0, 21):
    df = one_cutoff_table(c)
    # Append the df to the aggregated dataframe
    cutoffs_df = cutoffs_df.append(df)

print(cutoffs_df)
# Reset the index
robustness_matrix_goodness_of_fit = cutoffs_df.reset_index(drop=True)
# Save the dataframe
robustness_matrix_goodness_of_fit.to_csv('robustness_matrix_goodness_of_fit.csv', index=False)
# Print the dataframe to latex
robustness_matrix_goodness_of_fit.to_latex('robustness_matrix_goodness_of_fit.tex', index=False, escape=False)
# Make it a latex with a long table

