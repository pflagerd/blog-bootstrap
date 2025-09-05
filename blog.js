class Article {
    constructor(element, index) {
        this.element = element;
        this.index = index;
        this.articleId = this.element.id || `article-${index}`;
        this.element.id = this.articleId;

        this.contentChildren = Array.from(this.element.children);
        this.toggleSpan = null;
        this.isCollapsed = null;

        this.init();
    }

    init() {
        if (this.contentChildren.length < 1) return;

        this.createToggleControl();
        this.loadInitialState();
        this.applyState(this.isCollapsed);
        this.attachEventListeners();
    }

    createToggleControl() {
        this.toggleSpan = document.createElement("span");
        this.toggleSpan.className = "toggle-control";
        this.contentChildren[0].appendChild(this.toggleSpan);
    }

    loadInitialState() {
        const storedState = localStorage.getItem(this.articleId);

        if (storedState === null) {
            // First-time load: collapse all except the first article
            this.isCollapsed = this.index !== 0;
        } else {
            this.isCollapsed = storedState === "collapsed";
        }
    }

    getHeightForFirstN(n) {
        this.element.style.height = 'auto';
        void this.element.offsetHeight; // Force layout recalculation

        let total = 0;
        for (let i = 0; i < Math.min(n, this.contentChildren.length); i++) {
            const el = this.contentChildren[i];
            const style = getComputedStyle(el);
            total += el.offsetHeight + parseFloat(style.marginTop) + parseFloat(style.marginBottom);
        }
        return total + parseFloat(getComputedStyle(document.body).fontSize); // Add 1 em
    }

    getFullHeight() {
        this.element.style.height = 'auto';
        void this.element.offsetHeight; // Force layout recalculation

        let height = this.contentChildren.reduce((acc, el) => {
            const style = getComputedStyle(el);
            return acc + el.offsetHeight + parseFloat(style.marginTop) + parseFloat(style.marginBottom);
        }, 0);
        height += parseFloat(getComputedStyle(document.body).fontSize); // Add 1 em
        return height;
    }

    applyState(collapsed) {
        this.isCollapsed = collapsed;
        const targetHeight = collapsed ? this.getHeightForFirstN(3) : this.getFullHeight();

        this.element.style.height = targetHeight + "px";
        this.toggleSpan.textContent = collapsed ? "Expand ▼" : "Collapse ▲";
        this.saveState();

        if (!collapsed) {
            this.element.addEventListener('transitionend', () => {
                this.element.style.height = 'auto';
            }, { once: true });
        }
    }

    saveState() {
        localStorage.setItem(this.articleId, this.isCollapsed ? "collapsed" : "expanded");
    }

    toggle() {
        const collapsed = this.toggleSpan.textContent.includes("Expand");
        this.element.style.height = this.element.offsetHeight + 'px';

        requestAnimationFrame(() => {
            this.applyState(!collapsed);
        });
    }

    attachEventListeners() {
        this.toggleSpan.addEventListener("click", () => {
            this.toggle();
        });
    }

    // Public API methods for external control
    expand() {
        if (this.isCollapsed) {
            this.toggle();
        }
    }

    collapse() {
        if (!this.isCollapsed) {
            this.toggle();
        }
    }

    getState() {
        return {
            id: this.articleId,
            isCollapsed: this.isCollapsed,
            index: this.index
        };
    }
}

class ArticleManager {
    constructor() {
        this.articles = [];
        this.init();
    }

    init() {
        document.addEventListener("DOMContentLoaded", () => {
            this.initializeArticles();
        });
    }

    initializeArticles() {
        const articleElements = document.querySelectorAll("article");

        articleElements.forEach((element, index) => {
            const article = new Article(element, index);
            this.articles.push(article);
        });
    }

    // Public API for managing all articles
    expandAll() {
        this.articles.forEach(article => article.expand());
    }

    collapseAll() {
        this.articles.forEach(article => article.collapse());
    }

    getArticleById(id) {
        return this.articles.find(article => article.articleId === id);
    }

    getAllStates() {
        return this.articles.map(article => article.getState());
    }

    getArticleCount() {
        return this.articles.length;
    }
}

// Initialize the article system
const articleManager = new ArticleManager();