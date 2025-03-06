from PIL import Image

# Open the first image
image1 = Image.open("D:\ITESO 1 Semestre\Algoritmos y Programación\Python\BIOROBOTFMS\Moon_img.jpg")

# Open the second image
image2 = Image.open("D:\ITESO 1 Semestre\Algoritmos y Programación\Python\BIOROBOTFMS\Moon_img.jpg")

# Get the size of the images
width1, height1 = image1.size
width2, height2 = image2.size

# Create a new image with a width that is the sum of both images' widths and the height of the taller image
new_image = Image.new('RGB', (width1 + width2, max(height1, height2)))

# Paste the first image at (0, 0)
new_image.paste(image1, (0, 0))

# Paste the second image at (width1, 0)
new_image.paste(image2, (width1, 0))

# Save the new image
new_image.save("joined_image.jpg")

print("The images have been joined and saved as joined_image.jpg")