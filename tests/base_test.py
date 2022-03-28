"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git_page">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker_page">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python_flask_page">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd_page">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/pylint_others">Article1</a>' in response.data
    assert b'<a class="nav-link" href="/overview_solid">Article2</a>' in response.data
    assert b'<a class="nav-link" href="/oops_terms">Article3</a>' in response.data
    assert b'<a class="nav-link" href="/aaa_testing">Article4</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/git_page")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/docker_page")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/python_flask_page")
    assert response.status_code == 200
    assert b"Python Flask" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/cicd_page")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_article1(client):
    """This makes the index page"""
    response = client.get("/pylint_others")
    assert response.status_code == 200
    assert b"Pylint & Others" in response.data

def test_request_article2(client):
    """This makes the index page"""
    response = client.get("/overview_solid")
    assert response.status_code == 200
    assert b"SOLID Principles & Design Pattern" in response.data

def test_request_article3(client):
    """This makes the index page"""
    response = client.get("/oops_terms")
    assert response.status_code == 200
    assert b"Object Oriented Programming (OOP) Terms in Python:" in response.data

def test_request_article4(client):
    """This makes the index page"""
    response = client.get("/aaa_testing")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data