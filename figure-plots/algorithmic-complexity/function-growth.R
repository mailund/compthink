library(magrittr)
library(tibble)
library(ggplot2)
library(dplyr)
library(patchwork)

n <- 20
x <- seq(1, n, length.out = 2*n)

const <- tibble(x = x, growth = "Constant", time = 1)
log <- tibble(x = x, growth = "Logarithmic", time = log(x))
lin <- tibble(x = x, growth = "Linear", time = x)
loglin <- tibble(x = x, growth = "Log-linear", time = x * log(x))
quad <- tibble(x = x, growth = "Quadratic", time = x**2)
cub <- tibble(x = x, growth = "Cubic", time = x**3)
exp <- tibble(x = x, growth = "Exponential", time = 2**x)

fast <- rbind(const, log, lin, loglin) %>% mutate(
  growth = factor(growth, levels = c("Constant", "Logarithmic", "Linear", "Log-linear"))
)
slow <- rbind(lin, loglin, quad) %>% mutate(
  growth = factor(growth, levels = c("Linear", "Log-linear", "Quadratic"))
)
slower <- rbind(quad, cub) %>% mutate(
  growth = factor(growth, levels = c("Quadratic", "Cubic"))
)
veryslow <- rbind(quad, cub, exp) %>% mutate(
  growth = factor(growth, levels = c("Quadratic", "Cubic", "Exponential"))
)

plot_time <- function(x) {
  ggplot(x, aes(x = x, y = time, linetype = growth)) +
  scale_linetype("Growth") +
  geom_line() + theme_minimal() + xlab("n") + ylab("Time") + theme(
    text = element_text(family = "Luminari")
  )
}

(fast %>% plot_time()) + (slow %>% plot_time()) + (slower %>% plot_time()) + (veryslow %>% plot_time())
ggsave("../figures/function-growth.pdf", width = 10, height = 5)
