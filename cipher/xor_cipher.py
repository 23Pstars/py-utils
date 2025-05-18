import os

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

key = 7
current_script = os.path.basename(__file__)
output_dir = "encoded"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir('.'):
    if not os.path.isfile(filename):
        continue
    if filename == current_script:
        continue
    # Read original data from file
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    # Encrypt and write to file in 'encoded' directory with the same filename
    encrypted = xor_cipher(data, key).encode().hex()
    enc_filename = os.path.join(output_dir, filename)
    with open(enc_filename, 'w', encoding='utf-8') as f:
        f.write(encrypted)
    print(f"Encoded {filename} -> {enc_filename}")
