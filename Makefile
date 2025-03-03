.PHONY: install

install:
	@echo "Installing required Python libraries..."
	@pip3 install matplotlib --break-system-packages
	@pip3 install numpy --break-system-packages
	@pip3 install tk --break-system-packages
	@echo "Installation complete!"

#Installation for required libraries in Raspberry pi	