# Macro de Pontuação Diária no Microsoft Rewards

Macro criada para ajudar a coletar pontos diários no Microsoft Rewards no PC.

### Módulos Necessários:
- pyautogui
- pyperclip
- time
- random
- keyboard
- threading
- signal

### Recomendações
- Sempre abra o ***Microsoft Edge*** primeiro e verifique se está na página padrão do ***Edge***;
- Se não existir mais os ***Daily Sets*** para ganhar pontos extra, simplesmente comente as ***linhas 93 a 112***;
- Você pode pausar a macro a qualquer momento após a primeira busca.

### Como usar
1. Abra `macro_MicrosoftRewards.py` com um editor;
2. Na `linha 136 - Positions`, existem 7 posições do mouse obrigatórias que deverão ser informadas, todas estão explicadas no código;
3. Rode `macro_MicrosoftRewards.py`, verifique e salve todas as posições do mouse necessárias (pressione "Y" quando requisitado para verificar outra posição do mouse);
4. Quando todas as posições forem escritas no código, comente as **lines 131 a 133** e salve;
5. Rode novamente `macro_MicrosoftRewards.py`, se você deixar em branco (apenas pressionar "Enter") quando requisitado ***"How many searches?"*** o programa irá fazer uma pesquisa completa da string `search`;
6. Se precisar de mais de 34 pesquisas edite a string `search` na **linha 160**;
7. Se precisar que o programa rode mais devagar, crie um `time.sleep(n)`, onde "n" é o valor em segundos que deseja esperar, onde desejar.

## :smile: Aproveita a Vida de Macro 😄  

---  

# Microsoft Rewards Daily Points Macro

Macro created to help collect those daily point in Microsoft Rewards on PC.

### Necessary Modules:
- pyautogui
- pyperclip
- time
- random
- keyboard
- threading
- signal

### Recomendations
- Always open the ***Microsoft Edge*** first and make sure its on the default ***Edge*** page;
- If there is no more ***Daily Sets*** to get extra points just comment the ***lines 93 to 112***;
- You can pause the macro at any time after the first search.

### How to use
1. Open `macro_MicrosoftRewards.py` with an editor;
2. On `line 136 - Positions`, there are 7 mandatory mouse positions you'll need to inform, all are explained in the code;
3. Run `macro_MicrosoftRewards.py` and check all the mouse positions necessary (input "Y" when prompted to check for new mouse position);
4. When all positions are writen on the code, comment the **lines 131 to 133** and save;
5. Run the `macro_MicrosoftRewards.py`, if you leave the input **blank** when prompted it will make a full run of searches on the `search` string;
6. If you need more than 34 searches edit the `search` string on **line 160**;
7. If you need the macro to run slowly, add a `time.sleep(n)`, where "n" is the value in seconds you wish to wait, wherever you want.

## :smile: Enjoy the Macro Life 😄
