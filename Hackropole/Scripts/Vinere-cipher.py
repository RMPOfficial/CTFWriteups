def vc_decipher(ciphertext, key) -> str:
    result, kIdx = [], 0
    for i in ciphertext:
        if i.isalpha():
            CTbase = ord('A') if i.isupper() else ord('a');
            result.append(chr((ord(i) - (ord(key[kIdx].upper()) - ord('A')) - CTbase) % 26 + CTbase))
            kIdx = (kIdx + 1) % len(key)
        else: result.append(i)
    return "".join(result)
   
print(vc_decrypt("""Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.""", "FCSC"))