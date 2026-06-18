---
title: ''
summary: ''
date: 2026-06-17
type: landing

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
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle
  - block: markdown
    content:
      title: 'Research'
      text: |-
        I work on the predictability of the Martian atmosphere, CNOP, and nonlinear dynamics.
        I also write blogs, build small tools, and keep a gallery of talks and field photos.
    design:
      columns: '1'
  - block: markdown
    content:
      title: 'Recent Updates'
      text: |-
        <div class="recent-updates">
          <article class="recent-update">
            <time datetime="2026-06-17">2026-06-17</time>
            <div>
              <h3>迁移到了新框架</h3>
              <p>12分钟，AI就帮我迁移好了！目前站点可能还是有些大大小小的问题，会慢慢修复。</p>
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
  - block: collection
    id: news
    content:
      title: Recent News
      page_type: blog
      count: 6
      filters:
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      order: desc
    design:
      view: card
      spacing:
        padding: [0, 0, 0, 0]
---
