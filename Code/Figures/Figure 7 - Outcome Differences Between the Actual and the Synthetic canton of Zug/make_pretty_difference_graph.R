# Load necessary packages
library(ggplot2)
library(tidyr)
library(tidyverse)
library(dplyr)
library(extrafont)

# Read the data
data <- read_csv("formatted_0_ZG_df.csv")

# Format the date
data$month <- as.Date(data$month, format = "%Y-%m-%d")

# Calculate the difference
data <- data %>%
  mutate(diff = Y - Y_star)

# Create the ggplot
# Create the ggplot
# Create the ggplot
# Create the ggplot
p <- ggplot(data, aes(x = month, y = diff)) +
  geom_line(color = "#268BCC", linetype = "solid") +
  geom_vline(xintercept = as.Date("2021-01-31"), linetype = "dotted", color = "black") +
  geom_hline(yintercept = 0, linetype = "solid", color = "black") +
  geom_ribbon(data = data[data$month > as.Date("2020-12-31"), ],
              aes(ymin = 0, ymax = diff), alpha = 0.3, fill = "darkgrey") +
  labs(x = "Year (on a monthly basis)", y = "Outcome Difference (Y - Y*)") +
  theme_bw() +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.title = element_text(face = "bold"),
        text = element_text(family = "Source Sans Pro"),
        legend.title = element_blank(),
        legend.text = element_text(size = 12)) +
  annotate("text", x = as.Date("2021-01-31"), y = max(data$diff), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000")

print(p)

print(p)

print(p)


print(p)

# Save the plot
# ggsave("difference_graph.png", p, width = 10, height = 6, units = "in", dpi = 400)
