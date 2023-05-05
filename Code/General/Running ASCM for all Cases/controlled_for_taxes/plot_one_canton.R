library(tidyverse)
library(ggplot2)
library(glue)

# Read the command line arguments
args = commandArgs(trailingOnly = TRUE)
my_canton = as.character(args[1])
file_path = as.character(args[2])
cutoff = as.character(args[3])
df = read_csv(file_path)

# Only select where canton = canton or canton = synth_canton

df = df %>% filter(canton == my_canton | canton == glue("synth_{my_canton}"))

# drop all columns except canton, companies, month and days
df = df %>% select(canton, companies, month, days)

# Plot the companies over time (days) for canton ZG and synth_ZG
ggplot(df, aes(x = days, y = companies, color = canton)) +
  geom_line() +
  labs(x = "Days", y = "Companies", title = glue("Companies over time for {my_canton} and synthetic {my_canton}")) +
  theme_bw()

# Save the plot
ggsave(glue("controlled_for_taxes/{my_canton}/{cutoff}_total_companies_{my_canton}.png"), width = 10, height = 5)