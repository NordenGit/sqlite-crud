pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                        bat 'docker stop sqlite-crud-running || exit 0'
                        bat 'docker rm sqlite-crud-running || exit 0'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    def buildResult = build job: 'sqlite-crud', propagate: false
                    if (buildResult.result == 'SUCCESS') {
                        echo "Build sqlite-crud succeeded"
                    } else {
                        echo "Build sqlite-crud failed with status: ${buildResult.result}"
                    }
                }
            }
        }
    }
}
