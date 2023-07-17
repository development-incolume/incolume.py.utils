# CHANGELOG


All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Conventional Commit](https://www.conventionalcommits.org/pt-br/v1.0.0/).

This file was automatically generated for [incolumepy.utils](https://gitlab.com/development-incolume/incolumepy.utils/-/tree/2.6.0)

---


## [2.6.0]	 &#8212; 	2023-07-11:
### Added
  - Ampliado abrangência para Python3.11
  - Documentação compilada acrescentada ao versionamento
  - Lint pylama
  - Compatibilidade com Python 3.11
  - Documentação no formato HTML
  - Ordenação de etiquetas no CHANGELOG.md
  - Encapsulamento Mock em testes de acesso a arquivos
  - módulo incolumepy.utils.changelog para tratar de recuros do changelog
  - Aderência a convensão de commit disponível em https://www.conventionalcommits.org/pt-br/v1.0.0/
  - Aderência a Keep a Changelog disponível em https://keepachangelog.com/pt-BR/1.0.0/
### Changed
  - 'make setup' aperfeisoado para configuração do ambiente em apenas um comando
  - Aplicado ISO8601 para data em registros automatizados via comando make
  - Automação de script para gerar release e patch via comando make
  - Estilização do CHANGELOG.md
  - Cobertura de 100% em incolumepy.utils.__init__.py
  - Alteração nas regras githooks para melhoria de gerenciamento do projeto e garantir o versionamento semântico disponível em https://semver.org/lang/pt-BR/
### Deprecated
  - função "incolumepy.utils.update_changelog" tornada obsoleta em favor "incolumepy.utils.changelog.update_changelog"
### Removed
  - Lint flake8 substituído por lint pylama
  - Compatibilidade com Python 3.6
  - Pacote coverage
  - Pacote jupyter
  - Refinamento da configuração com as novas funcionalidades.
  - Suite de testes nose desativada permanentemente
### Changed
  - Estilo visual atualizado
  - Estilização em cores para resposta de commits
  - Branches main/master protegido contra alterações indevidas
  - Politica de validação com Black e isort diretamente via git hooks
  - Mensagens geradas pela ferramenta poetry autenticadas na execução
  - 100% de cobertura atingido
  - Complexidade ciclomática limitada (5)
  - Aualizado pacotes de dependências do projeto
  - Melhoria nos processos automatizados
  - Refinamento na configuração do pylint
  - Refinamento na configuração do pylama

## [2.6.0rc5]	 &#8212; 	2022-12-12:
### Changed
  - Estilização em cores para resposta de commits
  - Branches main/master protegido contra alterações indevidas
  - Politica de validação com Black e isort diretamente via git hooks
  - Mensagens geradas pela ferramenta poetry autenticadas na execução

## [2.6.0rc4]	 &#8212; 	2022-12-08:
### Changed
  - 100% de cobertura atingido
  - Complexidade ciclomática limitada (5)
  - Aualizado pacotes de dependências do projeto
  - Melhoria nos processos automatizados
  - Refinamento na configuração do pylint
  - Refinamento na configuração do pylama
### Removed
  - Pacote coverage
  - Pacote jupyter

## [2.6.0rc3]	 &#8212; 	2022-12-06:
### Changed
  - Refinamento da configuração com as novas funcionalidades.

## [2.6.0rc2]	 &#8212; 	2022-12-06:
### Added
  - Lint pylama
  - Compatibilidade com Python 3.11
  - Documentação no formato HTML
### Removed
  - Lint flake8 substituído por lint pylama
  - Compatibilidade com Python 3.6

## [2.6.0rc1]	 &#8212; 	2022-12-05:
### Added
  - Ampliado abrangência para Python3.11
  - Documentação compilada acrescentada ao versionamento
  - Ordenação de etiquetas no CHANGELOG.md
  - Encapsulamento Mock em testes de acesso a arquivos
### Changed
  - 'make setup' aperfeisoado para configuração do ambiente em apenas um comando
  - Aplicado ISO8601 para data em registros automatizados via comando make
  - Automação de script para gerar release e patch via comando make
### Removed
  - Suite de testes nose desativada permanentemente

## [2.6.0-rc.0]	 &#8212; 	2022-12-03:
### Added
  - módulo incolumepy.utils.changelog para tratar de recuros do changelog
  - Aderência a convensão de commit disponível em https://www.conventionalcommits.org/pt-br/v1.0.0/
  - Aderência a Keep a Changelog disponível em https://keepachangelog.com/pt-BR/1.0.0/
### Changed
  - Estilização do CHANGELOG.md
  - Cobertura de 100% em incolumepy.utils.__init__.py
  - Alteração nas regras githooks para melhoria de gerenciamento do projeto e garantir o versionamento semântico disponível em https://semver.org/lang/pt-BR/
### Deprecated
  - função "incolumepy.utils.update_changelog" tornada obsoleta em favor "incolumepy.utils.changelog.update_changelog"

## [2.5.4]	 &#8212; 	2022-03-13:
### Added
  - Documentação automatizada com sphinx

## [2.5.3]	 &#8212; 	2022-03-13:
### Changed
  - utils.files.realfilename Fatorado para sanar complexidade ciclomática.

## [2.5.2]	 &#8212; 	2022-03-13:
### Changed
  - Correções lint style
  - Visual CHANGELOG

## [2.5.1]	 &#8212; 	2022-03-12:
### Removed
  - Pacotes obsoletos removidos.

## [2.5.0]	 &#8212; 	2022-03-12:
### Added
  - Geração do CHANGELOG, padronizado de acordo com 'keep a changelog'
  - e geração automática com entradas extraídas de git/tags.

## [2.4.1]	 &#8212; 	2022-03-08:
### Fixed
  - Correções em update_changelog

## [2.4.0]	 &#8212; 	2022-03-07:
### Added
  - Método update_changelog acrescentado

## [2.3.0]	 &#8212; 	2022-02-16:
### Added
  - Acrescentado Método identify_dom_url_verbose

## [2.2.0]	 &#8212; 	2022-02-16:
### Added
  - retrocompatibilidade Python3.6+ garantida.

## [2.1.0]	 &#8212; 	2022-02-16:
### Added
  - Módulo 'incolumepy.utils.url' acrescentado

## [2.0.0]	 &#8212; 	2022-02-16:
### Changed
  - Atualização de teste para key_sort_2_versions
  - Gerenciador de pacotes alterado para poetry
  - Redefinição de estrutura
  - Switch de testes alterado para pytest
### Deprecated
  - Funcionalidades obsoletas sinalizadas como deprecated.
### Removed
  - Módulo incolumepy.utils.sequences deixou de existir

## [2.0.0-rc.2]	 &#8212; 	2022-02-15:
### Changed
  - Atualização de teste para key_sort_2_versions

## [2.0.0-rc.1]	 &#8212; 	2022-02-15:
### Deprecated
  - Funcionalidades obsoletas sinalizadas como deprecated.

## [2.0.0-rc.0]	 &#8212; 	2022-02-15:
### Changed
  - Redefinição de estrutura

## [1.7.0]	 &#8212; 	2022-02-15:
### Added
  - Acrescentado milhar e key_sort_2_versions

## [1.6.3]	 &#8212; 	2022-02-01:
### Fixed
  - Correção de pane FileNotFoundError

## [1.6.2]	 &#8212; 	2022-01-30:
### Changed
  - Refactor espectro de busca para namespace

## [1.6.1]	 &#8212; 	2022-01-24:
### Fixed
  - Diversas pequenas Correções

## [1.6.0]	 &#8212; 	2022-01-23:
### Removed
  - Metodos obsoletos desativados

## [1.5.0]	 &#8212; 	2022-01-22:
### Added
  - Aplicado utilização de linters, e integrado ao tox e Makefile

## [1.4.0]	 &#8212; 	2022-01-21:
### Added
  - Makefile adicionado com funções básicas

## [1.3.2]	 &#8212; 	2022-01-21:
### Changed
  - Atualização do README

## [1.3.1]	 &#8212; 	2022-01-21:
### Fixed
  - filemode para githooks corrigidos

## [1.3.0]	 &#8212; 	2022-01-21:
### Added
  - githooks acrescentados

## [1.2.0]	 &#8212; 	2022-01-21:
### Changed
  - Unificado versionamento com pyproject.toml

## [1.1.1]	 &#8212; 	2020-12-03:
### Changed
  - Atualização de configurações

## [1.1.0]	 &#8212; 	2018-11-22:
### Added
  - Novas funcionalidades acrescentadas

## [1.0.1]	 &#8212; 	2018-10-19:
### Added
  - acrescentado o logging para realfilename

## [1.0.0]	 &#8212; 	2018-10-19:
### Added
  - acrescentado o modulo decorator

## [0.9.4]	 &#8212; 	2018-06-09:
### Fixed
  - Chamada do pacote utils através do Namespace

## [0.9.3]	 &#8212; 	2018-06-08:
### Fixed
  - Nova implementação para incolumepy.utils.utils.namespace

## [0.9.2]	 &#8212; 	2018-06-08:
### Fixed
  - package incolumepy.utils.sequencias remaked into incolumepy.sequencias

## [0.9.1]	 &#8212; 	2018-06-01:
### Fixed
  - corrigido namespace

## [0.9.0]	 &#8212; 	2018-05-31:
### Added
  - nonexequi para restrição de execução em serie

## [0.8.0]	 &#8212; 	2018-05-22:
### Added
  - ll() adicionado

## [0.7.2]	 &#8212; 	2018-05-12:
### Changed
  - atualização EXAMPLE.rst

## [0.7.1]	 &#8212; 	2018-05-12:
### Fixed
  - atualizações no setup
  - Evolução na apresentação da documentação

## [0.7.0]	 &#8212; 	2018-05-12:
### Added
  - added incolumepy.utils.files.ll

## [0.6.0]	 &#8212; 	2018-05-05:
### Added
  - automatic tests adding

## [0.5.0]	 &#8212; 	2018-05-04:
### Added
  - incolumepy.utils.files adding

## [0.4.0]	 &#8212; 	2018-05-04:
### Added
  - incolumepy.utils.fake_cpf adding

## [0.3.0]	 &#8212; 	2018-05-04:
### Added
  - incolumepy.utils.sequencia

## [0.2.0]	 &#8212; 	2018-05-04:
### Added
  - implementação para def namespace

## [0.1.0]	 &#8212; 	2018-05-04:
### Added
  - initial Commit
---

[0.2.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.1.0...0.2.0
[0.3.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.2.0...0.3.0
[0.4.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.3.0...0.4.0
[0.5.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.4.0...0.5.0
[0.6.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.5.0...0.6.0
[0.7.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.6.0...0.7.0
[0.7.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.7.0...0.7.1
[0.7.2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.7.1...0.7.2
[0.8.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.7.2...0.8.0
[0.9.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.8.0...0.9.0
[0.9.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.9.0...0.9.1
[0.9.2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.9.1...0.9.2
[0.9.3]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.9.2...0.9.3
[0.9.4]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.9.3...0.9.4
[1.0.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/0.9.4...1.0.0
[1.0.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.0.0...1.0.1
[1.1.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.0.1...1.1.0
[1.1.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.1.0...1.1.1
[1.2.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.1.1...1.2.0
[1.3.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.2.0...1.3.0
[1.3.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.3.0...1.3.1
[1.3.2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.3.1...1.3.2
[1.4.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.3.2...1.4.0
[1.5.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.4.0...1.5.0
[1.6.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.5.0...1.6.0
[1.6.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.6.0...1.6.1
[1.6.2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.6.1...1.6.2
[1.6.3]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.6.2...1.6.3
[1.7.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.6.3...1.7.0
[2.0.0-rc.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/1.7.0...2.0.0-rc.0
[2.0.0-rc.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.0.0-rc.0...2.0.0-rc.1
[2.0.0-rc.2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.0.0-rc.1...2.0.0-rc.2
[2.0.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.0.0-rc.2...2.0.0
[2.1.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.0.0...2.1.0
[2.2.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.1.0...2.2.0
[2.3.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.2.0...2.3.0
[2.4.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.3.0...2.4.0
[2.4.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.4.0...2.4.1
[2.5.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.4.1...2.5.0
[2.5.1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.5.0...2.5.1
[2.5.2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.5.1...2.5.2
[2.5.3]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.5.2...2.5.3
[2.5.4]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.5.3...2.5.4
[2.6.0-rc.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.5.4...2.6.0-rc.0
[2.6.0rc1]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.6.0-rc.0...2.6.0rc1
[2.6.0rc2]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.6.0rc1...2.6.0rc2
[2.6.0rc3]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.6.0rc2...2.6.0rc3
[2.6.0rc4]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.6.0rc3...2.6.0rc4
[2.6.0rc5]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.6.0rc4...2.6.0rc5
[2.6.0]: https://gitlab.com/development-incolume/incolumepy.utils/-/compare/2.6.0rc5...2.6.0
