y = [63 18 14 10 3 1];
bar(y)

%xticks([1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19])
xticklabels({'JDK', 'Web', 'OSS', 'Official docs', 'Book', 'Company'})
%xlabel('Project','FontSize',15)
ylabel('Clone pairs','FontSize',15)
%t_legend=legend('Fresh', 'Outdated', 'Dead');
%set(t_legend,'FontSize',15);
set(gca,'FontSize',15);
set(gca,'XTickLabelRotation',45)
box on

h=gcf;
set(h,'PaperPositionMode','auto');         
set(h,'PaperOrientation','landscape');
set(h,'Position',[50 50 500 300]);
print('ex_sources','-dpdf','-bestfit')