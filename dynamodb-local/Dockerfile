FROM amazonlinux:latest
LABEL maintainer="Hidehiko-Inoue <hidehiko.inoue@gmail.com>"

# You have to prepare these packages.
ADD dynamodb_local_latest.tar.gz /srv/

RUN : \
  && : installing packages \
  && yum -y -q upgrade \
  && yum -y -q install \
      java-1.8.0-openjdk-headless \
  && yum -y -q clean all \
  && yum -y -q autoremove \
  && : setting environment \
  && cd /root \
  && cp /etc/skel/.bash* . \
  && echo 'export LANG=en_US.utf8' >>./.bashrc \
  && echo 'export LC_ALL=en_US.utf8' >>./.bashrc \
  && echo 'export JAVA_HOME=/usr/lib/jvm/jre' >>./.bashrc \
  && : End of RUN

WORKDIR /srv
EXPOSE 8000/tcp
ENTRYPOINT [ "java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar" ]
