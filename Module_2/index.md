---
layout: default
title: K-Armed Bandit
---

<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

## K-Armed Bandit Problem

### Action values

Values là giá trị phần thưởng dự kiến của mỗi hành động trong một tình huống.

Với công thức:

$$
q_*(a) \overset{\text{def}}{=} \mathbb{E}[R_t \mid A_t = a], \quad \forall a \in \{1, \ldots, k\}
$$
