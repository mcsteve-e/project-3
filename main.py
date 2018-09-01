'''
        Author:  McSteve Ezikeoha
        Title:   Hashmap
        Date:    May 10, 2018
'''

from Associator import *
import traceback

def help():
	print("quit")
	print("help")
	print("print")
	print("clear")
	print("debug")
	print("stats")
	print("dump")
	print("hash KEY")
	print("put KEY=VALUE")
	print("get KEY")
	print("del KEY")
	print("find VALUE")
	print("find overflow KEY")
	print("find empty")
	print("xfile FILENAME      -- run commands from this file")
	print("?python command")


def execute(command):
	try:
		if command.startswith("xfile "):
			execute_from_file(command[6:])
		elif command[0] == "#":
			print(command)
		elif command == "print":
			a.print()
		elif command == "clear":
			a.clear()
		elif command.startswith("hash "):
			word = command[5:]
			print(word, a._hash(word), a._rehash(word))
		elif command == "debug":
			a.debug()  # turn on debugging
		elif command == "stats":
			print(a.stats())
		elif command == "dump":
			print(a.dump())
		elif command == "dump to file":
			filename = input("Enter filename: ")
			with open(filename,"w") as f:
				f.write(a.dump())
			f.close()
		elif command.startswith("put "):
			temp = command[4:]
			if "=" in temp:
				temp = command[4:].split("=")
				key=temp[0];  value = temp[1]
				a.put(key,value)
			else:
				print("Illegal put command!  Needs to look like\n     put key=value")
		elif command.startswith("get "):
			key = command[4:]
			if a.exists(key):
				print("   ..." + a.get(key))
			else:
				print("This key is not in the Associator")
		elif command.startswith("del "):
			key = command[4:]
			if a.exists(key):
				print("   ..." + a.get(key)+" deleted!")
				a.delete(key)
			else:
				print("This key is not in the Associator")
		elif command.startswith("find "):
			print(a.find(command[5:]))
		elif command.startswith("find overflow "):
			print(a._find_ovflow(command[14:]))
		elif command == "find empty":
			print(a._find_empty(command[10:]))
		elif command[0] == "?":
			print(eval(command[1:]))
		else:
			print("Unknown command; try help")
		
	except Exception as e:
		tb = traceback.format_exc()
		print("Caught a run-time error and recovered from it.")
		print(e.__class__.__name__, end=", ")
		print(e)
		print(tb)

def execute_from_file(filename):
	with open(filename) as f:
		contents = f.read()
		for line in contents.split("\n"):
			execute(contents)

def main():
	global a
	a =  Associator(10)
	while True:
		command = input("> ")
		if command == "": continue
		if command == "quit" or command == "q":
			break
		if command == "help" or command == "?":
			help()
		else:
			execute(command)

main()
