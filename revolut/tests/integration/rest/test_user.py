def test_register_user(client_with_db):
    data = {"username": "revolut", "password": "123"}
    response = client_with_db.post("/create-user", json=data)

    assert response.status_code == 201
    assert response.json["username"] == "revolut"


def test_update_user(client_with_db, auth):
    data = {"username": "admin", "password": "1234"}
    response = client_with_db.post("/update-user/1", json=data, headers=auth)
    assert response.json["username"] == "admin"


def test_delete_user(client_with_db, auth):
    response = client_with_db.get("/delete-user/1", headers=auth)
    assert response.json == "Deleted!!!!"


def test_list_user(client_with_db, auth):
    expected = [{"id": 2, "username": "revolut"}]
    response = client_with_db.get("/list-user", headers=auth)
    assert response.json == expected
