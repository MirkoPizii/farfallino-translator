"""This Python3 module let you to translate text into farfallino language.
"""
# Author: Mirko Pizii
# Email: info@mirkopizii.com
# Website: www.mirkopizii.com
# License: WTFPL


def is_vovel(letter):
    return letter.lower() in 'aeiouy'


def farfallino_transform(text):
    text_transformed = ''
    for char in text:
        text_transformed += '{}f{}'.format(char, char) if is_vovel(char) else char
    return text_transformed
