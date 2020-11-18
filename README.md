# PythonGUI-FirebaseRealtimeDatabase
In this we Insert, Update, Delete and search the records that are present in Firebase. Also we are representing the data in Treeview (Table format) in GUI

# Firebase Realtime Database

First Make database in Firebase (Realtime Database).
change the rules for your requirement. In My case I have given Read and Write permission to True(Not suitable for production) I have selected this for Test.

# Required modules that needed 
pip install requests   
pip install python-firebase

for more details visit  https://pypi.org/project/python-firebase/

# Note

When you run this Line -> from firebase import firebase  
you will face runtime error related to filename async.py
Solution for this rename the file in firebase module folder to anyname in my case I have rename this to async.py to asyncn.py in firebase folder, Also do changes in firebase.py, __init__.py inside it.

We used some basic methods to Insert, Update, Delete and search the Data that are present in Firebase.

Notes are there in Code, Incase any help or suggestion please connect with me here

Thank you !
