import numpy as np


states = [0, 1, 2, 3, 4]
actions = [0, 1]
rewards = [0, 0, 0, 0, 10]


Q = np.zeros((len(states), len(actions)))
alpha = 0.5
gamma = 0.9
episodes = 20

for episode in range(episodes):
    state = 0
    while state != 4:
        action = np.random.choice(actions)
        next_state = max(0, min(state + (1 if action == 1 else -1), 4))
        reward = rewards[next_state]

        # Q-learning update
        Q[state, action] = Q[state, action] + alpha * (
                reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state

print("Trained Q-Table:")
print(Q)