# server.py
from socket import socket, AF_INET, SOCK_STREAM
serverSock = socket( AF_INET, SOCK_STREAM )
serverSock.bind( ("", 3000) )
serverSock.listen( 1 )
connectionSock, addr = serverSock.accept()
print( str( addr ), "님이 접속했습니다" )
data = connectionSock.recv( 1024 )
print( "받은메시지 : ", data.decode( "utf-8" ) )
connectionSock.send( "Im am a server.".encode( "utf-8" ) )
print( "메세지를 보냈습니다" )


