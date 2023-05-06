library(tidyverse)
library(ggplot2)
library(extrafont)

# Read in all_example_mspes.csv
df <- read_csv("all_example_mspes.csv")

# Only keep the columns t, diff_A, diff_B, diff_C, diff_D
df <- df %>% select(t, diff_A, diff_B, diff_C, diff_D)

# import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)

# Reshape the data for ggplot
df_long <- df %>% gather(key = "diff", value = "value", -t)

df_long$unit_category <- ifelse(df_long$diff == "diff_A", "unit A", "other units")
print(df_long)
# Create the plot
p <- ggplot(df_long, aes(x = t, y = value, color = unit_category)) +
  geom_line(aes(linetype = diff)) +
  geom_vline(xintercept = 20, linetype = "dotted", color = "black") +
  geom_hline(yintercept = 0, linetype = "solid", color = "black") +
  labs(x = "Time (t)", y = "Outcome Differences (Y - Y*)") +
  scale_color_manual(name = NULL, values = c("unit A" = "#268BCC", "other units" = "#ff9f00")) +
  scale_linetype_manual(values = c("diff_A" = "solid", "diff_B" = "dashed", "diff_C" = "dashed", "diff_D" = "dashed")) +
  theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
                     legend.title = element_blank(), legend.text = element_text(size = 12)) +
  annotate("text", x = 20, y = max(df_long$value), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000") +
  guides(linetype = FALSE)



# Print the plot
print(p)
# Save the plot
ggsave("difference_graph.png", width = 10, height = 6, units = "in", dpi = 400)