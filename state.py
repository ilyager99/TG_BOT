from aiogram.fsm.state import State, StatesGroup

class User(StatesGroup):
    name = State()  
    weight = State()  
    height = State()  
    age = State()  
    activity_level = State()  
    city = State()  
    calorie_goal = State()  
    logged_water = State() 
    logged_calories = State() 
    burned_calories = State() 

class Food(StatesGroup):
    product = State() 
    gram = State()

class Workout(StatesGroup):
    name_w = State() 
    time = State() 
    water_intake_w = State() 
