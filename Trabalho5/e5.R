m = c(0,0.189,0.110,0.113,0.215,
      0.189,0,0.179,0.192,0.211,
      0.11,0.179,0,0.09405,0.205,
      0.113,0.192,0.0940,0,0.214,
      0.215,0.211,0.205,0.214,0)
dim(m) = c(5,5)
colnames(m) = c('Gorila','Orangotango','Humano','Chimpanzé','Gibão')
rownames(m) = colnames(m)
d = as.dist(m)

png(file="myplot.png")

library(ape)
tr = nj(d)
plot(tr,cex=2,tip.color=rainbow(6))
axisPhylo()
dev.off()

