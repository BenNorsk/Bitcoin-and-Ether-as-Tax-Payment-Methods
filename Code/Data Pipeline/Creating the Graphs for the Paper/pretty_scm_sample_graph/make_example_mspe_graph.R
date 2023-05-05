library(tidyverse)
library(ggplot2)
library(extrafont)

# Read in example_mspes.csv
df <- read_csv("example_mspes.csv")
df2 <- read_csv("example_scm.csv")

# Rename the columns in df2 from "Y_star" to "Y_star_A"
df2 <- df2 %>% rename(Y_star_A = Y_star, Y_A = Y)

# Join df2 on df1 on t, with the column Y_star_A from df2
df <- df %>% left_join(df2, by = "t")


# Define the column MSPE_A_pre
df <- df %>% mutate(MSPE_A_pre = mean((Y[t <= 20] - Y_star_A[t <= 20])^2))
df <- df %>% mutate(MSPE_A_post = mean((Y[t > 20] - Y_star_A[t > 20])^2))
df <- df %>% mutate(MSPE_A_ratio = MSPE_A_post / MSPE_A_pre)

# Define the difference of Y_A - Y_star_A
df <- df %>% mutate(diff_A = Y_A - Y_star_A)
df <- df %>% mutate(diff_B = Y - Y_star_B)
df <- df %>% mutate(diff_C = Y - Y_star_C)
df <- df %>% mutate(diff_D = Y - Y_star_D)

# Rename the column Y.
print(df)

# Save as a .csv
# write.csv(df, "all_example_mspes.csv")
