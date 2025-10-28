# Use the official Python 3.10.12 image
FROM python:3.10.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Upgrade pip to version 24.0
RUN pip install --upgrade pip==24.0

# Install git
RUN apt-get update && apt-get install -y git ffmpeg && apt-get clean

# Create a working directory
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/prashkrans/yt_video_downloader.git .

# Install the required Python packages
RUN pip install -r requirements.txt

# Expose port 7870
EXPOSE 7870

# Set environment variable for Gradio to listen on all interfaces
ENV GRADIO_SERVER_NAME=0.0.0.0

# Run the main_gradio.py script
CMD ["python", "main_gradio.py"]
