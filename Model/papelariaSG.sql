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
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    id_estoque_cd INT,
    acao VARCHAR(50),
    valor_antigo VARCHAR(255),
    valor_novo VARCHAR(255),
    usuario VARCHAR(100),
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
   

INSERT INTO fabricante
(nome_fabrica, cnpj, telefone, email, cidade, tipo_fabrica)
VALUES
('Faber Castell', 12345678000199, 49999999999, 'contato@fabercastell.com', 'São Paulo', 'Material Escolar');

INSERT INTO produto
(nome, descricao, codigo_barras, preco_custo, unidade_medida, id_fabricante)
VALUES
('Caneta Azul', 'Caneta esferográfica azul', '7891234567890', 2.50, 1.00, 1);

INSERT INTO fornecedor
(nome_fornecedor, cnpj, telefone, email, prazo_entrega, id_produto)
VALUES
('Distribuidora PapelMax', 98765432000188, 49988887777, 'vendas@papelmax.com', '7 dias', 1);

INSERT INTO pedido
(data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor)
VALUES
('2026-05-20', '2026-05-27', 250.00, 100, 'Em transporte', 1);

INSERT INTO estoque_cd
(quantidade, prox_pedido, qtd_minima, qtd_maxima, local_estoque, id_pedido)
VALUES
(50, '2026-06-01', 10, 100, 'Corredor A - Prateleira 3', 1);


    
    UPDATE estoque_cd
SET quantidade = 70
WHERE id_estoque_cd = 2 ;
