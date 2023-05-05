library(tidyverse)
library(extrafont)

df_long <- read_csv("transformed_data.csv")
print(df_long)

# Create the plot
p <- ggplot(df_long, aes(x = month, y = diff, color = unit_category)) +
  geom_line(aes(linetype = ifelse(unit_category == "ZG", "dashed", "solid"),
            color = ifelse(unit_category == "ZG", "#268BCC", "#ff9f00"))) +
  geom_hline(yintercept = 0, linetype = "solid", color = "black") +
  labs(x = "Year (on a monthly basis)", y = "Outcome Differences (Y - Y*)") +
  scale_color_manual(name = "Cantons", values = c("#268BCC", "#ff9f00"), labels = c("ZG", "other cantons")) +
  theme_bw() +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.title = element_text(face = "bold"),
        text = element_text(family = "Source Sans Pro"),
        legend.title = element_blank(),
        legend.text = element_text(size = 12)) +
  guides(linetype = FALSE) +
  annotate("text", x = as.Date("2021-01-31"), y = max(df_long$diff), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000") +
  geom_vline(xintercept = as.Date("2021-01-31"), linetype = "dotted", color = "black")



print(p)


# Print the plot
print(p)

# Save the plot
ggsave("all_outcome_differences.png", width = 10, height = 6, units = "in", dpi = 400)
