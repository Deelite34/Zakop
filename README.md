# Zakop
Work in progress excercise Django website based off popular Polish social website www.wykop.pl 

# installation
create virtual environment `python -m venv venv_zakop_app`  
launch virtual environment `.\venv_zakop_app\scripts\activate` (powershell command)  
Install required modules `pip install -r requirements.txt`  
Create database `python manage.py migrate`  
Run server `python manage.py runserver`

# Goals
✅ Design and implement models of sqlite database  
✅ Create skeleton of website, placebo buttons  
✅ Add colour scheme  
✅ Add basic account functionality, logging in and out, creating account  
🟩 CURRENTLY WIP: Add findings feature  
                  - Form can be used to add findings  
                  - Newest findings are shown on front page with their basic information   
                  - Commenting findings  
                  - Try to implement tags  
                  - Optional: Accept image for finding, resize/compress it then save it in the server  
🟩 Add mikroblog feature - blog where users can create posts, attach pictures to posts, respond to them, rate posts, tags  
🟩 Research and decide on deplaying website for everyone to be able to see the end result easily  
🟩 Optional: Learn javascript(possibly required javascript framworks too) and implement features that need it, for example rating posts, adding comments without refreshing page etc.  
🟩 Learn more about Django
                  



