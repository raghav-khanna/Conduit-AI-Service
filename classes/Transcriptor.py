'''
Transcriptor.py
This file contains the Transcriptor class which is responsible for transcribing the audio file.
Constructor -
    Takes the audio file path and model name as input
Functions -
    1. transcribe - Transcribes the audio file and returns the text
    2. save_transcription - Saves the transcription to a file
'''

import whisper
import logging
import os

logging.getLogger('requests').setLevel(logging.ERROR)
logging.basicConfig(level = 10, format = "%(levelname)s:%(message)s:\n")  # Comment this line to stop showing the messages


class Transcriptor:

    def __init__(self, audio_file_folder_path, audio_file_name = '', model_name = "large-v2", output_file_path = "", output_file_name = ""):
        self.audio_file_folder_path = audio_file_folder_path
        self.audio_file_name = audio_file_name
        self.model_name = model_name
        self.output_file_path = output_file_path
        self.output_file_name = output_file_name
        # Load the model
        logging.info(f"Loading model {self.model_name}")
        try:
            self.model = whisper.load_model(self.model_name)
        except Exception as e:
            logging.error(f"Error loading model {self.model_name} - {e}")
        self.transcription = ""

    def transcribe(self):
        # Check if the audio file name is provided
        if self.audio_file_name == '':
            logging.info("Audio file name is empty, transcribing all the files inside the folder")
            # Get each file in the folder and transcribe
            for file in sorted(os.listdir(self.audio_file_folder_path)):
                filename = os.fsdecode(file)
                if filename.endswith(".wav"):
                    logging.debug(f"Transcribing {filename}")
                    audio_file_path = os.path.join(self.audio_file_folder_path, filename)
                    try:
                        self.transcription += self.model.transcribe(audio_file_path, task = "translate", fp16 = False)["text"]
                    except Exception as e:
                        logging.error(f"Error transcribing {filename} - {e}")
                    logging.debug(f"Transcription completed for {filename}")
                else:
                    logging.debug(f"Skipping invalid format file - {filename}")
        else:
            audio_file_path = os.path.join(self.audio_file_folder_path, self.audio_file_name)
            try:
                self.transcription = self.model.transcribe(audio_file_path, task = "translate")["text"]
            except Exception as e:
                logging.error(f"Error transcribing {self.audio_file_name} - {e}")

        return self.transcription

    def save_transcription(self):
        if self.transcription == "":
            logging.error("Transcription is empty, cannot save")
            return
        try:
            if self.audio_file_name == '' and self.output_file_path == '':
                output_file_path = os.path.join(self.audio_file_folder_path, "transcription.txt")
            elif self.output_file_path == '':
                output_file_path = os.path.join(self.audio_file_folder_path, self.audio_file_name.split(".")[0] + "_transcription.txt")
            elif self.output_file_name != '':
                output_file_path = os.path.join(self.output_file_path, self.output_file_name, "transcription.txt")
            else:
                output_file_path = os.path.join(self.output_file_path, "transcription.txt")
        except Exception as e:
            logging.error(f"Error creating output file path - {e}")
        try:
            with open(output_file_path, 'w', encoding = "utf-8") as f:
                f.write(self.transcription)
            logging.info(f"Transcription saved to {output_file_path}")
        except Exception as e:
            logging.error(f"Error saving transcription - {e}")