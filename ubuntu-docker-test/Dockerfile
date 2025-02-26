# Start with Ubuntu latest
FROM ubuntu:latest

# Set non-interactive mode for apt commands
ENV DEBIAN_FRONTEND=noninteractive

# Update and install some useful packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    nano \
    git \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /app

# Create a simple text file in the container
RUN echo "Hello from my custom Ubuntu container" > hello.txt

# Set the default command
CMD ["/bin/bash"]