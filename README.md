# Projeto Safe Password Generator (em Python)

Neste repositório está o projeto usado para mostrar minhas *skills* e estudos sobre aplicações voltadas à **cibersegurança**, com foco na **geração de senhas seguras**.

---

## Sobre o projeto

O [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html#appA) recomenda que senhas fortes tenham:

- **Pelo menos 8 caracteres** para sites que utilizam **autenticação multifator (MFA)**  
- **Pelo menos 15 caracteres** para sites que **não exigem multifator**

Com base nessas recomendações, este projeto apresenta três ferramentas diferentes para geração de senhas seguras.

As bibliotecas utilizadas foram:
- `random`
- `string`

---

##  Ferramentas disponíveis

###  Primeira opção: Safe Password Generator NIST (NIST 800-63B rules)

Nesta ferramenta seguimos os padrões sugeridos pela NIST 800-63B:

> “Verifiers and CSPs **SHALL** require passwords that are used as a single-factor authentication mechanism to be a minimum of 15 characters in length.  
> Verifiers and CSPs **MAY** allow passwords that are only used as part of multi-factor authentication processes to be shorter but **SHALL** require them to be a minimum of eight characters in length.”

Assim, o usuário pode gerar uma senha aleatória e segura seguindo o padrão NIST para **multi-factor authentication** (mínimo de 8 caracteres).

---

### Segunda opção: Safe Password Generator (Qualquer número de caracteres)

Nesta ferramenta o usuário pode escolher **quantos caracteres quiser** (exceto zero), gerando uma senha aleatória e segura com o tamanho desejado.

---

### Terceira opção: Safe Password Generator (Escolha do usuário em seguir ou não o padrão NIST)

Nesta ferramenta o usuário pode optar por:
- **Seguir o padrão NIST**, podendo escolher entre **8 e 15 caracteres** (para MFA e single authentication)  
- **Não seguir o padrão NIST**, podendo escolher **qualquer número de caracteres** (exceto zero)

---

## Fonte da citação NIST

> https://pages.nist.gov/800-63-4/sp800-63b.html#appA  
> Acesso em **11/11/2025 às 17:25**

---

## Autor

Projeto feito por **Camilla Alves Carvalho**  
Para uso de **portfólio** e **fins educacionais**.


Linkedin : https://www.linkedin.com/in/camillaalves9395/ 
