FROM docker.elastic.co/elasticsearch/elasticsearch:7.5.0
RUN elasticsearch-plugin install analysis-kuromoji
COPY user_dict.csv /usr/share/elasticsearch/config