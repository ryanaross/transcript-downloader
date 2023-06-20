from bs4 import BeautifulSoup
import os
import sys


def get_channel_videos(html_file_path):
    with open(html_file_path, 'r', encoding='utf8') as f:
        contents = f.read()

    # Find the start of the desired section
    start_index = contents.find('style-scope ytd-expandable-tab-renderer')

    # Trim the contents to start at the desired section
    if start_index != -1:
        contents = contents[start_index:]
    else:
        print("The desired text 'style-scope ytd-expandable-tab-renderer' was not found in the HTML file.")
        return []

    soup = BeautifulSoup(contents, 'html.parser')

    video_links = []
    for a in soup.find_all('a', id='video-title-link'):
        title = a.get('title')
        url = a.get('href')
        if not url.startswith('https://www.youtube.com/shorts'):  # Skip shorts
            video_links.append((title, url))

    return video_links


if __name__ == "__main__":
    html_file_path = sys.argv[1]
    channel_name = os.path.basename(
        html_file_path).replace(' - YouTube.html', '')
    video_list_file = channel_name + '.txt'

    video_links = get_channel_videos(html_file_path)
    with open(video_list_file, 'w', encoding='utf-8') as f:
        for title, link in video_links:
            f.write(f'{title}\t{link}\n')
