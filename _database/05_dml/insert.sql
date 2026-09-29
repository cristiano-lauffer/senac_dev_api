use dev_api;

insert into carros (nom_carro, nom_marca, num_ano_fabricacao, num_ano_modelo, nom_cor, nom_combustivel, num_placa)
	select
		'Clio' nom_carro,
		'Renault' nom_marca,
		2007 num_ano_fabricacao,
		2008 num_ano_modelo,
		'Prata' nom_cor,
		'Gasolina' nom_combustivel,
		'III-9999' num_placa
;

insert into carros (nom_carro, nom_marca, num_ano_fabricacao, num_ano_modelo, nom_cor, nom_combustivel, num_placa)
	select
		'Sandero' nom_carro,
		'Renault' nom_marca,
		2013 num_ano_fabricacao,
		2014 num_ano_modelo,
		'Prata' nom_cor,
		'Gasolina' nom_combustivel,
		'JJJ-8888' num_placa
;