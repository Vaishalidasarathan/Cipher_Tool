pipeline {
  agent none
  stages {
    stage('Build') {
      agent {
        docker {
          image 'python:3'
        }
<<<<<<< HEAD
        stage('Test') {
            agent {
                docker {
                    
                    image 'grihabor/pytest'
                  
                }
            }
            steps {
                sh 'python --version'
                sh 'apt-get install secretpy'
                sh 'apt-get install console-menu'
                sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
=======

      }
      steps {
        sh 'python -m py_compile Source/CipherTool.py'
        stash(name: 'compiled-results', includes: 'Source/*.py*')
      }
    }

    stage('Test') {
      post {
        always {
          junit 'test-reports/results.xml'
>>>>>>> d95ffc0ad9b537dbe33dc8c3e77d4cd08d54112e
        }

      }
      steps {
        sh 'python --version'
        sh 'apt-get install secretpy'
        sh 'python -m pip install console-menu --user root'
        sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}