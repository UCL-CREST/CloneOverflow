size_stats <- read.csv("~/Documents/CloneOverflow/cloneoverflow-latex/clone_size_stats.csv")
View(size_stats)
mean(size_stats["SD",1:570])
boxplot(size_stats,ylab="clone size",outline = FALSE)
boxplot(size_stats,ylab="clone size",outline = TRUE)


clone_ratio_stats <- read.csv("~/Documents/CloneOverflow/cloneoverflow-latex/clone_ratio_stats.csv")
View(clone_ratio_stats)
boxplot(clone_ratio_stats,ylab="clone ratio (%)",outline = FALSE)
boxplot(clone_ratio_stats,ylab="clone ratio (%)",outline = TRUE)

clone_frequency_stats <- read.csv("~/Documents/CloneOverflow/cloneoverflow-latex/clone_frequency_stats.csv")
View(clone_frequency_stats)
boxplot(clone_frequency_stats,ylab="clone pairs per snippet",outline = FALSE)
boxplot(clone_frequency_stats,ylab="clone pairs per snippet",outline = TRUE)