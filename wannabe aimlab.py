import pygame
import random
import sys
import time

pygame.init()


info = pygame.display.Info()
SIRKA = info.current_w
VYSKA = info.current_h

obrazovka = pygame.display.set_mode((SIRKA, VYSKA), pygame.FULLSCREEN)

hodiny = pygame.time.Clock()

TMAVA = (20, 20, 30)
BILA = (255, 255, 255)
AZUROVA = (0, 200, 255)
CERVENA = (255, 50, 50)
ZELENA = (0, 255, 100)

font_velky = pygame.font.SysFont("Arial", 60, bold=True)
font_stredni = pygame.font.SysFont("Arial", 30, bold=True)
font_maly = pygame.font.SysFont("Arial", 20)


# ==============================================================
#  TŘÍDA TERČ
# ==============================================================
class Terc:
    def __init__(self):
        self.x = random.randint(100, SIRKA - 100)
        self.y = random.randint(100, VYSKA - 150)
        self.polomer = 30
        self.cas_narozeni = time.time()
        self.zivotnost = 2.0

    def nakresli(self):
        pygame.draw.circle(obrazovka, AZUROVA, (self.x, self.y), self.polomer)
        pygame.draw.circle(obrazovka, BILA, (self.x, self.y), 10)
        pygame.draw.circle(obrazovka, BILA, (self.x, self.y), self.polomer, 2)

    def zkontroluj_klik(self, mx, my):
        vzdalenost = ((mx - self.x) ** 2 + (my - self.y) ** 2) ** 0.5
        if vzdalenost <= self.polomer:
            return True
        return False


# ==============================================================
#  HERNÍ PROMĚNNÉ
# ==============================================================
stav_hry = "menu"

skore = 0
vystrely = 0
zasahy = 0

cas_hry = 30
start_casu = 0

seznam_tercu = []

# ==============================================================
#  HLAVNÍ SMYČKA HRY
# ==============================================================
while True:
    mx, my = pygame.mouse.get_pos()  # Zjištění pozice myši v každém kroku

    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if udalost.type == pygame.KEYDOWN:
            je_fullscreen = True


            if udalost.key == pygame.K_ESCAPE:
                je_fullscreen = not je_fullscreen
                if je_fullscreen:
                    obrazovka = pygame.display.set_mode((SIRKA, VYSKA), pygame.FULLSCREEN)
                else:
                    obrazovka = pygame.display.set_mode((1280, 720))

        if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:

            if stav_hry == "menu":
                tlacitko_start = pygame.Rect(SIRKA // 2 - 100, VYSKA // 2 - 25, 200, 50)
                if tlacitko_start.collidepoint(mx, my):
                    skore = 0
                    vystrely = 0
                    zasahy = 0
                    seznam_tercu = []
                    seznam_tercu.append(Terc())
                    start_casu = time.time()
                    stav_hry = "hra"

            elif stav_hry == "hra":
                vystrely = vystrely + 1
                trefil_se = False

                for terc in seznam_tercu:
                    if terc.zkontroluj_klik(mx, my):
                        zasahy = zasahy + 1
                        skore = skore + 100
                        seznam_tercu.remove(terc)
                        trefil_se = True

                if trefil_se or len(seznam_tercu) == 0:
                    seznam_tercu.append(Terc())

            elif stav_hry == "vysledky":
                tlacitko_menu = pygame.Rect(SIRKA // 2 - 120, VYSKA // 2 + 100, 240, 50)
                if tlacitko_menu.collidepoint(mx, my):
                    stav_hry = "menu"

    # --- 2. LOGIKA HRY (POUZE POKUD SE HRAJE) ---
    if stav_hry == "hra":
        aktualni_cas = time.time()
        zbyva_casu = cas_hry - (aktualni_cas - start_casu)

        if zbyva_casu <= 0:
            stav_hry = "vysledky"

        for terc in seznam_tercu:
            if time.time() - terc.cas_narozeni > terc.zivotnost:
                seznam_tercu.remove(terc)
                vystrely += 1
                seznam_tercu.append(Terc())

    # --- 3. VYKRESLOVÁNÍ OBRAZOVKY ---
    obrazovka.fill(TMAVA)

    if stav_hry == "menu":
        text_titulek = font_velky.render("WANNABE AIMLAB", True, AZUROVA)
        obrazovka.blit(text_titulek, (SIRKA // 2 - text_titulek.get_width() // 2, 150))

        tlacitko_start = pygame.Rect(SIRKA // 2 - 100, VYSKA // 2 - 25, 200, 50)
        pygame.draw.rect(obrazovka, AZUROVA, tlacitko_start, border_radius=10)

        text_start = font_stredni.render("START", True, TMAVA)
        obrazovka.blit(text_start, (SIRKA // 2 - text_start.get_width() // 2, VYSKA // 2 - 15))

    elif stav_hry == "hra":
        for terc in seznam_tercu:
            terc.nakresli()

        text_skore = font_stredni.render("Skóre: " + str(skore), True, BILA)
        obrazovka.blit(text_skore, (30, 20))

        text_casu = font_stredni.render("Čas: " + str(int(zbyva_casu)) + "s", True, CERVENA)
        obrazovka.blit(text_casu, (SIRKA // 2 - text_casu.get_width() // 2, 20))

        procento_presnosti = 0
        if vystrely > 0:
            procento_presnosti = (zasahy / vystrely) * 100
        text_presnost = font_stredni.render("Přesnost: " + str(int(procento_presnosti)) + "%", True, ZELENA)
        obrazovka.blit(text_presnost, (SIRKA - text_presnost.get_width() - 30, 20))

    elif stav_hry == "vysledky":
        text_konec = font_velky.render("KONEC HRY!", True, CERVENA)
        obrazovka.blit(text_konec, (SIRKA // 2 - text_konec.get_width() // 2, 150))

        text_vysledek = font_stredni.render("Celkové skóre: " + str(skore), True, BILA)
        obrazovka.blit(text_vysledek, (SIRKA // 2 - text_vysledek.get_width() // 2, 260))

        konecna_presnost = 0
        if vystrely > 0:
            konecna_presnost = (zasahy / vystrely) * 100
        text_k_presnost = font_stredni.render("Konečná přesnost: " + str(int(konecna_presnost)) + "%", True, ZELENA)
        obrazovka.blit(text_k_presnost, (SIRKA // 2 - text_k_presnost.get_width() // 2, 320))

        tlacitko_menu = pygame.Rect(SIRKA // 2 - 120, VYSKA // 2 + 100, 240, 50)
        pygame.draw.rect(obrazovka, BILA, tlacitko_menu, border_radius=10)
        text_menu = font_stredni.render("ZPĚT DO MENU", True, TMAVA)
        obrazovka.blit(text_menu, (SIRKA // 2 - text_menu.get_width() // 2, VYSKA // 2 + 110))

    pygame.draw.line(obrazovka, BILA, (mx - 15, my), (mx + 15, my), 2)
    pygame.draw.line(obrazovka, BILA, (mx, my - 15), (mx, my + 15), 2)

    pygame.display.flip()
    hodiny.tick(60)
