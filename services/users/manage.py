
import unittest
from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

# Register a new cli command 'recreate_db'.
# Run unsing 'docker-compose -f docker-compose-dev.yml run users python manage.py recreate_db'
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# Register a new cli command 'test'
@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()



