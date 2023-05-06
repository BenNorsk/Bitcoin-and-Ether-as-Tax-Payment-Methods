import pandas as pd


def calculate_treatment_effect(y_post, y_star_post):
    time_units = len(y_post)
    diff = 0
    for i in range(len(y_post)):
        diff += y_post[i] - y_star_post[i]
    effect = diff / time_units
    # Round the effect to 2 places after the comma {.2f}
    print(format(effect, ".2f"))
    return effect


df = pd.read_csv('formatted_0_ZG_df.csv')


# Select only rows where day > 1796
df = df[df['days'] > 1796]

# Turn the column Y_star into a list
y_star = df["Y_star"].values
y = df["Y"].values
calculate_treatment_effect(y, y_star)
