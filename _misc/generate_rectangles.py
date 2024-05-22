from PIL import Image, ImageDraw
from datetime import datetime

def generate_rectangles(rectangle_dimensions, rows_columns, padding, transparent=False):
	# Extract individual values
	rect_width, rect_height = rectangle_dimensions
	rows, columns = rows_columns
	padding_x, padding_y = padding

	# Calculate image size based on rectangle dimensions and no. of rows, columns
	new_width = (rect_width + padding_x) * columns - padding_x
	new_height = (rect_height + padding_y) * rows - padding_y

	# New image with white or transparent background
	if transparent:
		image = Image.new("RGBA", (new_width, new_height), color=(255, 255, 255, 0))
	else:
		image = Image.new("RGB", (new_width, new_height), color="white")

	# Draw blue rectangles on the white background
	draw = ImageDraw.Draw(image)
	for row in range(rows):
		for col in range(columns):
			x = col * (rect_width + padding_x)
			y = row * (rect_height + padding_y)
			draw.rectangle([x, y, (x + rect_width)-1, (y + rect_height)-1], fill=(0, 0, 255))
	return image

def copy_image_rows_columns(input_image_path, rows_columns, padding, transparent=False):
	# Open the input image, get rows and columns from the tuple
	original_image = Image.open(input_image_path)
	rows, columns = rows_columns
	padding_x, padding_y = padding

	# Calculate the new image size with padding
	new_width = (original_image.width + padding_x) * columns - padding_x
	new_height = (original_image.height + padding_y) * rows - padding_y

	# Create a new blank image with the calculated size
	if transparent:
		new_image = Image.new("RGBA", (new_width, new_height), color=(255, 255, 255, 0))
	else:
		new_image = Image.new("RGB", (new_width, new_height), color="white")

	# Paste the original image into the new image with padding
	for row in range(rows):
		for col in range(columns):
			x_offset = col * (original_image.width + padding_x)
			y_offset = row * (original_image.height + padding_y)
			new_image.paste(original_image, (x_offset, y_offset))

	return new_image

####################################################################################

if __name__ == "__main__":
	dimensions = (104, 71)
	rows_columns = (1, 12)
	padding = (16, 0)

	current_time = datetime.now().strftime("%H.%M.%S")

	result_image = generate_rectangles(dimensions, rows_columns, padding, True)
	result_image.save(f"output_image_{current_time}.png")

	# result_image = copy_image_rows_columns("aaa.png", rows_columns, padding, True)
	# result_image.save(f"output_image_{current_time}.png")




