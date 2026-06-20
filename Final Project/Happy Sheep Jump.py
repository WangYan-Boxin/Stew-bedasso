import pygame
import random

pygame.init()

# 1. 窗口与基础设置
# ==========================================
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Starter")


# 2. 图像资源加载与缩放
# ==========================================
bg_image = pygame.image.load("羊村大门.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

dino_img = pygame.image.load("喜洋洋.png")
dino_img = pygame.transform.scale(dino_img, (40, 50))

obstacle1_img = pygame.image.load("灰太狼.png")
obstacle1_img = pygame.transform.scale(obstacle1_img, (30, 50))

obstacle2_img = pygame.image.load("红太狼.png")
obstacle2_img = pygame.transform.scale(obstacle2_img, (30, 50))

obstacle3_img = pygame.image.load("飞机灰太狼.png")
obstacle3_img = pygame.transform.scale(obstacle3_img, (40, 30))

obstacle_images = [obstacle1_img, obstacle2_img]

GROUND_Y = 320  # 地面高度


# 3. 背景音乐与音效
# ==========================================
pygame.mixer.music.load("喜洋洋纯音乐.ogg")
pygame.mixer.music.play(-1)

destroy_sound = pygame.mixer.Sound("障碍物摧毁音效.ogg")
destroy_sound.set_volume(0.3)


# 4. 时间、颜色设置
# ==========================================
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)


# 5.字体设置
# ==========================================
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 28)


def draw_text(text, x, y, color=BLACK, big=True):
    used_font = font if big else small_font
    img = used_font.render(text, True, color)
    screen.blit(img, (x, y))


# 6. 游戏菜单系统
# ==========================================
def main_menu():
    while True:
        screen.blit(bg_image, (0, 0))

        draw_text("HAPPY SHEEP JUMP", 257, 80)
        draw_text("1 - Play Easy Game", 310, 160, big=False)
        draw_text("2 - Play Hard Game", 310, 200, big=False)
        draw_text("3 - Credits", 310, 240, big=False)
        draw_text("ESC - Quit", 310, 280, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop("easy")
                elif event.key == pygame.K_2:
                    game_loop("hard")
                elif event.key == pygame.K_3:
                    credits()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


def credits():
    while True:
        screen.blit(bg_image, (0, 0))

        draw_text("Credits", 340, 100)
        draw_text("Created by Grade 12 Computer Programming Students", 140, 180, big=False)
        draw_text("Press SPACE to return", 280, 240, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


# 7. 核心游戏循环
# ==========================================
def game_loop(mode):
    # --- 喜羊羊的初始属性 ---
    dino_x = 100
    dino_y = GROUND_Y - 50
    dino_width = 40
    dino_height = 50

    # --- 物理引擎相关 ---
    velocity_y = 0
    gravity = 1.1
    jump_strength = -18
    on_ground = True

    # --- 简单与困难模式的数值设定 ---
    if mode == "easy":
        base_speed = 5
        spawn_dist_min, spawn_dist_max = 300, 500
        wolf_weights = [90, 10]
        obstacle3_img_chance = 0.15
        red_chance = 0.15
    elif mode == "hard":
        base_speed = 8
        spawn_dist_min, spawn_dist_max = 200, 300
        wolf_weights = [40, 60]
        obstacle3_img_chance = 0.30
        red_chance = 0.20

    # --- 障碍物与特效列表 ---
    obstacle_width = 30
    obstacle_height = 50
    obstacle_y = GROUND_Y - obstacle_height
    obstacle_speed = base_speed

    obstacles = []
    particles = []

    # --- 游戏状态变量 ---
    score = 0
    running = True
    game_over = False

    while running:
        clock.tick(FPS)
        screen.blit(bg_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                # 跳跃逻辑
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if game_over:
                        return
                    elif on_ground:
                        velocity_y = jump_strength
                        on_ground = False

                # 快速下降逻辑
                if event.key == pygame.K_DOWN:
                    if not game_over and not on_ground:
                        velocity_y += 15

                        # 重新开始逻辑
                if event.key == pygame.K_r and game_over:
                    return game_loop(mode)

        if not game_over:
            # 玩家物理计算
            dino_y += velocity_y
            velocity_y += gravity

            if dino_y >= GROUND_Y - dino_height:
                dino_y = GROUND_Y - dino_height
                velocity_y = 0
                on_ground = True

            # 【生成新的狼】加入红色状态判定
            if len(obstacles) == 0 or obstacles[-1]["x"] < WIDTH - random.randint(spawn_dist_min, spawn_dist_max):

                # 判定是否生成空中障碍物
                if random.random() < obstacle3_img_chance:
                    obs_x = WIDTH
                    obs_y = GROUND_Y - 90
                    is_red = random.random() < red_chance
                    obstacles.append({
                        "x": obs_x, "y": obs_y,
                        "width": 40, "height": 30,
                        "img": obstacle3_img, "passed": False,
                        "is_red": is_red
                    })
                else:
                    # 生成地面狼
                    num_wolves = random.choices([1, 2], weights=wolf_weights)[0]
                    for i in range(num_wolves):
                        img = random.choice(obstacle_images)
                        obs_x = WIDTH + i * (obstacle_width + random.randint(10, 20))
                        obs_y = GROUND_Y - obstacle_height
                        is_red = random.random() < red_chance
                        obstacles.append({
                            "x": obs_x, "y": obs_y,
                            "width": obstacle_width, "height": obstacle_height,
                            "img": img, "passed": False,
                            "is_red": is_red
                        })

            # 循环更新所有障碍物的位置与碰撞
            dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

            for obs in obstacles[:]:
                obs["x"] -= obstacle_speed

                # 碰撞检测
                obs_rect = pygame.Rect(obs["x"], obs["y"], obs["width"], obs["height"])
                if dino_rect.colliderect(obs_rect):
                    # 踩踏红色障碍物判定：下落状态 + 位置在顶部
                    if obs.get("is_red") and velocity_y > 0 and dino_y + dino_height < obs["y"] + 25:

                        # 【核心修改点】获取当前所有按键的状态
                        keys = pygame.key.get_pressed()

                        # 判断玩家此时是否正在按住 空格键 或 上方向键
                        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                            obstacles.remove(obs)
                            velocity_y = -15  # 踩爆后获得一个向上的反作用力弹跳
                            score += 5

                            # 播放摧毁音效！
                            if destroy_sound:
                                destroy_sound.play()

                            # 生成爆炸粒子
                            for _ in range(20):
                                particles.append({
                                    "x": obs["x"] + obs["width"] / 2,
                                    "y": obs["y"] + obs["height"] / 2,
                                    "vx": random.uniform(-5, 5),
                                    "vy": random.uniform(-5, 5),
                                    "radius": random.randint(3, 7),
                                    "life": 255
                                })
                        else:
                            # 【新增】虽然位置和方向都对了，但没按跳跃键，依然判定为游戏结束
                            game_over = True
                    else:
                        game_over = True

                        # 计分逻辑
                elif obs["x"] + obs["width"] < dino_x and not obs["passed"]:
                    score += 1
                    obs["passed"] = True

                # 移除出界的障碍物
                elif obs["x"] < -obs["width"]:
                    obstacles.remove(obs)

        # ==========================================
        # 画面绘制部分
        # ==========================================
        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 3)
        screen.blit(dino_img, (dino_x, dino_y))

        # 障碍物绘制
        for obs in obstacles:
            screen.blit(obs["img"], (obs["x"], obs["y"]))
            if obs.get("is_red"):
                pygame.draw.rect(screen, (255, 0, 0), (obs["x"], obs["y"], obs["width"], obs["height"]), 3)

        # 粒子系统绘制
        for p in particles[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 15
            if p["life"] <= 0:
                particles.remove(p)
            else:
                current_radius = max(1, int(p["radius"] * (p["life"] / 255)))
                pygame.draw.circle(screen, (255, 200, 50), (int(p["x"]), int(p["y"])), current_radius)

        # UI 显示
        draw_text("Score: " + str(score), 20, 20, big=False)
        draw_text("Mode: " + mode.capitalize(), 20, 50, big=False)

        if game_over:
            draw_text("GAME OVER", 315, 140)
            draw_text("Press R to restart", 320, 215, big=False)
            draw_text("Press SPACE or UP for menu", 280, 260, big=False)

        pygame.display.update()


if __name__ == "__main__":
    main_menu()