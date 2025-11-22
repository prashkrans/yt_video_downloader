import gradio as gr

from _1_download_yt_video import download_video
from _2_extract_audio_from_yt_video import extract_audio
from _utils import PARAMS_JSON_PATH, json_write, resolution_map, clear_resources


def download_yt_video(
    yt_video_url,
    file_name,
    resolution_key
):
    clear_resources()
    resolution = resolution_map[resolution_key]
    # Create dictionary
    params_dict = {
        'YT_VIDEO_URL': f'{yt_video_url}',
        'FILE_NAME': f'{file_name}',
        'RESOLUTION': f'{resolution}p'
    }

    json_write(PARAMS_JSON_PATH, params_dict)


    downloaded_video_path = download_video(yt_video_url, file_name, resolution)
    audio_file_path = extract_audio(file_name)

    print(f'downloaded_video_path: {downloaded_video_path}')
    print(f'audio_file_path: {audio_file_path}')

    return (
        gr.Video(value=downloaded_video_path),
        gr.Audio(value=audio_file_path)
    )

interface = gr.Interface(
    fn = download_yt_video,
    inputs = [
        gr.Textbox(label="Input YT Video URL"),
        gr.Textbox(label="Input File Name"),
        gr.Radio(
            label='Select video resolution',
            choices=['SD', 'HD', 'FHD'],
            value='HD'
        )
    ],
    outputs = [ # Note: Change the ngrok server in config.json
        gr.Video(label="YT Video Preview"),
        gr.Audio(label="YT Audio Preview")
    ],
    title="Download a youtube video using url and extract audio from it",
    description="""
    Copy a youtube video link and input file name | Click Submit and after processing completes, download the video 
    and/or audio 
    """
)

interface.queue(api_open=False).launch(
    theme=gr.themes.Glass(),
    server_port=7870
) # Local launch | Different server_port from auto_subs

"""
Gradio Themes:
— gr.themes.Base()
— gr.themes.Default()
— gr.themes.Glass()
— gr.themes.Monochrome()
— gr.themes.Soft()
"""