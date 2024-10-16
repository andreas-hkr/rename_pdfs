import sys
from pathlib import Path
from random import randint


def generate_random_name(length):
    name = ''.join(f'{randint(0, 15):x}' for _ in range(length))        # Random hex string of length
    return f'Task_{name}.pdf'


def main():
    if len(sys.argv) == 1:                                              # Use default length of 5 characters
        length = 5
    elif len(sys.argv) == 2:                                            # Use user specified length
        length = int(sys.argv[1])
    else:
        print('Usage (2 options):')
        print('1) python3 anonymous_filenames.py')
        print('2) python3 anonymous_filenames.py <length>')
        print()
        exit(1)

    files = [file for file in Path('.').iterdir() if file.is_file()]    # Get all files in dir
    pdf_files = filter(lambda f: f.suffix.lower() == '.pdf', files)     # Keep only pdf files

    for file in pdf_files:
        file.rename(generate_random_name(length))


if __name__ == '__main__':
    main()
