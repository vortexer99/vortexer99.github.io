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
