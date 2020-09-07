%1:original, 2:bilatera70 3:nlmeans_21_3 4:wavelet_visu_1.58 5:bayes,
%6:bm3d, 7:dft

ax = ["Original","Bilateral","NLmeans", "VisuShrink","BayesShrink", "BM3D", "BandReject"];
ev_piqe = zeros(1,7);
ev_niqe = zeros(1,7);
ev_brisque = zeros(1,7);
for i=[1:1:7]
    x = eval(join(['x',int2str(i)]));
    i
    ev_piqe(i) = piqe(x);
    ev_niqe(i) = niqe(x);
    ev_brisque(i) = brisque(x);
end
axis=categorical(ax);
axis=reordercats(axis,ax);

figure
plot(axis,ev_piqe,'-o','MarkerEdgeColor','r',...
    'MarkerFaceColor','r',...
    'MarkerSize',10)
ylim([0 50])
title("Piqe Results")
figure
plot(axis,ev_niqe,'-o','MarkerEdgeColor','r',...
    'MarkerFaceColor','r',...
    'MarkerSize',10)
ylim([0 7])
title("Niqe Results")

figure
plot(axis,ev_brisque,'-o','MarkerEdgeColor','r',...
    'MarkerFaceColor','r',...
    'MarkerSize',10)
ylim([0 55])
title("Brisque Results")