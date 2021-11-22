pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/Vaibhavi1707/JenkinsDemo.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 main.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}
