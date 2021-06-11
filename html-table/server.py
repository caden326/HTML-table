from flask import Flask, render_template 
app = Flask(__name__)    


@app.route('/')          
def index():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    users
    return render_template('index.html', users = users )
    # for index in range(len(users)):
    #     for key in users[index]:
    #         return (users[index][key])


if __name__=="__main__":   
        app.run(debug=True)    
