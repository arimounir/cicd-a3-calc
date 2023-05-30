pipeline {
    agent {
        label 'docker'
    }
    triggers {
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('API tests') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2E tests') {
            steps {
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
        }
        unstable {
            mail to: 'arielmogui92@gmail.com',
                subject: "Unstable Pipeline: ${currentBuild.fullDisplayName}",
                body: "Ha ocurrido un fallo. Build #${env.BUILD_NUMBER}. Job name: ${env.JOB_NAME}"
        }
        failure {
            mail to: 'arielmogui92@gmail.com',
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Ha ocurrido un fallo. Build #${env.BUILD_NUMBER}. Job name: ${env.JOB_NAME}"
        }
    }
}