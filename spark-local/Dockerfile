FROM amazonlinux:latest
LABEL maintainer="Hidehiko-Inoue <hidehiko.inoue@gmail.com>"

# You have to prepare these packages.
ADD hadoop-3.1.0.tar.gz /opt/
ADD spark-2.3.0-bin-hadoop2.7.tgz /opt/

RUN : \
  && : installing packages \
  && yum -y -q upgrade \
  && yum -y -q install \
      java-1.8.0-openjdk-headless \
      python36 python36-pip \
  && yum -y -q clean all \
  && yum -y -q autoremove \
  && pip-3.6 install -q \
      jupyter boto3 \
  && : preparing Hadoop and Spark \
  && cd /opt \
  && chown root:root hadoop-3.1.0 \
  && ln -s hadoop-3.1.0 hadoop \
  && chown root:root spark-2.3.0-bin-hadoop2.7 \
  && ln -s spark-2.3.0-bin-hadoop2.7 spark \
  && : setting environment \
  && cd /root \
  && cp /etc/skel/.bash* . \
  && echo 'export LANG=en_US.utf8' >>./.bashrc \
  && echo 'export LC_ALL=en_US.utf8' >>./.bashrc \
  && echo 'export JAVA_HOME=/usr/lib/jvm/jre' >>./.bashrc \
  && echo 'export HADOOP_HOME=/opt/hadoop' >>./.bashrc \
  && echo 'export SPARK_HOME=/opt/spark' >>./.bashrc \
  && echo 'export PATH=$SPARK_HOME/bin:$HADOOP_HOME/bin:$PATH' >>./.bashrc \
  && cd /opt/spark/conf \
  && echo 'export SPARK_DIST_CLASSPATH=$(hadoop classpath)' >>./spark-env.sh \
  && echo 'export PYSPARK_PYTHON=/usr/bin/python36' >>./spark-env.sh \
  && echo 'export PYSPARK_DRIVER_PYTHON=jupyter' >>./spark-env.sh \
  && echo 'export PYSPARK_DRIVER_PYTHON_OPTS="notebook --ip 0.0.0.0 --allow-root "' >>./spark-env.sh \
  && : End of RUN

EXPOSE 8888/tcp
EXPOSE 4040/tcp
ENTRYPOINT [ "bash", "-lc", "pyspark" ]
