from classes.AudioFileSplitter import AudioFileSplitter
from classes.Transcriptor import Transcriptor

def main() -> int:
    afs = AudioFileSplitter('/Users/pranavchatur/Conduit-AI-Service/data/input/foodChoice.wav')
    afs.multiple_split(1)
    transcriptor = Transcriptor('/Users/pranavchatur/Conduit-AI-Service/data/splitFiles/', '', 'large-v2', '/Users/pranavchatur/Conduit-AI-Service/data/output/')
    transcription = transcriptor.transcribe()
    print(f"The transcription is: {transcription}")
    transcriptor.save_transcription()
    return 0


if __name__ == "__main__":
    main()
