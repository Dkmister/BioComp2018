leuk <- read.csv("https://web.stanford.edu/~hastie/CASI_files/DATA/leukemia_big.csv")

leuk <- na.omit(leuk)

leuk <- scale(leuk)

fit <- kmeans(leuk,2) # 2 cluster solution

library(cluster)
clusplot(leuk, fit$cluster, color=TRUE, shade=TRUE,
   labels=2, lines=0)

