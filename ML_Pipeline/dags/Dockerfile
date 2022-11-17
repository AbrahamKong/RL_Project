FROM apache/airflow:2.4.2
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         zip unzip gcc g++ pkg-config libfreetype6-dev libpng-dev  \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
RUN pip install --upgrade pip
RUN pip install Cmake
RUN pip install matplotlib==3.2.2
RUN pip install tflearn==0.5.0
RUN pip install certifi==2022.9.24
RUN pip install charset-normalizer==2.1.1
RUN pip install gym==0.11.0
RUN pip install idna==3.4
RUN pip install pyglet==1.5.27
RUN pip install requests==2.28.1
RUN pip install six==1.16.0
RUN pip install urllib3==1.26.12
RUN pip install tensorflow==2.10.0