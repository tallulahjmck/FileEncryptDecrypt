from cryptography.fernet import Fernet # import cryptography module
## Fernet is authenticated cryptography which doesn’t allow to read and/or modify the file without a “key”

#create the key and save it in the same folder as our data file
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)#displays the key, should be the same if you open with text editor

### encryting the file ###

f = Fernet(key)# initialise the Fernet object as store is as a local variable f

with open('grades.csv', 'rb') as original_file: #We read our original data (grades.csv file) into original
    original = original_file.read()

encrypted = f.encrypt(original) #We encrypt the data using the Fernet object and store it as encrypted

with open ('enc_grades.csv', 'wb') as encrypted_file: #write it into a new .csv file called “enc_grades.csv”
    encrypted_file.write(encrypted)

### decrypting the file ###

f = Fernet(key)# initialise the Fernet object as store is as a local variable f

with open('enc_grades.csv', 'rb') as encrypted_file: #we read our encrypted data (enc_grades.csv file) into encrypted
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted) # decrypt the data using the Fernet object and store it as decrypted

with open('dec_grades.csv', 'wb') as decrypted_file: #we write it into a new .csv file called “dec_grades.csv”
    decrypted_file.write(decrypted)
