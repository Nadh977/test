#include "serv_cli_fifo.h"
#include "Handlers_Cli.h"
int main(){
    /* Déclarations */
    char *pipe_1 = QUESTION;
    char *pipe_2 = REPONSE;
    int f1, f2;
    struct rep reponse;
    struct qtn question;
    /* Ouverture des tubes nommés */
    f1 = open(pipe_1, O_WRONLY);
    f2 = open(pipe_2, O_RDONLY);
    /* Installation des Handlers */
    signal(SIGUSR1, hand_reveil);
    /* Construction et envoi d’une question */
    question.pid = getpid();
    srand(getpid());
    question.n = rand() % NMAX + 1;
    write(f1, &question, sizeof(question));
    /* Attente de la réponse */
    pause();
    /* Lecture de la réponse */
    read(f2, &reponse, sizeof(reponse));
    /* Envoi du signal SIGUSR1 au serveur */
    kill(reponse.pid, SIGUSR1);
    /* Traitement local de la réponse */    
    printf("Numéros envoyé au total %d\n", question.n);
    printf("Numéros reçu :\n");
    for(int i=0; i < question.n; i++){
        printf("%d  \n", reponse.resultat[i]);
    }
    fflush(stdout);
    return 0;    
}
