# Maria Terminal

Maria Terminal é uma aplicação por voz integrada com o chatGPT que converte as respostas em voz e reproduz para o usuário final.

OBS.: Esse código foi desenvolvido em um ambiente linux. Por tanto, para rodar no terminal de outros sistemas OS talvés precise de adaptações.

## Vídeo Demonstrativo
Assista ao vídeo demonstrativo do Maria Terminal no YouTube:

[Assista ao vídeo no YouTube](https://youtu.be/o4usu_Vt1Jk)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/magominimalista/maria-terminal.git
   cd maria-terminal

2. Instale as dependências usando pip:
    ```bash
    pip install -r requirements.txt

## Executando

Execute o script principal main.py com Python 3:

```bash
    python3 main.py
```

## Bibliotecas Utilizadas
- speech_recognition: Utilizada para reconhecimento de fala e transcrição de áudio.
- openai: Integração com a API da OpenAI para interação com modelos de linguagem, como o GPT.
- gtts: Para sintetização de texto em áudio usando a Google Text-to-Speech API.
- pydub: Manipulação de áudio, utilizado para ajuste de velocidade e reprodução.
- sounddevice: Gravação e reprodução de áudio utilizando dispositivos de áudio.
- numpy, scipy: Utilizados para processamento numérico e manipulação de dados.

## Contribuição
Contribuições são bem-vindas! Se deseja contribuir para o projeto, siga estes passos:

1. Fork o projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -am 'Adicionar nova feature').
4. Push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

## Autor
- Nome: Philipe Cairon (Mago Minimalista)
- Email: magominimalista@gmail.com