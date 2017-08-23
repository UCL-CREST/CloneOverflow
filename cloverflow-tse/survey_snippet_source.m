group1 = [13 20 30 20 18; 
    1 5 12 15 13; 
    4 8 15 18 28; 
    67 32 10 1 2; 
    42 26 19 10 11; 
    2 4 23 8 20];

group2 = [14 20 19 10 14; 
    3 5 9 0 14; 
    5 6 16 13 16; 
    36 38 7 1 1; 
    24 28 16 5 4; 
    1 2 14 6 17];

bar_handle = bar(group2,'stacked');
ylim([0 120])
ylabel('Amount','FontSize',16);
xticklabels({'Personal projects', 'Company projects', 'Open source projects', 'Write from scratch', 'Modify from questions', 'Others'});
xtickangle(30);
set(gca,'fontsize',16);
grid on

l = cell(1,6);
l{1}='Very frequently'; l{2}='Frequently'; l{3}='Occasionally'; l{4}='Rarely'; l{5}='Very rarely'; l{6}='Never';
legend(bar_handle,l,'Location','Northeast','fontsize',12);

% print('survey_snippet_source','-dpdf','-bestfit')