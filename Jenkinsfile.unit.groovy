pipeline {
    agent {
        label 'docker'
    }
    triggers {
        // Configuración de un trigger que le dice a Jenkins que revise cada 5 minutos la rama asociada para detectar si hubo cambios y disparar el build.
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/arimounir/cicd-a3-calc.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                echo 'Unit testing stage!'
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('API tests') {
            steps {
                echo 'API testing stage!'
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2E tests') {
            steps {
                echo 'E2E testing stage!'
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        failure {
        // Configuración de envío de mail solo en builds fallidos al correo UNIR del autor. El cuerpo del mail contiene el número de build y nombre de trabajo
            mail to: 'ariel.moguillansky827@comunidadunir.net',
                subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                body: "Ha ocurrido un fallo. Build #${env.BUILD_NUMBER}. Job name: ${env.JOB_NAME}"
        }
    }
}