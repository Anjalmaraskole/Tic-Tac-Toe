pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Anjalmaraskole/Tic-Tac-Toe.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t anjali789/tic-tac:1 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop tic-tac || true'
                sh 'docker rm tic-tac || true'
                sh 'docker run -d --name tic-tac -p 5000:5000 anjali789/tic-tac:1'
            }
        }
    }
}
