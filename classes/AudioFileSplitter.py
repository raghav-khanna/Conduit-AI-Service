from pydub import AudioSegment
import math
import os
from utils.LogHandling import log_prog, log_val


class AudioFileSplitter():

    __split_folder = './data/splitFiles/'

    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.__file_name = os.path.basename(file_path)
        self.__audio = AudioSegment.from_wav(self.__file_path)

    def single_split(self, from_min: int, to_min: int, split_file_name: str):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.__audio[t1:t2]
        split_audio.export(self.__split_folder + '/' + split_file_name, format = "wav")

    def multiple_split(self, min_per_split: int):
        total_mins = math.ceil(self.__audio.duration_seconds / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.__file_name
            self.single_split(i, i + min_per_split, split_fn)
            log_prog('Chunk ' + str(i) + ' has been completed')
        log_prog('Splitting complete')
