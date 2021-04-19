__doc__ = """openssl utils

Symmetric encryption
--------------------

	encrypt:
	-------
	
		parameter:
		---------
		in_file   	: input file  (plain text file)
		out_file	: output file (to save encrypt data)
		passwd		: password for encryption (default: "")
		cipher		: cipher name (default: "seed")
		iter		: Number Itration (default: 0)
		pbkdf2		: Use password-based key derivation (default: False)
		b64			: base64 output (default: False)
	
		>>> encrypt(in_file, **kwargs)
	
	
	decrypt:
	-------
	
		parameter:
		---------
		in_file   	: input file  (encrypted file)
		out_file	: output file (to save decrypted data)
		passwd		: password for decryption (default: "")
		cipher		: cipher name (default: "seed")
		iter		: Number Itration (default: 0)
		pbkdf2		: Use password-based key derivation (default: False)
		b64			: base64 input (default: False)
	
		>>> decrypt(in_file, **kwargs)
	
	list cipher:
	-----------
	
		ciphers.cipher_list		(type: list)



Asymmetric encryption:
---------------------
	
	# comming soon
"""

from openssltool import sym