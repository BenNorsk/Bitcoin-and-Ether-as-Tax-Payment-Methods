# load the required libraries
library(dplyr)
library(tidyverse)

# read the data into a data frame
df <- read_csv("pretty_master_data.csv")

# Make a df, which summarises the cantons with a max number of companies < 5，
# together into one canton called "others"


# calculate the summary statistics for each variable by canton
df_summary <- df %>%
  group_by(canton) %>%
  summarize(
    # COMPANIES
    mean_companies = mean(companies, na.rm = TRUE),
    sd_companies = sd(companies, na.rm = TRUE),
    min_companies = min(companies, na.rm = TRUE),
    p25_companies = quantile(companies, probs = 0.25, na.rm = TRUE),
    p50_companies = quantile(companies, probs = 0.5, na.rm = TRUE),
    p75_companies = quantile(companies, probs = 0.75, na.rm = TRUE),
    max_companies = max(companies, na.rm = TRUE)
  )

# print the summary statistics table
print(df_summary)

# save it to a csv file
write_csv(df_summary, "summary_statistics_companies.csv")


# ---- Summarising only the control variables for the main text ----


# calculate the summary statistics for each variable by canton
df_summary <- df %>%
  group_by(canton) %>%
  summarize(
    # TAXES
    mean_taxes = mean(taxes, na.rm = TRUE),
    sd_taxes = sd(taxes, na.rm = TRUE),
    # WORKING POPULATION
    mean_working_population = mean(working_population, na.rm = TRUE),
    sd_working_population = sd(working_population, na.rm = TRUE),
    # SHARE OF FINANCE
    mean_share_finance = mean(`share of financial sector`, na.rm = TRUE),
    sd_share_finance = sd(`share of financial sector`, na.rm = TRUE),
    # SHARE OF IT
    mean_share_it = mean(`share of IT sector`, na.rm = TRUE),
    sd_share_it = sd(`share of IT sector`, na.rm = TRUE)
  )

# print the summary statistics table
print(df_summary)

# save it to a csv file
write_csv(df_summary, "summary_statistics_control_variables.csv")





# ----- Summarising all for the appendix! -----
df <- read_csv("aggregated_industry_data.csv")

# calculate the summary statistics for each variable by canton
df_summary <- df %>%
  group_by(canton) %>%
  summarize(
    # COMPANIES
    mean_companies = mean(companies, na.rm = TRUE),
    sd_companies = sd(companies, na.rm = TRUE),
    min_companies = min(companies, na.rm = TRUE),
    p25_companies = quantile(companies, probs = 0.25, na.rm = TRUE),
    p50_companies = quantile(companies, probs = 0.5, na.rm = TRUE),
    p75_companies = quantile(companies, probs = 0.75, na.rm = TRUE),
    max_companies = max(companies, na.rm = TRUE),
    # TAXES
    mean_taxes = mean(taxes, na.rm = TRUE),
    sd_taxes = sd(taxes, na.rm = TRUE),
    # WORKING POPULATION
    mean_working_population = mean(working_population, na.rm = TRUE),
    sd_working_population = sd(working_population, na.rm = TRUE),
    # SHARE OF FINANCE
    mean_share_finance = mean(`share of financial sector`, na.rm = TRUE),
    sd_share_finance = sd(`share of financial sector`, na.rm = TRUE),
    # SHARE OF IT
    mean_share_it = mean(`share of IT sector`, na.rm = TRUE),
    sd_share_it = sd(`share of IT sector`, na.rm = TRUE),
    # TREATMENT
    mean_treatment = mean(treatment, na.rm = TRUE)
  )

# print the summary statistics table
print(df_summary)

# save it to a csv file
write_csv(df_summary, "summary_statistics_for_appendix.csv")
