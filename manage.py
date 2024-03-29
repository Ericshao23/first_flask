from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from first_flask_project import app
from  models import User

manager = Manager(app)

#使用Migrate绑定app和db
migrate =Migrate(app,db)

#添加迁移脚本的命令道manager中
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()