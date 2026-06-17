from __future__ import annotations

import html
import re
import sys
import webbrowser
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

try:
    from PySide6.QtCore import QSize, Qt, QUrl
    from PySide6.QtGui import QAction, QColor, QDesktopServices, QFont, QFontDatabase, QPainter, QPen
    from PySide6.QtWidgets import (
        QApplication,
        QComboBox,
        QFormLayout,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QListWidget,
        QListWidgetItem,
        QMainWindow,
        QMessageBox,
        QPushButton,
        QSplitter,
        QStatusBar,
        QStyledItemDelegate,
        QStyle,
        QTabWidget,
        QTextBrowser,
        QTextEdit,
        QToolBar,
        QVBoxLayout,
        QWidget,
    )
except ModuleNotFoundError as exc:  # pragma: no cover
    raise SystemExit("Missing PySide6. Install it with: python -m pip install PySide6") from exc


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"


@dataclass(frozen=True)
class ContentItem:
    title: str
    date: str
    section: str
    path: Path
    rel_path: str
    url: str
    tags: list[str] = field(default_factory=list)
    types: list[str] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)
    lengths: list[str] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    content_type: str = ""
    summary: str = ""
    body: str = ""
    in_tech_notes: bool = False
    raw_front_matter: str = ""
    editable: bool = False

    @property
    def display_section(self) -> str:
        if self.in_tech_notes:
            return "Tech Notes"
        return SECTION_LABELS.get(self.section, self.section)


SECTION_LABELS = {
    "blog": "Blog",
    "tech": "Tech",
    "gallery": "Gallery",
    "cv": "CV",
    "pip": "PIP",
    "milestones": "Milestones",
    "tags": "Tags",
    "home": "Home",
}

TYPE_TAGS = {
    "Blogpost": "blogpost",
    "Homework": "homework",
    "Lecnote": "lecture-note",
    "Life-exp": "life-exp",
    "Life-Exp": "life-exp",
    "Tools": "tool",
    "index": "index",
    "Index": "index",
}

TOPIC_TAGS = {
    "AI": "ai",
    "Atmospheric Model": "numerical-modelling",
    "Atmospheres": "atmospheric-science",
    "Combinatorics": "combinatorics",
    "Cybernetics": "cybernetics",
    "Dynamical System": "dynamical-systems",
    "Ensemble forecast": "ensemble-forecasting",
    "Experiments": "experiments",
    "Fluid Mechanics": "fluid-mechanics",
    "Heat Transfer": "heat-transfer",
    "Humanity": "humanities",
    "Humanities": "humanities",
    "Linear Algebra": "linear-algebra",
    "Logic": "logic",
    "Mathematic": "mathematics",
    "Mathematics": "mathematics",
    "Mathematical Analysis": "mathematical-analysis",
    "Mathematical method of Physics": "mathematical-methods-in-physics",
    "Mechanics": "mechanics",
    "Nonlinear Dynamics": "nonlinear-dynamics",
    "Optimization": "optimization",
    "Physic": "physics",
    "Probability and Mathematical Statistics": "probability-statistics",
    "Software Engineering": "software-engineering",
    "Thermal-Dynamic": "thermodynamics",
    "Vector calculus": "vector-calculus",
}

PROJECT_TAGS = {
    "PIP-RANDPDE": "pip-randpde",
}

LENGTH_TAGS = {
    "1-5 Pages": "1-5-pages",
    "6-10 Pages": "6-10-pages",
    "11-30 Pages": "11-30-pages",
    "31-100 Pages": "31-100-pages",
    "100+ Pages": "100-plus-pages",
    "31-60 Slides": "31-60-slides",
    "Not in pages": "not-in-pages",
    "not-in-pages": "not-in-pages",
}

EDITABLE_ORDER = [
    "title",
    "date",
    "url",
    "tags",
    "types",
    "topics",
    "project_tags",
    "lengths",
    "authors",
    "aliases",
    "type",
    "summary",
]


class ContentListDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option, index) -> None:
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing, True)

        selected = bool(option.state & QStyle.State_Selected)
        hover = bool(option.state & QStyle.State_MouseOver)
        item = index.data(Qt.UserRole)
        section = getattr(item, "display_section", "")

        background = "#ffffff"
        border = "#e5e7eb"
        if selected:
            background = "#eff6ff"
            border = "#2563eb"
        elif hover:
            background = "#f8fafc"
            border = "#bfdbfe"

        rect = option.rect.adjusted(3, 3, -3, -3)
        painter.setPen(QPen(QColor(border), 1))
        painter.setBrush(QColor(background))
        painter.drawRoundedRect(rect, 7, 7)

        text_rect = rect.adjusted(12, 8, -12, -8)
        title = index.data(Qt.DisplayRole) or ""
        title_lines = title.splitlines()
        title_text = title_lines[0] if title_lines else ""
        meta_text = title_lines[1] if len(title_lines) > 1 else ""

        title_font = QFont(option.font)
        title_font.setBold(True)
        painter.setFont(title_font)
        painter.setPen(QColor("#0f172a"))
        metrics = painter.fontMetrics()
        painter.drawText(
            text_rect,
            Qt.AlignLeft | Qt.AlignTop,
            metrics.elidedText(title_text, Qt.ElideRight, text_rect.width()),
        )

        meta_font = QFont(option.font)
        meta_font.setPointSize(max(8, meta_font.pointSize() - 1))
        painter.setFont(meta_font)
        painter.setPen(QColor("#64748b"))
        meta_rect = text_rect.adjusted(0, 25, -86, 0)
        painter.drawText(
            meta_rect,
            Qt.AlignLeft | Qt.AlignTop,
            painter.fontMetrics().elidedText(meta_text, Qt.ElideRight, meta_rect.width()),
        )

        badge_rect = text_rect.adjusted(text_rect.width() - 78, 23, 0, -2)
        painter.setPen(QPen(QColor("#dbe4ef"), 1))
        painter.setBrush(QColor("#f8fafc"))
        painter.drawRoundedRect(badge_rect, 9, 9)
        painter.setPen(QColor("#475569"))
        painter.drawText(badge_rect, Qt.AlignCenter, section[:18])
        painter.restore()

    def sizeHint(self, option, index) -> QSize:
        return QSize(super().sizeHint(option, index).width(), 68)


class SiteManager(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        font_family = preferred_font_family()
        if font_family:
            QApplication.setFont(QFont(font_family, 9))

        self.items: list[ContentItem] = []
        self.filtered: list[ContentItem] = []
        self.current: ContentItem | None = None
        self.dirty = False
        self.loading_editor = False

        self.setWindowTitle("Site Content Manager")
        self.resize(1500, 840)
        self.setMinimumSize(1100, 680)
        self.build_ui()
        self.apply_style()
        self.reload()

    def build_ui(self) -> None:
        toolbar = QToolBar("Tools")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(self.reload)
        toolbar.addAction(refresh_action)

        open_file_action = QAction("Open File", self)
        open_file_action.triggered.connect(self.open_current_file)
        toolbar.addAction(open_file_action)

        open_page_action = QAction("Open Page", self)
        open_page_action.triggered.connect(self.open_current_page)
        toolbar.addAction(open_page_action)

        toolbar.addSeparator()

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_current)
        toolbar.addAction(save_action)
        self.save_action = save_action

        revert_action = QAction("Revert", self)
        revert_action.triggered.connect(self.revert_current)
        toolbar.addAction(revert_action)
        self.revert_action = revert_action

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        root = QSplitter(Qt.Horizontal)
        root.setChildrenCollapsible(False)
        self.setCentralWidget(root)

        sidebar = QWidget()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(230)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(14, 16, 12, 16)
        sidebar_layout.setSpacing(10)

        title = QLabel("Filters")
        title.setObjectName("PanelTitle")
        sidebar_layout.addWidget(title)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search title, tag, preview...")
        self.search_input.textChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.search_input)

        self.section_filter = QComboBox()
        self.section_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.section_filter)

        self.tag_filter = QComboBox()
        self.tag_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.tag_filter)

        self.type_filter = QComboBox()
        self.type_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.type_filter)

        self.topic_filter = QComboBox()
        self.topic_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.topic_filter)

        self.project_filter = QComboBox()
        self.project_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.project_filter)

        self.length_filter = QComboBox()
        self.length_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.length_filter)

        self.author_filter = QComboBox()
        self.author_filter.currentIndexChanged.connect(self.apply_filters)
        sidebar_layout.addWidget(self.author_filter)

        self.stats_label = QLabel()
        self.stats_label.setObjectName("MutedText")
        self.stats_label.setWordWrap(True)
        sidebar_layout.addWidget(self.stats_label)
        sidebar_layout.addStretch(1)
        root.addWidget(sidebar)

        middle = QWidget()
        middle.setObjectName("ListPanel")
        middle_layout = QVBoxLayout(middle)
        middle_layout.setContentsMargins(12, 16, 12, 16)
        middle_layout.setSpacing(10)

        self.list_title = QLabel("Content")
        self.list_title.setObjectName("PanelTitle")
        middle_layout.addWidget(self.list_title)

        self.item_list = QListWidget()
        self.item_list.setItemDelegate(ContentListDelegate(self.item_list))
        self.item_list.currentRowChanged.connect(self.show_current)
        self.item_list.setSpacing(2)
        middle_layout.addWidget(self.item_list, 1)
        root.addWidget(middle)

        detail = QWidget()
        detail.setObjectName("DetailPanel")
        detail_layout = QVBoxLayout(detail)
        detail_layout.setContentsMargins(12, 16, 14, 16)
        detail_layout.setSpacing(10)

        self.detail_title = QLabel("Preview")
        self.detail_title.setObjectName("PanelTitle")
        detail_layout.addWidget(self.detail_title)

        self.detail_tabs = QTabWidget()

        self.detail_browser = QTextBrowser()
        self.detail_browser.setOpenExternalLinks(True)
        self.detail_tabs.addTab(self.detail_browser, "Preview")

        editor = QWidget()
        editor_layout = QVBoxLayout(editor)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.setSpacing(10)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        self.title_edit = QLineEdit()
        self.date_edit = QLineEdit()
        self.url_edit = QLineEdit()
        self.authors_edit = QLineEdit()
        self.tags_edit = QLineEdit()
        self.types_edit = QLineEdit()
        self.topics_edit = QLineEdit()
        self.projects_edit = QLineEdit()
        self.lengths_edit = QLineEdit()
        self.aliases_edit = QLineEdit()
        self.page_type_edit = QLineEdit()
        for widget in [
            self.title_edit,
            self.date_edit,
            self.url_edit,
            self.authors_edit,
            self.tags_edit,
            self.types_edit,
            self.topics_edit,
            self.projects_edit,
            self.lengths_edit,
            self.aliases_edit,
            self.page_type_edit,
        ]:
            widget.textChanged.connect(self.mark_dirty)

        form.addRow("Title", self.title_edit)
        form.addRow("Date", self.date_edit)
        form.addRow("URL", self.url_edit)
        form.addRow("Authors", self.authors_edit)
        form.addRow("Legacy tags", self.tags_edit)
        form.addRow("Types", self.types_edit)
        form.addRow("Topics", self.topics_edit)
        form.addRow("Projects", self.projects_edit)
        form.addRow("Lengths", self.lengths_edit)
        form.addRow("Aliases", self.aliases_edit)
        form.addRow("Page type", self.page_type_edit)
        editor_layout.addLayout(form)

        editor_toolbar = QHBoxLayout()
        self.normalize_button = QPushButton("Normalize from Tags")
        self.normalize_button.clicked.connect(self.normalize_current_taxonomy)
        editor_toolbar.addWidget(self.normalize_button)
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_current)
        editor_toolbar.addWidget(self.save_button)
        self.revert_button = QPushButton("Revert")
        self.revert_button.clicked.connect(self.revert_current)
        editor_toolbar.addWidget(self.revert_button)
        editor_toolbar.addStretch(1)
        editor_layout.addLayout(editor_toolbar)

        self.body_edit = QTextEdit()
        self.body_edit.setAcceptRichText(False)
        self.body_edit.textChanged.connect(self.mark_dirty)
        editor_layout.addWidget(self.body_edit, 1)

        self.detail_tabs.addTab(editor, "Edit")
        detail_layout.addWidget(self.detail_tabs, 1)

        button_row = QHBoxLayout()
        self.open_file_button = QPushButton("Open File")
        self.open_file_button.clicked.connect(self.open_current_file)
        button_row.addWidget(self.open_file_button)
        self.open_page_button = QPushButton("Open Page")
        self.open_page_button.clicked.connect(self.open_current_page)
        button_row.addWidget(self.open_page_button)
        button_row.addStretch(1)
        detail_layout.addLayout(button_row)
        root.addWidget(detail)

        root.setSizes([230, 500, 770])

    def apply_style(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow {
                background: #f8fafc;
            }
            QToolBar {
                background: #ffffff;
                border: 0;
                border-bottom: 1px solid #e5e7eb;
                spacing: 8px;
                padding: 6px;
            }
            QWidget#Sidebar,
            QWidget#ListPanel,
            QWidget#DetailPanel {
                background: #ffffff;
            }
            QLabel#PanelTitle {
                color: #0f172a;
                font-size: 16px;
                font-weight: 700;
            }
            QLabel#MutedText {
                color: #64748b;
                line-height: 1.45;
            }
            QLineEdit,
            QComboBox {
                border: 1px solid #dbe4ef;
                border-radius: 6px;
                padding: 7px 9px;
                background: #ffffff;
                color: #0f172a;
            }
            QListWidget {
                border: 0;
                background: #ffffff;
                outline: 0;
            }
            QTextBrowser {
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                background: #ffffff;
                padding: 10px;
            }
            QTextEdit {
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                background: #ffffff;
                color: #0f172a;
                font-family: "Cascadia Mono", "Consolas", "Microsoft YaHei UI", monospace;
                font-size: 13px;
                padding: 10px;
            }
            QTabWidget::pane {
                border: 0;
            }
            QTabBar::tab {
                border: 1px solid #dbe4ef;
                border-bottom: 0;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                background: #f8fafc;
                color: #475569;
                padding: 8px 14px;
                margin-right: 4px;
            }
            QTabBar::tab:selected {
                background: #ffffff;
                color: #0f172a;
            }
            QPushButton {
                border: 1px solid #dbe4ef;
                border-radius: 6px;
                background: #ffffff;
                color: #0f172a;
                padding: 7px 12px;
            }
            QPushButton:hover {
                background: #f8fafc;
                border-color: #bfdbfe;
            }
            """
        )

    def reload(self) -> None:
        if self.dirty and not self.confirm_discard_changes():
            return
        self.set_dirty(False)
        self.items = scan_content(ROOT)
        self.populate_filters()
        self.apply_filters()
        self.status.showMessage(f"Loaded {len(self.items)} content files", 4000)

    def populate_filters(self) -> None:
        current_section = self.section_filter.currentData() if self.section_filter.count() else "all"
        current_tag = self.tag_filter.currentData() if self.tag_filter.count() else "all"
        current_type = self.type_filter.currentData() if self.type_filter.count() else "all"
        current_topic = self.topic_filter.currentData() if self.topic_filter.count() else "all"
        current_project = self.project_filter.currentData() if self.project_filter.count() else "all"
        current_length = self.length_filter.currentData() if self.length_filter.count() else "all"
        current_author = self.author_filter.currentData() if self.author_filter.count() else "all"

        sections = sorted({item.display_section for item in self.items})
        tags = sorted({tag for item in self.items for tag in item.tags}, key=str.casefold)
        types = sorted({value for item in self.items for value in item.types}, key=str.casefold)
        topics = sorted({value for item in self.items for value in item.topics}, key=str.casefold)
        projects = sorted({value for item in self.items for value in item.projects}, key=str.casefold)
        lengths = sorted({value for item in self.items for value in item.lengths}, key=str.casefold)
        authors = sorted({author for item in self.items for author in item.authors}, key=str.casefold)

        self.section_filter.blockSignals(True)
        self.section_filter.clear()
        self.section_filter.addItem("All sections", "all")
        for section in sections:
            self.section_filter.addItem(section, section)
        restore_combo(self.section_filter, current_section)
        self.section_filter.blockSignals(False)

        self.tag_filter.blockSignals(True)
        self.tag_filter.clear()
        self.tag_filter.addItem("All tags", "all")
        self.tag_filter.addItem("No tags", "__untagged__")
        for tag in tags:
            self.tag_filter.addItem(tag, tag)
        restore_combo(self.tag_filter, current_tag)
        self.tag_filter.blockSignals(False)

        populate_value_filter(self.type_filter, "All types", "No type", types, current_type)
        populate_value_filter(self.topic_filter, "All topics", "No topic", topics, current_topic)
        populate_value_filter(self.project_filter, "All projects", "No project", projects, current_project)
        populate_value_filter(self.length_filter, "All lengths", "No length", lengths, current_length)

        self.author_filter.blockSignals(True)
        self.author_filter.clear()
        self.author_filter.addItem("All authors", "all")
        self.author_filter.addItem("No author", "__no_author__")
        for author in authors:
            self.author_filter.addItem(author, author)
        restore_combo(self.author_filter, current_author)
        self.author_filter.blockSignals(False)

    def apply_filters(self) -> None:
        query = self.search_input.text().strip().lower()
        section = self.section_filter.currentData() if self.section_filter.count() else "all"
        tag = self.tag_filter.currentData() if self.tag_filter.count() else "all"
        type_value = self.type_filter.currentData() if self.type_filter.count() else "all"
        topic = self.topic_filter.currentData() if self.topic_filter.count() else "all"
        project = self.project_filter.currentData() if self.project_filter.count() else "all"
        length = self.length_filter.currentData() if self.length_filter.count() else "all"
        author = self.author_filter.currentData() if self.author_filter.count() else "all"

        items = self.items
        if section and section != "all":
            items = [item for item in items if item.display_section == section]
        if tag == "__untagged__":
            items = [item for item in items if not item.tags]
        elif tag and tag != "all":
            items = [item for item in items if tag in item.tags]
        items = filter_by_list_value(items, type_value, "types")
        items = filter_by_list_value(items, topic, "topics")
        items = filter_by_list_value(items, project, "projects")
        items = filter_by_list_value(items, length, "lengths")
        if author == "__no_author__":
            items = [item for item in items if not item.authors]
        elif author and author != "all":
            items = [item for item in items if author in item.authors]
        if query:
            items = [item for item in items if item_matches_query(item, query)]

        self.filtered = sorted(items, key=item_sort_key)
        self.render_list()

    def render_list(self) -> None:
        previous_path = self.current.rel_path if self.current else ""
        self.item_list.blockSignals(True)
        self.item_list.clear()
        selected_row = 0
        for index, item in enumerate(self.filtered):
            list_item = QListWidgetItem(format_list_label(item))
            list_item.setData(Qt.UserRole, item)
            list_item.setToolTip(item.rel_path)
            self.item_list.addItem(list_item)
            if item.rel_path == previous_path:
                selected_row = index
        self.item_list.blockSignals(False)

        self.list_title.setText(f"Content ({len(self.filtered)}/{len(self.items)})")
        self.stats_label.setText(build_stats_text(self.items, self.filtered))

        if self.filtered:
            self.item_list.setCurrentRow(min(selected_row, len(self.filtered) - 1))
            self.show_current(self.item_list.currentRow())
        else:
            self.current = None
            self.detail_title.setText("Preview")
            self.detail_browser.setHtml("<p>No matching content.</p>")
            self.clear_editor()

    def show_current(self, row: int) -> None:
        if row < 0 or row >= len(self.filtered):
            return
        target = self.filtered[row]
        if self.current and self.dirty and target.rel_path == self.current.rel_path:
            return
        if self.current and self.dirty and target.rel_path != self.current.rel_path:
            previous = self.current.rel_path
            if not self.confirm_discard_changes():
                previous_row = next((i for i, item in enumerate(self.filtered) if item.rel_path == previous), -1)
                if previous_row >= 0:
                    self.item_list.blockSignals(True)
                    self.item_list.setCurrentRow(previous_row)
                    self.item_list.blockSignals(False)
                return
        self.current = target
        self.detail_title.setText(self.current.title or self.current.rel_path)
        self.detail_browser.setHtml(detail_html(self.current))
        self.load_editor(self.current)

    def open_current_file(self) -> None:
        if not self.current:
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(self.current.path)))

    def open_current_page(self) -> None:
        if not self.current or not self.current.url:
            return
        url = self.current.url
        if url.startswith("/"):
            url = "https://vortexer99.github.io" + url
        if not QDesktopServices.openUrl(QUrl(url)):
            webbrowser.open(url)

    def load_editor(self, item: ContentItem) -> None:
        self.loading_editor = True
        self.title_edit.setText(item.title)
        self.date_edit.setText(item.date)
        self.url_edit.setText(item.url)
        self.authors_edit.setText(list_to_text(item.authors))
        self.tags_edit.setText(list_to_text(item.tags))
        self.types_edit.setText(list_to_text(item.types))
        self.topics_edit.setText(list_to_text(item.topics))
        self.projects_edit.setText(list_to_text(item.projects))
        self.lengths_edit.setText(list_to_text(item.lengths))
        self.aliases_edit.setText(list_to_text(item.aliases))
        self.page_type_edit.setText(item.content_type)
        self.body_edit.setPlainText(item.body)

        for widget in [
            self.title_edit,
            self.date_edit,
            self.url_edit,
            self.authors_edit,
            self.tags_edit,
            self.types_edit,
            self.topics_edit,
            self.projects_edit,
            self.lengths_edit,
            self.aliases_edit,
            self.page_type_edit,
            self.body_edit,
            self.normalize_button,
            self.save_button,
            self.revert_button,
        ]:
            widget.setEnabled(item.editable)
        self.save_action.setEnabled(item.editable)
        self.revert_action.setEnabled(item.editable)

        self.loading_editor = False
        self.set_dirty(False)
        if not item.editable:
            self.status.showMessage("This page has complex front matter; use Open File for manual edits.", 4000)

    def clear_editor(self) -> None:
        self.loading_editor = True
        for widget in [
            self.title_edit,
            self.date_edit,
            self.url_edit,
            self.authors_edit,
            self.tags_edit,
            self.types_edit,
            self.topics_edit,
            self.projects_edit,
            self.lengths_edit,
            self.aliases_edit,
            self.page_type_edit,
        ]:
            widget.clear()
            widget.setEnabled(False)
        self.body_edit.clear()
        self.body_edit.setEnabled(False)
        self.normalize_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.revert_button.setEnabled(False)
        self.save_action.setEnabled(False)
        self.revert_action.setEnabled(False)
        self.loading_editor = False
        self.set_dirty(False)

    def mark_dirty(self) -> None:
        if not self.loading_editor and self.current and self.current.editable:
            self.set_dirty(True)

    def set_dirty(self, dirty: bool) -> None:
        self.dirty = dirty
        suffix = " *" if dirty else ""
        if self.current:
            self.detail_title.setText((self.current.title or self.current.rel_path) + suffix)

    def confirm_discard_changes(self) -> bool:
        result = QMessageBox.question(
            self,
            "Unsaved changes",
            "Discard unsaved changes to the current file?",
            QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Cancel,
        )
        return result == QMessageBox.Discard

    def normalize_current_taxonomy(self) -> None:
        tags = text_to_list(self.tags_edit.text())
        self.types_edit.setText(list_to_text(map_tags(tags, TYPE_TAGS)))
        self.topics_edit.setText(list_to_text(map_tags(tags, TOPIC_TAGS)))
        self.projects_edit.setText(list_to_text(map_tags(tags, PROJECT_TAGS)))
        self.lengths_edit.setText(list_to_text(map_tags(tags, LENGTH_TAGS)))
        self.set_dirty(True)

    def revert_current(self) -> None:
        if self.current:
            self.load_editor(self.current)
            self.detail_browser.setHtml(detail_html(self.current))
            self.status.showMessage("Reverted editor fields", 3000)

    def save_current(self) -> None:
        if not self.current:
            return
        if not self.current.editable:
            QMessageBox.information(
                self,
                "Read-only page",
                "This page has complex front matter. Open the file and edit it manually.",
            )
            return

        meta = parse_simple_yaml(self.current.raw_front_matter)
        set_meta_scalar(meta, "title", self.title_edit.text())
        set_meta_scalar(meta, "date", self.date_edit.text())
        set_meta_scalar(meta, "url", self.url_edit.text())
        set_meta_list(meta, "tags", text_to_list(self.tags_edit.text()))
        set_meta_list(meta, "types", text_to_list(self.types_edit.text()))
        set_meta_list(meta, "topics", text_to_list(self.topics_edit.text()))
        set_meta_list(meta, "project_tags", text_to_list(self.projects_edit.text()))
        set_meta_list(meta, "lengths", text_to_list(self.lengths_edit.text()))
        set_meta_list(meta, "authors", text_to_list(self.authors_edit.text()))
        set_meta_list(meta, "aliases", text_to_list(self.aliases_edit.text()))
        set_meta_scalar(meta, "type", self.page_type_edit.text())

        body = self.body_edit.toPlainText()
        new_text = "---\n" + serialize_front_matter(meta) + "---\n\n" + body.lstrip("\n")
        self.current.path.write_text(new_text, encoding="utf-8", newline="\n")
        self.set_dirty(False)
        selected_path = self.current.rel_path
        self.reload()
        for row, item in enumerate(self.filtered):
            if item.rel_path == selected_path:
                self.item_list.setCurrentRow(row)
                break
        self.status.showMessage(f"Saved {selected_path}", 5000)


def scan_content(root: Path) -> list[ContentItem]:
    tech_note_urls = parse_tech_note_urls(root / "content" / "tech" / "_index.md")
    items: list[ContentItem] = []
    for path in sorted((root / "content").rglob("*.md")):
        if path.name.startswith("."):
            continue
        text = read_text(path)
        meta, body, raw_front_matter = split_front_matter(text)
        section = content_section(root, path)
        url = str(meta.get("url") or infer_url(root, path, section))
        tags = as_list(meta.get("tags"))
        types = as_list(meta.get("types"))
        topics = as_list(meta.get("topics"))
        projects = as_list(meta.get("project_tags"))
        lengths = as_list(meta.get("lengths"))
        aliases = as_list(meta.get("aliases"))
        authors = as_list(meta.get("authors"))
        title = str(meta.get("title") or fallback_title(path))
        date = str(meta.get("date") or "")
        summary = str(meta.get("summary") or markdown_summary(body))
        rel_path = path.relative_to(root).as_posix()
        items.append(
            ContentItem(
                title=title,
                date=date,
                section=section,
                path=path,
                rel_path=rel_path,
                url=url,
                tags=tags,
                types=types,
                topics=topics,
                projects=projects,
                lengths=lengths,
                authors=authors,
                aliases=aliases,
                content_type=str(meta.get("type") or ""),
                summary=summary,
                body=body,
                in_tech_notes=url in tech_note_urls,
                raw_front_matter=raw_front_matter,
                editable=is_simple_front_matter(raw_front_matter),
            )
        )
    return items


def parse_tech_note_urls(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = read_text(path)
    urls = set(re.findall(r'href="(/posts/[^"]+)"', text))
    urls.update(re.findall(r"\]\((/posts/[^)]+)\)", text))
    return {normalize_site_url(url) for url in urls}


def split_front_matter(text: str) -> tuple[dict[str, object], str, str]:
    if not text.startswith("---"):
        return {}, text, ""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, flags=re.S)
    if not match:
        return {}, text, ""
    raw_front_matter = match.group(1)
    return parse_simple_yaml(raw_front_matter), match.group(2), raw_front_matter


def parse_simple_yaml(raw: str) -> dict[str, object]:
    result: dict[str, object] = {}
    current_key = ""
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+-\s+", line) and current_key:
            value = clean_scalar(re.sub(r"^\s+-\s+", "", line))
            existing = result.get(current_key)
            if not isinstance(existing, list):
                existing = []
                result[current_key] = existing
            existing.append(value)
            continue
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            current_key = key.strip()
            value = value.strip()
            if value == "":
                result[current_key] = []
            elif value in ("|-", "|", ">-", ">"):
                result[current_key] = ""
            else:
                result[current_key] = clean_scalar(value)
    return result


def is_simple_front_matter(raw: str) -> bool:
    if not raw.strip():
        return False
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if re.match(r"^\s{4,}\S", line):
            return False
        if re.match(r"^[A-Za-z_][\w-]*:\s*(\|-?|\>-?)\s*$", line):
            return False
    return True


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1]
    return value


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        if not value.strip():
            return []
        return [part.strip() for part in re.split(r"[,，;；]", value) if part.strip()]
    return [str(value)]


def list_to_text(values: list[str]) -> str:
    return ", ".join(values)


def text_to_list(value: str) -> list[str]:
    return unique_list(part.strip() for part in re.split(r"[,，;；]\s*", value) if part.strip())


def unique_list(values) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def map_tags(tags: list[str], mapping: dict[str, str]) -> list[str]:
    return unique_list(mapping[tag] for tag in tags if tag in mapping)


def set_meta_scalar(meta: dict[str, object], key: str, value: str) -> None:
    value = value.strip()
    if value:
        meta[key] = value
    else:
        meta.pop(key, None)


def set_meta_list(meta: dict[str, object], key: str, values: list[str]) -> None:
    if values:
        meta[key] = values
    else:
        meta.pop(key, None)


def serialize_front_matter(meta: dict[str, object]) -> str:
    keys = [key for key in EDITABLE_ORDER if key in meta]
    keys.extend(key for key in meta if key not in keys)
    lines: list[str] = []
    for key in keys:
        value = meta[key]
        if isinstance(value, list):
            if not value:
                continue
            lines.append(f"{key}:")
            lines.extend(f"  - {yaml_scalar(str(item))}" for item in value)
        elif value not in (None, ""):
            lines.append(f"{key}: {yaml_scalar(str(value))}")
    return "\n".join(lines) + "\n"


def yaml_scalar(value: str) -> str:
    if value == "":
        return "''"
    if re.match(r"^[A-Za-z0-9_./@+-]+$", value):
        return value
    escaped = value.replace("'", "''")
    return f"'{escaped}'"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def content_section(root: Path, path: Path) -> str:
    rel = path.relative_to(root / "content")
    if len(rel.parts) == 1:
        return "home" if rel.name == "_index.md" else rel.stem
    return rel.parts[0]


def infer_url(root: Path, path: Path, section: str) -> str:
    rel = path.relative_to(root / "content")
    if rel.as_posix() == "_index.md":
        return "/"
    if path.name == "_index.md":
        return "/" + "/".join(rel.parts[:-1]) + "/"
    if path.name == "index.md":
        return "/" + "/".join(rel.parts[:-1]) + "/"
    return "/" + rel.with_suffix("").as_posix() + "/"


def normalize_site_url(url: str) -> str:
    if not url:
        return ""
    if not url.startswith("/"):
        return url
    return "/" + url.strip("/") + "/"


def fallback_title(path: Path) -> str:
    if path.name in ("index.md", "_index.md"):
        return path.parent.name.replace("-", " ").title()
    return path.stem.replace("-", " ").title()


def markdown_summary(body: str, *, max_chars: int = 260) -> str:
    cleaned = re.sub(r"```.*?```", " ", body, flags=re.S)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    cleaned = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = re.sub(r"[#>*_`~\-]+", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned[:max_chars] + ("..." if len(cleaned) > max_chars else "")


def item_matches_query(item: ContentItem, query: str) -> bool:
    haystack = " ".join(
        [
            item.title,
            item.date,
            item.display_section,
            item.rel_path,
            item.url,
            item.summary,
            " ".join(item.tags),
            " ".join(item.types),
            " ".join(item.topics),
            " ".join(item.projects),
            " ".join(item.lengths),
            " ".join(item.authors),
        ]
    ).lower()
    return query in haystack


def item_sort_key(item: ContentItem) -> tuple[int, str, str]:
    date = parse_date(item.date)
    timestamp = int(date.timestamp()) if date else 0
    return (-timestamp, item.display_section, item.title.casefold())


def parse_date(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value[:10])
    except ValueError:
        return None


def format_list_label(item: ContentItem) -> str:
    taxonomy = item.topics or item.types or item.tags
    tags = ", ".join(taxonomy[:3]) if taxonomy else "no taxonomy"
    date = item.date or "no date"
    return f"{item.title}\n{date} / {tags}"


def build_stats_text(all_items: list[ContentItem], filtered: list[ContentItem]) -> str:
    sections: dict[str, int] = {}
    tag_count = 0
    topic_count = 0
    for item in all_items:
        sections[item.display_section] = sections.get(item.display_section, 0) + 1
        tag_count += len(item.tags)
        topic_count += len(item.topics)
    section_text = "\n".join(f"{name}: {count}" for name, count in sorted(sections.items()))
    return (
        f"Total files: {len(all_items)}\n"
        f"Filtered: {len(filtered)}\n"
        f"Legacy tag assignments: {tag_count}\n"
        f"Topic assignments: {topic_count}\n\n"
        f"{section_text}"
    )


def detail_html(item: ContentItem) -> str:
    tags = ", ".join(item.tags) or "None"
    types = ", ".join(item.types) or "None"
    topics = ", ".join(item.topics) or "None"
    projects = ", ".join(item.projects) or "None"
    lengths = ", ".join(item.lengths) or "None"
    authors = ", ".join(item.authors) or "None"
    aliases = ", ".join(item.aliases) or "None"
    preview = html.escape(markdown_summary(item.body, max_chars=1200)).replace("\n", "<br>")
    body_lines = len(item.body.splitlines())
    body_chars = len(item.body)
    return f"""
    <style>
      body {{
        color: #1f2937;
        font-family: "Microsoft YaHei UI", "Segoe UI", sans-serif;
        font-size: 14px;
        line-height: 1.6;
      }}
      h1 {{
        margin: 0 0 12px 0;
        color: #0f172a;
        font-size: 24px;
      }}
      h2 {{
        margin: 18px 0 8px 0;
        color: #334155;
        font-size: 15px;
      }}
      table {{
        width: 100%;
        border-collapse: collapse;
      }}
      td {{
        border-bottom: 1px solid #e5e7eb;
        padding: 8px 10px;
        vertical-align: top;
      }}
      td:first-child {{
        width: 128px;
        background: #f8fafc;
        color: #475569;
        font-weight: 700;
      }}
      .preview {{
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        background: #f8fafc;
        padding: 12px;
      }}
      a {{
        color: #2563eb;
        text-decoration: none;
        font-weight: 700;
      }}
    </style>
    <h1>{html.escape(item.title)}</h1>
    <table>
      <tr><td>Section</td><td>{html.escape(item.display_section)}</td></tr>
      <tr><td>Date</td><td>{html.escape(item.date or "None")}</td></tr>
      <tr><td>Legacy tags</td><td>{html.escape(tags)}</td></tr>
      <tr><td>Types</td><td>{html.escape(types)}</td></tr>
      <tr><td>Topics</td><td>{html.escape(topics)}</td></tr>
      <tr><td>Projects</td><td>{html.escape(projects)}</td></tr>
      <tr><td>Lengths</td><td>{html.escape(lengths)}</td></tr>
      <tr><td>Authors</td><td>{html.escape(authors)}</td></tr>
      <tr><td>Page type</td><td>{html.escape(item.content_type or "None")}</td></tr>
      <tr><td>URL</td><td><a href="{html.escape(item.url)}">{html.escape(item.url or "None")}</a></td></tr>
      <tr><td>Aliases</td><td>{html.escape(aliases)}</td></tr>
      <tr><td>File</td><td>{html.escape(item.rel_path)}</td></tr>
      <tr><td>Size</td><td>{body_lines} lines / {body_chars} chars</td></tr>
      <tr><td>Editable</td><td>{"Yes" if item.editable else "Open file manually"}</td></tr>
    </table>
    <h2>Content Preview</h2>
    <div class="preview">{preview or "No preview text."}</div>
    """


def restore_combo(combo: QComboBox, value: object) -> None:
    index = combo.findData(value)
    combo.setCurrentIndex(index if index >= 0 else 0)


def populate_value_filter(
    combo: QComboBox,
    all_label: str,
    empty_label: str,
    values: list[str],
    current_value: object,
) -> None:
    combo.blockSignals(True)
    combo.clear()
    combo.addItem(all_label, "all")
    combo.addItem(empty_label, "__empty__")
    for value in values:
        combo.addItem(value, value)
    restore_combo(combo, current_value)
    combo.blockSignals(False)


def filter_by_list_value(items: list[ContentItem], value: object, attr: str) -> list[ContentItem]:
    if value == "__empty__":
        return [item for item in items if not getattr(item, attr)]
    if value and value != "all":
        return [item for item in items if value in getattr(item, attr)]
    return items


def preferred_font_family() -> str:
    families = set(QFontDatabase.families())
    for family in [
        "Microsoft YaHei UI",
        "Microsoft YaHei",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "Segoe UI",
    ]:
        if family in families:
            return family
    return ""


def main(argv: list[str] | None = None) -> int:
    app = QApplication(argv or sys.argv)
    window = SiteManager()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
