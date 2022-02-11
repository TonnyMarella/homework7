import requests

video_url = 'https://player.vimeo.com/video/314271027?h=ca85dc694b&app_id=122963'


def down_video(url):
    try:
        response = requests.get(url=url)
        with open("req.video.mp4", 'wb') as file:
            file.write(response.content)

        return "Downloaded!"
    except Exception as _ex:
        return "Oooppss.."


def main():
    print(down_video(url=video_url))