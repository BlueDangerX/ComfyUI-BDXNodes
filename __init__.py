"""
@author: BlueDangerX
@title: BDXNodes
"""

import shutil
import folder_paths
import os
import sys

comfy_path = os.path.dirname(folder_paths.__file__)
bdxnodes_path = os.path.join(os.path.dirname(__file__))

def setup_js():
    # remove garbage
    old_js_path = os.path.join(comfy_path, "web", "extensions", "core", "SelectCopyPasta.js")
    if os.path.exists(old_js_path):
        os.remove(old_js_path)

    old_js_path = os.path.join(comfy_path, "web", "extensions", "core", "NodeJumper.js")
    if os.path.exists(old_js_path):
        os.remove(old_js_path)

    old_ip_path = os.path.join(comfy_path, "web", "extensions", "core", "imageProcessorWorker.js")
    if os.path.exists(old_ip_path):
        os.remove(old_ip_path)

    # setup js
    js_dest_path = os.path.join(comfy_path, "web", "extensions", "BDXNodes")
    if not os.path.exists(js_dest_path):
        os.makedirs(js_dest_path)

    js_src_path = os.path.join(bdxnodes_path, "js", "SelectCopyPasta.js")
    shutil.copy(js_src_path, js_dest_path)

    js_src_path = os.path.join(bdxnodes_path, "js", "NodeJumper.js")
    shutil.copy(js_src_path, js_dest_path)

    # setup ip
    ip_dest_path = os.path.join(comfy_path, "web", "extensions", "BDXNodes")
    if not os.path.exists(ip_dest_path):
        os.makedirs(ip_dest_path)

    ip_src_path = os.path.join(bdxnodes_path, "js", "imageProcessorWorker.js")
    shutil.copy(ip_src_path, ip_dest_path)

setup_js()


from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]