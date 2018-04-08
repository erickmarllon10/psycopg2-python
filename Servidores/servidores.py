#coding: utf-8
import psycopg2
from Usuarios import usuarios

def addServer():
    print "------------------------------------"
    print "------ Cadastro de Servidores ------"
    print "------------------------------------"
    ip = raw_input ("Digite o endereco IP do servidor: ")
    serverName = raw_input ("Digite o nome do servidor: ")
    admLogin = raw_input ("Digite o nome do Sysadmin: ")

    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=onxenti user=onxentiadmin password=123456")
        cur = con.cursor()
        sql = "insert into servers(endereco,nome,sysadmin) values(%s, %s, %s)"
        sql_data = (ip, serverName, admLogin)
        cur.execute (sql, sql_data)
	con.commit()
	print "Servidor %s de ip %s cadastrado com sucesso"%(serverName, ip)
    except Exception as e:
        print "Erro: %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()

def delServer():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=onxenti user=onxentiadmin password=7487105")
        cur = con.cursor()
        cur.execute ("select * from servers")
        for srvs in cur.fetchall():
            print srvs
        opcao = raw_input ("Digite o id do servidor para remove-lo: ")
        sql = "delete from servers where id = (%s)"
        cur.execute (sql, opcao)
        con.commit()
        print "Servidor removido com sucesso"
    except Exception as e:
        print "Erro: %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()

def defAdmin():
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=onxenti user=onxentiadmin password=7487105")
        cur = con.cursor()
        cur.execute ("select * from servers")
        for srvs in cur.fetchall():
            print srvs
        opcao = raw_input("Digite o id do servidor que voce deseja definir o administrador: ")
        admin = raw_input("Digite o login do administrador: ")
        sql = "update servers set sysadmin = (%s) where id = (%s)"
        sql_data = (admin, opcao)
        cur.execute (sql, sql_data)
        con.commit()
        print "Administrador definido com sucesso"
    except Exception as e:
        print "Falha ao definir administrador: \n%s"%e
    finally:
        cur.close()
        con.close()

