library(tidyverse)
library(ggplot2)
library(extrafont)

# read the CSV data into a data frame
df <- read.csv("pretty_master_data.csv")
print(df)

# convert the "month" column to a date format
df$month <- as.Date(df$month)

# define the order of the cantons
canton_order <- c("ZG", "ZH", "GE", "TI", "VD", "avg. other canton")

# convert the "canton" column to a factor with the specified order
df$canton <- factor(df$canton, levels = canton_order)

# # import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)



# # register the "sourcesanspro" font
# loadfonts()

# plot the "companies" column against the "month" column, grouped by canton, no background
ggplot(df, aes(x = month, y = companies, group = canton, color = canton)) +
  geom_line() + 
  scale_color_manual(values = c("#268BCC", "#56B4F1", "#ff9f00", "#ff2200",  "#bfdf6e", "#b1b1b1")) +
  labs(x = "Year (on a monthly basis)", y = "Outcome (Y)", color = "Canton") +
  theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
         legend.title = element_text(face = "bold"), legend.text = element_text(size = 12)) + 
  geom_vline(xintercept = as.numeric(as.Date("2021-01-31")), linetype = "dotted") +
annotate("text", x = as.Date("2021-01-31"), y = max(df$companies), label = "treatment", vjust = -1, hjust = -0.1, color = "#000000")


# Save the plot as png (high quality)
#ggsave("companies.png", width = 10, height = 6, units = "in", dpi = 400)