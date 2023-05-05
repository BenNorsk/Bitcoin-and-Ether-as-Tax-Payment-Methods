library(tidyverse)
library(ggplot2)
library(extrafont)

# Read in all_example_mspes.csv
df <- read_csv("all_example_mspes.csv")

# Only keep the columns t, MSPE_A_ratio, MSPE_B_ratio, MSPE_C_ratio, MSPE_D_ratio
df <- df %>% select(t, MSPE_A_ratio, MSPE_B_ratio, MSPE_C_ratio, MSPE_D_ratio)
# import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)


# Load necessary packages
library(ggplot2)
library(tidyr)

# Reshape the data for ggplot
df_bar <- df %>% 
  select(MSPE_A_ratio, MSPE_B_ratio, MSPE_C_ratio, MSPE_D_ratio) %>% 
  summarise_all(mean, na.rm = TRUE) %>% 
  gather(key = "Unit", value = "MSPE_X_ratio") %>%
  mutate(Unit = gsub("MSPE_", "", Unit),
         Unit = gsub("_ratio", "", Unit)) %>%
  arrange(MSPE_X_ratio)


# Adjust the Unit column to show only the unit labels
df_bar$Unit <- gsub("MSPE_", "", df_bar$Unit)
df_bar$Unit <- gsub("_ratio", "", df_bar$Unit)

# Create the bar chart
p_bar <- ggplot(df_bar, aes(x = Unit, y = MSPE_X_ratio, fill = Unit)) +
  geom_bar(stat = "identity", width = 0.2) +  # Change the width value to adjust the column width
  labs(x = "", y = "MSPE Ratio", fill = "Unit") +
  scale_fill_manual(values = c("A" = "#ff2200", "B" = "#ff9f00", "C" = "#ff9f00", "D" = "#ff9f00")) +
  theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
                     legend.title = element_text(face = "bold"), legend.text = element_text(size = 12))

# Print the bar chart
print(p_bar)

# Save the bar chart
ggsave("bar_chart.png", width = 10, height = 6, units = "in", dpi = 400)


