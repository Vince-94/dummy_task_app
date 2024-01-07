FROM public.ecr.aws/lambda/python:3.10
ARG DEBIAN_FRONTEND=noninteractive


########################
# INSTALL DEPENDENCIES #
########################


# Python deps
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

# Copy volume
COPY main.py ${LAMBDA_TASK_ROOT}/main.py

# EXPOSE 8000


##################
# Final Settings #
##################

ENV force_color_prompt=yes

# CMD ["bash"]
CMD ["main.lambda_handler"]
