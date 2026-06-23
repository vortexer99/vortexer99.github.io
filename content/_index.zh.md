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
        text: 下载简历
        url: /uploads/resume.pdf
      headings:
        about: '简介'
        education: '教育经历'
        interests: '研究兴趣'
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
      title: '近期更新'
      text: |-
        <div class="recent-updates">
          <article class="recent-update">
            <div class="recent-update__date">
              <time datetime="2026-06-18">6月18日</time>
              <span>2026</span>
            </div>
            <div class="recent-update__body">
              <div class="recent-update__meta">
                <span>站点</span>
                <span>整理</span>
              </div>
              <h3>网站结构继续整理</h3>
              <p>Tech 页面拆成项目展示和技术随笔两类视图，Blog 增加标签入口，并重新整理了若干视觉细节。</p>
            </div>
          </article>

          <article class="recent-update">
            <div class="recent-update__date">
              <time datetime="2026-06-17">6月17日</time>
              <span>2026</span>
            </div>
            <div class="recent-update__body">
              <div class="recent-update__meta">
                <span>迁移</span>
                <span>HugoBlox</span>
              </div>
              <h3>迁移到了新框架</h3>
              <p>站点从旧的 Academic Pages 迁移到 HugoBlox。当前版本会继续修掉迁移后留下的页面、搜索和样式问题。</p>
            </div>
          </article>
        </div>
    design:
      columns: '1'
  - block: markdown
    id: explore
    content:
      title: 继续浏览
      text: |-
        当前先开放中文首页。博客、技术项目、图集和简历仍沿用原有页面，后续可以逐步补齐对应的中文栏目。

        - [博客归档](/blog/)
        - [技术与项目](/tech/)
        - [图集](/gallery/)
        - [英文简历](/cv/)
    design:
      columns: '1'
---
