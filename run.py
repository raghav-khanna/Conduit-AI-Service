from classes.AudioFileSplitter import AudioFileSplitter
from classes.Transcriptor import Transcriptor

def main() -> int:
    afs = AudioFileSplitter('<project-destination>/Conduit-AI-Service/data/input/ezyZip-2.wav')
    afs.multiple_split(1)
    transcriptor = Transcriptor('<project-destination>/Conduit-AI-Service/data/splitFiles/', '', '', '<project-destination>/Conduit-AI-Service/data/output/')
    transcription = transcriptor.transcribe()
    print(f"The transcription is: {transcription}")
    transcriptor.save_transcription()
    return 0


if __name__ == "__main__":
    main()
