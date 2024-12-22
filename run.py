from classes.AudioFileSplitter import AudioFileSplitter


def main() -> int:
    afs = AudioFileSplitter('<project-destination>/Conduit-AI-Service/data/input/ezyZip-2.wav')
    afs.multiple_split(1)
    return 0


if __name__ == "__main__":
    main()
