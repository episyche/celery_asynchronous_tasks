from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import clip_video


class Clip_Video_API(APIView):

    def  post(self, request):

        """
            This post API crop a subclip from an existing video file
            using moviepy and save the cropped clip to a local directory.
        Args:
            video_file: name of the file located in the directory /home/ubuntu/media/.
            clip_name: file name for newly clipped video.
            start_time: duration from which the clip should start.
            end_time: duration from which the clip should end.
        Returns:
            data : Clip video's full file path
        """

        try:
            data = request.data
            media_dir = "/home/ubuntu/media/"
            video_file_path = media_dir + data['video_file']
            clip_path = media_dir + data['clip_name']
            clip_video.delay(video_file_path, data, clip_path)
            data, st, msg = clip_path, 200, "Video clipped successfully"
        except Exception as error:
            print(error)
            data, st, msg = "", 500, "Error while clipping the video"
        resp_json = {"data":data, "st":st, "msg":msg}
        return Response(resp_json)