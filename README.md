# Unified Data Set about National Security Letters

This repository provides the unified data set that we collected for the paper with the title "An Empirical Analysis on the Use and Reporting of National Security Letters".

We aggregate data from three different sources:
1. OIG, FISA and ASTR reports mandated by the USA PATRIOT Improvement and Reauthorization Act and the USA FREEDOM Act
2. Company transparency reports that include the number of received NSLs
3. NSLs disclosed by companies after the NSL's nondisclosure requirement is lifted

Structure of our data:
- The folder [scripts/analysis](/scripts/analysis/) contains Jupyter notebooks that parse and plot our data.
- Raw data sources, including automatically parsed HTML websites, transparency reports, and the PDF of released NSL letters are in [data/raw](/data/raw/)
- We parse the raw data with a mix of automated scripts and manual analysis, and produce clean CSV files for the extracted data for easy processing. These files are in [data/extracted](/data/extracted/).
- Finally, we process and plot the data, producing figures for our paper and other analysis. The resulting figures are in [data/extracted](/data/extracted/), and the scripts that produce the plots are in [scripts/analysis](/scripts/analysis/).