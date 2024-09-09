### Pre-requisite: 
Download and Install the Docker Desktop. 

### 1. To run yt_video_downloader in docker directly:
```
cd workspace
mkdir yt_video_downloader_docker
cd yt_video_downloader_docker
nano Dockerfile

# Paste the contents of Dockerfile and save it
docker build -t yt_video_downloader_image .

# Yet to verify the below:
docker run -d -p 7870:7870 --name yt_video_downloader_container yt_video_downloader_image

# Using 7870 port as the main_gradio.py is launched in port 7870
# Use the docker desktop console to stop and start this container
```

### 2. To run yt_video_downloader in docker using docker hub in Windows 10/11:
- Run the `YT_Video_Downloader_Setup.bat` by double clicking on it.
- It automatically pulls a working image (~500 MBs) from the public repo of `yt_video_downloader` from the docker hub, then creates a container from it and runs it.
- There's no need to clone the repo here as the `.bat` file and the `docker image` from the docker hub does everything here.
- Then use the docker desktop console to stop and start this container as required.
- **Troubleshoot:** Whenever there's any issue simply delete both the yt_video_downloader container and image in the docker desktop console and re-run the `YT_Video_Downloader_Setup.bat` (only once).
