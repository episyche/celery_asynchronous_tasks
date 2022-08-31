from rest_framework.response import Response
from rest_framework.views import APIView
from moviepy.editor import VideoFileClip

class Clip_Video_API(APIView):

    def  post(self, request):
        data = request.data
        print(data)
        video_file = "/home/ubuntu/media/example_video.mp4"
        video = VideoFileClip(video_file)
        clip = video.subclip(data['start_time'],data['end_time'])
        clip.write_videofile("/home/ubuntu/media/clip.mp4")

        return Response("POST method from the api")