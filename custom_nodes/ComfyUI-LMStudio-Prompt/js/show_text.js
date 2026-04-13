import { app } from "../../scripts/app.js";

const TEXTAREA_MIN_HEIGHT = "100px";

app.registerExtension({
    name: "LMStudio.Widgets",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "LMStudioPrompt") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            onNodeCreated?.apply(this, arguments);
            const node = this;
            requestAnimationFrame(() => {
                for (const w of node.widgets || []) {
                    if (w.inputEl && w.inputEl.tagName === "TEXTAREA") {
                        w.inputEl.style.minHeight = TEXTAREA_MIN_HEIGHT;
                    }
                }
                const computed = node.computeSize();
                node.setSize([
                    Math.max(computed[0], 350),
                    Math.max(computed[1], 450),
                ]);
            });
        };
    },
});
