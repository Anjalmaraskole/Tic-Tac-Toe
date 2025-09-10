pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Anjalmaraskole/Tic-Tac-Toe.git'  
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t anjali789/tic-tac:1 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 anjali789/tic-tac:1'
            }
        }
    }
}
