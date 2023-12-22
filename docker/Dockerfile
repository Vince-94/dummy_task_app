FROM public.ecr.aws/lambda/python:3.12


########################
# INSTALL DEPENDENCIES #
########################

RUN echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc

WORKDIR ${LAMBDA_TASK_ROOT}

# Python deps
COPY requirements.txt .
RUN pip3 install --upgrade -r requirements.txt

# Copy volume
COPY . .

EXPOSE 8000


##################
# Final Settings #
##################

RUN echo "source /usr/share/bash-completion/completions/git" >> ~/.bashrc

ENV force_color_prompt=yes

# CMD ["bash"]
CMD ["main.handler"]