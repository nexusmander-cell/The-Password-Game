import pyzipper

password = b"1234"

with pyzipper.AESZipFile("Example.zip", 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
    zipf.setpassword(password)
