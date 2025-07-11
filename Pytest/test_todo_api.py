import requests
import uuid

ENDPOINT = "https://todo.pixegami.io/"
#Endpoint information: https://todo.pixegami.io/docs

response = requests.get(ENDPOINT)
print(response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload = { 
        'content': 'my test content',
        'user_id': 'test_user',
        'task_id': 'test_task_id',
        'is_done': False,
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200

    data = response.json()
    print(data)

    task_id = data['task']['task_id']
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")

    assert get_task_response.status_code == 200
    task_data = get_task_response.json()
    assert task_data['content'] == payload['content']
    assert task_data['user_id'] == payload['user_id']


def test_can_update_task():
    payload = new_task_payload()

    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    new_payload = { 
        'content': 'my updated content',
        'user_id': payload['user_id'],
        'task_id': task_id,
        'is_done': True,
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()

    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']

def test_can_list_tasks():
    #create N tasks
    N = 3

    payload = new_task_payload()

    for _ in range(N):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload['user_id']
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()

    tasks = data['tasks']
    assert len(tasks) == N
    print(data)

def test_can_delete_task():
    #cretae task
    #delete task
    #get task with error
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
    

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f'test_user_{uuid.uuid4().hex}'
    return { 
        'content': 'my test content',
        'user_id': user_id,
        'is_done': False,
    }