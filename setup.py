from setuptools import setup, find_packages

setup(
    name="seldoncore_huggingface_diffusion",
    version="1.0.0",
    description="HuggingFace Diffusion on Seldon Core",
    author="Sho Akiyama",
    author_email="akiyamashou@protonmail.com",
    packages=find_packages(),
    install_requires=[
        "torch==1.13.1",
        "diffusers==0.21.4",
        "safetensors==0.4.0",
        "transformers==4.25.1",
        "seldon-core==1.17.1",
        "pillow==10.0.1",
        "omegaconf==2.3.0",
    ],
    extras_require={
        "dev": [
            "autoflake==2.2.1",
            "black==23.9.1",
            "flake8==6.1.0",
            "pytest==7.4.2",
        ]
    },
)
