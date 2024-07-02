pipeline {
    agent { label 'master' }

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
		        bat 'start /min python rest_app.py &'
		        bat 'start /min python web_app.py &'
		        bat 'start /min python backend_testing.py'
		        echo 'ttttttttttttttttttttt'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sleep 15
            }
        }
    }
}