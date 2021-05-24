FROM katonic/notebook-env:base

USER root

RUN apt-get update && apt-get -y install gcc
RUN apt-get install -y --reinstall build-essential

RUN pip3 install pandas==1.0.5 numpy==1.19.5 sklearn==0.24.0

RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update
RUN apt-get install -y kubectl

ADD ./iris_knn/knn.py  /opt/knn.py

ENTRYPOINT ["/usr/local/bin/python3"]
CMD ["/opt/knn.py"]

COPY . ./

USER katonic

