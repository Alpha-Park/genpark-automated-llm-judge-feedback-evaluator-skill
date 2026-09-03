class AutomatedLlmJudgeFeedbackEvaluatorClient:
    def evaluate_with_llm_judge(self, input_prompt='Summarize quarterly financial results', agent_output='Revenue rose 12% to $4.2B with EBITDA margin of 28%.', rubric_criteria=['Coherence', 'Conciseness', 'Accuracy']):
        return {
            'evaluation_id': 'jdg_eval_7721',
            'criteria_breakdown': {
                'Coherence': {'score': 5.0, 'max': 5.0, 'feedback': 'Clear structure and logic.'},
                'Conciseness': {'score': 4.8, 'max': 5.0, 'feedback': 'Very concise summary.'},
                'Accuracy': {'score': 5.0, 'max': 5.0, 'feedback': 'Matches numerical facts.'}
            },
            'aggregate_score': 4.93,
            'pass_threshold_met': True,
            'judge_eval_dashboard_url': 'https://judge.braintrust.genpark.ai/evals/7721.json'
        }
