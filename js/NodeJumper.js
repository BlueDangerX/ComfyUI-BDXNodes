import { api } from "../../scripts/api.js";
import { app } from "../../scripts/app.js";

class NodeJumper {
    constructor() {
        this.properties = { previousName: "", showOutputText: true, binputs: "" };
        // this.binputs = {}
        for (let index = 0; index < 10; index++) {
            this.addInput(`Node ${(index+1)} (ALT + ${index})`, "*");    
            // this.binputs[index] = {} 
        }

        this.setupKeyListener();
        this.isVirtualNode = true;


        // watch for rgnode bad links alert 
        const observer = new MutationObserver(this.detectRGnodeBadLinks);
        const targetNode = document.body;
        const config = { attributes: false, childList: true, subtree: true };
        observer.observe(targetNode, config);
    }

    setupKeyListener() {
        document.addEventListener("keydown", (event) => {
            if (event.altKey && event.code === 'Backquote') {
                this.centerOnNode(this);
            }
        });
    }

    onConnectionsChange(slotType, slot, isChangeConnect, link_info) {
        
        if (slotType === 1) {
            // On disconnect
            if (!isChangeConnect) {
                this.inputs[slot].type = '*';
                this.inputs[slot].name = `Node ${(slot+1)} (ALT + ${slot+1})`;
            } else if (link_info && this.graph) {
                this.handleConnectionChange(slot, link_info);
            }
            
        }
        // this.update();
    }

    handleConnectionChange(slot, link_info) {
        const fromNode = this.graph.getNodeById(link_info.origin_id);
        if (fromNode) {
            const type = fromNode.outputs[link_info.origin_slot].type;
            this.inputs[slot].type = type;
            this.inputs[slot].name = `${fromNode.title} (ALT+${slot})`;
            this.addKeyListener(slot, fromNode);
            // this.addNewInputIfNeeded(slot);
            // console.log(`this inputs`, this.inputs)
        } else {
            console.error("Error: Node input undefined.");
        }
    }

    //hacky method on hold, was trying to hide UI connection links to Node Jumper but caused issues.
    detectRGnodeBadLinks(mutationsList, observer) {
        for(let mutation of mutationsList) {
            if (mutation.type === 'childList') {
                const element = document.querySelector('[msg-id="bad-links"]');
                if (element) {
                    element.style.display = 'none';
                    observer.disconnect();
                    break;
                }
            }
        }
    };


    addKeyListener(slot, targetNode) {
        document.addEventListener("keydown", (event) => {
            if (event.altKey && event.code === 'Digit'+slot) {
                this.centerOnNode(targetNode);
            }
        });
    }

    centerOnNode(node) {
        const canvas = app.canvas;

        // this.applyJumpEffect(canvas, node);
        canvas.ds.offset[0] = -node.pos[0] - node.size[0] * 0.5 + (canvas.canvas.width * 0.5) / canvas.ds.scale;
        canvas.ds.offset[1] = -node.pos[1] - node.size[1] * 0.5 + (canvas.canvas.height * 0.5) / canvas.ds.scale;
        canvas.dirty_bgcanvas = true;
        canvas.dirty_canvas = true;

    }

    addNewInputIfNeeded(slot) {
        let last_slot_number = this.inputs.length;
        if (last_slot_number === 10){ return }

        let last_slot = this.inputs[slot];
        if(last_slot.link !== undefined) {
            this.addInput(`Node ${last_slot_number+1}`, "*");
        }
    }

    onContextMenu(menu) {
        menu.push({
            title: 'Toggle Links Visibility',
            callback: () => this.toggleLinksVisibility()
        });
        return menu;
    }


    applyJumpEffect(canvas, node) {
        const originalOffsetX = -node.pos[0] - node.size[0] * 0.5 + (canvas.canvas.width * 0.5) / canvas.ds.scale;
        const originalOffsetY = -node.pos[1] - node.size[1] * 0.5 + (canvas.canvas.height * 0.5) / canvas.ds.scale;
        const duration = 300;
        const jumpIntensity = 5; 

        let startTime = Date.now();

        const jump = () => {
            let elapsed = Date.now() - startTime;
            let remaining = duration - elapsed;

            if (remaining <= 0) {
                // Reset the canvas position after jumping
                canvas.ds.offset[0] = originalOffsetX;
                canvas.ds.offset[1] = originalOffsetY;
                canvas.dirty_bgcanvas = true;
                canvas.dirty_canvas = true;
                return;
            }

            // Apply jumping effect
            canvas.ds.offset[0] = originalOffsetX + (Math.random() - 0.5) * jumpIntensity;
            canvas.ds.offset[1] = originalOffsetY + (Math.random() - 0.5) * jumpIntensity;
            canvas.dirty_bgcanvas = true;
            canvas.dirty_canvas = true;

            requestAnimationFrame(jump);
        };

        jump();
    }
}

LiteGraph.registerNodeType("Node Jumper", Object.assign(NodeJumper, { title: "Node Jumper 😱" }));
NodeJumper.category = "BDXNodes";

app.registerExtension({
    name: "BDXNodes.NodeJumper",
    setup() {
        console.log(`BDXNodes loaded`);
    },
    registerCustomNodes() {

    }
});
