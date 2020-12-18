pipeline {
  agent none
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
<<<<<<< HEAD
        stage('Test') {
            agent {
                docker {
                    
                    image 'grihabor/pytest'
                    image 'grihabor/pytestrenovate/pip
'
                  
                }
            }
            steps {
                sh 'python --version'
                sh 'pip install secretpy'
                sh 'pip install console-menu'
                sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
=======

      }
      post {
        always {
          junit 'test-reports/results.xml'
>>>>>>> 748f46be72c3552d2d99469b7941689261c76359
        }

      }
      steps {
        sh 'python --version'
        sh 'sudo apt-get install secretpy'
        sh 'apt-get install console-menu'
        sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}