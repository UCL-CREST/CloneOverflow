rankings = [48 32 0 3 3; 
    30 44 5 6 1; 
    38 36 11 2 0; 
    29 40 11 5 1];

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

l = cell(1,5);
l{1}='Strongly agree'; l{2}='Agree'; l{3}='Undecided'; l{4}='Disagree'; l{5}='Strongly disagree';
legend(bar_handle,l,'Location','northoutside','fontsize',12,'Orientation','horizontal');

% print('survey_snippet_source', '-bestfit', '-dpdf')