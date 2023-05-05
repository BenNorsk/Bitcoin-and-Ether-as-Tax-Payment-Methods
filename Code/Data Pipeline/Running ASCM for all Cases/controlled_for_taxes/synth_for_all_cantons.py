import pandas as pd
import sys
import os
from make_one_synth_dataset import *


def set_canton_to_treated(canton, days, df):
    # Where canton = canton, and days >= days, set treated to True
    df.loc[(df['canton'] == canton) & (df['days'] >= days), 'treatment'] = 1
    # Everywhere else, set treated to False
    df.loc[(df['canton'] != canton) | (df['days'] < days), 'treatment'] = 0
    return df

def filter_cantons(df, cutoff):
    # Get all rows where days = 2526
    rows = df[df['days'] == 2526]
    # Get all cantons where the number of companies is less than cutoff
    cantons = rows[rows['companies'] >= cutoff]['canton'].unique()
    return cantons

def execute_action(df, cantons, rspe, cutoff):
    for canton in cantons:
            # Set canton to treated
            canton_df = set_canton_to_treated(canton, 1827, df)
            # Save to CSV
            file_path = f'controlled_for_taxes/{canton}/{cutoff}_prelim_synth_{canton}.csv'
            canton_df.to_csv(file_path, index=False)
            # Run "Rscript synth_control_one_canton.R canton file_path"
            os.system(f'Rscript synth_control_one_canton.R {canton} {file_path} {cutoff}')
            # Create a synth dataset for the canton
            weights = pd.read_csv(f'controlled_for_taxes/{canton}/{cutoff}_weights.csv')
            file_path = f'controlled_for_taxes/{canton}/{cutoff}_synth_{canton}.csv'
            save_synth_df(canton_df, weights, canton, file_path)
            # plot the synth dataset
            os.system(f'Rscript plot_one_canton.R {canton} {file_path} {cutoff}')
            # Plot the difference and save the RMSPE
            os.system(f'Rscript statistically_test_one_canton.R {canton} {file_path} {cutoff}')
            rspe_canton = pd.read_csv(f'controlled_for_taxes/{canton}/{cutoff}_rspe_{canton}.csv')
            # mspe_before,mspe_after,mspe_ratio
            row = {'canton': canton,
                    'RSPE_before': rspe_canton['mspe_before'].iloc[0],
                    'RSPE_after': rspe_canton['mspe_after'].iloc[0],
                    'RSPE_ratio': rspe_canton['mspe_ratio'].iloc[0],
                    'cutoff': cutoff}
            rspe = rspe.append(row, ignore_index=True)
    print(rspe)
    return rspe

def main():
    # Read data
    df = pd.read_csv('aggregated_industry_data.csv')
    # Filter out all cantons except ZG, ZH, TI, GE and VD
    cutoff = 0
    rspe = pd.DataFrame(columns=['canton', 'RSPE_before', 'RSPE_after', 'RSPE_ratio', 'cutoff'])
    while cutoff <= 20:
        cantons = filter_cantons(df, cutoff)
        filtered_df = df[df['canton'].isin(cantons)]
        # Iterate over cantons
        print(f'cutoff: {cutoff}')
        rspe = execute_action(filtered_df, cantons, rspe, cutoff)
        cutoff += 1
    rspe.to_csv('rspes.csv', index=False)


if __name__ == '__main__':
    main()



