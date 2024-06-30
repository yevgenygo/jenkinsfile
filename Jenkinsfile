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
		bat 'start /b python rest_app.py > output.log 2>&1'
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