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

      }
      post {
        always {
          junit 'test-reports/results.xml'
        }

      }
      steps {
        sh 'python --version'
        sh 'pip3 install secretpy --jenkins'
        sh 'pip install console-menu'
        sh 'py.test --junit-xml test-reports/results.xml Source/testCipher.py'
      }
    }

  }
  options {
    skipStagesAfterUnstable()
  }
}