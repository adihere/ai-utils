import configparser
import openai
from pydub import AudioSegment
from pydub.playback import play


# Read the configuration file
config = configparser.ConfigParser()
config.read('py-texttospeech/config.ini')

openai.api_key = config.get('openai','api_key')


dialogue_path = config['files']['dialogue_path']
audio_base_path = config['files']['audio_file_path']


def text_to_speech(text, voice):
    try:
        response = openai.Audio.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        audio_content = response['audio_content']
        audio_file_path = f"{audio_base_path}/output_{voice}.mp3"

        with open(audio_file_path, "wb") as audio_file:
            audio_file.write(audio_content)

        # Load the audio file and play it
        audio = AudioSegment.from_file(audio_file_path)
        play(audio)
        audio_file.close()  # Close the file after playing

    except Exception as e:
        print(f"An error occurred during audio generation: {e}")


def read_dialogue_file(file_path):
    with open(file_path, 'r') as file:
        dialogue = file.readlines()
    return dialogue


if __name__ == "__main__":
    # Read the text file
    dialogue = read_dialogue_file(dialogue_path)

    # Simulate conversation using different voices
    voices = ["nova", "onyx"]
    for i, line in enumerate(dialogue):
        voice = voices[i % 2]  # Alternate between Nova and Onyx
        print(f"Using voice {voice} for line: {line.strip()}")
        text_to_speech(line.strip(), voice)