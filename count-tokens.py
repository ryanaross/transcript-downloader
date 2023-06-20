import tiktoken
import sys
import os

if __name__ == "__main__":
    transcript_file = sys.argv[1]

    file_contents = ""
    with open(transcript_file, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    encoding = tiktoken.encoding_for_model("gpt-4")
    num_tokens = len(encoding.encode(file_contents))
    print(num_tokens)
