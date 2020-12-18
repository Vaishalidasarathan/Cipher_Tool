pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {
                sh 'python -m py_compile Source/CipherTool.py'
                stash(name: 'compiled-results', includes: 'Source/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    
                    image 'grihabor/pytest'
                  
                }
            }
            steps {
                sh 'python --version'
                sh 'python -m pip install secretpy --user root'
                sh 'python -m pip install console-menu --user root'
                sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }   
}
