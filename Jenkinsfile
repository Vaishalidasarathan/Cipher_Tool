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
        stage('preTest') {
            agent {
                docker {
                    image 'renovate/pip'
                }
            steps {
                    sh 'python --version'
                    sh 'pip install secretpy'
                    sh 'pip install console-menu'
                }
            }

        }
        stage('Test') {
            agent {
                docker {                    
                    image 'grihabor/pytest'
                }
            }
            steps {
              
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
