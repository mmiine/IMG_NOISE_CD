%[Original, median3, bilateral_70_10, nlmeans_25_5, dft,visu,bayes,bm3d]

list = ["Original", "Median", "Bilateral", "NLmeans", "Band-Reject", "VisuShrink", "BayesShirnk", "BM3D"];
len = length(list);
Brisque = zeros(1,len);
Niqe = zeros(1,len);
Piqe = zeros(1,len);

for i=1:len
Brisque(i) = brisque(eval(['cdata' num2str(i)]));
Niqe(i) = niqe(eval(['cdata' num2str(i)]));
Piqe(i) = piqe(eval(['cdata' num2str(i)]));
end

figure
plot(Niqe,'-ok','LineWidth',1,'MarkerSize',8,'MarkerEdgeColor','r','MarkerFaceColor','r');
title("Niqe Results")
ylabel("Score")
xticklabels(list)
xtickangle(45)

figure
plot(Piqe,'-ok','LineWidth',1,'MarkerSize',8,'MarkerEdgeColor','r','MarkerFaceColor','r');
title("Piqe Results")
ylabel("Score")
xticklabels(list)
xtickangle(45)

figure
plot(Brisque,'-ok','LineWidth',1,'MarkerSize',8,'MarkerEdgeColor','r','MarkerFaceColor','r');
title("Brisque Results")
ylabel("Score")
xticklabels(list)
xtickangle(45)

figure
for i=1:len
    subplot(4,2,i)
    imshow(eval(['cdata' num2str(i)]));
    title(list(i))
end
