The code is about the "CAESAR CIPHER" the basic and the first cryptographic algorithm.The code given below is simple to understand for beginners and it looks like a long code but it is simple.Here is the sample code
  
  This is sample code for "Encryption".
    
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower().
    
   This is a good program for better understanding of working and implementation of "CAESAR CIPHER". 
   
   NOTE:This program is done in python(3.6.1) Version.
