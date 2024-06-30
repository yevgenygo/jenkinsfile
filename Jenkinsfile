pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				git 'https://github.com/yevgenygo/-Devops_Experts_Project_Part2'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}