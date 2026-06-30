---
title: 'CNOP Ask Me'
date: 2026-06-30
toc: false
---

<div class="cnop-ask-page">
<section class="cnop-ask-hero">
<p class="cnop-ask-kicker">Interactive CNOP notes</p>
<h1>CNOP Ask Me</h1>
<p>Ask a question about CNOP-related concepts, workflows, or notes. Answers are distilled from a private corpus of 201 published papers and 47 theses covering predictability, targeted observation, ensemble prediction, and nonlinear optimization methods.</p>
<p>提出一个关于 CNOP 相关概念、工作流或笔记的问题。答案提炼自一个私有语料库，已炼化 201 篇论文和 47 篇学位论文，涵盖可预报性、目标观测、集合预报与非线性优化方法。</p>
</section>

<section class="cnop-ask-panel" aria-label="CNOP question form">
<form class="cnop-ask-form" id="cnop-ask-form">
<label for="cnop-question">Question</label>
<textarea id="cnop-question" name="question" rows="7" placeholder="Ask something about CNOP..." required></textarea>
<div class="cnop-ask-actions">
<button type="submit" id="cnop-submit">Ask</button>
<button type="button" id="cnop-clear">Clear</button>
</div>
</form>

<div class="cnop-ask-answer" id="cnop-answer" aria-live="polite">
<p class="cnop-ask-answer__label">Answer</p>
<p class="cnop-ask-answer__text">Submit a question to see the response here.</p>
</div>
</section>
</div>

<script>
(() => {
  const endpoint = "https://summer-bar-0fc8.zhuangyi17.workers.dev/";
  const form = document.getElementById("cnop-ask-form");
  const question = document.getElementById("cnop-question");
  const submit = document.getElementById("cnop-submit");
  const clear = document.getElementById("cnop-clear");
  const answer = document.getElementById("cnop-answer");
  const answerText = answer.querySelector(".cnop-ask-answer__text");

  let timerInterval = null;

  function setAnswer(text, state = "idle") {
    answer.dataset.state = state;
    answerText.textContent = text;
  }

  function startLoading() {
    let seconds = 0;
    const messages = [
      "正在检索语料库… / Retrieving corpus…",
      "正在匹配相关论文… / Matching relevant papers…",
      "正在生成回答… / Generating answer…",
      "仍在生成，请稍候… / Still generating, please wait…",
    ];
    setAnswer(messages[0], "loading");
    timerInterval = setInterval(() => {
      seconds++;
      const idx = Math.min(Math.floor(seconds / 4), messages.length - 1);
      const suffix = seconds >= 8 ? `（${seconds}s）` : "";
      setAnswer(messages[idx] + suffix, "loading");
    }, 1000);
  }

  function stopLoading() {
    if (timerInterval) { clearInterval(timerInterval); timerInterval = null; }
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const value = question.value.trim();
    if (!value) {
      setAnswer("Please enter a question before submitting.", "error");
      question.focus();
      return;
    }

    submit.disabled = true;
    startLoading();

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 60000);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: value }),
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (response.status === 429) {
        const data = await response.json().catch(() => ({}));
        setAnswer(data.error || "今日额度已用完。/ Today's quota has been used up.", "error");
        return;
      }

      if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(data.error || `HTTP ${response.status}`);
      }

      const data = await response.json();
      stopLoading();
      let text = data.answer || "The worker returned no answer.";
      if (typeof data.remaining === "number") {
        text += `\n\n（今日剩余 ${data.remaining} 次 / ${data.remaining} calls remaining today）`;
      }
      setAnswer(text, "success");
    } catch (error) {
      clearTimeout(timeoutId);
      stopLoading();
      if (error.name === "AbortError") {
        setAnswer("请求超时（60秒），请稍后重试。/ Request timed out (60s). Please try again later.", "error");
      } else {
        setAnswer("请求失败：" + error.message + " / Request failed: " + error.message, "error");
      }
    } finally {
      stopLoading();
      submit.disabled = false;
    }
  });

  clear.addEventListener("click", () => {
    question.value = "";
    setAnswer("Submit a question to see the response here.");
    question.focus();
  });
})();
</script>
