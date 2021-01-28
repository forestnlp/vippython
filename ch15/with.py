
with open('aaa','r') as f:
    print(f.read())


with open('logo.png','rb') as src:
    with open('logo3.png','wb') as target:
        target.write(src.read())