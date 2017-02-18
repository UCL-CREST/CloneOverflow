nd = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_nicad_df_130901_1234_fixedclonelines/qualitas_projects.csv', 1, 1);
sd = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_simian_df_130901_1234_fixedclonelines/qualitas_projects.csv', 1, 1);
ne = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_nicad_fse13_130901_1234_fixedclonelines/qualitas_projects.csv', 1, 1);
se = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_simian_fse13_130901_1234_fixedclonelines/qualitas_projects.csv', 1, 1);

so_sd = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_simian_df_130901_1234_fixedclonelines/fragment_stats.csv', 1, 1);
so_sd_count = so_sd(:,1);
so_nd = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_nicad_df_130901_1234_fixedclonelines/fragment_stats.csv', 1, 1);
so_nd_count = so_nd(:,1);

so_se = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_simian_fse13_130901_1234_fixedclonelines/fragment_stats.csv', 1, 1);
so_se_count = so_se(:,1);
so_ne = csvread('/Users/Chaiyong/IdeasProjects/StackOverflowAnalyzer/stats_nicad_fse13_130901_1234_fixedclonelines/fragment_stats.csv', 1, 1);
so_ne_count = so_ne(:,1);

% subplot(1,2,1)
% sosd_hist=histogram(so_sd_count,'NumBins', 60)
% ylabel('No. of snippets','FontSize',16)
% xlabel('No. of clone pairs','FontSize',16)
% set(gca,'FontSize',16);
% dim = [.19 .6 .3 .3];
% str = 'NumBins=60, BinWidth=23';
% annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');
% 
% subplot(1,2,2)
% sdhist=histogram(sd,'NumBins', 60)
% ylabel('No. of projects','FontSize',16)
% xlabel('No. of clone pairs','FontSize',16)
% set(gca,'FontSize',16);
% dim = [.63 .6 .3 .3];
% str = 'NumBins=60, BinWidth=266';
% annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');
% 
% h=gcf;
% set(h,'PaperPositionMode','auto');         
% set(h,'PaperOrientation','landscape');
% set(h,'Position',[50 50 800 300]);
% print('hist_sd','-dpdf','-bestfit')

subplot(1,2,1)
sond_hist=histogram(so_nd_count,'NumBins',60)
ylabel('No. of snippets','FontSize',16)
xlabel('No. of clone pairs','FontSize',16)
set(gca,'FontSize',16);
dim = [.19 .6 .3 .3];
str = 'NumBins=60, BinWidth=110';
annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');

subplot(1,2,2)
ndhist=histogram(nd,'NumBins', 60)
ylabel('No. of projects','FontSize',16)
xlabel('No. of clone pairs','FontSize',16)
set(gca,'FontSize',16);
dim = [.62 .6 .3 .3];
str = 'NumBins=60, BinWidth=5900';
annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');

h=gcf;
set(h,'PaperPositionMode','auto');         
set(h,'PaperOrientation','landscape');
set(h,'Position',[50 50 800 300]);
print('hist_nd','-dpdf','-bestfit')

% subplot(1,2,1)
% sose_hist=histogram(so_se_count,'NumBins', 60)
% ylabel('No. of snippets','FontSize',16)
% xlabel('No. of clone pairs','FontSize',16)
% set(gca,'FontSize',16);
% dim = [.16 .6 .3 .3];
% str = 'NumBins=60, BinWidth=640000';
% annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');
% 
% subplot(1,2,2)
% sehist=histogram(se,'NumBins', 60)
% ylabel('No. of projects','FontSize',16)
% xlabel('No. of clone pairs','FontSize',16)
% set(gca,'FontSize',16);
% dim = [.6 .6 .3 .3];
% str = 'NumBins=60, BinWidth=311000';
% annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');
% 
% h=gcf;
% set(h,'PaperPositionMode','auto');         
% set(h,'PaperOrientation','landscape');
% set(h,'Position',[50 50 800 300]);
% print('hist_se','-dpdf','-bestfit')
% 
% subplot(1,2,1);
% sone_hist=histogram(so_ne_count,'NumBins', 60);
% ylabel('No. of snippets','FontSize',16)
% xlabel('No. of clone pairs','FontSize',16)
% set(gca,'FontSize',16);
% dim = [.16 .6 .3 .3];
% str = 'NumBins=60, BinWidth=12800';
% annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');
% 
% subplot(1,2,2);
% nehist=histogram(ne,'NumBins', 60);
% ylabel('No. of projects','FontSize',16);
% xlabel('No. of clone pairs','FontSize',16)
% set(gca,'FontSize',16);
% dim = [.6 .6 .3 .3];
% str = 'NumBins=60, BinWidth=455000';
% annotation('textbox',dim,'String',str,'FitBoxToText','on','FontSize',15,'LineStyle','none');
% sone_hist;
% nehist;
% 
% h=gcf;
% set(h,'PaperPositionMode','auto');         
% set(h,'PaperOrientation','landscape');
% set(h,'Position',[50 50 800 300]);
% print('hist_ne','-dpdf','-bestfit')