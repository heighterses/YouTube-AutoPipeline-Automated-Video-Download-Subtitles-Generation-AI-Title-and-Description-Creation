import yt_dlp
import ffmpeg


# tentative variables for tetsing

merge_video_path = 'C:\\Users\\Abdul\\Desktop\\videos\\v2.mp4'
merge_audio_path = 'C:\\Users\\Abdul\\Desktop\\audio\\a2.webm'
output_merge_video_path = 'C:\\Users\\Abdul\\Desktop\\after_merge\\merge_test.mp4'


# def download_video(video_url):
#     try:
#         # Set options for downloading video (MP4) and audio (MP3)
#         video_opts = {
#             'format': 'bestvideo[ext=mp4][height<=1080]/best[ext=mp4]',  # Ensure video format is MP4 and up to 1080p
#             'outtmpl': 'C:\\Users\\Abdul\\Desktop\\videos\\%(title)s.%(ext)s',  # Video save path
#         }
#
#         audio_opts = {
#             'format': 'bestaudio[ext=mp3]/bestaudio',  # Ensure audio format is MP3
#             'outtmpl': 'C:\\Users\\Abdul\\Desktop\\audio\\%(title)s.%(ext)s',  # Audio save path
#         }
#
#         # Use yt-dlp to fetch video information
#         with yt_dlp.YoutubeDL(video_opts) as ydl:
#             info_dict = ydl.extract_info(video_url, download=False)
#
#             # Extract video details
#             video_title = info_dict.get('title', 'Unknown Title')
#             thumbnail_url = info_dict.get('thumbnail', 'No Thumbnail Available')
#
#             print(f"Video Title: {video_title}")
#             print(f"Thumbnail URL: {thumbnail_url}")
#
#             # Download video (MP4)
#             ydl.download([video_url])
#             print("Video downloaded successfully!")
#
#         # Download audio (MP3)
#         with yt_dlp.YoutubeDL(audio_opts) as ydl_audio:
#             ydl_audio.download([video_url])
#             print("Audio downloaded successfully!")
#
#     except Exception as e:
#         print(f"Error: {e}")
#
# # Test with a YouTube video URL
# url = "https://www.youtube.com/watch?v=2CwVpAKOfRE"
# download_video(url)

# We need to merge the audio to the video because the library I have used it will remove the audio from video

def merge_audio(video_file, audio_file, output_file):
    try:
        input_video = ffmpeg.input(video_file)
        input_audio = ffmpeg.input(audio_file)
        ffmpeg.output(input_video, input_audio, output_file, vcodec='copy', acodec='aac', strict='experimental').run()
    except Exception as e:
        print(e)

merge_audio(merge_video_path, merge_audio_path,output_merge_video_path)
