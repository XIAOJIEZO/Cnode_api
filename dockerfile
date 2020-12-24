FROM  jenkins/jenkins:2.249.3-lts-alpine

USER root
WORKDIR /etc/apk/
RUN echo "https://mirrors.ustc.edu.cn/alpine/v3.12/main/" > repositories \
 && echo "https://mirrors.ustc.edu.cn/alpine/v3.12/community/" >> repositories \
 && apk update \
 && apk add python3
 && python3 -m ensurepip --default-pip
