from api import create_app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager
import click
from api.models import Products
app=create_app('production')
manager=Manager(app)
@app.cli.command('gendata')
@click.argument('size')
def gendata(size):
    Products.generatefake(size)
    
@app.shell_context_processor
def make_shell_context():
    return {'Products':Products}
manager.add_command('db',MigrateCommand)
manager.add_command('shell',shell_context=make_shell_context)

if __name__ == "__main__":
    manager.run()

