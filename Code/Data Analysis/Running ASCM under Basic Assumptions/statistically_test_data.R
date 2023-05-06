library(tidyverse)
library(ggplot2)

df = read_csv("synth_ZG.csv")
print(df)

# Only select where canton = ZG or canton = ZG_synth
df = df %>% filter(canton == "ZG" | canton == "synth_ZG")

print(df)

# drop all columns except canton, companies, month and days
df = df %>% select(canton, companies, month, days)
print(df)

# Insert all companies where canton = ZG into a new column called companies_ZG
df = df %>% mutate(companies_ZG = ifelse(canton == "ZG", companies, NA))
df = df %>% mutate(companies_synth = ifelse(canton == "synth_ZG", companies, NA))

# Drop the column canton
df = df %>% select(-canton)
df = df %>% select(-companies)
print(df)

# Move all values of companies_synth one row up
df = df %>% mutate(companies_ZG = lag(companies_ZG, 1))
df = df %>% mutate(month = lag(month, 1))
print(df)

# Delete all values where month = NA
df = df %>% filter(!is.na(month))
print(df)

# Create a new column called companies_diff = companies_ZG - companies_synth
df = mutate(df, companies_diff = companies_ZG - companies_synth)
print(df)

# Plot the differences
ggplot(df, aes(x = days, y = companies_diff)) + geom_line()

# Save the difference plot
ggsave("companies_diff_ZG.png", width = 10, height = 5)

pre_treatment = df %>% filter(days < 1827)
treatment = df %>% filter(days >= 1827)

# printe the avg squared difference before treatment
print(mean(pre_treatment$companies_diff^2))

# printe the avg squared difference during treatment
print(mean(treatment$companies_diff^2))

# print the ratio of the two
print(mean(pre_treatment$companies_diff^2) / mean(treatment$companies_diff^2))