library(tidyverse)
library(ggprism)
require(ggplot2)
library(showtext)
font_families()
cluster_name <- read.csv("C:/Users/79403/Desktop/药物筛选/plot/cluster_name.csv")
nu_cluster$cluster <- nu_cluster$cluster+1
cluster <- table(nu_cluster$cluster) %>%
           as.data.frame()  
cluster$Var1 <- as.numeric(cluster$Var1)
cluster$Var1 <- as.character(cluster$Var1)
cluster <- cluster %>%
           arrange(Freq) 
cluster$Var1 <- fct_inorder(cluster$Var1)

pdf("culster.pdf", width=8, height=4,family =  "sans")
ggplot(data = cluster,aes(x = Var1, y = Freq, fill=Freq)) +
  geom_col()+
  coord_flip() + 
  scale_fill_gradient(low ="#386CB0" ,high = "#E64B35CC")+
  theme_classic()+
  theme_prism(base_family = "sans")+
  labs(y= "Number", x="Cluster", fill="Number")+
  guides(fill = guide_legend(title = "Your Legend Title")) 
  
dev.off()
