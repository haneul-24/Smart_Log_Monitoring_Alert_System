
pipeline{
    agent any

    environment{
        IMAGE_NAME = "smart-log-monitoring-alert-system"
        USER_NAME = "sejal9706"
        CONTAINER_NAME = "smart_log_monitoring_alert_system"
        SERVER_NAME = "haneul"
        SERVER_IP = "10.241.244.227 "

    }

    stages{
        stage('Checkout'){
            steps{
                git branch:'main', url: 'https://github.com/haneul-24/Smart_Log_Monitoring_Alert_System.git'
            }
        }


        stage('Docker Build'){
            steps{
                sh "docker build -t ${USER_NAME}/${IMAGE_NAME} ."
            }
        }

        stage('Run Test'){
            steps{
                sh "docker compose up --build --abort-on-container-exit"
            }
            post{
                always{ 
                    junit 'target/*.xml'
                    sh 'docker compose down'
                }
            }
        }

        stage('Approval- Docker-push'){
            steps{
                input "Approve Push to Docker-Hub?"
            }
        }

        stage('Docker push'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'DockerHub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )
                ]){
                    sh '''
                echo $PASS | docker login -u $USER --password-stdin
                docker push ${USER_NAME}/${IMAGE_NAME}
                '''

                }
            }
        }

        stage('Approval- Docker-Deploy'){
            steps{
                input "Approve Deployment to Production?"
            }
        }

        stage('Deploy'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'DockerHub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )
                ]){
                    sshagent(['app-server-key']){
                    sh '''
                    ssh ${SERVER_NAME}@{SERVER_IP} "
                        echo $PASS | docker login -u $USER --password-stdin
                        cd /home/haneul/Smart_Log_Monitoring_Alert_System
                        git pull origin main
                        docker pull ${USER_NAME}/${IMAGE_NAME} 
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                        docker compose up -d
                    "
                    '''
                    } 
                } 
            }
        }

    }

    post{
        failure{
            echo "failure"
            mail to: 'sej0697ian@gmail.com',
            subject: "FAILED: ${env.JOB_NAME} - BUILD#${env.BUILD_NUMBER}",
            body: "Job '${env.JOB_NAME}' (${env.BUILD_URL}) FAILED"
        }

        success{
            echo "Build and tests stages are successful"
            
        }
    }
}



