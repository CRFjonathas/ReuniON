# Engenharia de Requisitos

## 1. Atores 👥
* **Administrador:** Responsável por criar usuários e gerenciar o Inventário de TI.
* **Usuário Comum:** Responsável por agendar e gerenciar reuniões.

## 2. Regras de Negócio (RN) 📜
* **RN01 - Edição Colaborativa:** Qualquer usuário autenticado pode editar ou cancelar reuniões, independentemente de quem as criou (visando a flexibilidade da seção).
* **RN02 - Segurança de Rede:** O sistema deve ser acessível apenas dentro da subnet/IPs da seção (bloqueio via Firewall/Middleware).
* **RN03 - Controle de Estoque:** Apenas Administradores podem Adicionar, Editar ou Remover itens do inventário.

## 3. Requisitos Funcionais (RF) ⚙️
* [ ] **Autenticação:** Login com usuário e senha para acessar o sistema.
* [ ] **Inventário (CRUD):** Cadastro de equipamentos (Notebooks, Câmeras, etc.) com nº de patrimônio.
* [ ] **Agendamento:** Formulário contendo:
    - Data, Hora de Teste, Hora de Início.
    - Local, Solicitante (Seção/Pessoa), Técnico Responsável.
    - Link da reunião e Equipamentos necessários.
* [ ] **Gestão de Status:** Fluxo de 'Agendada' -> 'Realizada' ou 'Cancelada'.
* [ ] **Exportação:** Botão para gerar PDF/Impressão dos dados da reunião.