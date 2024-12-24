from pydub import AudioSegment
import math
import os
from utils.LogHandling import log_prog, log_val


class AudioFileSplitter():

    def __init__(self, input_file_path: str, split_folder_path: str) -> None:
        self.__file_path = input_file_path
        self.__file_name_with_extension = os.path.basename(input_file_path)
        self.__file_name_without_extension = os.path.splitext(os.path.basename(input_file_path))[0]
        self.__audio = AudioSegment.from_wav(self.__file_path)
        self.__split_folder_path = split_folder_path

    def single_split(self, from_min: int, to_min: int, chunk_num: int = 0):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_file_name = str(chunk_num) + '_' + self.__file_name_with_extension
        split_audio = self.__audio[t1:t2]
        split_audio.export(os.path.join(self.__split_folder_path, self.__file_name_without_extension, split_file_name), format = "wav")

    def multiple_split(self, min_per_split: int):
        total_mins = math.ceil(self.__audio.duration_seconds / 60)
        chunk_num = 1
        for i in range(0, total_mins, min_per_split):
            self.single_split(i, i + min_per_split, chunk_num)
            log_prog('Chunk ' + str(chunk_num) + ' has been completed')
            chunk_num += 1
        log_prog('Splitting complete')
