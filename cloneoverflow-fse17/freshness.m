y = [13	6 1;
3	15	2;
10	5	0;
5	7	0;
2	5	0;
0	6	0;
5	0	0;
0	4	0;
0	3	0;
1	2	0;
2	1	0;
0	3	0;
3	0	0;
0	2	0;
0	1	1;
1	0	0;
1	0	0;
1	0	0;
1	0	0];
bar(y,'stacked')

P=findobj(gca,'type','patch');
C=['w','k','m','g']; % make a colors list 
for n=1:length(P) 
set(P(n),'facecolor',C(n));
end

xticks([1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19])
xticklabels({'hibernate', 'spring', 'eclipse-SDK', 'hadoop', 'tomcat', ...
    'junit', 'log4j', 'jfreechart', 'jgraph', 'jung2', 'poi', 'struts2', ... 
    'weka', 'aspectj', 'jasperreports', 'antlr', 'ant', 'itext', 'jgrapht'})
%xlabel('Project','FontSize',15)
ylabel('Clone pair','FontSize',15)
t_legend=legend('Fresh', 'Outdated', 'Dead');
set(t_legend,'FontSize',15);
set(gca,'FontSize',15);
set(gca,'XTickLabelRotation',45)
box on

h=gcf;
set(h,'PaperPositionMode','auto');         
set(h,'PaperOrientation','landscape');
set(h,'Position',[50 50 1200 500]);
print('freshness','-dpdf','-bestfit')