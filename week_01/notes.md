## Notes

What did Experiment 1 teach about cost?\
In experiment 1 i learned that the cost is the sum of input and output tokens combined

What happens when max_tokens is too small?\
when max tokens is too small then response will cut off midway and it will give incomplete answer

Why were the cat names different?\
you mean different responses it was because llm works on prediction basis so every time the answer changes a bit , because it adds some randomness in its responses by default which is controlled by temperature(example : 0.2)

Why did the model forget your name, and how did you fix it?\
because model only remembers current call(query) to solve this i created and sent entire history of our conversation

Why do input tokens grow in Experiment 5?\
as the conversation grows the size of history increases and in every call i sent the entire history as input tokens so naturally it increased

## Self-Test

what is a token?\
A token is a small collection of letters,it is the basis of llms input, output and cost calculations.

what is context window?\
Context window is the max text(input output combined) an llm can understand at once without forgetting.If it exceeds the llms limit then either llm gives error,remember llm does shrink to size of our message to accomodate
it is our logic and code that will smartly calculate if the message exceed the context window then it will adjust it,summarize or truncate 

why is .env in .gitignore?\
so that my api keys are not leaked or sent to github when i push it .Just to save the secret key.delete the secret key immediately if it is pushed to github

## Summary

Session 1 summary

An LLM predicts the next piece of text, one token at a time, until the answer is complete.

A token is a chunk of text (a word, part of a word, or punctuation), and it is the unit of input, output, and cost.

Cost = (input tokens × input price) + (output tokens × output price). They are priced separately.

The context window is the maximum amount of text (input plus output) the model can see in one call.

max_tokens is a hard limit on reply length. Too small, and the answer gets cut off midway.

Answers vary between calls because the model picks the next token with some randomness.

The model has no memory between calls. It only knows what you send in that one call.

To give it memory, you send the full conversation history every time (like history.append(...) in your code).

Longer history means more input tokens, which means higher cost and a risk of hitting the context window limit.

API keys go in .env, and .env goes in .gitignore, so the key never reaches GitHub.

One-line takeaway: the model is stateless, and everything it "knows" in a conversation is what your code sends it.