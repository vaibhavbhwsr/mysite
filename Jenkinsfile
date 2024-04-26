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

        // stage('Build Dev Image') {
        //     steps {
        //         script {
        //             docker.withRegistry(DOCKER_REGISTRY, DOCKER_CREDENTIALS_ID) {  // Ensure DOCKER_CREDENTIALS_ID is set up in Jenkins
        //                 def image = docker.build(DEV_IMAGE, '-f ./mysite/Dockerfile.dev .')
        //                 // image.push()  // Push the dev image to the registry
        //             }
        //         }
        //     }
        // }

        // // stage('Test') {
        // //     steps {
        // //         script {
        // //             def container = docker.run(DEV_IMAGE, 'python manage.py test')
        // //             def result = container.waitFor(120)  // Set an appropriate timeout
        // //             container.logs()
        // //             if (result != 0) {
        // //                 error("Tests failed")
        // //             }
        // //         }
        // //     }
        // // }

        // stage('Build Prod Image') {
        //     steps {
        //         script {
        //             docker.withRegistry(DOCKER_REGISTRY, DOCKER_CREDENTIALS_ID) {
        //                 def image = docker.build(PROD_IMAGE, '-f ./mysite/Dockerfile.prod .')
        //                 // image.push()  // Push the prod image to the registry
        //             }
        //         }
        //     }
        // }
        stage('Copy .env.prod') {
            steps {
                // Copy .env.prod in repository cloned directory
                sh 'cat /home/ubuntu/.env.prod > .env.prod'
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Add your deployment steps here
                    // This could be a Docker Compose deployment, Kubernetes deployment, or other mechanisms
                    // For Docker Compose:
                    sh 'docker compose -f docker-compose.prod.yaml up -d'
                }
            }
        }
    }

    post {
        always {
            // Clean up resources
            cleanWs()  // Clean up the workspace
        }

        success {
            echo "Pipeline executed successfully!"
        }

        failure {
            echo "Pipeline execution failed. Please check logs for details."
        }
    }
}