void hand_reveil(int sig){
    printf("Signal %d reçu\n", sig);
}


void fin_serveur(int sig){
    if(sig != SIGUSR1){
        printf("Signal %d reçu, fermeture du serveur\n", sig);
        exit(0);
    }
}