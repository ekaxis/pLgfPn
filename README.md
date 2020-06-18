# pLgfPn

Scripts em Ansible para provisionamento, gerenciamento de configurações e implantação de aplicativos.

Os scripts foram feitos de modo a facilitar
futuras atualizações, adaptar para o seu cenário e evitar possíveis erros.

```
- dev
  - group_vars
    - all.yml.example
  - roles
    - filebeat
      - defaults
      - handlers
      - tasks
      - templates
    - snort
      - files
      - handlers
      - tasks
      - templates
    - suricata
      - tasks
    - zabbix-agent
      - files
      - handlers
      - tasks
      - templates
- rhel
  - group_vars
  - roles
    - elk
      - defaults
      - files
      - handlers
      - tasks
      - templates
    - filebeat
      - defaults
      - files
      - handlers
      - tasks
      - templates
    - graylog
      - files
      - handlers
      - tasks
    - snort
      - files
      - handlers
      - tasks
      - templates
    - suricata
      - files
      - handlers
      - tasks
      - templates
    - warn-agent
      - files
      - tasks
    - zabbix-agent
      - files
      - handlers
      - tasks
      - templates
    - zabbix-server
      - handlers
      - tasks
```

#### Instalações não estáveis
  * snort (hrel)
  * graylog (hrel)
  * zabbix-server (hrel)

Arquivos com variáveis foram nomeados com `.example`, para utilizar as roles, retirar as extensões e preencher os campos.

__warn-agent descontinuado, mantido por uma talvez reemplementação__

__Você precisa preencher o campo do username e senha do usuário da API do zabbix para cadastrar os agentes__

__Em caso de erros ou problema de segurança no processo de instalação, criar
issue no repositório que será corrigido o mais rápido possível, agradeço des de já
a cooperação.__
