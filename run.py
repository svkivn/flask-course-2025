from app import create_app
app = create_app(config_name="prod") # "dev", "test", "prod"

with app.app_context():
        print(f'App initialized with config: {app.config["SQLALCHEMY_DATABASE_URI"]=}, {app.config["SECRET_KEY"]=} ') 

if __name__ == "__main__":    
    app.run()


 

