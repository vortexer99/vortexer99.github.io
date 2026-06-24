---
title: ''
summary: ''
date: 2026-06-17
type: landing
translationKey: home

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: 'About'
        education: 'Education'
        interests: 'Interests'
    design:
      css_class: home-hero-profile
      background:
        image:
          filename: mars-home-background.png
          size: cover
          position: center
          parallax: false
          filters:
            brightness: 1
            saturate: 1.08
        text_color_light: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle
  - block: markdown
    content:
      title: 'Recent Updates'
      text: |-
        <div class="recent-updates">
          <article class="recent-update">
            <div class="recent-update__date">
              <time datetime="2026-06-18">Jun 18</time>
              <span>2026</span>
            </div>
            <div class="recent-update__body">
              <div class="recent-update__meta">
                <span>Site</span>
                <span>Polish</span>
              </div>
              <h3>网站结构继续整理</h3>
              <p>Tech 页面拆成项目展示和技术随笔两类视图，Blog 增加标签入口，并重新整理了若干视觉细节。</p>
            </div>
          </article>

          <article class="recent-update">
            <div class="recent-update__date">
              <time datetime="2026-06-17">Jun 17</time>
              <span>2026</span>
            </div>
            <div class="recent-update__body">
              <div class="recent-update__meta">
                <span>Migration</span>
                <span>HugoBlox</span>
              </div>
              <h3>迁移到了新框架</h3>
              <p>站点从旧的 Academic Pages 迁移到 HugoBlox。当前版本会继续修掉迁移后留下的页面、搜索和样式问题。</p>
            </div>
          </article>
        </div>
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Recent Posts
      filters:
        folders:
          - blog
    design:
      view: article-grid
      columns: 2
  - block: markdown
    id: friends
    content:
      title: Friends
      text: |-
        <div class="friend-links">
          <a class="friend-link" href="https://example.com/" target="_blank" rel="noopener">
            <span class="friend-link__name">Friend Site</span>
            <span class="friend-link__desc">Personal homepage and notes.</span>
          </a>
          <a class="friend-link" href="https://example.org/" target="_blank" rel="noopener">
            <span class="friend-link__name">Research Notes</span>
            <span class="friend-link__desc">Academic blog and resources.</span>
          </a>
          <a class="friend-link" href="https://example.net/" target="_blank" rel="noopener">
            <span class="friend-link__name">Tech Blog</span>
            <span class="friend-link__desc">Programming, tools, and experiments.</span>
          </a>
        </div>
    design:
      columns: '1'
---
