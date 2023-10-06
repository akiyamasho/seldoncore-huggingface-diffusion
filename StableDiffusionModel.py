import os
import base64
import io

from PIL import Image
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler


class StableDiffusionModel(object):
    def __init__(self):
        self.pipeline = StableDiffusionPipeline.from_single_file(
            os.path.join("artifacts", "model.safetensors")
        )
        self.pipeline.scheduler = EulerDiscreteScheduler.from_config(
            self.pipeline.scheduler.config
        )
        pass

    def predict(self, positive_prompt: str, negative_prompt: str):
        output_image: Image.Image = self.pipeline.run(
            positive_prompt, negative_prompt
        ).images[0]

        buffer = io.BytesIO()
        output_image.save(buffer, format="PNG")
        buffer.seek(0)

        data_uri = base64.b64encode(buffer.read()).decode("ascii")
        base64_image = f"data:image/png;base64,{data_uri}"

        return base64_image
