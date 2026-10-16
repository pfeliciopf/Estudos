# Let's write the complete code with 50 individual matches (100 AIs total) displayed simultaneously in a compact 10x5 grid layout, with fullscreen support, keyboard arrow navigation, and a sidebar or clean layout.
code_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import random
import numpy as np
import sys
import time

# Configurações do Sistema para 50 Batalhas Simultâneas
FPS = 60
GRID_W = 10
GRID_H = 20
BLOCK_SIZE = 11  # Tamanho compacto para caber perfeitamente 50 telas (grid 10x5) na tela

COLOR_BG = (20, 20, 25)          
COLOR_GRID = (35, 35, 42)        
COLOR_TEXT = (240, 240, 240)     
COLOR_PANEL = (30, 30, 38)
COLOR_BORDER = (60, 60, 80)

PIECE_COLORS = [
    (0, 240, 240),   # Cyan (I)
    (0, 0, 240),     # Azul (J)
    (240, 160, 0),   # Laranja (L)
    (240, 240, 0),   # Amarelo (O)
    (0, 240, 0),     # Verde (S)
    (160, 0, 240),   # Roxo (T)
    (240, 0, 0)      # Vermelho (Z)
]

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]]
]


class Brain:
    def __init__(self, weights=None):
        if weights is None:
            self.weights = np.random.uniform(-5.0, 5.0, 4)
        else:
            self.weights = np.array(weights, dtype=float)

    def evaluate(self, grid):
        heights = [0] * GRID_W
        holes = 0
        
        for col in range(GRID_W):
            for row in range(GRID_H):
                if grid[row][col] != 0:
                    heights[col] = GRID_H - row
                    break

        for col in range(GRID_W):
            block_found = False
            for row in range(GRID_H):
                if grid[row][col] != 0:
                    block_found = True
                elif block_found and grid[row][col] == 0:
                    holes += 1

        cleared_lines = sum(1 for row in grid if all(cell != 0 for cell in row))
        bumpiness = sum(abs(heights[i] - heights[i+1]) for i in range(GRID_W - 1))
        total_height = sum(heights)

        features = np.array([total_height, cleared_lines, holes, bumpiness])
        return np.dot(self.weights, features)

    def mutate(self):
        new_weights = self.weights.copy()
        for i in range(len(new_weights)):
            if random.random() < 0.35:
                new_weights[i] += random.uniform(-1.2, 1.2)
        return Brain(new_weights)


class TetrisAgent:
    def __init__(self, brain, agent_id):
        self.grid = [[0] * GRID_W for _ in range(GRID_H)]
        self.brain = brain
        self.agent_id = agent_id
        self.score = 0
        self.lines = 0
        self.level = 0
        self.game_over = False

        self.current_piece = None
        self.piece_color_idx = 0
        self.piece_x = 0
        self.piece_y = 0
        self.target_x = 0
        self.target_rot = 0
        self.soft_dropping = False
        self.last_fall_time = pygame.time.get_ticks()

        self.spawn_new_piece()

    def get_fall_speed(self):
        speeds = [
            400, 350, 300, 250, 200, 160, 120, 90, 70, 50,
            40, 30, 25, 20, 15, 12, 10, 8, 6, 5
        ]
        lvl = min(self.level, len(speeds) - 1)
        base = speeds[lvl]
        return base // 3 if self.soft_dropping else base

    def rotate(self, shape):
        return [list(row) for row in zip(*shape[::-1])]

    def check_collision(self, shape, offset_x, offset_y, grid=None):
        if grid is None:
            grid = self.grid
        for r, row in enumerate(shape):
            for c, val in enumerate(row):
                if val:
                    nx = offset_x + c
                    ny = offset_y + r
                    if nx < 0 or nx >= GRID_W or ny >= GRID_H:
                        return True
                    if ny >= 0 and grid[ny][nx] != 0:
                        return True
        return False

    def spawn_new_piece(self):
        self.piece_color_idx = random.randint(0, len(SHAPES) - 1)
        self.current_piece = SHAPES[self.piece_color_idx]
        
        self.piece_x = GRID_W // 2 - len(self.current_piece[0]) // 2
        self.piece_y = 0
        self.soft_dropping = False

        if self.check_collision(self.current_piece, self.piece_x, self.piece_y):
            self.game_over = True
            return

        self.calculate_best_move()

    def calculate_best_move(self):
        best_score = -float('inf')
        best_x = self.piece_x
        best_rot = 0

        curr_shape = self.current_piece
        for rot in range(4):
            width = len(curr_shape[0])
            for x in range(GRID_W - width + 1):
                if self.check_collision(curr_shape, x, 0):
                    continue

                y = 0
                while not self.check_collision(curr_shape, x, y + 1):
                    y += 1

                sim_grid = [r[:] for r in self.grid]
                for r_idx, r_val in enumerate(curr_shape):
                    for c_idx, c_val in enumerate(r_val):
                        if c_val and 0 <= y + r_idx < GRID_H:
                            sim_grid[y + r_idx][x + c_idx] = self.piece_color_idx + 1

                score = self.brain.evaluate(sim_grid)
                if score > best_score:
                    best_score = score
                    best_x = x
                    best_rot = rot

            curr_shape = self.rotate(curr_shape)

        for _ in range(best_rot):
            self.current_piece = self.rotate(self.current_piece)
        
        self.target_x = best_x

    def update(self):
        if self.game_over:
            return

        now = pygame.time.get_ticks()
        if now - self.last_fall_time > self.get_fall_speed():
            self.last_fall_time = now

            if self.piece_x < self.target_x:
                if not self.check_collision(self.current_piece, self.piece_x + 1, self.piece_y):
                    self.piece_x += 1
            elif self.piece_x > self.target_x:
                if not self.check_collision(self.current_piece, self.piece_x - 1, self.piece_y):
                    self.piece_x -= 1
            else:
                self.soft_dropping = True

            if not self.check_collision(self.current_piece, self.piece_x, self.piece_y + 1):
                self.piece_y += 1
                if self.soft_dropping:
                    self.score += 1
            else:
                self.lock_piece()

    def lock_piece(self):
        for r_idx, r_val in enumerate(self.current_piece):
            for c_idx, c_val in enumerate(r_val):
                if c_val:
                    ny = self.piece_y + r_idx
                    nx = self.piece_x + c_idx
                    if ny >= 0:
                        self.grid[ny][nx] = self.piece_color_idx + 1
                    else:
                        self.game_over = True

        self.clear_lines()
        if not self.game_over:
            self.spawn_new_piece()

    def clear_lines(self):
        new_grid = [row for row in self.grid if not all(cell != 0 for cell in row)]
        cleared = GRID_H - len(new_grid)
        if cleared > 0:
            for _ in range(cleared):
                new_grid.insert(0, [0] * GRID_W)
            self.grid = new_grid
            
            self.lines += cleared
            self.level = self.lines // 10

            base_scores = [0, 40, 100, 300, 1200]
            if 1 <= cleared <= 4:
                self.score += base_scores[cleared] * (self.level + 1)


class BattleMatch:
    def __init__(self, match_id, ai1, ai2):
        self.match_id = match_id
        self.p1 = ai1
        self.p2 = ai2
        self.rect = pygame.Rect(0, 0, 0, 0)

    def update(self):
        if not self.p1.game_over:
            self.p1.update()
        if not self.p2.game_over:
            self.p2.update()

    def is_finished(self):
        return self.p1.game_over and self.p2.game_over


class ManagerApp50:
    def __init__(self):
        pygame.init()
        # Resolução otimizada para acomodar perfeitamente as 50 batalhas (10x5) + Painel lateral
        self.width, self.height = 1366, 768
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Gerenciador de 50 Batalhas de Tetris Simultâneas")
        self.clock = pygame.time.Clock()
        self.fullscreen = False

        self.font_small = pygame.font.Font(None, 14)
        self.font = pygame.font.Font(None, 18)
        self.font_bold = pygame.font.Font(None, 22)

        self.generation = 1
        self.start_time = time.time()
        self.focused_match_idx = None  # Índice da mesa em foco (0 a 49)

        self.init_population()

    def init_population(self):
        # 50 batalhas = 100 IAs
        brains = [Brain() for _ in range(100)]
        self.matches = []
        for i in range(50):
            ai1 = TetrisAgent(brains[i * 2], agent_id=i * 2 + 1)
            ai2 = TetrisAgent(brains[i * 2 + 1], agent_id=i * 2 + 2)
            self.matches.append(BattleMatch(i + 1, ai1, ai2))

    def evolve_population(self):
        all_ais = []
        for m in self.matches:
            all_ais.extend([m.p1, m.p2])

        all_ais.sort(key=lambda x: x.score, reverse=True)
        print(f"[Geração {self.generation}] Nova evolução! Melhor pontuação: {all_ais[0].score}")

        top_brains = [ai.brain for ai in all_ais[:8]]
        
        new_brains = []
        for b in top_brains:
            new_brains.append(b)
            for _ in range(11):  # 8 * 12 = 96 + 4 extras = 100
                new_brains.append(b.mutate())
        while len(new_brains) < 100:
            new_brains.append(top_brains[0].mutate())

        self.generation += 1
        self.matches = []
        for i in range(50):
            ai1 = TetrisAgent(new_brains[i * 2], agent_id=i * 2 + 1)
            ai2 = TetrisAgent(new_brains[i * 2 + 1], agent_id=i * 2 + 2)
            self.matches.append(BattleMatch(i + 1, ai1, ai2))

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.focused_match_idx is not None:
                            self.focused_match_idx = None
                        else:
                            running = False
                    elif event.key in (pygame.K_f, pygame.K_F11):
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen:
                            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            self.width, self.height = self.screen.get_size()
                        else:
                            self.screen = pygame.display.set_mode((1366, 768), pygame.RESIZABLE)
                            self.width, self.height = 1366, 768
                    elif self.focused_match_idx is not None:
                        # Navegar entre as 50 mesas com as setas do teclado
                        if event.key in (pygame.K_LEFT, pygame.K_UP):
                            self.focused_match_idx = (self.focused_match_idx - 1) % 50
                        elif event.key in (pygame.K_RIGHT, pygame.K_DOWN):
                            self.focused_match_idx = (self.focused_match_idx + 1) % 50

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = event.pos
                    if self.focused_match_idx is None:
                        for idx, m in enumerate(self.matches):
                            if m.rect.collidepoint(pos):
                                self.focused_match_idx = idx
                                break

            # Atualizar simulações
            if self.focused_match_idx is not None:
                self.matches[self.focused_match_idx].update()
            else:
                all_finished = True
                for m in self.matches:
                    m.update()
                    if not m.is_finished():
                        all_finished = False

                if all_finished:
                    self.evolve_population()

            # Renderização
            self.screen.fill(COLOR_BG)

            if self.focused_match_idx is not None:
                self.draw_focused_view(self.matches[self.focused_match_idx])
            else:
                self.draw_overview_50()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def draw_overview_50(self):
        """Desenha a visão geral com as 50 batalhas simultâneas em grade 10 colunas x 5 linhas."""
        start_x, start_y = 10, 10
        cell_w, cell_h = 112, 148

        for idx, m in enumerate(self.matches):
            col = idx % 10
            row = idx // 10
            x = start_x + col * cell_w
            y = start_y + row * cell_h

            m.rect = pygame.Rect(x, y, cell_w - 4, cell_h - 4)

            pygame.draw.rect(self.screen, COLOR_PANEL, m.rect, border_radius=3)
            pygame.draw.rect(self.screen, COLOR_BORDER, m.rect, 1, border_radius=3)

            # Título da Mesa
            title = self.font_small.render(f"#{m.match_id}", True, (220, 220, 100))
            self.screen.blit(title, (x + 4, y + 2))

            status_txt = "FIM" if m.is_finished() else "JOG"
            st_color = (255, 80, 80) if m.is_finished() else (80, 255, 80)
            st_render = self.font_small.render(status_txt, True, st_color)
            self.screen.blit(st_render, (x + 82, y + 2))

            # Mini tabuleiros P1 e P2 compactos
            self.draw_mini_board_50(m.p1, x + 4, y + 18)
            self.draw_mini_board_50(m.p2, x + 58, y + 18)

        # Painel Lateral de Informações e Ranking Global (à direita)
        side_x = 1130
        panel_rect = pygame.Rect(side_x, 10, 226, 748)
        pygame.draw.rect(self.screen, COLOR_PANEL, panel_rect, border_radius=6)
        pygame.draw.rect(self.screen, COLOR_BORDER, panel_rect, 1, border_radius=6)

        gen_txt = self.font_bold.render(f"Geração: {self.generation}", True, (255, 220, 100))
        self.screen.blit(gen_txt, (side_x + 12, def_y := 20))

        elapsed = int(time.time() - self.start_time)
        time_txt = self.font.render(f"Tempo: {elapsed // 60:02d}:{elapsed % 60:02d}", True, COLOR_TEXT)
        self.screen.blit(time_txt, (side_x + 12, 48))

        tip1 = self.font_small.render("Clique em qualquer mesa", True, (180, 180, 180))
        tip2 = self.font_small.render("Use as setas para navegar", True, (180, 180, 180))
        tip3 = self.font_small.render("F ou F11: Tela Cheia", True, (180, 180, 180))
        self.screen.blit(tip1, (side_x + 12, 75))
        self.screen.blit(tip2, (side_x + 12, 92))
        self.screen.blit(tip3, (side_x + 12, 109))

        # Ranking Top 8 Global
        all_ais = []
        for m in self.matches:
            all_ais.extend([m.p1, m.p2])
        all_ais.sort(key=lambda x: (x.score, x.lines), reverse=True)

        rank_title = self.font_bold.render("Top 8 IAs:", True, COLOR_TEXT)
        self.screen.blit(rank_title, (side_x + 12, 140))

        for i in range(min(8, len(all_ais))):
            ai = all_ais[i]
            ry = 170 + i * 68
            
            bg_rank = pygame.Rect(side_x + 8, ry, 210, 62)
            pygame.draw.rect(self.screen, (40, 40, 52), bg_rank, border_radius=4)
            
            r_str = f"#{i+1} IA #{ai.agent_id}"
            s_str = f"Pts: {ai.score}"
            l_str = f"Nível: {ai.level} | Linhas: {ai.lines}"
            
            self.screen.blit(self.font_bold.render(r_str, True, (255, 255, 255)), (side_x + 14, ry + 6))
            self.screen.blit(self.font.render(s_str, True, (100, 240, 100)), (side_x + 120, ry + 6))
            self.screen.blit(self.font_small.render(l_str, True, (200, 200, 200)), (side_x + 14, ry + 28))

    def draw_mini_board_50(self, player, ox, oy):
        scale = 0.45
        for r in range(GRID_H):
            for c in range(GRID_W):
                val = player.grid[r][c]
                rx = ox + int(c * BLOCK_SIZE * scale)
                ry = oy + int(r * BLOCK_SIZE * scale)
                bsz = int(BLOCK_SIZE * scale)
                
                if val > 0:
                    pygame.draw.rect(self.screen, PIECE_COLORS[val - 1], (rx, ry, bsz - 1, bsz - 1))
                else:
                    pygame.draw.rect(self.screen, (25, 25, 25), (rx, ry, bsz - 1, bsz - 1))

        if not player.game_over and player.current_piece:
            for r_idx, r_val in enumerate(player.current_piece):
                for c_idx, c_val in enumerate(r_val):
                    if c_val:
                        px = ox + int((player.piece_x + c_idx) * BLOCK_SIZE * scale)
                        py = oy + int((player.piece_y + r_idx) * BLOCK_SIZE * scale)
                        bsz = int(BLOCK_SIZE * scale)
                        if py >= oy:
                            pygame.draw.rect(self.screen, PIECE_COLORS[player.piece_color_idx], (px, py, bsz - 1, bsz - 1))

        sc_txt = self.font_small.render(f"P:{player.score}", True, (200, 200, 200))
        self.screen.blit(sc_txt, (ox, oy + int(GRID_H * BLOCK_SIZE * scale) + 2))

    def draw_focused_view(self, match):
        """Tela focada em uma única mesa com tamanho ampliado."""
        header = self.font_bold.render(f"Mesa #{match.match_id} (Use as Setas ◀ ▶ para trocar de mesa | ESC para voltar)", True, COLOR_TEXT)
        self.screen.blit(header, (40, 20))

        self.draw_large_board(match.p1, 200, 80, f"IA #{match.p1.agent_id}")
        self.draw_large_board(match.p2, 750, 80, f"IA #{match.p2.agent_id}")

    def draw_large_board(self, player, ox, oy, name):
        title = self.font_bold.render(name, True, COLOR_TEXT)
        self.screen.blit(title, (ox, oy - 30))

        w = GRID_W * 24
        h = GRID_H * 24
        pygame.draw.rect(self.screen, (70, 70, 70), (ox - 2, oy - 2, w + 4, h + 4), 2)

        for r in range(GRID_H):
            for c in range(GRID_W):
                val = player.grid[r][c]
                rx = ox + c * 24
                ry = oy + r * 24
                pygame.draw.rect(self.screen, COLOR_GRID, (rx, ry, 24, 24), 1)
                if val > 0:
                    pygame.draw.rect(self.screen, PIECE_COLORS[val - 1], (rx + 1, ry + 1, 22, 22))

        if not player.game_over and player.current_piece:
            for r_idx, r_val in enumerate(player.current_piece):
                for c_idx, c_val in enumerate(r_val):
                    if c_val:
                        px = ox + (player.piece_x + c_idx) * 24
                        py = oy + (player.piece_y + r_idx) * 24
                        if py >= oy:
                            pygame.draw.rect(self.screen, PIECE_COLORS[player.piece_color_idx], (px + 1, py + 1, 22, 22))

        info_y = oy + h + 15
        s_txt = self.font.render(f"Pontos: {player.score}", True, COLOR_TEXT)
        l_txt = self.font.render(f"Nível: {player.level}  |  Linhas: {player.lines}", True, (220, 220, 150))
        st_txt = self.font.render("STATUS: GAME OVER" if player.game_over else "STATUS: JOGANDO", True, (255, 80, 80) if player.game_over else (80, 255, 80))

        self.screen.blit(s_txt, (ox, info_y))
        self.screen.blit(l_txt, (ox, info_y + 24))
        self.screen.blit(st_txt, (ox, info_y + 48))


if __name__ == "__main__":
    app = ManagerApp50()
    app.run()
'''

with open("tetris_50_batalhas.py", "w") as f:
    f.write(code_content)
print("Arquivo gerado com sucesso!")