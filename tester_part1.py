import sys
import traceback

import datetime

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''
		
class expect:
	
	def __init__(self,function,*args,**kwargs):
		self.function = function
		self.args = args
		self.kwargs = kwargs
		
	def to_be(self,value,args):
		
		try:
			result = self.function(*self.args,**self.kwargs)
			if result == value:
				print ok("Got the expected value of %s for %s(%s)"
								% (repr(value),self.function.func_name,args))
			else:
				print error("Expected %s(%s) to be %s, but it returned %s instead."
								% (self.function.func_name,args,repr(value),repr(result)))
		except:
			print error("Exception while calculating %s(%s)\n%s"
								% (self.function.func_name,args,traceback.format_exc()))
			

def format_args(args,kwargs):
	out = ','.join(str(arg) for arg in args)
	
	kwarg_pairs = []
	
	for kwarg in kwargs.items():
		kwarg_pairs.append("%s=%s" % (str(kw) for kw in kwarg) )
		
	if kwarg_pairs:
		out = out + ',' + ','.join(kwarg_pairs)
		
	return out
		

def error(message):
	return bcolors.FAIL + "ERROR: " + message + bcolors.ENDC
	
def header(message):
	return bcolors.OKBLUE + message + bcolors.ENDC
	
def ok(message=''):
	return bcolors.OKGREEN + "OK: " + message + bcolors.ENDC
	
	
print header("Starting test for part 1")
print
	
try:
	from Lab06_part1 import *
except ImportError:
	print error("No Lab06_part1 found. Use 'ls' to check if it is there")
	sys.exit(1)
except:
	print error("Exception in your Lab06_part1.py code:\n"+traceback.format_exc())
	sys.exit(1)
	
	
# so we have the file!
try:
	player_stats
except NameError:
	print error("player_stats is not defined - make sure that is what you call the data structure you create\n")
	quit(1)
	
	
#testing higest score
print
print header("Testing highest_score...")
try:
	expect(highest_score,player_stats).to_be( ('ronaldo',datetime.date(2012,6,20),3), 'player_stats' )
except NameError:
	print error("higest_score is not defined - make sure that you name the functions exactly as the instructions say")
	

#testing higest score
print
print header("Testing highest_score_for_player...")
try:
	expect(highest_score_for_player,player_stats,'ronaldo').to_be( 3, 'player_stats,"ronaldo"' )
	expect(highest_score_for_player,player_stats,'rooney').to_be( 2, 'player_stats,"rooney"' )
	expect(highest_score_for_player,player_stats,'torres').to_be( 1, 'player_stats,"torres"' )
except NameError:
	print error("highest_score_for_player is not defined - make sure that you name the functions exactly as the instructions say")


	
#testing higest scorer
print
print header("Testing highest_scorer..")
try:
	expect(highest_scorer,player_stats).to_be( 'rooney', 'player_stats' )
except NameError:
	print error("higest_scorer is not defined - make sure that you name the functions exactly as the instructions say")
	
	
	
