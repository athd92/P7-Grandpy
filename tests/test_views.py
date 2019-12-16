import pytest
from main import app

@pytest.fixture(scope='session')
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_home_page_view(client):

    response = client.get('/')
    assert response.status == '200 OK'
    html = response.get_data(as_text=True)
    message = "Grandpy"
    assert message in html


def test_error_page_view(client):
    
    response = client.get('/wrong-way')
    assert response.status == "404 NOT FOUND"
    html = response.get_data(as_text=True)
    message = "La page que vous cherchiez n'existe pas ou n'est plus accessible"
    assert message in html


