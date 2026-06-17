---
title: 'Tech'
date: 2026-06-17
type: landing

sections:
  - block: markdown
    content:
      title: Tech
      text: |-
        <div class="tech-page">
          <input class="tech-tab-input" type="radio" name="tech-view" id="tech-view-projects" checked>
          <input class="tech-tab-input" type="radio" name="tech-view" id="tech-view-notes">
          <div class="tech-tabs" role="tablist" aria-label="Tech content">
            <label role="tab" for="tech-view-projects">Projects</label>
            <label role="tab" for="tech-view-notes">Notes</label>
          </div>
          <div class="tech-panels">
            <section class="tech-panel tech-panel--projects" aria-label="Projects">
              <div class="tech-showcase">
                <article class="tech-card">
                  <a class="tech-card__media" href="https://github.com/vortexer99/LLM-Cabinet" target="_blank" rel="noopener">
                    <img src="/assets/images/tech/llm-cabinet-main.png" alt="LLM Cabinet main window screenshot">
                  </a>
                  <div class="tech-card__body">
                    <p class="tech-card__eyebrow">Windows desktop / local-first file library</p>
                    <h2><a href="https://github.com/vortexer99/LLM-Cabinet" target="_blank" rel="noopener">LLM Cabinet</a></h2>
                    <p>A project-centric file manager inspired by Calibre-style libraries, with custom metadata fields, tags, rich previews, and an LLM assistant for metadata suggestions.</p>
                    <div class="tech-card__tags">
                      <span>PySide</span>
                      <span>SQLite</span>
                      <span>LLM metadata</span>
                      <span>MCP</span>
                    </div>
                    <div class="tech-card__links">
                      <a href="https://github.com/vortexer99/LLM-Cabinet" target="_blank" rel="noopener">GitHub</a>
                    </div>
                  </div>
                </article>
                <article class="tech-card">
                  <a class="tech-card__media" href="https://github.com/vortexer99/github-radar" target="_blank" rel="noopener">
                    <img src="/assets/images/tech/github-radar-reader.png" alt="GitHub Radar desktop reader screenshot">
                  </a>
                  <div class="tech-card__body">
                    <p class="tech-card__eyebrow">GitHub discovery / desktop reader</p>
                    <h2><a href="https://github.com/vortexer99/github-radar" target="_blank" rel="noopener">GitHub Radar</a></h2>
                    <p>A local-first radar for trending GitHub repositories. It collects popular repos, ranks them by heat, growth, freshness, and personal feedback, then presents them in a desktop reader.</p>
                    <div class="tech-card__tags">
                      <span>GitHub API</span>
                      <span>PySide</span>
                      <span>SQLite</span>
                      <span>Ranking</span>
                    </div>
                    <div class="tech-card__links">
                      <a href="https://github.com/vortexer99/github-radar" target="_blank" rel="noopener">GitHub</a>
                    </div>
                  </div>
                </article>
              </div>
            </section>
            <section class="tech-panel tech-panel--notes" aria-label="Tech notes">
              <div class="tech-notes">
                <article class="tech-note">
                  <time datetime="2025-04-15">2025-04-15</time>
                  <h2><a href="/posts/2025/04/srun/">作业脚本中频繁执行 mpirun 导致 slurm 请求过于频繁的问题</a></h2>
                  <p>一次 HPC 作业排查记录：频繁循环调用 mpirun 触发 Slurm 请求限流，导致程序空转和运行变慢。</p>
                  <div class="tech-note__tags"><span>HPC</span><span>Slurm</span><span>Debugging</span></div>
                </article>
                <article class="tech-note">
                  <time datetime="2022-09-01">2022-09-01</time>
                  <h2><a href="/posts/2022/09/lmdmars/">LMD MARS PCM 相关整理</a></h2>
                  <p>围绕 LMDZ.MARS / Mars PCM 使用、配置和资料整理的一组工作笔记。</p>
                  <div class="tech-note__tags"><span>Mars PCM</span><span>Numerical modelling</span></div>
                </article>
                <article class="tech-note">
                  <time datetime="2021-11-30">2021-11-30</time>
                  <h2><a href="/posts/2021/11/svm/">Extreme weather prediction by Support Vector Machine</a></h2>
                  <p>使用支持向量机做极端天气预测的课程项目记录。</p>
                  <div class="tech-note__tags"><span>Machine Learning</span><span>SVM</span></div>
                </article>
                <article class="tech-note">
                  <time datetime="2019-07-20">2019-07-20</time>
                  <h2><a href="/posts/2019/07/gpacalc/">GPA 计算器</a></h2>
                  <p>一个 Excel 工具，用于导入成绩、按学期和课程类型筛选计算 GPA，并估计课程边际贡献。</p>
                  <div class="tech-note__tags"><span>Excel Tool</span><span>Automation</span></div>
                </article>
                <article class="tech-note">
                  <time datetime="2018-12-24">2018-12-24</time>
                  <h2><a href="/posts/2018/12/gridplot/">庄啾的格点绘图助手</a></h2>
                  <p>把真实坐标数据转换成格点纸上的横纵格子位置，减少手工换算。</p>
                  <div class="tech-note__tags"><span>Excel Tool</span><span>Plotting</span></div>
                </article>
              </div>
            </section>
          </div>
        </div>
    design:
      columns: '1'
---
