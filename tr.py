from gradio_client import Client, handle_file
import random

# Initialize the Gradio client with your API key
client = Client("Hatman/AWS-Nova-Canvas")

# Set the prompt to complete missing parts of a building and show how it looked in the past
prompt = "repair it." 

# Call the API with the required parameters
result = client.predict(
    images=[handle_file('mezar.jpg')],  # Adjust the path to your image
    text=prompt,
    negative_text=None,
    similarity_strength=0.7,  # Increase for more accuracy
    height=1024,
    width=1024,
    quality="standard",
    cfg_scale=10,
    seed=random.randint(0,10),
    api_name="/image_variation"
)

# Print the result
print(result)
