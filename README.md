# openssltool

run openssl via python

**installation:**
```bash
$ python3 -m pip install openssltool

```

**examples:**
```python
>>> from openssltool import sym

>>> # encryption
>>> sym.encrypt("test.txt", out_file="file1.enc", iter=34, passwd="secret", cipher="bf")

>>> # decryption
>>> sym.decrypt("file1.enc", out_file="file1.txt", iter=34, passwd="secret", cipher="bf")

>>> # list all cipher
>>> sym.CIPHERS

```
