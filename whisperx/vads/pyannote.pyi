from _typeshed import Incomplete
from pyannote.audio.core.io import AudioFile as AudioFile
from pyannote.audio.pipelines import VoiceActivityDetection
from pyannote.audio.pipelines.utils import PipelineModel as PipelineModel
from pyannote.core import Annotation, SlidingWindowFeature as SlidingWindowFeature
from typing import Callable
from whisperx.vads.vad import Vad as Vad

def load_vad_model(
    device,
    vad_onset: float = 0.5,
    vad_offset: float = 0.363,
    use_auth_token=None,
    model_fp=None,
): ...

class Binarize:
    onset: Incomplete
    offset: Incomplete
    pad_onset: Incomplete
    pad_offset: Incomplete
    min_duration_on: Incomplete
    min_duration_off: Incomplete
    max_duration: Incomplete
    def __init__(
        self,
        onset: float = 0.5,
        offset: float | None = None,
        min_duration_on: float = 0.0,
        min_duration_off: float = 0.0,
        pad_onset: float = 0.0,
        pad_offset: float = 0.0,
        max_duration: float = ...,
    ) -> None: ...
    def __call__(self, scores: SlidingWindowFeature) -> Annotation: ...

class VoiceActivitySegmentation(VoiceActivityDetection):
    def __init__(
        self,
        segmentation: PipelineModel = "pyannote/segmentation",
        fscore: bool = False,
        use_auth_token: str | None = None,
        **inference_kwargs,
    ) -> None: ...
    def apply(self, file: AudioFile, hook: Callable | None = None) -> Annotation: ...

class Pyannote(Vad):
    vad_pipeline: Incomplete
    def __init__(
        self, device, use_auth_token=None, model_fp=None, **kwargs
    ) -> None: ...
    def __call__(self, audio: AudioFile, **kwargs): ...
    @staticmethod
    def preprocess_audio(audio): ...
    @staticmethod
    def merge_chunks(
        segments, chunk_size, onset: float = 0.5, offset: float | None = None
    ): ...
