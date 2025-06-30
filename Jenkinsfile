pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'No build needed for Python program'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests'
                // Use 'python' or 'python3' depending on your environment
                powershell 'C:\Users\ADMIN\AppData\Local\Programs\Python\Python310\python.exe -m unittest testcase.py'
            }
        }
    }

    post {
        failure {
            echo 'Build failed — sending notification email'
            emailext(
                subject: "⚠️ Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """<p><b>Job:</b> ${env.JOB_NAME} #${env.BUILD_NUMBER}</p>
                         <p><b>Status:</b> FAILED</p>
                         <p><b>See console output at:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                to: 'your-email@example.com'
            )
        }
        success {
            echo 'Build succeeded'
        }
    }
}
