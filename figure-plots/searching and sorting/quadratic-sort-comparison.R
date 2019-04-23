library(dplyr)
library(ggplot2)
library(tidyr)
library(magrittr)
library(extrafont)

df <- read.table("quadratic-sort-comparison.txt", header = FALSE)
names(df) <- c("data", "n", "alg", "comparisons", "swaps")

df %<>% gather(key = "operation", value = "count", comparisons, swaps) %>%
  mutate(data = factor(data, levels = c("sorted", "reversed", "almost_sorted", "permuted")),
         alg = factor(alg, levels = c("selection", "insertion", "bubble", "cocktail")))

capitalize <- function(string) {
  substr(string, 1, 1) <- toupper(substr(string, 1, 1))
  string
}
data_map <- c(almost_sorted = "Almost Sorted", permuted = "Random Permutation", sorted = "Sorted", reversed = "Reverse-sorted")

df %>% filter(operation == "comparisons") %>%
  ggplot(aes(x = n, y = count, colour = alg)) +
  facet_grid(data ~ alg, #scales = "free_y",
             labeller = labeller(data = data_map, operation = capitalize, alg = capitalize)) +
  geom_jitter(width = 1, height = 0) +
  stat_smooth(method = "lm", formula = y ~ x + I(x^2), size = 1, se = FALSE) +
  scale_color_grey("Algorithm") +
  theme_minimal() + xlab("Input size") + ylab("Counts") + theme(
    legend.position = "none",text = element_text(family = "Luminari")
  )
ggsave("quadratic-sort-comparison-comparisons.pdf", width = 10, height = 10)

df %>% filter(operation == "swaps") %>%
  ggplot(aes(x = n, y = count, colour = alg)) +
  facet_grid(data ~ alg, #scales = "free_y",
             labeller = labeller(data = data_map, operation = capitalize, alg = capitalize)) +
  geom_jitter(width = 1, height = 0) +
  stat_smooth(method = "lm", formula = y ~ x + I(x^2), size = 1, se = FALSE) +
  scale_color_grey("Algorithm") +
  theme_minimal() + xlab("Input size") + ylab("Counts") + theme(
    legend.position = "none",
    #text = element_text(family = "Bradley Hand Bold")
    text = element_text(family = "Luminari")
  )
ggsave("quadratic-sort-comparison-swaps.pdf", width = 6, height = 6)
