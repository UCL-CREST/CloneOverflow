answerers = [28 42 50 30 32 13; 
    4 10 21 16 28 121; 
    9 14 31 33 46 67; 
    106 71 17 2 3 1; 
    66 56 35 15 17 11; 
    3 7 38 14 37 101];

bar_handle = bar(answerers,'grouped');
% ylim([0 120])
ylabel('Amount','FontSize',16);
xticklabels({'Personal projects', 'Company projects', 'Open source projects', 'Write from scratch', 'Modify from questions', 'Others'});
xtickangle(30);
set(gca,'fontsize',16);
grid on

l = cell(1,6);
l{1}='Very frequently'; l{2}='Frequently'; l{3}='Occasionally'; l{4}='Rarely'; l{5}='Very rarely'; l{6}='Never';
legend(bar_handle,l,'Location','Northwest','fontsize',12);

print('survey_snippet_source', '-bestfit', '-dpdf')