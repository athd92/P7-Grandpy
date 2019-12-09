import controler.parser as script
import pytest


@pytest.fixture
def query():
    return {"message": "où se trouve la ville de dijon?"}

def test_display_question_entered_by_the_user(query):
    question = script.Parser(query)
    assert question.show_question() == {'message': 'où se trouve la ville de dijon?'}

def test_to_lower_and_no_accents(query):    
    question = script.Parser(query)
    assert question.to_lower_string() == 'ou se trouve la ville de dijon?'

def test_function_to_delete_stop_words(query):  
    question = script.Parser(query)        
    question.lowerStringQuestion = 'trouve ville dijon?'
    assert question.after_deleted_words() == 'trouve ville dijon?'

def test_extract_re_words_of_the_question(query):    
    question = script.Parser(query)
    question.lowerStringQuestion = 'trouve ville dijon?'
    result = question.extract_question()
    assert result == ['ville', 'dijon?']