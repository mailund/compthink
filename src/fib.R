library(tidyverse)
tbl <- read_table2("fib-memo.txt")

ggplot(tbl) +
    geom_line(aes(x = n, y = count)) + 
    theme_minimal()

ggsave("fib-memo.pdf")