# Question - https://www.testdome.com/d/python-interview-questions/9
#===============================================================================
# Implement a group_by_owners function that:
# 
# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
#the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
#===============================================================================
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy',
    'newFile.txt':'Stan'
}
class Dictionary():
    
    @staticmethod
    def valueToKey(files):
        valueSet = set(files.values())
        newDictionary = {}
        newList = []
        for i in valueSet:    
            for k,v in files.items():
                if i == v:
                    newList.append(k)
            newDictionary[i] = newList
            newList = []
        return newDictionary    

print (Dictionary.valueToKey(files))
