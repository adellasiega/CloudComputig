import os
import random
from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth

class NextcloudUser(HttpUser):
    auth = None
    user_name = None
    wait_time = between(2, 5)
    counter = 0

    # users to test this with.
    def on_start(self):
        user_idx = random.randrange(0, 30)
        self.user_name = f'locust_user{user_idx}'
        self.auth = HTTPBasicAuth(self.user_name, 'test_password1234!')

    @task
    def propfind(self):
        self.client.request("PROPFIND", f"/remote.php/dav/files/{self.user_name}/", auth=self.auth)

    @task
    def upload_big(self):
        filename = "file_1gb"
        with open('/data/' + filename, 'rb') as f:
            response = self.client.put("/remote.php/dav/files/" + self.user_name + "/" + filename,
                                       auth=self.auth, data=f, name=f"/remote.php/dav/files/{self.user_name}/file_1gb")

        if response.status_code != 201 and response.status_code != 204 :
            with open("output.txt", "a") as f:
                f.write(f"Error during PUT request: {response.status_code} for user {self.user_name}.\n")
            return

        for i in range(0, 5):
            self.client.get("/remote.php/dav/files/" + self.user_name + "/" + filename,
                            auth=self.auth, name=f"/remote.php/dav/files/{self.user_name}/file_1gb")

        self.client.delete("/remote.php/dav/files/" + self.user_name + "/" + filename,
                           auth=self.auth, name=f"/remote.php/dav/files/{self.user_name}/file_1gb")






