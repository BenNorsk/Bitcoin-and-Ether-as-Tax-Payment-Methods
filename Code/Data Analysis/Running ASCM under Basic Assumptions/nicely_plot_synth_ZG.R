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

# Plot the companies over time (days) for canton ZG and synth_ZG
ggplot(df, aes(x = days, y = companies, color = canton)) +
  geom_line() +
  labs(x = "Days", y = "Companies", title = "Companies over time for canton ZG and synth_ZG") +
  theme_bw()

# Save the plot
ggsave("nicely_plot_synth_ZG.png", width = 10, height = 5)