import pandas as pd

def save_df_as_ltablex_booktabs(df, filename, caption='', label=''):
    with open(filename, 'w') as f:
        f.write('\\begin{tabularx}{\\textwidth}{l' + 'X' * len(df.columns) + '}\n')
        f.write(f'\\caption{{{caption}}} \\label{{{label}}} \\\\\n')
        f.write('\\toprule[1.5pt]\n')
        f.write(' & '.join(['{}'] + [f'\\textbf{{{x}}}' for x in df.columns]) + ' \\\\\n')
        f.write('\\midrule[1.5pt]\n')
        f.write('\\endfirsthead\n')
        f.write('\\multicolumn{' + str(len(df.columns) + 1) + '}{c}%\n')
        f.write('{\\tablename\\ \\thetable\\ -- \\textit{Continued from previous page}} \\\\\n')
        f.write('\\toprule[1.5pt]\n')
        f.write(' & '.join(['{}'] + [f'\\textbf{{{x}}}' for x in df.columns]) + ' \\\\\n')
        f.write('\\midrule[1.5pt]\n')
        f.write('\\endhead\n')
        f.write('\\bottomrule[1pt]\n')
        f.write('\\multicolumn{' + str(len(df.columns) + 1) + '}{r}{\\textit{Continued on next page}} \\\\\n')
        f.write('\\endfoot\n')
        f.write('\\bottomrule[1pt]\n')
        f.write('\\endlastfoot\n')

        for i, row in df.iterrows():
            row_str = ' & '.join([str(x) for x in row.values])
            f.write(f'{i} & {row_str} \\\\\n')

        f.write('\\end{tabularx}\n')