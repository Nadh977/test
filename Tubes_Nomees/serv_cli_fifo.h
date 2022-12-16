#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <signal.h>


#define NMAX 8
#define QUESTION "fifo1"
#define REPONSE "fifo2"

struct qtn{
    int pid;
    int n;
};

struct rep{
    int pid;
    int resultat[NMAX];
};
