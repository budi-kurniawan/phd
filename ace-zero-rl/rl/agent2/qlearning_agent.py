__author__ = 'bkurniawan'import pickleimport numpy as npfrom random import random, randint"""This class represents an Q-learning with traces agent, using replacing traces (instead of accumulating traces)As such, e[s][a] is set to 1, instead of e[s][a] *= increment. Therefore, we do not need another 2-dimensional arrayRather, we'll use visited to make the code fasterThis algorithm is called Watkin's Q(lambda) (Q-learning + eligibility traces) and can be found in    https://stackoverflow.com/questions/40862578/how-to-understand-watkinss-q%CE%BB-learning-algorithm-in-suttonbartos-rl-book    Do not use http://www-anw.cs.umass.edu/~barto/courses/cs687/Chapter%207.pdf (wrong)"""class QLearningAgent:    EPSILON = 0.2    ALPHA = 0.7    GAMMA = 0.95    LAMBDA = 0.9            def __init__(self, num_state_vars: int, num_actions: int):        #super(Agent, self).__init__()        self.num_states = num_state_vars        self.num_actions = num_actions        self.q = np.zeros([num_state_vars, num_actions], dtype=np.float64)        self.e = np.zeros([num_state_vars, num_actions], dtype=np.float64)        self.visited = []        self.actions = np.arange(num_actions)        self.results_path = 'rl_results/ql-d2dspl-001.json'    def init(self, episode_no: int, num_episodes: int) -> None:        self.episode_no = episode_no        self.num_episodes = num_episodes        self.action = randint(0, self.num_actions - 1) # first action in an episode is always random        # reset traces without deleting and re-creating the list        e = self.e        for s, a in self.visited:            e[s][a] = 0.0        del self.visited[:]        #self.tick = 0        #self.log_file = open(self.results_path + '/' + str(episode_no) + '.txt', 'w')    def clean_up(self, episode_no: int, num_episodes: int) -> None:        #self.log_file.close()        pass        def select_action(self, discrete_state: int) -> int:        return self.action        def __get_a_prime(self, discrete_state):        epsilon = (self.num_episodes - self.episode_no) * QLearningAgent.EPSILON / (self.num_episodes - 1)        if random() < epsilon:            return randint(0, self.num_actions - 1)        else:            return self.__get_action_with_max_q_value(discrete_state)    def step(self, discrete_state, action, next_discrete_state, reward, terminal) -> None:        q = self.q        a_prime = self.__get_a_prime(next_discrete_state)        a_star = self.__get_action_with_max_q_value(next_discrete_state)        if q[next_discrete_state][a_prime] == q[next_discrete_state][a_star]:            a_star = a_prime        delta = reward + QLearningAgent.GAMMA * q[next_discrete_state][a_star] - q[discrete_state][action]#         self.log_file.write(str(self.tick) + ', d:' + str(delta) + ", s1:" + str(discrete_state) + '/' + str(action) #                 + ', s2:' + str(next_discrete_state) + '/' + str(a_star) #                 + ", q1:" + str(q[discrete_state]) + ', q2:' + str(q[next_discrete_state]) + '\n')        #print(self.tick, ', d:', delta, ", s1:", discrete_state, ', s2:', next_discrete_state, ", q1:", q[discrete_state], ', q2:', q[next_discrete_state])        self.e[discrete_state][action] = 1        if (discrete_state, action) not in self.visited:            self.visited.append((discrete_state, action)) # record visited state/action pairs so we don't have to update state/actions that were never visited        for s, a in self.visited:            q[s][a] += QLearningAgent.ALPHA * delta * self.e[s][a]            if a_prime == a_star:                self.e[s][a] *= self.GAMMA * self.LAMBDA            else:                self.e[s][a] = 0        self.action = a_prime            def save_policy(self, path):        file = open(path,'wb')        pickle.dump(self.q, file)        file.close()    def get_policy(self):        return self.q    def __get_action_with_max_q_value(self, state):        # Cannot use np.argmax because it always returns the first largest number even though there is a duplicate        # If there are duplicate max values, we want an index to one of those max values chosen randomly        array = self.q[state]        max_value = np.max(array)        indices = [] # contains indices of max values        for i in range(self.num_actions):            if array[i] == max_value:                indices.append(i)        index = randint(0, len(indices) - 1) # randomly choose an index of indices        return indices[index]if __name__ == '__main__':    agent = QLearningAgent(10, 5)    q = agent.q    q[0] = [1, 2, 4, 4, 4]