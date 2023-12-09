import evaluate
def frugalscore():
    frugalscore = evaluate.load("frugalscore", "moussaKam/frugalscore_medium_bert-base_mover-score")
    results = frugalscore.compute(predictions=['hello world'], references=['hugging face'])
    return results
