import os
import shutil
from classes.AudioFileSplitter import AudioFileSplitter
from classes.Transcriptor import Transcriptor
from pydub import AudioSegment
from utils.LogHandling import log_err, log_val


def main() -> int:
    base_data_path: str = '<your-repo-location>/Conduit-AI-Service/data/'
    input_file_path: str = os.path.join(base_data_path, 'input/Ra.m4a')

    split_files_path: str = os.path.join(base_data_path, 'splitFiles')
    output_file_path: str = os.path.join(base_data_path, 'output')
    (file_name_without_extension, input_file_extension) = os.path.splitext(os.path.basename(input_file_path))
    presence_of_converted_file = False

    if input_file_extension == '.m4a':
        try:
            sound = AudioSegment.from_file(input_file_path, format = 'm4a')
            input_file_path = input_file_path[0:-4] + '.wav'
            sound.export(input_file_path, format = 'wav')
            presence_of_converted_file = True
        except Exception as ex:
            log_err('Error while converting .m4a to .wav')
            log_err(ex)
            return 1

    try:
        os.makedirs(os.path.join(split_files_path, file_name_without_extension), exist_ok = True)
        os.makedirs(os.path.join(output_file_path, file_name_without_extension), exist_ok = False)
    except Exception as ex:
        log_err(ex)
        log_err('Transcription for a file with same name already exists')
        return 1

    try:
        AudioFileSplitter(input_file_path, split_files_path).multiple_split(1)
        transcriptor = Transcriptor(audio_file_folder_path = os.path.join(split_files_path, file_name_without_extension), output_file_path = output_file_path, output_file_name = file_name_without_extension)
        transcription = transcriptor.transcribe()
        log_val('The transcription is: ' + transcription)
        transcriptor.save_transcription()
    finally:
        shutil.rmtree(os.path.join(split_files_path, file_name_without_extension))
        if presence_of_converted_file:
            os.remove(input_file_path)

    return 0


if __name__ == "__main__":
    main()
