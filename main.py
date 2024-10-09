import yt_dlp

def download_video(video_url):
    try:
        # Set options for downloading video (MP4) and audio (MP3)
        video_opts = {
            'format': 'bestvideo[ext=mp4][height<=1080]/best[ext=mp4]',  # Ensure video format is MP4 and up to 1080p
            'outtmpl': 'C:\\Users\\Abdul\\Desktop\\videos\\%(title)s.%(ext)s',  # Video save path
        }

        audio_opts = {
            'format': 'bestaudio[ext=mp3]/bestaudio',  # Ensure audio format is MP3
            'outtmpl': 'C:\\Users\\Abdul\\Desktop\\audio\\%(title)s.%(ext)s',  # Audio save path
        }

        # Use yt-dlp to fetch video information
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

            # Extract video details
            video_title = info_dict.get('title', 'Unknown Title')
            thumbnail_url = info_dict.get('thumbnail', 'No Thumbnail Available')

            print(f"Video Title: {video_title}")
            print(f"Thumbnail URL: {thumbnail_url}")

            # Download video (MP4)
            ydl.download([video_url])
            print("Video downloaded successfully!")

        # Download audio (MP3)
        with yt_dlp.YoutubeDL(audio_opts) as ydl_audio:
            ydl_audio.download([video_url])
            print("Audio downloaded successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Test with a YouTube video URL
url = "https://www.youtube.com/watch?v=CQXpxmIMl8s"
download_video(url)
