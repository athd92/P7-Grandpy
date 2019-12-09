from wordlist import stopWords
from stop_words import get_stop_words
import unidecode
import re
import string


class Parser():
    """
    Class used to instance the entire question in a string
    """
    def __init__(self, question):
        self.question = question  # json 
        self.lowerQuestionClean = ''
        self.lowerQuestionWithoutWords = ''
    
    def show_question(self):
        '''Method used to cdisplay the string question '''
        return self.question
            
    def to_lower_string(self):
        '''Method used to convert in lower case the question'''
        self.question = self.question['message'].lower()        
        self.lowerStringQuestion = unidecode.unidecode(self.question) #unicode for special chars   
        return self.lowerStringQuestion
    
    def after_deleted_words(self):
        '''Method used to delete stop words'''
        liste = []
        tempList = self.lowerStringQuestion.split(' ')        
        stop_words = get_stop_words('french')
        for i in tempList:
            if i not in stop_words:
                liste.append(i)
        self.lowerQuestionWithoutWords = ' '.join(liste) 
        return self.lowerQuestionWithoutWords

    def extract_question(self):
        '''Method used to extract the name of the city'''
        finalString = []
        badWords = []
        query = self.after_deleted_words()  
        liste = re.findall(r'\bcherch[a-zA-Z]*|\blocal[a-zA-Z]*|\bsitu[a-zA-Z]*|\badress[a-zA-Z]*|\btrouve[a-zA-Z]*', query)
        
        for i in liste:
            badWords.append(i)
        query = query.split(' ')
        
        for i in query:
            if i not in badWords:
                finalString.append(i)
        return finalString
        

        
        
                

      




        




        

    


