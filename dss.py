from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS





##-------------------Key Generation ---------------------------##

key = ECC.generate(curve='P-256')

f = open('privkey.pem','w')
f.write(key.export_key(format='PEM'))
f.close()
f = open('pubkey.pem','w')
f.write(key.public_key().export_key(format='PEM'))
f.close()



message = b'I give my permission to order #4355'
key = ECC.import_key(open('privkey.pem').read())
h = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)


key = ECC.import_key(open('pubkey.pem').read())
h = SHA256.new(message)
verifier = DSS.new(key, 'fips-186-3')
try:
	verifier.verify(h, signature)
	print("The message is authentic.")
except ValueError:
	print("The message is not authentic.")
