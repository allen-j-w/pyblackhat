# -*-coding:utf-8 -*-
import threading
import paramiko
import subprocess


def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, 5555, username=user, password=passwd)
	ssh_session = client.get_transport().open_session()

	if ssh_session.active:
		ssh_session.send('ls')
		print ssh_session.recv(1024)

	return



def main():
	ssh_command('127.0.0.1', 'python', 'hack', 'ls')
	pass

if __name__ == '__main__':
	main()