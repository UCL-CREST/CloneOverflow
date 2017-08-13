group1 = [14 20 19 10 14 7; 3 5 9 0 14 53; 
    5 6 16 13 16 28; 36 38 7 1 1 1; 
    24 28 16 5 4 7; 1 2 14 6 17 44];

group2 = [13 20 30 19 18 11; 1 5 12 14 13 66; 
    4 8 15 17 28 39; 66 32 10 1 2 0; 
    42 26 18 10 11 4; 2 4 23 8 20 54];

bar_handle = bar(group1,'grouped');
ylim([0 70])
ylabel('Amount','FontSize',16);
xticklabels({'Personal projects', 'Company projects', 'Open source projects', 'Write from scratch', 'Modify from questions', 'Others'});
xtickangle(30);
set(gca,'fontsize',16);
grid on

l = cell(1,6);
l{1}='Very frequently'; l{2}='Frequently'; l{3}='Occasionally'; l{4}='Rarely'; l{5}='Very rarely'; l{6}='Never';
legend(bar_handle,l,'Location','Northwest','fontsize',12);

% print('survey_snippet_source','-dpdf','-bestfit')