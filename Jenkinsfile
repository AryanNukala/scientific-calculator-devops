pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'aryannukala/scientific-calculator'
        DOCKER_TAG = 'latest'
        DOCKER_CREDENTIALS = 'dockerhub-credentials'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest test_calculator.py -v'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS) {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }
        
        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying application using Ansible...'
                ansiblePlaybook(
                    playbook: 'deploy-playbook.yml',
                    inventory: 'inventory.ini',
                    colorized: true
                )
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
