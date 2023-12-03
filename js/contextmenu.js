// import { app } from "../../../scripts/app.js";


// // Adds context menu entries, code partly from pyssssscustom-scripts

// function addMenuHandler(nodeType, cb) {
// 	const getOpts = nodeType.prototype.getExtraMenuOptions;
// 	nodeType.prototype.getExtraMenuOptions = function () {
// 		const r = getOpts.apply(this, arguments);
// 		cb.apply(this, arguments);
// 		return r;
// 	};
// }

// function addNode(name, nextTo, options) {
// 	console.log("name:", name);
// 	console.log("nextTo:", nextTo);
// 	options = { side: "left", select: true, shiftY: 0, shiftX: 0, ...(options || {}) };
// 	const node = LiteGraph.createNode(name);
// 	app.graph.add(node);
	
// 	node.pos = [
// 		options.side === "left" ? nextTo.pos[0] - (node.size[0] + options.offset): nextTo.pos[0] + nextTo.size[0] + options.offset,
		
// 		nextTo.pos[1] + options.shiftY,
// 	];
// 	if (options.select) {
// 		app.canvas.selectNode(node, false);
// 	}
// 	return node;
// }

// app.registerExtension({
// 	name: "BDXNodesContextmenu",
// 	async beforeRegisterNodeDef(nodeType, nodeData, app) {
// 		if (nodeData.input && nodeData.input.required) {
// 			addMenuHandler(nodeType, function (_, options) {
// 				options.unshift(
// 					{
// 					content: "Add GetNode",
// 					callback: () => {addNode("GetNode", this, { side:"left", offset: 30});}
// 					},
// 					{
// 					content: "Add SetNode",
// 					callback: () => {addNode("SetNode", this, { side:"right", offset: 30 });
// 					},
					
// 				});
// 			});
				
// 		}
		

// 	},
// 		async setup(app) {
// 			const onChange = (value) => {
// 				if (value) {
// 					const valuesToAddToIn = ["GetNode"];
// 					const valuesToAddToOut = ["SetNode"];
			
// 					for (const arr of Object.values(LiteGraph.slot_types_default_in)) {
// 						for (const valueToAdd of valuesToAddToIn) {
// 							const idx = arr.indexOf(valueToAdd);
// 							if (idx !== 0) {
// 								arr.splice(idx, 1);
// 							}
// 							arr.unshift(valueToAdd);
// 						}
// 					}
			
// 					for (const arr of Object.values(LiteGraph.slot_types_default_out)) {
// 						for (const valueToAdd of valuesToAddToOut) {
// 							const idx = arr.indexOf(valueToAdd);
// 							if (idx !== 0) {
// 								arr.splice(idx, 1);
// 							}
// 							arr.unshift(valueToAdd);
// 						}
// 					}
// 				}
// 			};
			
// 			app.ui.settings.addSetting({
// 				id: "KJNodes.SetGetMenu",
// 				name: "🔗💥⛓️ Make Set/Get -nodes defaults (turn off and reload to disable)",
// 				defaultValue: false,
// 				type: "boolean",
// 				options: (value) => [
// 					{
// 						value: true,
// 						text: "On",
// 						selected: value === true,
// 					},
// 					{
// 						value: false,
// 						text: "Off",
// 						selected: value === false,
// 					},
// 				],
// 				onChange: onChange,
				
// 			});
// 			app.ui.settings.addSetting({
// 				id: "KJNodes.DisableMiddleClickDefault",
// 				name: "Middle click default node adding",
// 				defaultValue: false,
// 				type: "boolean",
// 				options: (value) => [
// 					{ value: true, text: "On", selected: value === true },
// 					{ value: false, text: "Off", selected: value === false },
// 				],
// 				onChange: (value) => {
// 					LiteGraph.middle_click_slot_add_default_node = value;
// 				},
// 			});
// }
// });
