from app import create_app, db
app = create_app(config_name="dev") # "dev", "test", "prod"

with app.app_context():
        print(f'App initialized with config: {app.config["SQLALCHEMY_DATABASE_URI"]=}')
        db.create_all() 

if __name__ == "__main__":    
    app.run()


 

