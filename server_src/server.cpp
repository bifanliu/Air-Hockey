//////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////TCP//////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////

#include <arpa/inet.h>
#include <netinet/in.h>
#include <cstring>
#include <sys/socket.h>
#include <sys/wait.h> // close
#include <semaphore.h>
#include <iostream>
#include <chrono> // time
#include <thread>
#include <queue>
using namespace std;

#define PORT 16902
#define MULTIPUCK 1
#define SINGLEPUCK 2
#define THREADLIMIT 100

typedef struct pthread_arg_t{
	int new_socket_fd;
    int competitor;
    int semcount;
    int presemcount;
    string msg;
} pthread_arg_t;

sem_t critical;
sem_t sem[THREADLIMIT];

// global paremeter
int clientcount = 0;
int servercount = 0;
queue <pthread_arg_t *> SQueue, MQueue;



//thread information
void *task(void *data);
void *server_task(void *data);

//main function
int main(int argc,char *argv[]){
    // semaphore init
    sem_init(&critical, 1, 1);
    for(int j = 0; j < THREADLIMIT; j++)
        sem_init(&sem[j], 1, 1);

    // if no complete input then over
	if(argc != 1){
		printf("Input Error!\n");
        return 0;
    }

    // set server socket paremeter
	int sockfd,clientSocket;
	struct sockaddr_in serverAddr,newAddr;

    // client socket set
    socklen_t addr_size;
	addr_size = sizeof(newAddr);

	// server socket set
	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
		printf("[-]Error in connection.\n");
		return 0;
	}
	serverAddr.sin_family = AF_INET;
	serverAddr.sin_port = htons(PORT);
	serverAddr.sin_addr.s_addr = inet_addr("0.0.0.0");
    // build socket to serverAddr port
	if(bind(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0){
		printf("[-]Error in binding.\n");
        close(sockfd);
		return 0;
	}
    // maximum client is 20 and if listen error return -1
	if(listen(sockfd, 20) < 0){
		printf("[-]Error in binding.\n");
        close(sockfd);
        return 0;
	}

    printf("[+]Listening....\n");
	// start accept client request
	while(1){
        // wait client request
		clientSocket = accept(sockfd, (struct sockaddr*)&newAddr, &addr_size);
        if(clientSocket < 0){
		    printf("Client request is failed!\n");
		    continue;
		}
        pthread_t *NewThread = new pthread_t;
        if(pthread_create(NewThread, NULL, server_task, (void *)&clientSocket) < 0){
            printf("pthread create error\n");
        }
	}

	close(sockfd);

	return 0;
}

void *server_task(void *arg){
    int clientSocket = *((int *)arg);
    printf("%d\n", clientSocket);
    // set client socket paremeter
    char number[1024];
    // read number 1 means multipuck 2 means singlepuck
    read(clientSocket,number,1024);
    // create thread content
    pthread_arg_t *pthread_arg;
    pthread_t *NewThread = new pthread_t;
    pthread_arg = (pthread_arg_t *)malloc(sizeof(pthread_arg_t));
    pthread_arg->new_socket_fd = clientSocket;
    pthread_arg->semcount = clientcount;
    clientcount++;
    // which number is 1 or 2
    if(atoi(number) == MULTIPUCK){
        pthread_arg->msg = "multi";
        // protect queue
        sem_wait(&critical);
        MQueue.push(pthread_arg);
        if(MQueue.size() == 2){
            pthread_arg_t *pthread_arg_opponet = MQueue.front();
            pthread_arg->competitor = pthread_arg_opponet->new_socket_fd;
            pthread_arg_opponet->competitor = pthread_arg->new_socket_fd;
            pthread_arg->presemcount = pthread_arg_opponet->semcount;
            pthread_arg_opponet->presemcount = pthread_arg->semcount;
            // delete first
            MQueue.pop();
            // delete secode
            MQueue.pop();
            // create thread
            while(pthread_create(NewThread, NULL, task, (void *)pthread_arg) < 0){
                printf("pthread create error\n");
            }
        }
        else{
            pthread_arg->competitor = -1;
            // create thread
            while(pthread_create(NewThread, NULL, task, (void *)pthread_arg) < 0){
                printf("pthread create error\n");
            }
        }
        sem_post(&critical);
        // multipuck produce thread
        // MPthread(clientSocket);
    }
    else if(atoi(number) == SINGLEPUCK){
        pthread_arg->msg = "single";
        // protect queue
        sem_wait(&critical);
        SQueue.push(pthread_arg);
        if(SQueue.size() == 2){
            pthread_arg_t *pthread_arg_opponet = SQueue.front();
            pthread_arg->competitor = pthread_arg_opponet->new_socket_fd;
            pthread_arg_opponet->competitor = pthread_arg->new_socket_fd;
            pthread_arg->presemcount = pthread_arg_opponet->semcount;
            pthread_arg_opponet->presemcount = pthread_arg->semcount;
            // delete first
            SQueue.pop();
            // delete second
            SQueue.pop();
            // create thread
            while(pthread_create(NewThread, NULL, task, (void *)pthread_arg) < 0){
                printf("pthread create error\n");
            }
        }
        else{
            pthread_arg->competitor = -1;
            while(pthread_create(NewThread, NULL, task, (void *)pthread_arg) < 0){
                printf("pthread create error\n");
            }
        }
        sem_post(&critical);
        // multipuck produce thread
        // MPthread(clientSocket);
    }
        
    pthread_join(*NewThread, NULL);
}

void* task(void *arg){
    // let pthread_arg into paremeter
	pthread_arg_t *pthread_arg = (pthread_arg_t *)arg;
	int newSocket = pthread_arg->new_socket_fd;
    string msg = pthread_arg->msg;
    int p = pthread_arg->competitor;
    int *sem_value = new int;
    // set receive msg char array
    char chmsg[128];
    // p less than 0 means is first client 
    if(p < 0){
        // if first client will stop in here to read "start"
        memset(chmsg,'\0',128);
        read(newSocket,chmsg,128);
        // printf("1. client%d read client%d content is %s\n", pthread_arg->new_socket_fd, pthread_arg->new_socket_fd, chmsg);
        p = pthread_arg->competitor;
        // if read over from myself than over
        if(strncmp(chmsg, "over", 4) != 0){
            write(p, "start1", 6);
            // printf("2. client%d write to client%d content is %s\n", pthread_arg->new_socket_fd, p, "start1");
        }
        else{
            // If it doesn't wait for the next client , the queue will pop
            sem_wait(&critical);
            if(MQueue.size() == 1 && strncmp(msg.c_str(), "multi", msg.length()) == 0){
                MQueue.pop();
            }
            else if(SQueue.size() == 1 && strncmp(msg.c_str(), "single", 6) == 0){
                SQueue.pop();
            }
            sem_post(&critical);
            // send start1 to end main
            write(newSocket, (const void *)"start1", 6);
            // printf("3. client%d write to client%d content is %s\n", newSocket, newSocket, "start1");
        }
    }
    else if(p >= 0){
        // write status to client
        write(p,(const void *)"start2",6);
        // printf("4. client%d write to client%d content is %s\n", newSocket, p, "start2");
        // wait start2 read into client
        memset(chmsg,'\0',128);
        read(newSocket,chmsg,128);
        // printf("5. client%d read client%d content is %s\n", pthread_arg->new_socket_fd, pthread_arg->new_socket_fd, chmsg);
    }

    while(strncmp(chmsg,"over",4) != 0){
        // read self coordinate
        sem_wait(&sem[pthread_arg->presemcount]);
    	memset(chmsg,'\0',128);
        read(newSocket,chmsg,128);
        // printf("6. client%d read client%d content is %s\n", pthread_arg->new_socket_fd, pthread_arg->new_socket_fd, chmsg);
        sem_getvalue(&sem[pthread_arg->presemcount], sem_value);
        // write to opponent
        // first
        if(*sem_value == 0){
            sem_post(&sem[pthread_arg->semcount]);
            sem_wait(&sem[pthread_arg->presemcount]);
        }
        else{
            sem_wait(&sem[pthread_arg->presemcount]);
            sem_post(&sem[pthread_arg->semcount]);
        }
        if(strncmp(chmsg,"over",4) == 0 || strncmp(chmsg,"gameover",8) == 0){
            write(p,chmsg,128);
            // printf("7. client%d write to client%d content is %s\n", newSocket, p, chmsg);
            break;
        }
        // 10 msec = 0.001 so frequecy is 1/0.001 = 1000HZ
        std::chrono::microseconds period(10);

        // evaluate
        double frequency = 1.0 / std::chrono::duration_cast<std::chrono::duration<double>>(period).count();

        // sleep for the remaining time in the period
        auto remainingTime = period - std::chrono::duration_cast<std::chrono::microseconds>(
            std::chrono::high_resolution_clock::now().time_since_epoch()
        ) % period;

        std::this_thread::sleep_for(remainingTime);

        // output result
        write(p,chmsg,128);
        // printf("8. client%d write to client%d content is %s\n", newSocket, p, chmsg);
        sem_post(&sem[pthread_arg->semcount]);
    }

    // thread over
    free(pthread_arg);
    pthread_exit(NULL);
}



// #include <arpa/inet.h>
// #include <netinet/in.h>
// #include <cstring>
// #include <sys/socket.h>
// #include <sys/wait.h> // close
// #include <semaphore.h>
// #include <iostream>
// #include <chrono> // time
// #include <thread>
// #include <queue>
// using namespace std;

// #define SERVERPORT 7000
// #define MULTIPUCK 0
// #define SINGLEPUCK 1

// // protect queue
// sem_t sem;

// typedef struct _ClientData{
//     sockaddr_in ClientAddr;
//     int ClientType;
//     int ClientSockfd;
// } ClientData;

// // set queue to put multipuck player and singlepuck player
// queue<*ClientData> SQueue, MQueue;

// // thread function
// void *client_task(void *arg);

// // This game use TCP to Receive all client and 
// int main(int argc,char *argv[]){
//     // if no complete input then over
// 	if(argc != 1){
// 		printf("Input Error!\n");
//         return 0;
//     }

//     // Receive data buffer
//     char buffer[1024];

//     // set sockfd
//     int sockfd;
// 	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
// 		printf("[-]Error in connection.\n");
// 		return 0;
// 	}

//     // Init sem
//     sem_init(&sem, 1, 1);

//     // set server sockaddr_in
//     struct sockaddr_in serverAddr;

//     serverAddr.sin_family = AF_INET;
// 	serverAddr.sin_port = htons(SERVERPORT);
// 	serverAddr.sin_addr.s_addr = inet_addr("0.0.0.0");

//     // set client sockaddr_in
// 	struct sockaddr_in clientAddr;
//     socklen_t len = sizeof(clientAddr);

//     // build socket to serverAddr port
// 	if(bind(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0){
// 		printf("[-]Error in binding.\n");
//         close(sockfd);
// 		return 0;
// 	}

//     // maximum client is 20 and if listen error return -1
// 	if(listen(sockfd, 20) < 0){
// 		printf("[-]Error in binding.\n");
//         close(sockfd);
//         return 0;
// 	}

// 	// start accept client request
//     printf("Start Receive\n");

// 	while(1){

//         // wait client request
//         int reply_sockfd;
// 		reply_sockfd = accept(sockfd, (struct sockaddr*)&clientAddr, &len);
//         if(reply_sockfd < 0){
// 		    printf("Client request is failed!\n");
// 		    continue;
// 		}

//         // wait client send data
//         recv(reply_sockfd, buffer, 1024, 0);

//         // print info
//         printf("get message from [%s:%d]: %s\n", inet_ntoa(clientAddr.sin_addr), ntohs(clientAddr.sin_port), buffer);

//         // print info
//         printf("Server receive from [%s:%d]: %s\n", inet_ntoa(clientAddr.sin_addr), ntohs(clientAddr.sin_port), buffer);

//         // decide is multipuck or single puck 
//         ClientData *NewClient = new ClientData;
//         NewClient->ClientAddr = clientAddr;
//         NewClient->ClientSockfd = reply_sockfd;
//         sem_wait(&sem);
//         if(atoi(buffer) == SINGLEPUCK){
//             // put into SQueue
//             NewClient->ClientType = SINGLEPUCK;
//             SQueue.push(NewClient);
//         }
//         else if(atoi(buffer) == MULTIPUCK){
//             NewClient->ClientType = MULTIPUCK;
//             MQueue.push(NewClient);
//         }
//         sem_post(&sem);
//         // create pthread
//         pthread_t *NewThread = new pthread_t;
//         if(pthread_create(NewThread, NULL, client_task, (void *)NewClient) < 0){
//             printf("pthread create error\n");
//         } 
// 	}

// 	close(sockfd);

// 	return 0;
// }

// void *client_task(void *arg){
//     // load arg data
//     ClientData *Client = (ClientData *)arg;
//     // if queue size is 2
//     sem_wait(&sem);
//     if(Client->ClientType == SINGLEPUCK && SQueue.size() == 2){
//         // queue is first in first out
//         ClientData *Opponent = SQueue.front();
//         SQueue.pop();
//         SQueue.pop();
//         send(Client->ClientSockfd, "running", 7, 0);
//         printf("send message to [%s:%d]: %s\n", inet_ntoa(Client->ClientAddr.sin_addr), ntohs(Client->ClientAddr.sin_port), "running");
//         send(Opponent->ClientSockfd, "running", 7, 0);
//         printf("send message to [%s:%d]: %s\n", inet_ntoa(Opponent->ClientAddr.sin_addr), ntohs(Opponent->ClientAddr.sin_port), "running");
//         sem_post(&sem);
//     }
//     else if(Client->ClientType == MULTIPUCK && MQueue.size() == 2){
//         // queue is first in first out
//         ClientData *Opponent = MQueue.front();
//         MQueue.pop();
//         MQueue.pop();
//         send(Client->ClientSockfd, "running", 7, 0);
//         printf("send message to [%s:%d]: %s\n", inet_ntoa(Client->ClientAddr.sin_addr), ntohs(Client->ClientAddr.sin_port), "running");
//         send(Opponent->ClientSockfd, "running", 7, 0);
//         printf("send message to [%s:%d]: %s\n", inet_ntoa(Opponent->ClientAddr.sin_addr), ntohs(Opponent->ClientAddr.sin_port), "running");
//         sem_post(&sem);
//     }
//     // if queue size is 1
//     else if(Client->ClientType == MULTIPUCK && MQueue.size() == 1){
//         // send waiting
//         send(Client->ClientSockfd, "waiting", 7, 0);
//         // wait running send to my
//     }
//     else if(Client->ClientType == SINGLEPUCK && SQueue.size() == 1){

//     }
// }

// // sendto(sockfd, "start2", 1024, 0, (struct sockaddr *)pthread_arg->OpponentSockaddr, len);