import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

const TEXTAREA_MIN_HEIGHT = "100px";

app.registerExtension({
    name: "Becky3Common.ShowText",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "ShowText_Simple") return;

        const onNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            onNodeCreated?.apply(this, arguments);
            const node = this;
            const w = ComfyWidgets["STRING"](
                node, "output", ["STRING", { multiline: true }], app
            ).widget;
            w.inputEl.readOnly = true;
            w.inputEl.style.opacity = "0.85";
            w.inputEl.style.fontSize = "13px";
            w.inputEl.style.minHeight = TEXTAREA_MIN_HEIGHT;
            node._outputWidget = w;

            requestAnimationFrame(() => {
                const computed = node.computeSize();
                node.setSize([
                    Math.max(computed[0], 320),
                    Math.max(computed[1], 280),
                ]);
            });
        };

        const onExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            onExecuted?.apply(this, arguments);
            if (this._outputWidget && message?.text) {
                const text = Array.isArray(message.text)
                    ? message.text.join("\n")
                    : message.text;
                this._outputWidget.value = text;
            }
        };
    },
});
