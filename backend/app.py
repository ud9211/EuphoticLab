from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import eventlet

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dishes.db'
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

class Dish(db.Model):
    dishId = db.Column(db.Integer, primary_key=True)
    dishName = db.Column(db.String(100), nullable=False)
    imageUrl = db.Column(db.String(200), nullable=False)
    isPublished = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'dishId': self.dishId,
            'dishName': self.dishName,
            'imageUrl': self.imageUrl,
            'isPublished': self.isPublished
        }

@app.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.query.all()
    return jsonify([dish.to_dict() for dish in dishes])

@app.route('/toggle_publish/<int:dish_id>', methods=['POST'])
def toggle_publish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    dish.isPublished = not dish.isPublished
    db.session.commit()
    socketio.emit('update', dish.to_dict())
    return jsonify(dish.to_dict())

def initialize_database():
    with app.app_context():
        db.create_all()
        if not Dish.query.first():
            initial_data = [
                {"dishId": 1, "dishName": "Jeera Rice", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg", "isPublished": True},
                {"dishId": 2, "dishName": "Paneer Tikka", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg", "isPublished": True},
                {"dishId": 3, "dishName": "Rabdi", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg", "isPublished": True},
                {"dishId": 4, "dishName": "Chicken Biryani", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg", "isPublished": True},
                {"dishId": 5, "dishName": "Alfredo Pasta", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg", "isPublished": True}
            ]
            for dish_data in initial_data:
                dish = Dish(**dish_data)
                db.session.add(dish)
            db.session.commit()

if __name__ == '__main__':
    initialize_database()
    socketio.run(app, debug=True)
