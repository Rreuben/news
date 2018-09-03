'''Module that contains startup configurations'''

from flask_script import Manager, Server
from app import create_app

# instances for the create_app
APP = create_app('development')

MANAGER = Manager(APP)
MANAGER.add_command('server', Server)

@MANAGER.command
def test():

    '''
    Run the unit test
    '''

    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    MANAGER.run()
