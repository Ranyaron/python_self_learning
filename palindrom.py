def reverse(text):
    text = text.replace(' ', '').replace('-', '').replace('!', '').lower()
    if text == text[::-1]:
        print('Palindrom')
    else:
        print('NO')


reverse('---А роза упала на лапу Азора!!!')
