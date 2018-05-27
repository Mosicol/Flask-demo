
from flask_script import Manager
from flask_migrate_demo import app
from exts import db
import models   #这个一定要导入
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)   #把所有命令放到db里面

if __name__ == '__main__':
    manager.run()