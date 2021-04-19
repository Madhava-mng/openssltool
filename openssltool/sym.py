# os 	: linux, mac
# need  : openssl tool installed

from subprocess import run as _run
from os import system as _system
from time import strftime as _strftime
from os.path import isfile as _isfile


CIPHERS = [
	"aes-128-cbc",
	"aes-128-ecb",
	"aes-192-cbc",
	"aes-192-ecb",
	"aes-256-cbc",
	"aes-256-ecb",
	"aria-128-cbc",
	"aria-128-cfb",
	"aria-128-cfb1",
	"aria-128-cfb8",
	"aria-128-ctr",
	"aria-128-ecb",
	"aria-128-ofb",
	"aria-192-cbc",
	"aria-192-cfb",
	"aria-192-cfb1",
	"aria-192-cfb8",
	"aria-192-ctr",
	"aria-192-ecb",
	"aria-192-ofb",
	"aria-256-cbc",
	"aria-256-cfb",
	"aria-256-cfb1",
	"aria-256-cfb8",
	"aria-256-ctr",
	"aria-256-ecb",
	"aria-256-ofb",
	"base64",
	"bf",
	"bf-cbc",
	"bf-cfb",
	"bf-ecb",
	"bf-ofb",
	"camellia-128-cbc",
	"camellia-128-ecb",
	"camellia-192-cbc",
	"camellia-192-ecb",
	"camellia-256-cbc",
	"camellia-256-ecb",
	"cast",
	"cast-cbc",
	"cast5-cbc",
	"cast5-cfb",
	"cast5-ecb",
	"cast5-ofb",
	"des",
	"des-cbc",
	"des-cfb",
	"des-ecb",
	"des-ede",
	"des-ede-cbc",
	"des-ede-cfb",
	"des-ede-ofb",
	"des-ede3",
	"des-ede3-cbc",
	"des-ede3-cfb",
	"des-ede3-ofb",
	"des-ofb",
	"des3",
	"desx",
	"rc2",
	"rc2-40-cbc",
	"rc2-64-cbc",
	"rc2-cbc",
	"rc2-cfb",
	"rc2-ecb",
	"rc2-ofb",
	"rc4",
	"rc4-40",
	"seed",
	"seed-cbc",
	"seed-cfb",
	"seed-ecb",
	"seed-ofb",
	"sm4-cbc",
	"sm4-cfb"
]


def encrypt(in_file , passwd='' , cipher = 'seed', iter=0, out_file = _strftime('enc_%y%m%d_%H%M%S'), pbkdf2=False, b64=False):

	# eliminate

	if(not _isfile(in_file)):
		return {"status":"negative", "error": f"file not found: {in_file}"}

	if(not str(iter).isdigit() and not iter >= 0):
		return {"status":"negative", "error":"Iter: Invalied Itration"}

	if(cipher not in CIPHERS):
		return {"status":"negative", "error":"Cipher: Invalied Cipher"}

	if(len(out_file) == 0):
		return {"status":"negative", "error":"OutFile: Nofile given"}

	
	# Proceed

	const_string = f'openssl {cipher} -in {in_file} -out {out_file} -k "{passwd}"'

	if(iter > 0):
		const_string += f' -iter {str(iter)}'
	
	if(pbkdf2):
		const_string += ' -pbkdf2'

	if(b64):
		const_string += ' -a'


	# exec

	_system(const_string)

	return {
	"status":"positive",
	"cipher":cipher,
	"in_file":in_file,
	"out_file":out_file,
	"iter": iter,
	"passwd": "*"*len(passwd),
	"pbkdf2": pbkdf2,
	"base64": b64
	}



def decrypt(in_file , passwd='' , cipher = 'seed', iter=0, out_file = _strftime('dec_%y%m%d_%H%M%S'), pbkdf2=False, b64=False):

	# eliminate

	if(not _isfile(in_file)):
		return {"status":"negative", "error": f"file not found: {in_file}"}

	if(not str(iter).isdigit() and not iter >= 0):
		return {"status":"negative", "error":"Iter: Invalied Itration"}

	if(cipher not in CIPHERS):
		return {"status":"negative", "error":"Cipher: Invalied Cipher"}

	if(len(out_file) == 0):
		return {"status":"negative", "error":"OutFile: Nofile given"}
	# Proceed

	const_string = f'openssl {cipher} -d -in {in_file} -out {out_file} -k "{passwd}"'

	if(iter > 0):
		const_string += f' -iter {str(iter)}'
	
	if(pbkdf2):
		const_string += ' -pbkdf2'

	if(b64):
		const_string += ' -a'


	# exec

	_system(const_string)

	return {
	"status":"positive",
	"cipher":cipher,
	"in_file":in_file,
	"out_file":out_file,
	"iter": iter,
	"passwd": "*"*len(passwd),
	"pbkdf2": pbkdf2,
	"base64": b64
	}

