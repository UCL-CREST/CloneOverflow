%fresh =     (1, 4, 0, 7, 5, 11, 0, 0, 0, 1, 0, 0, 0, 2, 3, 0, 3, 0)
%outdated =  (0, 0, 2, 5, 9, 4,  2, 4, 4, 0, 2, 2, 3, 1, 9, 1, 0, 7)
%deleted =   (0, 0, 0, 0, 0, 1,  0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0)
%other =     (0, 0, 0, 0, 0, 0,  0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
y = [1 0 0 0; 4 0 0 0; 0 2 0 0; 7 5 0 0; 5 9 0 0; 11 4 1 0; 0 2 0 0; 0 4 0 0; 0 4 0 1; 1 0 0 0; 0 2 0 0; 0 2 0 0; 0 3 0 0; 2 1 0 0; 3 9 2 0; 0 1 0 0; 3 0 0 0; 0 7 0 0];

bar_handle = bar(y,'stacked');

set(bar_handle(1),'FaceColor',[0 0.6 0]);
set(bar_handle(2),'FaceColor','yellow');
set(bar_handle(3),'FaceColor','red');
set(bar_handle(4),'FaceColor','blue');

ylabel('Amount','FontSize',18);
xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]);
xticklabels({'ant', 'log4j', 'aspectj', 'eclipse', 'hadoop', 'hibernate','jasperreports', 'jfreechart', 'jgraph', 'jgrapht','jstock','jung','junit','poi','spring','struts','tomcat','weka'});
xtickangle(45);

set(gca,'fontsize',18);
grid on
l = cell(1,4);
l{1}='Fresh'; l{2}='Outdated'; l{3}='Deleted'; l{4}='Not found';
legend(bar_handle,l,'fontsize',18);

%print('outdated','-dpdf','-bestfit')