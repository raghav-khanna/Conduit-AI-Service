from classes.AudioFileSplitter import AudioFileSplitter
from classes.Transcriptor import Transcriptor
import os


def main() -> int:
    base_data_path: str = '/Users/pranavchatur/Conduit-AI-Service/data/'
    input_file_path: str = os.path.join(base_data_path, 'input/Rainbow Plaza.wav')
    split_files_path: str = os.path.join(base_data_path, 'splitFiles')
    output_file_path: str = os.path.join(base_data_path, 'output')

    file_name_without_extension = os.path.splitext(os.path.basename(input_file_path))[0]
    os.makedirs(os.path.join(split_files_path, file_name_without_extension), exist_ok = False)
    os.makedirs(os.path.join(output_file_path, file_name_without_extension), exist_ok = False)

    AudioFileSplitter(input_file_path, split_files_path).multiple_split(1)
    transcriptor = Transcriptor(audio_file_folder_path = os.path.join(split_files_path, file_name_without_extension), output_file_path = output_file_path, output_file_name = file_name_without_extension)
    transcription = transcriptor.transcribe()
    print(f"The transcription is: {transcription}")
    transcriptor.save_transcription()
    return 0


if __name__ == "__main__":
    main()
