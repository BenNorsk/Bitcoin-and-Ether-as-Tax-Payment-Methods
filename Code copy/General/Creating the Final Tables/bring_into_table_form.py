import pandas as pd

def save_df_as_longtable(df, filename, caption='', label='', index=False):
    with open(filename, 'w') as f:
        f.write('\\begin{longtable}{|' + '|'.join(['l' for _ in range(len(df.columns))]) + '|}\n')
        f.write(f'\\caption{{{caption}}} \\label{{{label}}} \\\\\n')
        f.write('\\hline\n')
        f.write(' & '.join(df.columns) + ' \\\\\n')
        f.write('\\hline\n')
        f.write('\\endfirsthead\n')
        f.write('\\multicolumn{' + str(len(df.columns)) + '}{c}%\n')
        f.write('{\\tablename\\ \\thetable\\ -- \\textit{Continued from previous page}} \\\\\n')
        f.write('\\hline\n')
        f.write(' & '.join(df.columns) + ' \\\\\n')
        f.write('\\hline\n')
        f.write('\\endhead\n')
        f.write('\\hline \\multicolumn{' + str(len(df.columns)) + '}{r}{\\textit{Continued on next page}} \\\\\n')
        f.write('\\endfoot\n')
        f.write('\\hline\n')
        f.write('\\endlastfoot\n')

        for i, row in df.iterrows():
            row_str = ' & '.join([str(x) for x in row.values])
            if index:
                row_str = f'{i} & {row_str}'
            f.write(f'{row_str} \\\\\n')
            f.write('\\hline\n')

        f.write('\\end{longtable}\n')

df = pd.read_csv('data_analysis.csv', index_col=0)
print(df)

# Reset the index
df = df.reset_index()
print(df)

# Choose the columns:
colums = ["name", "founded", "canton", "industry"]
df = df[colums]
print(df)

# Rename the columns:
df = df.rename(columns={"name": "name", "founded": "founding date", "canton": "canton", "industry": "sector"})
print(df)

# Save the dataframe as a latex file
df.to_latex('data_analysis.tex')
save_df_as_longtable(df, 'data_analysis_longtable.tex', caption='Sample Companies', label='tab:companies', index=True)
df.to_csv("companies.csv")
