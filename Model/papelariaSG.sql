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