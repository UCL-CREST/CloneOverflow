y = [5 1 79; 22 2 202; 4 5 78;];
bar(y,'stacked')

P=findobj(gca,'type','patch');
C=['w','k','m','g']; % make a colors list 
for n=1:length(P) 
set(P(n),'facecolor',C(n));
end

xticks([1 2 3])
xticklabels({'QS', 'UD', 'EX'})
%xlabel('Project','FontSize',15)
ylabel('No. of file','FontSize',15)
t_legend=legend('No license', 'Compatible license', 'Incompatible license');
set(t_legend,'FontSize',15);
set(gca,'FontSize',15);
%set(gca,'XTickLabelRotation',45)
box on

h=gcf;
set(h,'PaperPositionMode','auto');         
set(h,'PaperOrientation','landscape');
set(h,'Position',[50 50 800 500]);
print('license_violation','-dpdf','-bestfit')