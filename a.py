import ascii_magic
print('Cre by binhdev-simp')
output = ascii_magic.from_image_file("9.jpg",columns=100,char="*")
ascii_magic.to_terminal(output)