from moviepy.editor import VideoFileClip
from celery import shared_task

@shared_task
def clip_video(video_file_path, request_data, clip_path):
    video = VideoFileClip(video_file_path)
    clip = video.subclip(request_data['start_time'],request_data['end_time'])
    clip.write_videofile(clip_path)
    print("file clipped")