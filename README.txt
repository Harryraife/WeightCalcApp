# flask-todo-example
A sample to-do list app using flask

## Usage

* in a linux machine run the code below.
sudo apt install python3 python3-pip python3-venv chromium-browser -y

*then to initalise the app run the following code 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report=html

* In order to register a lift you need to first create a user at /add-lifter
* once you've created a user you can add a lift at /add-lift
* in order to view all lifters go to /view-lifters
* in order to view all the lifts logged go to /view-lifts
* in order to change a users details go to /update-lifter/id where id is the id of the lifter you want to update
* in order to update a lift fo to /update-lift/id where id is the id of the lift you want to change
* to delete a lifter from the database go to /delete-lifter/id where id is the id of the lifter you want to delete
* to delete a lift logged go to /delete-lifte/id where id is the id of the lift you want to delete 