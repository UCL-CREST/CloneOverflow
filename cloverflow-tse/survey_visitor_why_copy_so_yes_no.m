rankings = [80 0 6; 
    74 5 7; 
    74 11 2; 
    69 11 6];

bar_handle = bar(rankings,'grouped');
% ylim([0 120])
ylabel('Amount','FontSize',16);
xticklabels({'Easy to find', 
    'Solve similar problems', 
    'Helpful context', 
    'Voting and accepted answers'});
xtickangle(30);
set(gca,'fontsize',16);
grid on

l = cell(1,3);
l{1}='Agree'; l{2}='Undecided'; l{3}='Disagree';
legend(bar_handle,l,'Location','northoutside','fontsize',12,'Orientation','horizontal');

% print('survey_snippet_source', '-bestfit', '-dpdf')