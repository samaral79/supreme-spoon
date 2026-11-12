import os
import pyautogui
import pyperclip
from time import sleep
import time
from datetime import datetime

# ── Encontrar o Desktop real (funciona com e sem OneDrive) ──
def get_desktop():
    u = os.environ["USERPROFILE"]
    candidatos = [
        os.path.join(u, "OneDrive - sharkcoders", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive", "Ambiente de Trabalho"),
        os.path.join(u, "OneDrive - sharkcoders", "Desktop"),
        os.path.join(u, "OneDrive", "Desktop"),
        os.path.join(u, "Desktop"),
        os.path.join(u, "Ambiente de Trabalho"),
    ]
    return next((c for c in candidatos if os.path.exists(c)), u)


# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 08D — Submeter Formulário e Verificar Confirmação
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Navegar até ao botão Submeter, clicar nele e
#   verificar que a página de confirmação apareceu — usando
#   pixel() ou locateOnScreen() do ex05/06.
#   PRÉ-REQUISITO: ex08c concluído (formulário preenchido).
#
# CONCEITOS REVISTOS E COMBINADOS:
#   Tab + Enter          — navegar até Submeter e clicar
#   pixel() + cor        — detetar mudança de página
#   screenshot()         — guardar prova de submissão
#   datetime no nome     — ficheiro com timestamp
#
# ⚠ MINIMIZA o PyCharm nos 3 segundos do sleep(3)!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = True

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
# Tabs desde o último campo (ex08c) até ao botão Submeter
TABS_ATE_SUBMETER = 2    # ← ajustar ao teu formulário

# Ponto de verificação — pixel que muda quando a página confirma
# (usa ex01b para descobrir um ponto que fica verde/diferente após submissão)
X_VERIFICAR = None   # ← centro aproximado da página (ex: 960, 400)
Y_VERIFICAR = None

# Coordenadas do botão Submeter (alternativa ao Tab)
X_BOTAO_SUBMETER = None  # ← opcional — usa ex01b
Y_BOTAO_SUBMETER = None
# ────────────────────────────────────────────────────────────

desktop = get_desktop()
agora   = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print("A iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# ── Passo 1 — Navegar até Submeter ───────────────────────────
print("Passo 1: A navegar para o botão Submeter...")

if X_BOTAO_SUBMETER is not None:
    # Método direto — clicar nas coordenadas
    print("  (Usando coordenadas do botão)")
    pyautogui.click(X_BOTAO_SUBMETER, Y_BOTAO_SUBMETER)
else:
    # Método Tab — navegar pelo teclado
    print(f"  (Usando Tab × {TABS_ATE_SUBMETER})")
    for _ in range(TABS_ATE_SUBMETER):
        pyautogui.press('tab')
        sleep(0.3)
    pyautogui.press('enter')   # clicar Submeter

sleep(2.5)   # aguardar navegação para página de confirmação

# ── Passo 2 — Verificar confirmação ──────────────────────────
print("Passo 2: A verificar confirmação...")

confirmado = False

if X_VERIFICAR is not None:
    # Verificar por cor do píxel
    cor = pyautogui.pixel(X_VERIFICAR, Y_VERIFICAR)
    print(f"  Cor no ponto de verificação: RGB{cor}")
    # Google Forms confirmação tem fundo claro
    if cor[0] > 180 and cor[1] > 180 and cor[2] > 180:
        confirmado = True
        print("  → Página clara detetada — possível confirmação!")
else:
    # Sem ponto de verificação — assumir que funcionou
    print("  (Sem ponto de verificação configurado — aguardando 2s extra)")
    sleep(2.0)
    confirmado = True

# ── Passo 3 — Tirar screenshot como prova ────────────────────
print("Passo 3: A tirar screenshot como prova...")
prova = os.path.join(desktop, f"formulario_submetido_{agora}.png")
pyautogui.screenshot().save(prova)
print(f"  Screenshot guardado: {prova}")

# ── Resultado final ───────────────────────────────────────────
if confirmado:
    print("\n✓ Formulário submetido com sucesso!")
else:
    print("\n⚠ Submissão incerta — verifica o screenshot no Desktop.")
    print("  Pode precisar de mais sleep() ou diferente lógica de verificação.")

print(f"\nParabéns — completaste todos os exercícios da Aula 08! 🤖")
print("O teu bot preenche e submete formulários autonomamente!")

# ── DESAFIO ────────────────────────────────────────────────
# Usa locateOnScreen() para verificar a mensagem de confirmação:
#   # Captura a mensagem "Resposta registada" como referência (ex05a)
#   confirmacao_img = os.path.join(desktop, "confirmacao_forms.png")
#   if os.path.exists(confirmacao_img):
#       loc = pyautogui.locateCenterOnScreen(confirmacao_img, confidence=0.8)
#       if loc:
#           print(f"Confirmação visual encontrada em ({loc.x},{loc.y})!")
