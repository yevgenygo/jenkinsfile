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
			enviroment{
				db_cred = credentials('1')
				}
            steps {
                echo 'run backend..' 
		        echo "cred $1"
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