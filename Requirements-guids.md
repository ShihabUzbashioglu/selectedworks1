📄 INSTALLATION_GUIDE.md

# 📦 Installation & Environment Setup Guide Welcome to **all-of-my-projects** – a mega collection of diverse and experimental software projects written in various languages and built using different frameworks and technologies. This guide will help you set up your environment correctly and avoid common issues that may occur when trying to run these projects. --- ## 🧰 General Requirements Depending on the project, you may need to install: - Python (3.7+) - Node.js & npm/yarn - Java (8/11/17) - PHP (with Composer) - Ruby (with Bundler) - .NET SDK (Core or Framework) - Docker & Docker Compose - C/C++ Compiler (gcc/clang) - Make / CMake / Meson / Ninja - Git - SQLite / MySQL / PostgreSQL - Android Studio / Xcode - Other tools depending on the specific technology You can install some of these using: ### Ubuntu/Debian-based Systems: ```bash sudo apt update sudo apt install -y python3 python3-pip nodejs npm git php composer ruby-full openjdk-17-jdk build-essential curl sqlite3 

Arch Linux:

sudo pacman -Syu python nodejs npm git php composer ruby jdk-openjdk base-devel sqlite 

MacOS (with Homebrew):

brew install python node git php composer ruby openjdk sqlite 

📦 Python Dependencies

If a project contains a requirements.txt or pyproject.toml, you can run:

pip install -r requirements.txt # OR pip install poetry && poetry install 

⚠️ Some Python projects may also require virtualenv or venv. You can create and activate an isolated environment:

python3 -m venv venv source venv/bin/activate 

🌐 Node.js / JavaScript Projects

If there's a package.json, run:

npm install # OR yarn install 

To run:

npm start # OR npm run dev 

Some projects may use TypeScript, so ensure you have:

npm install -g typescript 

☕ Java Projects

If you find pom.xml (Maven):

mvn clean install 

If you find build.gradle (Gradle):

./gradlew build 

🐘 PHP Projects

If a project has composer.json:

composer install 

🐳 Dockerized Projects

If there's a Dockerfile or docker-compose.yml, run:

docker-compose up --build # OR docker build -t project-name . docker run project-name 

Make sure Docker is running.

⚠️ Common Issues

Missing library: Run the install command again.

Port already in use: Check and kill the process using that port (lsof -i :PORT).

Permission denied: Try chmod +x script.sh or run with sudo.

Module not found: Reinstall dependencies or check PYTHONPATH, NODE_PATH, etc.

Path too long (Windows): Use Git Bash or WSL.

💡 Pro Tips

Use VSCode with proper extensions for each language.

Install Docker Desktop for containerized environments.

Use .env.example files to configure your environment.

🤝 Need Help?

If you encounter issues or want to discuss improvements or collaboration ideas, feel free to contact me at:

📧 shihabuzbashioglu@gmail.com

🧠 Reminder

These projects were made over years of learning and experimentation. Many can be taken as a foundation for more powerful and production-ready tools. Your feedback and contributions are most welcome!

✅ Happy Hacking!