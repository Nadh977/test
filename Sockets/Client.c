// C program for the Client Side

#include "Server_Client.h"


// Driver Code
int main()
{
	// Seed the random number generator with the current time
	srand(time(NULL));
	int requete_client;
	int network_socket;
	// Create a sock_socket
	network_socket = socket(AF_INET,
							SOCK_STREAM, 0);

	// port number and address
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_addr.s_addr = INADDR_ANY;
	server_address.sin_port = htons(PORT);

	// socket connection
	int connection_status = connect(network_socket,
									(struct sockaddr*)&server_address,
									sizeof(server_address));

	// Check for connection error
	if (connection_status < 0) {
		perror("Error\n");
		exit(1);
	}

	printf("Connection effectué avec succès !\n");

	// Generate a random number requete_client
	requete_client = rand() % NMAX + 1;



    /* Construction et envoi d’une question */
	send(network_socket, &requete_client, sizeof(requete_client), 0);
	printf("Il y'a au total %d Numéros envoyés\n",requete_client);
    /* Lecture de la réponse */
    int reponse[NMAX];
    recv(network_socket, reponse, sizeof(reponse), 0);
	/* Traitement local de la réponse */    
	printf("Numéros reçu de la part du serveur :\n");
    for(int i=0; i < requete_client; i++){
        printf("%d \n ", reponse[i]);
    }
    fflush(stdout);

    // Close the connection
    close(network_socket);

    return 0;
}


