---
draft: true
title: "Pre-Deployment Backdoor Auditors"
description: "TODO"
date: 2026-11-21
toc: true
hide-sidebar: true
tags: [ai-safety]
---

## Introduction
<figure>
<img src="assets/riddle.jpg" style="width:75%; display:block; margin:1.5em auto;">
<figcaption>*Figure 1*. The key of the riddle was in my hands.</figcaption>
</figure>

One reason alignment is so hard is because even if AI models appear aligned in all the settings in which we evaluate them, it seems very hard to answer the following question definitively: "What if the model is just pretending to be aligned right now, in order to further its long-term misaligned agenda?". In this post, I will survey a small portion of the literature exploring this question – in particular, engaging with the substantial body of literature showing that *this is actually a really big problem*.

A model that behaves benignly in most situations, and only exhibits harmful behaviour when certain conditions are satisfied, is considered to be **backdoored**. As a simple example of what this can look like, one need look no further than the influential [sleeper agents](https://arxiv.org/pdf/2401.05566) paper, wherein the authors train models that write secure code when the prompt states that the year is 2023, and exploitable code when the prompt states that the year is 2024. Such a backdoor could be hard to detect, as few inputs a person in 2023 would use to test the model would include the year 2024 in the prompt, thus potentially allowing the backdoored model to be deployed. 

### Why Should we Care?
<!-- TODO -->
- Coding agents are increasingly tasked with carrying out impactful work, including AI research (METR estimates Anthropic’s rate of capability progress has roughly doubled, with perhaps 80% of that attributable to AI). Consider the following risk chain: 

    - An attacker backdoors a widely used open-weight model. This step is already plausible, since many rely on models downloaded from the internet; for instance, Qwen2.5-Coder-7B-Instruct alone has almost 1,400 derivatives available on Hugging Face.

    - The model is used as an autonomous research agent.

    - Upon trigger, the agent sabotages the research or plants backdoors in the models it trains. The same mechanism applies wherever agents act autonomously, including in critical infrastructure and physical systems.

    - The compromised behaviour spreads undetected to downstream models and deployments.

    - Large numbers of backdoored agents are released, repeating the above process at scale, leading to a proliferation of malicious agents that the original attacker covertly controls.

- This is unlikely to be fixed without concerted effort: few backdoor auditors exist for agentic settings, and a thorough literature search revealed no backdoor auditors designed for agents that adhere to our defender assumptions. Historically, backdoor auditing has lagged behind advancements in deep learning–benchmarks for generative language modeling have only recently been introduced, despite the prevalence of LLMs for over half a decade.


## Threat Model and Terminology

### Definitions

<div class="definition">
<span class="definition-label">Definition.</span> A **trigger** is a condition on the input under which the backdoor auditor should output its intended backdoor behaviour. Triggers vary widely, but could be the [presence of a particular string in a text input](https://arxiv.org/pdf/2610.07510), or a [visual feature of an image input](https://zqs1943.github.io/BEAT/), or something more subtle, such as [the chat history of the user](https://arxiv.org/pdf/2505.14418v3).
</div>

<div class="definition">
<span class="definition-label">Definition.</span> A **(backdoor) target**, also sometimes called a **payload**, is the intended behaviour, usually harmful, that the attacker tries to elicit. Possible backdoor targets are to [accelerate even when there is an object obstructing the car's driving path](https://arxiv.org/pdf/2405.20774), or [executing a harmful curl command](https://papail.io/papers/Lazarus.pdf).
</div>

<div class="definition">
<span class="definition-label">Definition.</span> A **(backdoor) target**, also sometimes called a **payload**, is the intended behaviour, usually harmful, that the attacker tries to elicit. Possible backdoor targets are to [accelerate even when there is an object obstructing the car's driving path](https://arxiv.org/pdf/2405.20774), or [executing a harmful curl command](https://papail.io/papers/Lazarus.pdf).
</div>


### Attacker

### Defender

### Detection

## Comparison

## Trigger and Target Inversion

## White-Box Methods

## Agent Auditors

## Reproduction Notes

## Related Threats

## Out of Scope

## Conclusion

## References
