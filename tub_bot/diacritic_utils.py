def replace_diacritics(text):
        text = text.replace('ā','a')
        text = text.replace('Ā','A')
        text = text.replace('ī','i')
        text = text.replace('Ī','I')
        text = text.replace('Ṣ','S')
        text = text.replace('ṣ','s')
        text = text.replace('ū','u')
        text = text.replace('Ū','U')
        text = text.replace('ẓ','z')
        text = text.replace('Ẓ','Z')
        text = text.replace('Ṭ','T')
        text = text.replace('ṭ','t')
        text = text.replace('ʿ','')
        text = text.replace('ʾ','')
        return text