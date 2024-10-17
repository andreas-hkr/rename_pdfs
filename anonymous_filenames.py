import sys
from pathlib import Path
from random import randint


def generate_random_name(length, prefix):
    name = ''.join(f'{randint(0, 15):x}' for _ in range(length))        # Random hex string of length
    return f'{prefix}_{name}.pdf'


def main():
    length = 5
    prefix = 'Task'
    if len(sys.argv) == 2:                                              # User specifies length
        length = int(sys.argv[1])
    elif len(sys.argv) == 3:
        length = int(sys.argv[1])                                       # User specifies length and prefix
        prefix = sys.argv[2]
    else:
        print('Usage (3 options):')
        print('1) python3 anonymous_filenames.py')
        print('2) python3 anonymous_filenames.py <length>')
        print('3) python3 anonymous_filenames.py <length> <prefix>')
        print()
        exit(1)

    files = [file for file in Path('.').iterdir() if file.is_file()]    # Get all files in dir
    pdf_files = filter(lambda f: f.suffix.lower() == '.pdf', files)     # Keep only pdf files

    for file in pdf_files:
        file.rename(generate_random_name(length, prefix))


if __name__ == '__main__':
    main()
