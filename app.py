import torch
import torch.nn as nn
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset


class WhisperModel(nn.Module):
    def __init__(self, sampling_rate=44100):
        super().__init__()
        self.model = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
        self.processor = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")
        self.model.config.forced_decoder_ids = None
        self.sampling_rate = sampling_rate
    
    def forward(self, x):
        
        if not isinstance(x, torch.Tensor):
            input_features = self.processor(x, sampling_rate=self.sampling_rate, return_tensors="pt").input_features
        else:
            input_features = x
            
        predicted_ids = self.model.generate(input_features)
        return self.processor.batch_decode(predicted_ids, skip_special_tokens=True)

if __name__ == "__main__":
    # load dummy dataset and read audio files
    ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
    sample = ds[0]["audio"]
    model = WhisperModel(sampling_rate=sample["sampling_rate"])
    
    output = model(sample["array"])
    
    