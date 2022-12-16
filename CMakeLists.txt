cmake_minimum_required(VERSION 3.24)
project(ProjetUnix_KebaierNadhir_2ING1 C)

set(CMAKE_C_STANDARD 11)

include_directories(Tubes_Nomees)
include_directories(Sockets)

add_executable(ProjetUnix_KebaierNadhir_2ING1
        Tubes_Nomees/Client.c
        Tubes_Nomees/Handlers_Cli.h
        Tubes_Nomees/Handlers_Serv.h
        Tubes_Nomees/serv_cli_fifo.h
        Tubes_Nomees/Server.c
        Sockets/Client.c
        Sockets/Server.c
        Sockets/Server_Client.h)
