library(tidyverse)
library(ggplot2)
library(extrafont)

# read the CSV data into a data frame
df <- read_csv("treatment_df.csv")
print(df)

# define the order of the cantons


# Rename the cases
case_names <- c("Case 0", "Case 1", "Case 2", "Case 3", "Case 4")
case_order <- c("Case 0", "Case 1", "Case 2", "Case 3", "Case 4")

# Now rename the cases
df$case <- case_names[df$case + 1]

# convert the "canton" column to a factor with the specified order
df$case <- factor(df$case, levels = case_order)

# # import the "sourcesanspro" font
font_path <- "Source_Sans_Pro"

# Import the fonts to the system font library
font_import(paths = font_path)



# # register the "sourcesanspro" font
# loadfonts()

# plot the "companies" column against the "month" column, grouped by canton, no background
ggplot(df, aes(x = cutoff, y = treatment_effect, group = case, color = case)) +
  geom_line() + 
  scale_color_manual(values = c("#268BCC", "#56B4F1", "#ff9f00", "#ff2200", "#bfdf6e")) +
  labs(x = "Cutoff (c)", y = "Treatment Effect (E)", color = "Case") +
  theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        axis.title = element_text(face = "bold"), text = element_text(family = "Source Sans Pro"),
         legend.title = element_text(face = "bold"), legend.text = element_text(size = 12)) + 
  geom_hline(yintercept = 0, linetype = "solid")


# Save the plot as png (high quality)
ggsave("treatment_effect.png", width = 10, height = 6, units = "in", dpi = 400)