pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
				git 'https://github.com/yevgenygo/jenkinsfile'
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