⚙️ Common Requirements & Setup Guide

This document helps you install the essential tools and libraries required to run most of the projects in this repository. Each project may need specific packages depending on its purpose (web, AI, hardware, etc.). Below is a general guideline.

🐍 Python Packages

Install packages using pip:

pip install package-name 

Most used packages:

flask – Web server and APIs
→ pip install flask

requests – HTTP requests
→ pip install requests

beautifulsoup4 – Web scraping
→ pip install beautifulsoup4

pandas – Data analysis
→ pip install pandas

numpy – Scientific computation
→ pip install numpy

matplotlib – Data visualization
→ pip install matplotlib

opencv-python – Image processing
→ pip install opencv-python

scikit-learn – Machine learning
→ pip install scikit-learn

tensorflow or torch – Deep learning
→ pip install tensorflow or pip install torch

pygame – Simple games
→ pip install pygame

🧰 Other Useful Tools

Python virtual environment
Create isolated environments for each project:

python -m venv env source env/bin/activate # On Windows use: env\Scripts\activate 

Jupyter Notebook
→ pip install notebook

Run using:

jupyter notebook 

🌐 Node.js Projects

For JavaScript-based projects (web apps, APIs):

Install dependencies:

npm install 

Run project:

npm start 

Make sure Node.js is installed.
Download: https://nodejs.org

🔧 Compilation and CLI Tools

For C/C++ or Linux-based scripts, you may need:

gcc – For compiling C/C++

make – For running Makefiles

bash – For shell scripts

git – Version control

Install them using:

sudo apt install build-essential git 

🐘 Database Tools

Some projects use databases. Common ones:

SQLite (built-in with Python via sqlite3)

MySQL → pip install mysql-connector-python

PostgreSQL → pip install psycopg2

❗ Troubleshooting Tips

If a project doesn’t work:

Make sure required libraries are installed.

Check for missing files like .env, .db, or data folders.

Make sure you are using the right Python version (python3.10+ is usually safe).

Some projects need admin privileges or external hardware.

Use a virtual environment to avoid conflicts.

📬 Questions?

If something doesn't work or you want help understanding a project, feel free to contact me:

📧 shihabuzbashioglu@gmail.com


🔗 8. Resources

Python Official Docs

Real Python Tutorials

PyPI - Python Package Index

Docker Docs

Flask Docs

Django Docs