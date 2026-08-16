document.addEventListener("DOMContentLoaded", () => {
    const articles = document.querySelectorAll("article");

    articles.forEach((article, index) => {
        const articleId = article.id || `article-${index}`;
        article.id = articleId;

        const contentChildren = Array.from(article.children);

        if (contentChildren.length < 1) return;

        // Inject toggle span into first child
        const toggleSpan = document.createElement("span");
        toggleSpan.className = "toggle-control";
        contentChildren[0].appendChild(toggleSpan);

        const getCollapsedChildCount = () => {
            // Collapsed preview = the heading (if the first child is an
            // <h1>-<h6>) plus any immediately-following siblings with
            // class "meta". Stops at the first non-meta element.
            let count = 0;
            if (contentChildren.length > 0 && /^H[1-6]$/.test(contentChildren[0].tagName)) {
                count = 1;
            }
            while (count < contentChildren.length && contentChildren[count].classList.contains('meta')) {
                count++;
            }
            return count;
        };

        const getHeightForFirstN = (n) => {
            article.style.height = 'auto';
            void article.offsetHeight;

            const count = Math.min(n, contentChildren.length);
            if (count === 0) return 0;

            // Measure the actual rendered bottom edge of the Nth child rather
            // than summing each child's own height: children can share a
            // line (e.g. consecutive <img> tags wrap like inline text), so
            // adding up individual heights overcounts whenever more than one
            // child ends up on the same row.
            const articleBox = article.getBoundingClientRect();
            const lastChildBox = contentChildren[count - 1].getBoundingClientRect();
            const style = getComputedStyle(article);

            // Trailing space after the cut: if hidden children follow, stop
            // in the real (already-rendered) gap before whichever one starts
            // highest up. Using the topmost of *all* remaining children,
            // rather than just the next one in DOM order, matters when
            // hidden inline siblings share a line and differ in height
            // (e.g. a landscape and a portrait photo side by side): the
            // shorter one's own top gets pushed down by baseline alignment,
            // so it alone would understate where the hidden content starts.
            // Otherwise this preview shows everything, so end with the
            // article's own bottom padding like a normal full card.
            const remainingChildren = contentChildren.slice(count);
            const trailingGap = remainingChildren.length > 0
                ? Math.min(...remainingChildren.map(el => el.getBoundingClientRect().top)) - lastChildBox.bottom
                : parseFloat(style.paddingBottom);

            return (lastChildBox.bottom - articleBox.top)
                + trailingGap
                + parseFloat(style.borderBottomWidth);
        };

        const getFullHeight = () => {
            article.style.height = 'auto';
            void article.offsetHeight;

            // The browser has already laid out all the content correctly
            // (including wrapped inline elements like <img> and <br>), so
            // just read the real rendered height instead of re-deriving it.
            return article.offsetHeight;
        };

        const storedState = localStorage.getItem(articleId);
        let isCollapsed;

        if (storedState === null) {
            // First-time load: only expand articles explicitly marked as such
            isCollapsed = !article.hasAttribute('data-default-expanded');
        } else {
            isCollapsed = storedState === "collapsed";
        }

        let currentlyCollapsed = isCollapsed;

        const applyState = (collapsed) => {
            const targetHeight = collapsed ? getHeightForFirstN(getCollapsedChildCount()) : getFullHeight();
            article.style.height = targetHeight + "px";
            toggleSpan.textContent = collapsed ? "Expand ▼" : "Collapse ▲";
            localStorage.setItem(articleId, collapsed ? "collapsed" : "expanded");
            currentlyCollapsed = collapsed;

            if (!collapsed) {
                article.addEventListener('transitionend', () => {
                    article.style.height = 'auto';
                }, {once: true});
            }
        };

        applyState(isCollapsed);

        // Images finish loading after this initial height is computed, so
        // an article containing them measures short on first load. Once
        // every still-loading image has settled, recompute the height for
        // whatever state the article is in now.
        const pendingImages = Array.from(article.querySelectorAll('img')).filter(img => !img.complete);
        if (pendingImages.length > 0) {
            let remaining = pendingImages.length;
            const onImageSettled = () => {
                remaining--;
                if (remaining === 0) applyState(currentlyCollapsed);
            };
            pendingImages.forEach(img => {
                img.addEventListener('load', onImageSettled, {once: true});
                img.addEventListener('error', onImageSettled, {once: true});
            });
        }

        toggleSpan.addEventListener("click", () => {
            const collapsed = toggleSpan.textContent.includes("Expand");
            article.style.height = article.offsetHeight + 'px';
            requestAnimationFrame(() => {
                applyState(!collapsed);
            });
        });
    });
});
