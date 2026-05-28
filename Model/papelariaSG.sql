create table fabricante(
id_fabricante int auto_increment primary key not null,
nome_fabrica varchar(100) not null,
cnpj bigint(18) not null,
telefone bigint(12) not null,
email text not null,
cidade varchar(60) not null,
tipo_fabrica text not null);

create table produto(
id_produto int auto_increment primary key not null,
nome text not null,
descricao text not null,
codigo_barras text not null,
preco_custo decimal(10,2) not null,
unidade_medida decimal(10,2) not null,
id_fabricante int,
foreign key (id_fabricante) references fabricante (id_fabricante));

create table fornecedor(
id_fornecedor int auto_increment primary key not null,
nome_fornecedor text not null,
cnpj bigint(18) not null,
telefone bigint(12) not null,
email text not null,
prazo_entrega text not null,
id_produto int,
foreign key (id_produto) references produto (id_produto));

create table pedido(
id_pedido int auto_increment primary key not null,
data_pedido date not null,
data_entrega date not null,
valor_total decimal (10,2) not null,
quantia_itens int not null,
entrega_status text not null,
id_fornecedor int,
foreign key (id_fornecedor) references fornecedor (id_fornecedor));
    
create table estoque_cd (
id_estoque_cd int auto_increment primary key,
quantidade int not null,
prox_pedido date not null,
qtd_minima int not null,
qtd_maxima int not null,
local_estoque text not null,
id_pedido int,
foreign key (id_pedido) references pedido (id_pedido));

create table loja (
id_loja int auto_increment primary key,
nome_loja text not null,
cnpj bigint(18) not null,
endereco text not null,
telefone bigint(12) not null,
gerente varchar(45) not null,
id_estoque_cd int,
foreign key (id_estoque_cd) references estoque_cd (id_estoque_cd));

create table estoque_loja (
id_estoque_loja int auto_increment primary key,
quantidade int not null,
prox_pedido date not null,
qtd_minima int not null,
qtd_maxima int not null,
preco_estoque decimal (10,2) not null,
id_loja int,
foreign key (id_loja) references loja (id_loja));

create table categoria (
id_categoria int auto_increment primary key,
nome_categoria text not null,
descricao text not null,
tipo text not null,
data_cadastro date not null,
estampa varchar(45) not null,
id_estoque_loja int,
foreign key (id_estoque_loja) references estoque_loja (id_estoque_loja));

create table movimentacao(
id_movimentacao int auto_increment primary key not null,
tipo text not null,
quantidade int not null,
origem varchar(50) not null,
destino varchar(45) not null,
data_movimentacao date not null,
id_categoria int,
foreign key (id_categoria) references categoria (id_categoria));

create table venda(
id_venda int auto_increment primary key not null,
quantidade int not null,
preco_venda decimal(10,2) not null,
lucro decimal(10,2) not null,
forma_pagamento text not null,
data_venda date not null,
id_movimentacao int,
foreign key (id_movimentacao) references movimentacao(id_movimentacao));

DELIMITER $$

CREATE TRIGGER tgr_after_update_produto 
AFTER UPDATE ON produto
FOR EACH ROW
BEGIN

IF OLD.preco_custo <> NEW.preco_custo THEN
INSERT INTO log_produto
(id_produto, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_produto, 'UPDATE_PRODUTO', OLD.preco_custo, NEW.preco_custo, USER());
END IF;

IF OLD.preco_custo <> NEW.preco_custo THEN
INSERT INTO log_produto
(id_produto, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_produto, 'UPDATE_PRODUTO', OLD.preco_custo, NEW.preco_custo, USER());
END IF;

IF OLD.preco_custo <> NEW.preco_custo THEN
INSERT INTO produto
(id_produto, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_produto, 'UPDATE_PRODUTO', OLD.preco_custo, NEW.preco_custo, USER());
END IF;
END$$

CREATE TABLE log_produto (
    id_log_produto INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT,
    acao VARCHAR(50),
    valor_antigo DECIMAL,
    valor_novo DECIMAL,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

DELIMITER $$

CREATE TRIGGER tgr_after_update_pedido
AFTER UPDATE ON pedido
FOR EACH ROW
BEGIN

IF OLD.valor_total <> NEW.valor_total THEN
INSERT INTO log_pedido
(id_pedido, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_pedido, 'UPDATE_VALOR', OLD.valor_total, NEW.valor_total, USER());
END IF;

IF OLD.valor_total <> NEW.valor_total THEN
INSERT INTO log_pedido
(id_pedido, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_pedido, 'UPDATE_VALOR', OLD.valor_total, NEW.valor_total, USER());
END IF;

IF OLD.valor_total <> NEW.valor_total THEN
INSERT INTO log_pedido
(id_pedido, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_pedido, 'UPDATE_VALOR', OLD.valor_total, NEW.valor_total, USER());
END IF;
END$$

CREATE TABLE log_pedido (
    id_log_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    acao VARCHAR(50),
    valor_antigo DECIMAL,
    valor_novo DECIMAL,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
DELIMITER $$

CREATE TRIGGER tgr_after_update_estoque_cd
AFTER UPDATE ON estoque_cd
FOR EACH ROW
BEGIN

IF OLD.quantidade <> NEW.quantidade THEN
INSERT INTO log_estoque_cd
(id_estoque_cd, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_estoque_cd, 'UPDATE_QUANTIDADE', OLD.quantidade, NEW.quantidade, USER());
END IF;

IF OLD.qtd_minima <> NEW.qtd_minima THEN
INSERT INTO log_estoque_cd
(id_estoque_cd, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_estoque_cd, 'UPDATE_QTD_MINIMA', OLD.qtd_minima, NEW.qtd_minima, USER());
END IF;

IF OLD.qtd_maxima <> NEW.qtd_maxima THEN
INSERT INTO log_estoque_cd
(id_estoque_cd, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_estoque_cd, 'UPDATE_QTD_MAXIMA', OLD.qtd_maxima, NEW.qtd_maxima, USER());
END IF;
END$$

CREATE TABLE log_estoque_cd (
    id_log_estoque_cd INT AUTO_INCREMENT PRIMARY KEY,
    id_estoque_cd INT,
    acao VARCHAR(50),
    valor_antigo INT,
    valor_novo INT,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
DELIMITER $$

CREATE TRIGGER tgr_after_update_loja
AFTER UPDATE ON loja
FOR EACH ROW
BEGIN

IF OLD.endereco <> NEW.endereco THEN
INSERT INTO log_loja
(id_loja, acao, endereco_antigo, endereco_novo, usuario)
VALUES
(OLD.id_loja, 'UPDATE_ENDERECO', OLD.endereco, NEW.endereco, USER());
END IF;

IF OLD.endereco <> NEW.endereco THEN
INSERT INTO log_loja
(id_loja, acao, endereco_antigo, endereco_novo, usuario)
VALUES
(OLD.id_loja, 'UPDATE_ENDERECO', OLD.endereco, NEW.endereco, USER());
END IF;

IF OLD.endereco <> NEW.endereco THEN
INSERT INTO log_loja
(id_loja, acao, endereco_antigo, endereco_novo, usuario)
VALUES
(OLD.id_loja, 'UPDATE_ENDERECO', OLD.endereco, NEW.endereco, USER());
END IF;
END$$

CREATE TABLE log_loja (
    id_log_loja INT AUTO_INCREMENT PRIMARY KEY,
    id_loja INT,
    acao VARCHAR(50),
    endereco_antigo TEXT,
    endereco_novo TEXT,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
DELIMITER $$

CREATE TRIGGER tgr_after_update_estoque_loja
AFTER UPDATE ON estoque_loja
FOR EACH ROW
BEGIN

IF OLD.quantidade <> NEW.quantidade THEN
INSERT INTO log_estoque_loja
(id_estoque_loja, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_estoque_loja, 'UPDATE_QUANTIDADE', OLD.quantidade, NEW.quantidade, USER());
END IF;

IF OLD.qtd_minima <> NEW.qtd_minima THEN
INSERT INTO log_estoque_loja
(id_estoque_loja, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_estoque_loja, 'UPDATE_QTD_MINIMA', OLD.qtd_minima, NEW.qtd_minima, USER());
END IF;

IF OLD.qtd_maxima <> NEW.qtd_maxima THEN
INSERT INTO log_estoque_loja
(id_estoque_loja, acao, valor_antigo, valor_novo, usuario)
VALUES
(OLD.id_estoque_loja, 'UPDATE_QTD_MAXIMA', OLD.qtd_maxima, NEW.qtd_maxima, USER());
END IF;
END$$

CREATE TABLE log_estoque_loja (
    id_log_estoque_loja INT AUTO_INCREMENT PRIMARY KEY,
    id_estoque_loja INT,
    acao VARCHAR(50),
    valor_antigo INT,
    valor_novo INT,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
DELIMITER $$

CREATE TRIGGER tgr_after_update_movimentacao
AFTER UPDATE ON movimentacao
FOR EACH ROW
BEGIN

IF OLD.destino <> NEW.destino THEN
INSERT INTO log_movimentacao
(id_movimentacao, acao, destino_antigo, destino_novo, usuario)
VALUES
(OLD.id_movimentacao, 'UPDATE_DESTINO', OLD.destino, NEW.destino, USER());
END IF;

IF OLD.destino <> NEW.destino THEN
INSERT INTO log_movimentacao
(id_movimentacao, acao, destino_antigo, destino_novo, usuario)
VALUES
(OLD.id_movimentacao, 'UPDATE_DESTINO', OLD.destino, NEW.destino, USER());
END IF;

IF OLD.destino <> NEW.destino THEN
INSERT INTO log_movimentacao
(id_movimentacao, acao, destino_antigo, destino_novo, usuario)
VALUES
(OLD.id_movimentacao, 'UPDATE_DESTINO', OLD.destino, NEW.destino, USER());
END IF;
END$$

CREATE TABLE log_movimentacao (
    id_log_movimentacao INT AUTO_INCREMENT PRIMARY KEY,
    id_movimentacao INT,
    acao VARCHAR(50),
    destino_antigo text,
    destino_novo text,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
DELIMITER $$

CREATE TRIGGER tgr_after_update_venda
AFTER UPDATE ON venda
FOR EACH ROW
BEGIN

IF OLD.lucro <> NEW.lucro THEN
INSERT INTO log_venda
(id_venda, acao, lucro_antigo, lucro_novo, usuario)
VALUES
(OLD.id_venda, 'UPDATE_LUCRO', OLD.lucro, NEW.lucro, USER());
END IF;

IF OLD.lucro <> NEW.lucro THEN
INSERT INTO log_venda
(id_venda, acao, lucro_antigo, lucro_novo, usuario)
VALUES
(OLD.id_venda, 'UPDATE_LUCRO', OLD.lucro, NEW.lucro, USER());
END IF;

IF OLD.lucro <> NEW.lucro THEN
INSERT INTO log_venda
(id_venda, acao, lucro_antigo, lucro_novo, usuario)
VALUES
(OLD.id_venda, 'UPDATE_LUCRO', OLD.lucro, NEW.lucro, USER());
END IF;
END$$

CREATE TABLE log_venda (
    id_log_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT,
    acao VARCHAR(50),
    lucro_antigo DECIMAL,
    lucro_novo DECIMAL,
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
