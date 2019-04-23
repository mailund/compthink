library(ggplot2)
library(tibble)

d <- tribble(
  ~repr,             ~number,
 "1.1[2] %*% 2^-11[2]", 2**-3 + 2**-4,
 "1.0[2] %*% 2^-11[2]", 2**-3,
 "1.1[2] %*% 2^-10[2]", 2**-2 + 2**-3,
 "1.0[2] %*% 2^-10[2]", 2**-2,
 "1.1[2] %*% 2^-01[2]", 2**-1 + 2**-2,
 "1.0[2] %*% 2^-01[2]", 2**-1,
 "1.0[2] %*% 2^00[2]",   1,
 "1.1[2] %*% 2^00[2]",   1 + 2**-1,
 "0.0[2] %*% 2^00[2]",   0,
 "1.1[2] %*% 2^01[2]",   2 + 1,
 "1.0[2] %*% 2^01[2]",   2,
 "1.1[2] %*% 2^10[2]",   2**2 + 2**1,
 "1.0[2] %*% 2^10[2]",   2**2,
 "1.1[2] %*% 2^11[2]",   2**3 + 2**2,
 "1.0[2] %*% 2^11[2]",   2**3,

 "-1.1[2] %*% 2^-11[2]", -(2**-3 + 2**-4),
 "-1.0[2] %*% 2^-11[2]", -(2**-3),
 "-1.1[2] %*% 2^-10[2]", -(2**-2 + 2**-3),
 "-1.0[2] %*% 2^-10[2]", -(2**-2),
 "-1.1[2] %*% 2^-01[2]", -(2**-1 + 2**-2),
 "-1.0[2] %*% 2^-01[2]", -(2**-1),
 "-1.0[2] %*% 2^00[2]",   -1,
 "-1.1[2] %*% 2^00[2]",   -(1 + 2**-1),
 "-1.1[2] %*% 2^01[2]",  -(2 + 1),
 "-1.0[2] %*% 2^01[2]",  -2,
 "-1.1[2] %*% 2^10[2]",  -(2**2 + 2**1),
 "-1.0[2] %*% 2^10[2]",  -2**2,
 "-1.1[2] %*% 2^11[2]",  -(2**3 + 2**2),
 "-1.0[2] %*% 2^11[2]",  -2**3
)

d <- d[order(d$number),]
d$i <- seq(min(d$number), max(d$number), length.out = nrow(d))

ggplot() +
  geom_point(
    data = d,
    mapping = aes(y = 0, x = number),
    size = 0.1
  ) +
  geom_text(
    data = d,
    mapping = aes(y = 0.01, x = i, label = repr),
    parse = TRUE, hjust = 0, vjust = 0.5, angle = 55, size = 3
  ) +
  geom_segment(
    data = d,
    mapping = aes(y = 0, yend = 0.01, x = number, xend = i),
    size = 0.1
  ) +
  scale_x_continuous(
    breaks = c(-12, -8, -6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 6, 8, 12)
  ) +
  coord_cartesian(ylim = c(-0.0, 0.015)) +
  theme_classic(base_size = 14) +
  labs(x = NULL, y = NULL) +
  theme(
    axis.line.x = element_line(size = 0.2),
    axis.ticks.x = element_line(size = 0.2),
    axis.line.y = element_blank(),
    axis.ticks.y = element_blank(),
    axis.text.y = element_blank()
  )

ggsave("../figures/number-line.pdf", width = 10, height = 6)
