windowsFonts(myFont = windowsFont("Arial"))
library(readxl)
library(tidyverse)
library(pheatmap)
library(ggalluvial) 

silhouette <- read_excel("C:/Users/79403/Desktop/药物筛选/cluster_selection.xlsx", 
                                sheet = "silhouette") %>%
  column_to_rownames(var = "...1" )
calinski <- read_excel("C:/Users/79403/Desktop/药物筛选/cluster_selection.xlsx", 
                                sheet = "calinski") %>%
  column_to_rownames(var = "...1" )

davies <- read_excel("C:/Users/79403/Desktop/药物筛选/cluster_selection.xlsx", 
                                sheet = "davies") %>%
  column_to_rownames(var = "...1" )

pdf("silhouette.pdf", width=15, height=10,family =  "sans")
ht(silhouette)
dev.off()

pdf("calinski.pdf",width=15, height=10,family =  "sans")
ht(calinski)
dev.off()

pdf("davies.pdf", width=15, height=10,family =  "sans")
ht(davies)
dev.off()

#sankey
cluster_name <- read.csv("C:/Users/79403/Desktop/药物筛选/cluster_name.csv")
ggplot(data = cluster_name,
       aes(axis1 = Product.Name, axis2 = CLogP, y =  cluster,fill = cluster)) +
  geom_alluvium(aes(fill = cluster)) +
  geom_stratum(aes(fill = cluster),alpha=0,size=0.7)+
  geom_text(stat = "stratum",
            aes(label = after_stat(stratum))) +
  scale_x_discrete(limits = c("group", "variable"),
                   expand = c(0.15, 0.05)) +
  theme_void()


ht <- function(x){pheatmap(x, 
                           # annotation_row=dfGene, # （可选）指定行分组文件
                           # annotation_col=dfSample, # （可选）指定列分组文件
                           show_colnames = TRUE, # 是否显示列名
                           show_rownames=TRUE,  # 是否显示行名
                           fontsize=10, # 字体大小 
                           color = colorRampPalette(c("#386CB0","#F7FCF0","#E64B35CC"))(50),# 指定热图的颜色
                           #color = colorRampPalette(c("#04a3ff","#ffffff","#ff349c"))(50),
                           annotation_legend = TRUE, # 是否显示图例
                           border_color= NA,# 边框颜色 NA表示没有
                           scale = "row", 
                           #annotation_colors=anncolor,
                           #annotation=Type,
                           #scale = "column",  # 指定归一化的方式。"row"按行归一化，"column"按列归一化，"none"不处理
                           cluster_rows = T, # 是否对行聚类
                           cluster_cols = F, # 是否对列聚类
                           #display_numbers = TRUE,
                           angle_col = 45,
                           fontfamily=  "sans",
                           fontsize_col = 15,
                           fontsize_row = 15
                           
)} 
