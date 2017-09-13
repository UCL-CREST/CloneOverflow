rankings = [1 7 6 32 43; 
    33 31 18 4 3; 
    47 32 6 3 1; 
    6 21 44 11 7; 
    5 8 14 26 36];

bar_handle = bar(rankings,'grouped');
% ylim([0 120])
ylabel('Amount','FontSize',16);
xticklabels({'Books', 'Official documentations', 'Stack Overflow', 'Online repos', 'Others'});
xtickangle(30);
set(gca,'fontsize',16);
grid on

l = cell(1,5);
l{1}='1st'; l{2}='2nd'; l{3}='3rd'; l{4}='4th'; l{5}='5th';
legend(bar_handle,l,'Location','Northeast','fontsize',12,'Orientation','horizontal');

% print('survey_snippet_source', '-bestfit', '-dpdf')