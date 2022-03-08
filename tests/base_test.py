"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/git_page">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker_page">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python_flask_page">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd_page">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

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
    assert b"Page 3" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/cicd_page")
    assert response.status_code == 200
    assert b"Page 4" in response.data
