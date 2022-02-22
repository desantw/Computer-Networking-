
from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My name is will"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 1025))
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    print (recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfrom = 'Mail From:<wld233@nyu.edu>'
    clientSocket.send(mailfrom)
    recv = clientSocket.recv(1024)
    print(recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rccptto = 'RCPT To: <wld233@nyu.edu>'
    clientSocket.send(rccptto)
    recv = clientSocket.recv(1024)
    print(recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = 'DATA'
    clientSocket.send(data)
    recv = clientSocket.recv(1024)
    print(recv)
    if recv[:3] != '354':
        print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send('Subject:Introduction')
    clientSocket.send('Hello')
    clientSocket.send(msg)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg)
    recv = clientSocket.recv(1024)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    Quit = 'QUIT'
    clientSocket.send(Quit)
    recv = clientSocket.recv(1024)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end
