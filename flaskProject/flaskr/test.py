from flask import current_app

def test1():
    with open('schema.sql') as f:
        pass
    # with current_app.open_resource('schema.sql') as f:
    #     pass


if __name__ == '__main__':
    test1()