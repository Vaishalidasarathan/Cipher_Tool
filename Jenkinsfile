pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
         stage('Email'){
            steps{
            emailext body: 'info',
            subject:"Pre Build Info" + " : " + env.JOB_NAME,
            to: 'dasarathanvaishali0@gmail.com'        
            }
        
        }
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
                
                sh 'py.test --junit-xml Source/results.xml Source/testCipher.py'
            }
            post {
                always {
                    junit 'Source/results.xml'
                    archiveArtifacts "Source/results.xml"
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
         stage('Email Deliver'){
            steps{
            emailext body: 'info',
            subject:env.JOB_NAME + " : " + currentBuild.currentResult,
            to: 'dasarathanvaishali0@gmail.com'        
            }
        
        }
    }
    
}
