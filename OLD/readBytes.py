import sys

def read_bytes_and_print_hex(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_content = file.read()
            hex_output = byte_content.hex()
            print(hex_output)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python readBytes.py <file_path>")
    else:
        file_path = sys.argv[1]
        read_bytes_and_print_hex(file_path)