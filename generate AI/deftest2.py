from diffusers import StableDiffusionPipeline
import torch
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = input("Enter a prompt to generate an image:")
image = pipe(prompt).images[0]  
image.save("generated_image.png")
image.show()
print("Image generated and saved as 'generated_image.png'")