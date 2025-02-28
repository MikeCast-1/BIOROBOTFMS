from PIL import Image


def rescale_image(input_path, output_path, width, height):
    # Open the input image
    with Image.open(input_path) as img:
        # Rescale the image
        img_rescaled = img.resize((width, height))
        # Save the rescaled image to the output path
        img_rescaled.save(output_path)
    

# Example usage
input_image_path = 'C:/Users/Usuario/Documents/pyhton/Test_img0.jpg'  # Replace with your input image path
output_image_path = 'C:/Users/Usuario/Documents/pyhton/Test_img1.jpg'  # Replace with your desired output image path
new_width = 8  # Replace with your desired width
new_height = 8  # Replace with your desired height

rescale_image(input_image_path, output_image_path, new_width, new_height)