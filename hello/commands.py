import click

from hello import app,db
from hello.models import Message
from faker import Faker
from faker.providers import BaseProvider
import random

fake=Faker()


@app.cli.command()
@click.option('--drop',is_flag=True,help='create after drop')
def initdb(drop):
    ''' initialize the database'''
    if drop:
        click.confirm('this operation will delete the database',abort=True)
        db.drop_all()
        click.echo('drop tables')
    db.create_all()
    click.echo('initialized database')
    
    
class Provider(BaseProvider):
    def age(self):
        return random.randint(20,30)
        
    def score(self):
        return random.randint(60,100)
        
fake.add_provider(Provider)
        

@app.cli.command()
@click.option('--count',default=20,help='message=20')
def forge(count):
    ''' generate fake messages'''
    db.drop_all()
    db.create_all()
    click.echo("working...")
    
    for i in range(count):
        message=Message(
        name=fake.name(),
        body=fake.sentence(),
        age=fake.age(),
        score=fake.score(),
        timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('created %d fake messages'%count)