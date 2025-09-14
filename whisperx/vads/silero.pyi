from _typeshed import Incomplete
from io import IOBase
from pathlib import Path
from typing import Mapping
from whisperx.vads.vad import Vad as Vad

AudioFile = str | Path | IOBase | Mapping

class Silero(Vad):
    vad_onset: Incomplete
    chunk_size: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __call__(self, audio: AudioFile, **kwargs): ...
    @staticmethod
    def preprocess_audio(audio): ...
    @staticmethod
    def merge_chunks(
        segments_list, chunk_size, onset: float = 0.5, offset: float | None = None
    ): ...
