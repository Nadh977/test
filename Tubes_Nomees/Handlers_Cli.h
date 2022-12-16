void hand_reveil(int sig){
    printf("Signal %d reçu, je suis le client: %d\n", sig,getpid());
}