def bob_key(alice_pp,bob_sk,p):
	return alice_pp**bob_sk%p

def alice_key(bob_pp,alice_sk,p):
	return bob_pp**alice_sk%p
	
	
def main():
	p = int(input("Enter the prime number: "))
	g = int(input("Enter the generator: "))
	alice_sk = int(input("Enter Alice Secret Key: "))
	bob_sk = int(input("Enter Bob secret Key: "))
	alice_pp = g**alice_sk%p
	bob_pp = g**bob_sk%p
	print("Bob Common Key :", bob_key(alice_pp,bob_sk,p))
	print("Alice Common Key : ", alice_key(bob_pp,alice_sk,p))
	
main()
