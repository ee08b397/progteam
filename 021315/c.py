#!/usr/local/bin

# A new e-mail service "Berlandesk" is going to be opened in Berland in the near future. The site administration wants to launch their project as soon as possible, that's why they ask you to help. You're suggested to implement the prototype of site registration system. The system should work on the following principle.
# Each time a new user wants to register, he sends to the system a request with his name. If such a name does not exist in the system database, it is inserted into the database, and the user gets the response OK, confirming the successful registration. If the name already exists in the system database, the system makes up a new user name, sends it to the user as a prompt and also inserts the prompt into the database. The new name is formed by the following rule. Numbers, starting with 1, are appended one after another to name (name1, name2, ...), among these numbers the least i is found so that namei does not yet exist in the database.

import sys

if __name__ == "__main__":

	db = {}
	N = int(sys.stdin.readline())
	for i in range(N):
		s = sys.stdin.readline().strip()
		if db.get(s) == None:
			db[s] = 0
			print "OK"
		else:
			db[s] += 1
			print s + str(db[s])
