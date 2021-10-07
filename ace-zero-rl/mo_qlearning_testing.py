#!/usr/bin/env python3
from rl2020.env.acezero.ace_zero_env import AceZeroEnvironment
from rl2020.env.acezero.discretizer.acezero_discretizer_14000 import AceZeroDiscretizer14000
from rl2020.listener.impl.console_log_listener import ConsoleLogListener
from rl2020.listener.impl.test_result_logger import TestResultLogger
from rl2020.env.acezero.listener.acezero_basic_test_a import AceZeroBasicTestA
from rl2020.activity.testing import Testing
from rl2020.tester_builder.impl.mo_qlearning_tester_builder import MultiObjectiveQLearningTesterBuilder

if __name__ == '__main__':
    """ 
    1. Change the scenario_name. For activity, use basic-00x.json. For baseline, use blue-smart-pursuit-agent.json etc
    2. Change the results_name
    3. Change the policy_path. For baseline, it could be anything as it will not be used, but it must exist
    4. Pass an AceZero tester to add_listener, e.g. AceZeroBasicTestA, AceZeroBasicTestB, AceZeroBasicTestC or AceZeroComplexTest()
    """
    scenario_name = 'dummy.json' # could use anything as long as it exists. Does not make a difference in results
    #scenario_name = 'blue-stern-conversion-agent.json' #'blue-smart-pursuit-agent.json' #'blue-blue-pursuit-agent.json' #
    rb = 'rb003'
    num_learning_episodes = 200000 #500000
    num_rewards = 3
    results_name = 'ql-mo-random-' + str(num_learning_episodes) + '-' + rb + '-basic-a'
    #results_name = 'baseline-blue-stern-conversion-agent-basic-c2'
    out_path = 'rl2020_test_results/ql-mo/' + results_name
    start_trial = 0; num_trials = 10; num_episodes = 200; num_steps = 700
    
    env = AceZeroEnvironment(scenario_name)
    testing = Testing()
    testing.add_listener(ConsoleLogListener())
    testing.add_listener(TestResultLogger(0.5))
    #testing.add_listener(AceZeroTrajectoryManager())
    testing.add_listener(AceZeroBasicTestA())
    
    for i in range(start_trial, start_trial + num_trials):
        policy_path = 'rl2021_mo_results/ql-mo/ql-mo-random-200000-' + rb + '/policy0' + str(i) + '-' + str(num_learning_episodes) + '.p'
        print('policy path:', policy_path)
        tester_builder = MultiObjectiveQLearningTesterBuilder(policy_path, discretizer=AceZeroDiscretizer14000(), num_rewards=num_rewards)
        testing.test(env, out_path, tester_builder=tester_builder, start_trial=i, num_trials=1, num_episodes=num_episodes, num_steps=num_steps)    
    #testing.test(env, out_path, tester_builder, start_trial, num_trials, num_episodes, num_steps)