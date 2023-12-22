FROM public.ecr.aws/amazonlinux/amazonlinux:latest


########################
# INSTALL DEPENDENCIES #
########################

# Update
RUN yum update -y && yum upgrade -y

RUN yum install -y sudo yum-utils
# RUN yum-config-manager --enable epel

# Ubuntu deps
RUN yum install -y \
    which sudo openssl-devel git file \
    wget zip unzip pkgconfig openssh-clients openssh-server \
    tmux gdb valgrind htop net-tools nmap \
    lynx libX11-devel bash-completion

RUN echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc

# Python deps
RUN yum install -y python3 python3-pip python3-future
RUN pip3 install --upgrade wheel argcomplete

# Python deps
RUN pip3 install --upgrade \
    requests fastapi uvicorn pydantic

# Copy volume
COPY ./src/ /home/$UBUNTU_USER/RestAPI-Toy


##################
# Final Settings #
##################

RUN echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc

WORKDIR /home/RestAPI-Toy/

ENV force_color_prompt=yes

COPY src/* ${LAMBDA_TASK_ROOT}

# CMD ["bash"]
CMD ["python3", "-m", "uvicorn", "main:app", "--reload"]