library(tidyverse)
library(ggplot2)
library(extrafont)


# Load df
df_hist = read_csv("mspes_no_cv.csv")
print(head(df_hist))

# Only select the data for cutoff = 0
df_hist = df_hist %>% filter(cutoff == 0)

# Where the MSPE_ratio is over 200, set it to 200.
df_hist = df_hist %>% mutate(MSPE_ratio = ifelse(MSPE_ratio > 200, 200, MSPE_ratio))

# Round all numbers in the df to 2 decimal places
df_hist = df_hist %>% mutate(MSPE_ratio = round(MSPE_ratio, 2))

print(df_hist)

font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)



library(ggplot2)

# Create example data
# Create the plot
# Create the plot
# Create example data
# Create the plot
# Set the upper limit
upper_limit <- 1e18

# Create the plot
ggplot(df_hist, aes(x = MSPE_ratio,
fill = ifelse(canton == "ZG", "ZG", "other cantons"))) +
geom_histogram(binwidth = 2.5, position = "stack", alpha = 0.5) +
scale_fill_manual(values = c("ZG" = "#268BCC", "other cantons" = "#ff9f00"),
labels = c("ZG", "other cantons")) +
labs(x = "MSPE Ratios (R)", y = "Count") +
scale_x_continuous(breaks = seq(0, 200, by = 50) , labels = c("0", "50", "100", "150", "> 200")) +
theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
legend.title = element_blank(), legend.text = element_text(size = 12))





# Save the bar chart
ggsave("R_histogram.png", width = 10, height = 6, units = "in", dpi = 400)