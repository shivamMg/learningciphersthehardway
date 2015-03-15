#!usr/bin/python3

# The script creates a paragraph of cipher text
# with a heading and with required markdown
# formatting

import random

Letters = 'abcdefghijkl mnopqrs tuvwxyz ABCDEFGH IJKLMNOPQRSTUVWXY Z1234567 890!!'
filepath = '../README.md'

def generate_cipher_text(length):
    cipher_text = str()
    for _ in range(0, length):
        cipher_text += random.choice(Letters)
    return cipher_text

if __name__ == '__main__':
    required_length = int(input('Length of text(min420 max2345): '))

    if required_length < 420 or required_length > 2346:
        print('Length of paragraph must be greater than 419 and less than 2346')
        print('Please try again')
    else:
        file_pointer = open(filepath, 'a')

        Heading = generate_cipher_text(required_length % 23)
        Paragraph = generate_cipher_text(required_length)

        # Create heading
        file_pointer.write('\n')
        file_pointer.write('### ' + Heading)
        file_pointer.write('\n\n')

        # Create paragraph of required length
        i = 1
        while i <= required_length:
            if i % 80 == 0:
                file_pointer.write('\n')
            else:
                file_pointer.write(Paragraph[i-1])
            i += 1

        file_pointer.write('\n')
        file_pointer.close()

        print("Paragraph entered successfully")
