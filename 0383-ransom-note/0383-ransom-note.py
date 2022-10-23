class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #take freq of char in ransomeNote dict
        ransom_dict={}
        for item in ransomNote:
            if(item in ransom_dict):
                ransom_dict[item] += 1
            else:
                ransom_dict[item] = 1
                
        #take freq of every char in magazine dict 
        magazine_dict={}
        for item in magazine:
            if(item in magazine_dict):
                magazine_dict[item] += 1
            else:
                magazine_dict[item] = 1
                
        #checking the exist or not       
        for key,value in ransom_dict.items():
            if key in magazine_dict.keys() and value<=magazine_dict[key]:
                continue
            else:
                return False
            
        return True