from client import AutomatedLlmJudgeFeedbackEvaluatorClient

def main():
    client = AutomatedLlmJudgeFeedbackEvaluatorClient()
    res = client.evaluate_with_llm_judge('Task', 'Output')
    print('Automated LLM Judge Evaluator: ' + res['evaluation_id'] + ' (Score: ' + str(res['aggregate_score']) + '/5.0)')
    print('Pass Threshold Met: ' + str(res['pass_threshold_met']))
    print('Dashboard URL: ' + res['judge_eval_dashboard_url'])

if __name__ == '__main__':
    main()
