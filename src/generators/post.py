from src.baseclasses.builder import BuilderBaseClass
from faker import Faker

fake = Faker()


class PostBuilder(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_id(self, post_id=1):
        self.result['id'] = post_id
        return self

    def set_title(self, title=fake.text(max_nb_chars=100)):
        self.result['title'] = title
        return self

    def set_body(self, body=fake.text(max_nb_chars=300)):
        self.result['body'] = body
        return self

    def set_user_id(self, user_id=1):
        self.result['userId'] = user_id
        return self

    def delete(self, key):
        self.result.pop(key)
        return self

    def reset(self):
        self.set_id()
        self.set_title()
        self.set_body()
        self.set_user_id()

        return self
