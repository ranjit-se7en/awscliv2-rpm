FROM centos:centos7.9.2009
RUN yum -y install \
    rpmdevtools \
    rpmlint

# for copying between host and container
RUN yum -y install \
    rsync

WORKDIR /root


COPY check_for_new_installer rebuildit respecit .
RUN chmod +x check_for_new_installer rebuildit respecit

RUN ./check_for_new_installer
RUN ./respecit
RUN rpmdev-setuptree
RUN ./rebuildit
#RUN rsync -ai $HOME/rpmbuild/RPMS/ ./RPMS/
ENTRYPOINT ["/usr/bin/rsync -ai"]
