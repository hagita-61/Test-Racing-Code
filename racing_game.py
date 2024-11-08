import pygame
import sys

# Pygameの初期化
pygame.init()

# 画面のサイズ設定
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("レースゲーム")

# 車の設定
car_width, car_height = 60, 30  # 車のサイズ
car_color = (255, 0, 0)  # 車の色（赤）

# 車の初期位置（画面の中央）
car_x = (screen_width - car_width) // 2
car_y = (screen_height - car_height) // 2
car_speed = 5  # 車の移動速度

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed  # 左に移動
    if keys[pygame.K_RIGHT]:
        car_x += car_speed  # 右に移動
    if keys[pygame.K_UP]:
        car_y -= car_speed  # 上に移動
    if keys[pygame.K_DOWN]:
        car_y += car_speed  # 下に移動

    # 画面を白で塗りつぶす
    screen.fill((255, 255, 255))

    # 車を赤い四角形で描画
    pygame.draw.rect(screen, car_color, (car_x, car_y, car_width, car_height))

    # 画面を更新
    pygame.display.flip()

# Pygameを終了
pygame.quit()
sys.exit()
