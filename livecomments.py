import pytchat
import re

# Function to extract video ID from a YouTube URL
def extract_video_id(url):
    video_id_match = re.search(r"(?<=v=)[^#&?]*", url)
    if video_id_match:
        return video_id_match.group(0)
    return None

def fetch_live_chat_messages(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        print('Invalid YouTube URL.')
        return

    output_file = f"{video_id}.txt"

    chat = pytchat.create(video_id=video_id)
    with open(output_file, "w", encoding="utf-8") as file:
        while chat.is_alive():
            for c in chat.get().sync_items():
                message = f"[{c.datetime}] [{c.author.name}]: {c.message}\n"
                file.write(message)
                print(message)

    print(f"Chat messages saved to {output_file}")

def main():
    # Replace with the URL of the YouTube video
    video_url = 'enter url here'

    fetch_live_chat_messages(video_url)

if __name__ == '__main__':
    main()
