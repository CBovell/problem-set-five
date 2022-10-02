
def addend(list, dict, value):
	dict[value] = ''
	list.append(value)
	
def removestart(list,dict):
	if len(list) == 0:
		return None

	dict.pop(list.pop(0))	
	return list.pop(0)
	
def containslinear(list, value):
	return value in list

def containshash(dict,value):
	return value in dict
