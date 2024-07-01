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
		        sh 'nohup python3 rest_app.py &'
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