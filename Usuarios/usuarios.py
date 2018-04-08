#coding: utf-8

import os
import json
import psycopg2

def registerUser():
    print "----------------------------------"
    print "------ Cadastro de usuarios ------"
    print "----------------------------------"
    usuario = raw_input("Digite o login: ")
    senha = raw_input("Digite a senha: ")
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=onxenti user=onxentiadmin password=123456")
        cur = con.cursor()
        sql = "insert into users(login_access,passwd) values(%s, %s)"
        sql_data = (usuario, senha)
        cur.execute (sql, sql_data)
        con.commit()
        print "Usuario %s cadastrado com sucesso"%usuario
    except Exception as e:
        print "Erro: %s"%e
        con.rollback()
    finally:
        cur.close()
        con.close()
		
def accessUser():
    print "--------------------------------------"
    print "------ Autenticação de usuários ------"
    print "--------------------------------------"
    login = raw_input("Digite o seu login: ")
    passw = raw_input("Digite a sua senha: ")
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=onxenti user=onxentiadmin password=7487105")
        cur = con.cursor()
        sql = "select * from users where login_access = (%s) and passwd = (%s)"
        sql_data = (login, passw)
        cur.execute (sql, sql_data)
        if cur.fetchone() == None:
            print "Falha ao autenticar"
        else:
            print "Usuario autenticado com sucesso"
    except Exception as e:
        print "Erro: %s"%e
    finally:
        cur.close()
        con.close()

def chPasswd():
    print "--------------------------------"
    print "------ Alteracao de senha ------"
    print "--------------------------------"
    try:
        con = psycopg2.connect("host=127.0.0.1 dbname=onxenti user=onxentiadmin password=7487105")
        cur = con.cursor()
        cur.execute ("select * from users")
        for u in (cur.fetchall()):
            print u[0],u[1]
        opcao = raw_input("Escolha o id de qual administrador deseja alterar a senha: ")
        newPass = raw_input("Digite a nova senha: ")
        sql = "update users set passwd = (%s) where id = (%s)"
        sql_data = (newPass, opcao)
        cur.execute (sql, sql_data)
        con.commit()
        print "Senha alterada com sucesso"
    except Exception as e:
        print "Erro ao alterar a senha: \n%s"%e
    finally:
        cur.close()
        con.close()

