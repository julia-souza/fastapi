## Instalação do Redis

```
sudo apt install redis-server
```

## Restaurando Backup

Com o servidor do Redis pausado, copie o arquivo dump.rdb da pasta /database deste projeto para dentro do diretório do Redis (Ex.: /var/lib/redis/6379/).

Por fim, levante o servidor do Redis novamente. OBS.: Caso não consiga restaurar o backup, basta fazer cadastros de demonstração novamente.

## Acesso ao Redis
### Conectando ao servidor
```
redis-cli
```
### Acessando valor
```
get {key}
```
### Limpando a base
```
flushall
```
## Cliente HTTP - Thunder Client

Instale a extensão thunder client no VS Code e importe as requisições dento do pacote client. Após importar, utilize a extensão para fazer as requisições HTTP contra a API.
