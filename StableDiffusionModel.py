from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler


class StableDiffusionModel(object):
    def __init__(self):
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4"
        )
        self.pipeline.scheduler = EulerDiscreteScheduler.from_config(
            self.pipeline.scheduler.config
        )
        pass

    def predict(self, positive_prompt: str, negative_prompt: str):
        output = self.pipeline.run(positive_prompt, negative_prompt)

        return
