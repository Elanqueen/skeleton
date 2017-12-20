#coding=utf-8
class Lexicon:

    direction = ['north','south','east','west','down','up','right','back']
    verb = ['go','stop','kill','eat']
    stop=['the','in','of','from','at','it']
    noun = ['door','bear','princess','cabinet']

    def conver_number(self,s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(self,cls):
        result=[]
        words = cls.split(" ")
        for word in words:
            if word in self.direction:
                result.append(('direction', word))
            elif word in self.verb:
                result.append(('verb', word))
            elif word in self.stop:
                result.append(('stop', word))
            elif word in self.noun:
                result.append(('noun', word))
            elif self.conver_number(word)!=None:
                result.append(('number',int(word)))
            else:
                result.append(('error', word))
        return result

if __name__ == '__main__':
    sentence = "I would like 20 pieces of cakes!"
    lexicon=Lexicon()
    print(lexicon.scan(sentence))