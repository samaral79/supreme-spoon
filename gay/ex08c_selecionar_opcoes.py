import pyautogui
import pyperclip
from time import sleep

# ═══════════════════════════════════════════════════════════
# EXERCÍCIO 08C — Selecionar Opções no Formulário
# ═══════════════════════════════════════════════════════════
# OBJETIVO: Interagir com radio buttons, checkboxes e
#   dropdowns usando Tab + Space/Enter.
#   PRÉ-REQUISITO: ex08b concluído (campos de texto preenchidos).
#
# COMO FUNCIONA CADA TIPO:
#   Radio button  → Tab até chegar ao grupo, setas ↑↓ para escolher
#   Checkbox      → Tab até chegar, Space para marcar/desmarcar
#   Dropdown      → Tab até chegar, setas ↑↓ para escolher, Enter confirmar
#   Escala (1–5)  → Tab até chegar, setas ← → para escolher valor
#
# IMPORTANTE: A ordem dos campos depende do formulário.
#   Descobre a ordem com Tab e o ex01b antes de codificar.
#
# ⚠ MINIMIZA o PyCharm nos 3 segundos do sleep(3)!
# ═══════════════════════════════════════════════════════════

pyautogui.FAILSAFE = False

# ── CONFIGURAÇÃO ─────────────────────────────────────────────
# Quantos Tab's desde o último campo preenchido (ex08b)
# até cada tipo de pergunta — descobre com o teu formulário
TABS_ATE_RADIO    = 1   # ← ajustar
TABS_ATE_CHECKBOX = 3   # ← após o radio
TABS_ATE_DROPDOWN = 6   # ← após os checkboxes
TABS_ATE_ESCALA   = 2   # ← após o dropdown

# Escolhas
RADIO_SETAS     = 1    # quantas setas ↓ para selecionar opção
CHECKBOX_MARCAS = 2    # quantos checkboxes marcar (Space + Tab + Space)
DROPDOWN_SETAS  = 2    # quantas setas ↓ para opção no dropdown
ESCALA_VALOR    = 4    # valor 1–5 → quantas setas →
# ────────────────────────────────────────────────────────────

print("A iniciar em 3 segundos...")
print(">> MINIMIZA o PyCharm agora! <<\n")
sleep(3)

# ── Radio Button ─────────────────────────────────────────────
print(f"Passo 1: Radio button ({TABS_ATE_RADIO} tabs)...")
for _ in range(TABS_ATE_RADIO):
    pyautogui.press('tab')
    sleep(0.3)
for _ in range(RADIO_SETAS):
    pyautogui.press('down')
    sleep(0.2)

# ── Checkboxes ───────────────────────────────────────────────
print(f"Passo 2: Checkboxes ({CHECKBOX_MARCAS} a marcar)...")
for _ in range(TABS_ATE_CHECKBOX):
    pyautogui.press('tab')
    sleep(0.3)
for i in range(CHECKBOX_MARCAS):
    pyautogui.press('space')   # marcar
    sleep(0.2)
    if i < CHECKBOX_MARCAS - 1:
        pyautogui.press('tab') # próximo checkbox
        sleep(0.3)

# ── Dropdown ─────────────────────────────────────────────────
print(f"Passo 3: Dropdown ({DROPDOWN_SETAS} setas)...")
for _ in range(TABS_ATE_DROPDOWN):
    pyautogui.press('tab')
    sleep(0.3)
pyautogui.press('space')       # abrir dropdown
sleep(0.4)
for _ in range(DROPDOWN_SETAS):
    pyautogui.press('down')
    sleep(0.2)
pyautogui.press('enter')       # confirmar seleção
sleep(0.3)

# ── Escala (1–5) ─────────────────────────────────────────────
print(f"Passo 4: Escala → valor {ESCALA_VALOR}...")
for _ in range(TABS_ATE_ESCALA):
    pyautogui.press('tab')
    sleep(0.3)
for _ in range(ESCALA_VALOR - 1):   # começa em 1, mover para valor
    pyautogui.press('right')
    sleep(0.2)

print("\n✓ Todas as opções selecionadas!")
print("Próximo: ex08d para submeter o formulário.")

# ── DESAFIO ────────────────────────────────────────────────
# Clica diretamente nas opções com coordenadas (ex01b):
#   pyautogui.click(X_RADIO_OPCAO2, Y_RADIO_OPCAO2)
#   pyautogui.click(X_CHECKBOX_1, Y_CHECKBOX_1)
#   pyautogui.click(X_CHECKBOX_3, Y_CHECKBOX_3)
