pipeline {
    agent any

    stages {
        stage('clone the code') {
            steps {
                echo 'cloning web server code..'
		git 'https://github.com/yevgenygo/-Devops_Experts_Project_Part2'
            }
        }
        stage('run backend') {
            steps {
                echo 'run backend..'

		bat 'python --version'
		bat 'dir' 
		bat 'start /b python rest_app.py'
		echo 'ttttttttttttttttttttt'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}