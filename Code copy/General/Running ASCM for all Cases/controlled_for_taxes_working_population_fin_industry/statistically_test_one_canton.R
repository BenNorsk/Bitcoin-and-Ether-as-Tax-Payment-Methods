library(tidyverse)
library(ggplot2)
library(glue)

args = commandArgs(trailingOnly = TRUE)
my_canton = as.character(args[1])
my_synth_canton = glue("synth_{my_canton}")
file_path = as.character(args[2])
cutoff = as.character(args[3])
df = read_csv(file_path)

# Only select where canton = ZG or canton = ZG_synth
df = df %>% filter(canton == my_canton | canton == my_synth_canton)

# drop all columns except canton, companies, month and days
df = df %>% select(canton, companies, month, days)

# Insert all companies where canton = ZG into a new column called companies_real
df = df %>% mutate(companies_real = ifelse(canton == my_canton, companies, NA))
df = df %>% mutate(companies_synth = ifelse(canton == my_synth_canton, companies, NA))

# Drop the column canton
df = df %>% select(-canton)
df = df %>% select(-companies)

# Move all values of companies_synth one row up
df = df %>% mutate(companies_real = lag(companies_real, 1))
df = df %>% mutate(month = lag(month, 1))
print(df)

# Delete all values where month = NA
df = df %>% filter(!is.na(month))
print(df)

# Create a new column called companies_diff = companies_real - companies_synth
df = mutate(df, companies_diff = companies_real - companies_synth)
print(df)

# Plot the differences with a dotted line at days = 1796

ggplot(df, aes(x = days, y = companies_diff)) + geom_line() + geom_vline(xintercept = 1796, linetype = "dashed")

# Save the difference plot
ggsave(glue("controlled_for_taxes/{my_canton}/{cutoff}_companies_diff_{my_canton}.png"), width = 10, height = 5)

pre_treatment = df %>% filter(days < 1827)
treatment = df %>% filter(days >= 1827)

# printe the avg squared difference before treatment
mspe_before = mean(pre_treatment$companies_diff^2)

# printe the avg squared difference during treatment
mspe_after = mean(treatment$companies_diff^2)

# print the ratio of the two
mspe_ratio = mspe_after / mspe_before

# Make a dataframe with this mspes, with the variable names as column names
mspe_df = data.frame(mspe_before, mspe_after, mspe_ratio)

# Turn it into a tibble
mspe_df = as_tibble(mspe_df)

# Save it as a csv
write_csv(mspe_df, glue("controlled_for_taxes/{my_canton}/{cutoff}_rspe_{my_canton}.csv"))