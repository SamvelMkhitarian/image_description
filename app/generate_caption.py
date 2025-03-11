import asyncio

import torch
from PIL import Image
from settings import MODEL_NAME
from transformers import (AutoTokenizer, VisionEncoderDecoderModel,
                          ViTImageProcessor)

model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)
feature_extractor = ViTImageProcessor.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


async def generate_caption(image: Image.Image) -> str:
    if image.mode != "RGB":
        image = image.convert("RGB")

    def _generate():
        pixel_values = feature_extractor(
            images=image, return_tensors="pt").pixel_values.to(device)
        output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
        preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        return preds[0].strip()

    caption = await asyncio.to_thread(_generate)
    return caption
