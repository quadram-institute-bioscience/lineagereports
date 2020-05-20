FROM continuumio/anaconda3
RUN conda config --add channels defaults
RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge
RUN conda install git pip
RUN pip install git+git://github.com/quadram-institute-bioscience/lineagereports.git
