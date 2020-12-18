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
                    
                    image 'harishr14/pytest'
                    

                }
            }
            steps {
                sh 'python --version'
                
                sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') { 
            agent any
            environment { 
                VOLUME = '$(pwd)/Source:/src'
                IMAGE = 'harishr14/pyinstall'
            }
            steps {
                dir(path: env.BUILD_ID) { 
                    unstash(name: 'compiled-results') 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F CipherTool.py'" 
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/Source/dist/CipherTool" 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
    
}
