from uuid_master import __version__


def test_happy_flow(client):
    initial_uuidmapping = {
        'frontend': 'frontend_id_1',
    }
    resp = client.post('/uuids', json=initial_uuidmapping)

    assert resp.status_code is 201
    assert 'Location' in resp.headers

    entity_loc = resp.headers['Location']
    resp = client.get(entity_loc)
    assert resp.status_code == 200
    assert resp.json == initial_uuidmapping

    uuidmapping_update = {
        'facturatie': 'facturatie_id_1'
    }
    resp = client.patch(entity_loc, json=uuidmapping_update)
    assert resp.status_code == 200

    updated_uuidmapping = {**initial_uuidmapping, **uuidmapping_update}
    resp = client.get(entity_loc)
    assert resp.status_code == 200
    assert resp.json == updated_uuidmapping

    uuidmapping_update2 = {
        'frontend': 'frontend_id_2',
        'facturatie': 'facturatie_id_1'
    }
    resp = client.patch(entity_loc, json=uuidmapping_update2)
    assert resp.status_code == 200

    updated_uuidmapping = uuidmapping_update2
    resp = client.get(entity_loc)
    assert resp.status_code == 200
    assert resp.json == updated_uuidmapping


def test_get_uuidmapping_404(client):
    resp = client.get('/uuids/non-existant')

    assert resp.status_code == 404
    assert resp.json == {
        'error': 'Not found'
    }


def test_post_uuidmapping_400(client):
    initial_uuidmapping = {
        'kassa': '123456',
        'fakeapp': '(°.°)'
    }

    resp = client.post('/uuids', json=initial_uuidmapping)

    assert resp.status_code == 400
    assert resp.json == {
        'error': 'Bad request'
    }


def test_patch_uuidmapping_404(client):
    uuidmapping_update = {
        'bestapp': '123456',
        'someotherapp': '(°.°)'
    }
    resp = client.patch('/uuids/non-existant', json=uuidmapping_update)

    assert resp.status_code == 404
    assert resp.json == {
        'error': 'Not found'
    }


def test_patch_uuidmapping_400(client):
    uuidmapping_update = {
        'kassa': '123456',
        'fakeapp': '(°.°)'
    }
    resp = client.patch('/uuids/non-existant', json=uuidmapping_update)

    assert resp.status_code == 400
    assert resp.json == {
        'error': 'Bad request'
    }