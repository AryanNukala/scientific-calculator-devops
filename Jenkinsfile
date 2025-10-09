pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'aryannukala/scientific-calculator'
        DOCKER_TAG = 'latest'
        DOCKER_CREDENTIALS = 'dockerhub-credentials'
        RECIPIENT_EMAIL = 'aryan.nukala123@gmail.com'
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
            mail to: "${RECIPIENT_EMAIL}",
                 subject: "SUCCESS: Scientific Calculator Pipeline",
                 body: "Hi Aryan,\n\nThe Jenkins pipeline for Scientific Calculator has completed successfully.\n\nRegards,\nJenkins"
        }
        failure {
            echo 'Pipeline failed!'
            mail to: "${RECIPIENT_EMAIL}",
                 subject: "FAILURE: Scientific Calculator Pipeline",
                 body: "Hi Aryan,\n\nThe Jenkins pipeline for Scientific Calculator has failed. Please check the Jenkins console output for details.\n\nRegards,\nJenkins"
        }
    }
}
