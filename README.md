# README

This set of Python scripts can be used to parse the video list from a YouTube channel's HTML file, download transcripts from these videos, and then count the number of tokens in these transcripts using the GPT-4 model from OpenAI's `tiktoken` library.

## parse-channel-list.py

This script takes a downloaded YouTube channel's HTML file as an argument, parses the file to extract video links and their titles, and writes them to a .txt file.

```bash
python parse-channel-list.py "<path_to_your_html_file>"
```

The output is a .txt file containing the video titles and URLs. This file will be located in the directory where you run the script, with the filename format `<channel_name>.txt`.

## download-transcripts.py

This script takes a .txt file (generated by `parse-channel-list.py`) as an argument, downloads the transcripts of the videos, and writes them to a new .txt file.

```bash
python download-transcripts.py "<path_to_your_txt_file>"
```

The output is a .txt file containing the video titles and their transcripts. This file will be located in the directory where you run the script, with the filename format `<channel_name>-transcripts.txt`.

## count-tokens.py

This script takes a transcript .txt file (generated by `download-transcripts.py`) as an argument, counts the number of GPT-4 tokens in the file's contents, and prints this count.

```bash
python count-tokens.py "<path_to_your_transcript_txt_file>"
```

The output is the number of tokens in the transcript file's contents, printed to the console.

## Requirements

- BeautifulSoup4
- requests
- youtube_transcript_api
- tiktoken

These dependencies can be installed with pip:

```bash
pip install beautifulsoup4 requests youtube_transcript_api tiktoken
```

**Note:** This assumes you have Python installed, and that you've replaced the placeholder arguments in the commands with the paths to your actual files. Also, the scripts must be run in the order listed above. The later scripts rely on the files generated by the earlier scripts.
