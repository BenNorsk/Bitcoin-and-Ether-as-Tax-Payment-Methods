library(magrittr)
library(tidyverse)
library(dplyr)
library(augsynth)

# Set the language option to English
Sys.setenv(LANGUAGE = "en")

data = read_csv("aggregated_industry_data.csv")
print(data)

data %>% select(days, canton, companies, treatment, working_population, taxes) 

asyn <- augsynth((companies ~ treatment | taxes), canton, days, data,
                progfunc = "Ridge", scm = T)


summary = summary(asyn)

# What data type is the summary?
print(asyn$weights)

# Save the weights in a tibble, where tthe first column is named canton, and the second is called weights.
weights = as_tibble(asyn$weights, rownames = "canton")
weights = rename(weights, weights = V1)
print(weights)

# Save the weights as CSV
# write_csv(weights, "weights.csv")


# Plot the differences
plot(asyn, type = "diff")
