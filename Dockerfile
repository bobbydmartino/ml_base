FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	tmux \
	wget \
	zsh \
	sudo \
	curl \
	rsync \
	git \
    unzip \
	python3-pip \
	python-is-python3 \
    python3-venv \
	&& rm -rf /var/lib/apt/lists/*


COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /root/	
ENTRYPOINT ["/bin/bash"]
