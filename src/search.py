import sqlite3

class TrieNode(): 
	def __init__(self): 
		
		self.children = {} 
		self.last = False

class Trie(): 
	def __init__(self): 

		self.root = TrieNode() 
		self.word_list = [] 

	def formTrie(self, keys): 

		for key in keys: 
			self.insert(key) # inserting one key to the trie. 

	def insert(self, key): 
	
		node = self.root 

		for a in list(key): 
			if not node.children.get(a): 
				node.children[a] = TrieNode() 

			node = node.children[a] 

		node.last = True

	def search(self, key): 
		 
		node = self.root 
		found = True

		for a in list(key): 
			if not node.children.get(a): 
				found = False
				break

			node = node.children[a] 

		return node and node.last and found 

	def suggestionsRec(self, node, word): 
	
		if node.last: 
			self.word_list.append(word) 

		for a,n in node.children.items(): 
			self.suggestionsRec(n, word + a) 

	def printAutoSuggestions(self, key): 
		
	
		not_found = False
		temp_word = '' 

		for a in list(key): 
			if not node.children.get(a):
				not_found = True
				break

			temp_word += a 
			node = node.children[a] 

		if not_found: 
			return 0
		elif node.last and not node.children: 
			return -1

		self.suggestionsRec(node, temp_word) 

		for s in self.word_list: 
			print(s) 
		return 1




# Driver Code 


sqlite3.connect('abc') 
con = sqlite3.connect('abc.db') # database file input
cur = con.cursor()


query="select username from user order by username"

cur.execute(query)
result=cur.fetchall()

keys = []


for r in result:
	keys.append(r[0])

	# print(r)

print("----------------------------------------------")
print(keys[0:5])

 # keys to form the trie structure.



status = ["Not found", "Found"] 

# creating trie object 
t = Trie() 

# creating the trie structure with the 
# given set of strings. 
t.formTrie(keys) 

# autocompleting the given key using
# our trie structure. 
key = input("enter string: ")
comp = t.printAutoSuggestions(key) 

if comp == -1: 
	print("No other strings found with this prefix\n") 
elif comp == 0: 
	print("No string found with this prefix\n") 

# This code is contributed by amurdia 
