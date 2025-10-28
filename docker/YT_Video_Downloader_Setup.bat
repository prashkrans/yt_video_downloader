@echo off

echo Downloading the Docker image, which is about 500 MB in size...

REM Step 1: Pull the Docker image from Docker Hub
docker pull nashprat/yt_video_downloader:v1.0

REM Step 2: Run the Docker container
docker run -d -p 7870:7870 --name yt_video_downloader nashprat/yt_video_downloader:v1.0

REM Add a delay of 5 seconds and display a message
echo Please wait for the application to start...
timeout /t 5 /nobreak >nul

REM Step 3: Open the default web browser
start "" "http://localhost:7870"

REM Done
echo Gradio app should be running at http://localhost:7870
exit