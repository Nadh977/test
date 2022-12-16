#include "serv_cli_fifo.h"
#include "Handlers_Serv.h"


int main(){
        FILE *fp = fopen("../outputserveur.txt", "w");
        printf("Serveur en attente de clients ...\n");
        fprintf(fp, "Serveur en attente de clients...\n");
        fflush(stdout);
        fflush(fp);
        /*Déclarations */
        char *pipe_1 = QUESTION;
        char *pipe_2 = REPONSE;
        int fd1, fd2;
        struct rep reponse;
        struct qtn question;

        /* Création des tubes nommés */
        mkfifo(pipe_1, 0666);
        mkfifo(pipe_2, 0666);
        /*initialisation du générateur de nombres aléatoires*/
        srand(getpid());
        /* Ouverture des tubes nommés */
        fd1 = open(pipe_1, O_RDWR);
        fd2 = open(pipe_2, O_WRONLY);
        /* Installation des Handlers */
        for(int i=1; i <= NSIG; i++){
                signal(i, fin_serveur);
        }
        signal(SIGUSR1, hand_reveil);
        while(1){
                /* lecture d’une question */
                read(fd1, &question, sizeof(question));
                printf("Question reçu de la part du client:  %d\n", question.pid);
                fprintf(fp, "Question reçu de la part du client:  %d\n", question.pid);
                fflush(stdout);
                fflush(fp);
                /* construction de la réponse */
                reponse.pid = getpid();
                for(int i=0; i < question.n; i++){
                        reponse.resultat[i] = rand() % NMAX + 1;
                }
                /* envoi de la réponse */
                write(fd2, &reponse, sizeof(reponse));
                /* envoi du signal SIGUSR1 au client concerné */
                kill(question.pid, SIGUSR1);
        }
        return 0;
}