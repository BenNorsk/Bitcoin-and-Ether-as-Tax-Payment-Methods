
library(tidyverse)
library(ggplot2)
library(extrafont)

# read the CSV data into a data frame
df <- read_csv("p_values.csv")

# # import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)



# # register the "sourcesanspro" font
# loadfonts()

# plot the "companies" column against the "month" column, grouped by canton, no background
df$case <- factor(df$case)  # Convert the case variable to a factor

# Define the custom case names
case_names <- c("Case 0", "Case 1", "Case 2", "Case 3", "Case 4", "minimal possible p-value")

# Update the case factor levels with custom names
levels(df$case) <- case_names

# Create the plot
plot <- ggplot(df, aes(x = cutoff, y = p_value, group = case, color = case, linetype = case)) +
  geom_line() +  
  scale_color_manual(name = "Case", 
                     values = c("#268BCC", "#56B4F1", "#ff9f00", "#ff2200", "#bfdf6e", "#000000")) +
  scale_linetype_manual(name = "Case", 
                        values = c("solid", "solid", "solid", "solid", "solid", "dashed")) +
  labs(x = "Cutoff (c)", y = "P-Value (p)") +
  theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
                     legend.title = element_text(face = "bold"), legend.text = element_text(size = 12)) +
  geom_text(data = df[df$case == "minimal possible p-value" & df$cutoff == 20, ], aes(x = cutoff, y = p_value, label = case),
            vjust = -1, hjust = 1, size = 3, color = "black")  




# Save the plot as png (high quality)
ggsave("p_values.png", width = 10, height = 6, units = "in", dpi = 400)