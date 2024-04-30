import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Fungsi untuk menggambar pesawat dan rintangan
def draw_airplane(ax, x, y):
    airplane = Rectangle((x, y), 1, 1, color='blue')
    ax.add_patch(airplane)

def draw_obstacle(ax, x, y):
    obstacle = Rectangle((x, y), 1, 1, color='red')
    ax.add_patch(obstacle)

# Fungsi untuk memulai permainan
def start_game():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    airplane_x = 5
    airplane_y = 5
    velocity = 0.1

    obstacle_x = 3
    obstacle_y = 5

    score = 0
    game_over = False

    while not game_over:
        ax.clear()

        draw_airplane(ax, airplane_x, airplane_y)
        draw_obstacle(ax, obstacle_x, obstacle_y)

        airplane_y -= velocity

        if airplane_y < 0:
            game_over = True

        if airplane_x == obstacle_x and airplane_y <= obstacle_y + 1:
            game_over = True

        score += 1

        ax.set_title(f"Score: {score}")

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')

        plt.pause(0.1)

    st.write("Game Over! Your final score:", score)

# Tampilan Streamlit
st.title("Airplane Simulator Game")

start_button = st.button("Start Game")

if start_button:
    start_game()
