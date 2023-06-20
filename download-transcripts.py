import requests
import os
import sys
import time
import random
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi


def scrape(URL):
    text = ""

    if "youtube.com" in URL:
        VIDEO_ID = URL.replace('https://www.youtube.com/watch?v=', '')
        try:
            data = YouTubeTranscriptApi.get_transcript(video_id=VIDEO_ID)
            for timestamp in data:
                text += timestamp["text"] + " "
        except:
            print(f"Could not download transcript for {URL}")
            pass
        return text[:-1]

    else:
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.text


if __name__ == "__main__":
    video_list_file = sys.argv[1]
    channel_name = os.path.basename(video_list_file).replace('.txt', '')
    transcripts_file = channel_name + '-transcripts.txt'

    with open(video_list_file, 'r', encoding='utf-8') as f:
        video_links = [line.strip().split('\t') for line in f]

    with open(transcripts_file, 'w', encoding='utf-8') as f:
        for title, link in video_links:
            time.sleep(random.randint(1, 10)/10)
            transcript = scrape(link)
            f.write(f'Video Title: {title}\nTranscript:\n{transcript}\n\n')
