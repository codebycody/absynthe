from tests import *
from recon import *
import argparse

#print(headersCheck("nutanix.com"))
def main():
	return True

def reconActions(target):
	fingerPrinter(target)
	#dirbuster lite
	#dirb(target)
	return True

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Absynthe Pentesting Assistant")
	parser.add_argument('-o', '--output', help='Output path', default='./')
	parser.add_argument('-t', '--target', help='Target for Testing')
	args = parser.parse_args()
	
	if(args.target is not None):
		reconActions(args.target)
	#print(args.output)

