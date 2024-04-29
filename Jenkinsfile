// This file is for both dev and production to run together

pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'https://index.docker.io/v1/'  // Docker Hub or your private registry
        DOCKER_CREDENTIALS_ID = '00053d22-5629-427d-9452-b0e36f2f8b8d'  // Jenkins credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        // Devlopment

        stage('Copy .env') {
            steps {
                // Copy .env.prod in repository cloned directory
                sh 'cp /var/lib/jenkins/workspace/.env .'
            }
        }

        stage('Deploy to Devlopment') {
            steps {
                script {
                    // Add your deployment steps here
                    // This could be a Docker Compose deployment, Kubernetes deployment, or other mechanisms
                    // For Docker Compose:
                    sh 'docker compose up --build -d'
                }
            }
        }

        // Production

        stage('Copy .env.prod') {
            steps {
                // Copy .env.prod in repository cloned directory
                sh 'cp /var/lib/jenkins/workspace/.env.prod .'
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Add your deployment steps here
                    // This could be a Docker Compose deployment, Kubernetes deployment, or other mechanisms
                    // For Docker Compose:
                    sh 'docker compose -f docker-compose.prod.yaml up --build -d'
                }
            }
        }
    }

    post {
        // always {
        //     // Clean up resources
        //     cleanWs()  // Clean up the workspace
        // }

        success {
            echo "Pipeline executed successfully!"
        }

        failure {
            echo "Pipeline execution failed. Please check logs for details."
        }
    }
}