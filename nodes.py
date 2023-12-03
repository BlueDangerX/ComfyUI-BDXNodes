import nodes
# import torch
# import torch.nn.functional as F
# import scipy.ndimage
# import numpy as np
# from PIL import ImageColor, Image, ImageDraw, ImageFont
import os
# import librosa
# from scipy.special import erf
# from .fluid import Fluid
# import comfy.model_management
# import math
from nodes import MAX_RESOLUTION

script_dir = os.path.dirname(os.path.abspath(__file__))

class BDXTestInt:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "value": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "steps": 5}),
        },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"

    CATEGORY = "BDXNodes"

    def get_value(self, value):
        return (value,)
    
# def gaussian_kernel(kernel_size: int, sigma: float, device=None):
#         x, y = torch.meshgrid(torch.linspace(-1, 1, kernel_size, device=device), torch.linspace(-1, 1, kernel_size, device=device), indexing="ij")
#         d = torch.sqrt(x * x + y * y)
#         g = torch.exp(-(d * d) / (2.0 * sigma * sigma))
#         return g / g.sum()


# class CreateAudioMask:
    
#     RETURN_TYPES = ("IMAGE",)
#     FUNCTION = "createaudiomask"
#     CATEGORY = "BDXNodes"

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                  "invert": ("BOOLEAN", {"default": False}),
#                  "frames": ("INT", {"default": 0,"min": 0, "max": 255, "step": 1}),
#                  "scale": ("FLOAT", {"default": 0.5,"min": 0.0, "max": 2.0, "step": 0.01}),
#                  "audio_path": ("STRING", {"default": "audio.wav"}),
#                  "width": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#                  "height": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#         },
#     } 

#     def createaudiomask(self, frames, width, height, invert, audio_path, scale):
#              # Define the number of images in the batch
#         batch_size = frames
#         out = []
#         masks = []
#         if audio_path == "audio.wav": #I don't know why relative path won't work otherwise...
#             audio_path = os.path.join(script_dir, audio_path)
#         audio, sr = librosa.load(audio_path)
#         spectrogram = np.abs(librosa.stft(audio))
        
#         for i in range(batch_size):
#            image = Image.new("RGB", (width, height), "black")
#            draw = ImageDraw.Draw(image)
#            frame = spectrogram[:, i]
#            circle_radius = int(height * np.mean(frame))
#            circle_radius *= scale
#            circle_center = (width // 2, height // 2)  # Calculate the center of the image

#            draw.ellipse([(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
#                       (circle_center[0] + circle_radius, circle_center[1] + circle_radius)],
#                       fill='white')
             
#            image = np.array(image).astype(np.float32) / 255.0
#            image = torch.from_numpy(image)[None,]
#            mask = image[:, :, :, 0] 
#            masks.append(mask)
#            out.append(image)

#         if invert:
#             return (1.0 - torch.cat(out, dim=0),)
#         return (torch.cat(out, dim=0),torch.cat(masks, dim=0),)
      

    
# class CreateGradientMask:
    
#     RETURN_TYPES = ("MASK",)
#     FUNCTION = "createmask"
#     CATEGORY = "BDXNodes"

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                  "invert": ("BOOLEAN", {"default": False}),
#                  "frames": ("INT", {"default": 0,"min": 0, "max": 255, "step": 1}),
#                  "width": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#                  "height": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#         },
#     } 
#     def createmask(self, frames, width, height, invert):
#         # Define the number of images in the batch
#         batch_size = frames
#         out = []
#         # Create an empty array to store the image batch
#         image_batch = np.zeros((batch_size, height, width), dtype=np.float32)
#         # Generate the black to white gradient for each image
#         for i in range(batch_size):
#             gradient = np.linspace(1.0, 0.0, width, dtype=np.float32)
#             time = i / frames  # Calculate the time variable
#             offset_gradient = gradient - time  # Offset the gradient values based on time
#             image_batch[i] = offset_gradient.reshape(1, -1)
#         output = torch.from_numpy(image_batch)
#         mask = output
#         out.append(mask)
#         if invert:
#             return (1.0 - torch.cat(out, dim=0),)
#         return (torch.cat(out, dim=0),)

# class CreateFadeMask:
    
#     RETURN_TYPES = ("MASK",)
#     FUNCTION = "createfademask"
#     CATEGORY = "BDXNodes"

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                  "invert": ("BOOLEAN", {"default": False}),
#                  "frames": ("INT", {"default": 0,"min": 0, "max": 255, "step": 1}),
#                  "width": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#                  "height": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#                  "interpolation": (["linear", "ease_in", "ease_out", "ease_in_out"],),
#                  "start_level": ("FLOAT", {"default": 1.0,"min": 0.0, "max": 1.0, "step": 0.01}),
#                  "midpoint_level": ("FLOAT", {"default": 0.5,"min": 0.0, "max": 1.0, "step": 0.01}),
#                  "end_level": ("FLOAT", {"default": 0.0,"min": 0.0, "max": 1.0, "step": 0.01}),
#         },
#     } 
    
#     def createfademask(self, frames, width, height, invert, interpolation, start_level, midpoint_level, end_level):
#         def ease_in(t):
#             return t * t

#         def ease_out(t):
#             return 1 - (1 - t) * (1 - t)

#         def ease_in_out(t):
#             return 3 * t * t - 2 * t * t * t

#         batch_size = frames
#         out = []
#         image_batch = np.zeros((batch_size, height, width), dtype=np.float32)
        
#         for i in range(batch_size):
#             t = i / (batch_size - 1)
            
#             if interpolation == "ease_in":
#                 t = ease_in(t)
#             elif interpolation == "ease_out":
#                 t = ease_out(t)
#             elif interpolation == "ease_in_out":
#                 t = ease_in_out(t)
            
#             if midpoint_level is not None:
#                 if t < 0.5:
#                     color = start_level - t * (start_level - midpoint_level) * 2
#                 else:
#                     color = midpoint_level - (t - 0.5) * (midpoint_level - end_level) * 2
#             else:
#                 color = start_level - t * (start_level - end_level)
            
#             image = np.full((height, width), color, dtype=np.float32)
#             image_batch[i] = image
            
#         output = torch.from_numpy(image_batch)
#         mask = output
#         out.append(mask)
        
#         if invert:
#             return (1.0 - torch.cat(out, dim=0),)
#         return (torch.cat(out, dim=0),)

# class CrossFadeImages:
    
#     RETURN_TYPES = ("IMAGE",)
#     FUNCTION = "crossfadeimages"
#     CATEGORY = "BDXNodes"

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                  "images_1": ("IMAGE",),
#                  "images_2": ("IMAGE",),
#                  "interpolation": (["linear", "ease_in", "ease_out", "ease_in_out", "bounce", "elastic", "glitchy", "exponential_ease_out"],),
#                  "transition_start_index": ("INT", {"default": 1,"min": 0, "max": 4096, "step": 1}),
#                  "transitioning_frames": ("INT", {"default": 1,"min": 0, "max": 4096, "step": 1}),
#                  "start_level": ("FLOAT", {"default": 0.0,"min": 0.0, "max": 1.0, "step": 0.01}),
#                  "end_level": ("FLOAT", {"default": 1.0,"min": 0.0, "max": 1.0, "step": 0.01}),
#         },
#     } 
    
#     def crossfadeimages(self, images_1, images_2, transition_start_index, transitioning_frames, interpolation, start_level, end_level):

#         def crossfade(images_1, images_2, alpha):
#             crossfade = (1 - alpha) * images_1 + alpha * images_2
#             return crossfade
#         def ease_in(t):
#             return t * t
#         def ease_out(t):
#             return 1 - (1 - t) * (1 - t)
#         def ease_in_out(t):
#             return 3 * t * t - 2 * t * t * t
#         def bounce(t):
#             if t < 0.5:
#                 return self.ease_out(t * 2) * 0.5
#             else:
#                 return self.ease_in((t - 0.5) * 2) * 0.5 + 0.5
#         def elastic(t):
#             return math.sin(13 * math.pi / 2 * t) * math.pow(2, 10 * (t - 1))
#         def glitchy(t):
#             return t + 0.1 * math.sin(40 * t)
#         def exponential_ease_out(t):
#             return 1 - (1 - t) ** 4

#         easing_functions = {
#             "linear": lambda t: t,
#             "ease_in": ease_in,
#             "ease_out": ease_out,
#             "ease_in_out": ease_in_out,
#             "bounce": bounce,
#             "elastic": elastic,
#             "glitchy": glitchy,
#             "exponential_ease_out": exponential_ease_out,
#         }

#         crossfade_images = []
        
#         alphas = torch.linspace(start_level, end_level, transitioning_frames)
#         for i in range(transitioning_frames):
#             alpha = alphas[i]
#             image1 = images_1[i - transition_start_index]
#             image2 = images_2[i + transition_start_index]
#             easing_function = easing_functions.get(interpolation)
#             alpha = easing_function(alpha)  # Apply the easing function to the alpha value

#             crossfade_image = crossfade(image1, image2, alpha)
#             crossfade_images.append(crossfade_image)
            
#         # Convert crossfade_images to tensor
#         crossfade_images = torch.stack(crossfade_images, dim=0)
#         # Append the remaining frames from images_2
#         remaining_images_2 = images_2[transition_start_index + transitioning_frames:]
#         crossfade_images = torch.cat([crossfade_images, remaining_images_2], dim=0)

#         # Append the beginning of images_1
#         beginning_images_1 = images_1[:transition_start_index]
#         crossfade_images = torch.cat([beginning_images_1, crossfade_images], dim=0)

#         return (crossfade_images,)

# class CreateTextMask:
    
#     RETURN_TYPES = ("IMAGE", "MASK",)
#     FUNCTION = "createtextmask"
#     CATEGORY = "BDXNodes"

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                  "invert": ("BOOLEAN", {"default": False}),
#                  "frames": ("INT", {"default": 1,"min": 1, "max": 4096, "step": 1}),
#                  "text_x": ("INT", {"default": 0,"min": 0, "max": 4096, "step": 1}),
#                  "text_y": ("INT", {"default": 0,"min": 0, "max": 4096, "step": 1}),
#                  "font_size": ("INT", {"default": 32,"min": 8, "max": 4096, "step": 1}),
#                  "text": ("STRING", {"default": "HELLO!"}),
#                  "font_path": ("STRING", {"default": "fonts\\TTNorms-Black.otf"}),
#                  "width": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#                  "height": ("INT", {"default": 256,"min": 16, "max": 4096, "step": 1}),
#                  "start_rotation": ("INT", {"default": 0,"min": 0, "max": 359, "step": 1}),
#                  "end_rotation": ("INT", {"default": 359,"min": -359, "max": 359, "step": 1}),
#         },
#     } 

#     def createtextmask(self, frames, width, height, invert, text_x, text_y, text, font_size, font_path, start_rotation, end_rotation):
#         # Define the number of images in the batch
#         batch_size = frames
#         out = []
#         masks = []
#         rotation = start_rotation
#         if frames > 1:
#             rotation_increment = (end_rotation - start_rotation) / (batch_size - 1)
#         if font_path == "fonts\\TTNorms-Black.otf": #I don't know why relative path won't work otherwise...
#             font_path = os.path.join(script_dir, font_path)
#         # Generate the text
#         for i in range(batch_size):
#            image = Image.new("RGB", (width, height), "black")
#            draw = ImageDraw.Draw(image)
#            font = ImageFont.truetype(font_path, font_size)
#            text_width, text_height = draw.textsize(text, font=font)
#            text_center_x = text_x + text_width / 2
#            text_center_y = text_y + text_height / 2
#            draw.text((text_x, text_y), text, font=font, fill="white")
#            image = image.rotate(rotation, center=(text_center_x, text_center_y))
#            image = np.array(image).astype(np.float32) / 255.0
#            image = torch.from_numpy(image)[None,]
#            mask = image[:, :, :, 0] 
#            masks.append(mask)
#            out.append(image)
#            rotation += rotation_increment
#         if invert:
#             return (1.0 - torch.cat(out, dim=0),)
#         return (torch.cat(out, dim=0),torch.cat(masks, dim=0),)
    
# class GrowMaskWithBlur:
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "mask": ("MASK",),
#                 "expand": ("INT", {"default": 0, "min": -MAX_RESOLUTION, "max": MAX_RESOLUTION, "step": 1}),
#                 "incremental_expandrate": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1}),
#                 "tapered_corners": ("BOOLEAN", {"default": True}),
#                 "flip_input": ("BOOLEAN", {"default": False}),
#                 "use_cuda": ("BOOLEAN", {"default": True}),
#                 "blur_radius": ("INT", {
#                     "default": 0,
#                     "min": 0,
#                     "max": 999,
#                     "step": 1
#                 }),
#                 "sigma": ("FLOAT", {
#                     "default": 1.0,
#                     "min": 0.1,
#                     "max": 10.0,
#                     "step": 0.1
#                 }),
#             },
#         }
    
#     CATEGORY = "BDXNodes"

#     RETURN_TYPES = ("MASK", "MASK",)
#     RETURN_NAMES = ("mask", "mask_inverted",)
#     FUNCTION = "expand_mask"
    
#     def expand_mask(self, mask, expand, tapered_corners, flip_input, blur_radius, sigma, incremental_expandrate, use_cuda):
#         if( flip_input ):
#             mask = 1.0 - mask
#         c = 0 if tapered_corners else 1
#         kernel = np.array([[c, 1, c],
#                            [1, 1, 1],
#                            [c, 1, c]])
#         growmask = mask.reshape((-1, mask.shape[-2], mask.shape[-1]))
#         out = []
#         for m in growmask:
#             output = m.numpy()
#             for _ in range(abs(expand)):
#                 if expand < 0:
#                     output = scipy.ndimage.grey_erosion(output, footprint=kernel)
#                 else:
#                     output = scipy.ndimage.grey_dilation(output, footprint=kernel)
#             if expand < 0:
#                 expand -= abs(incremental_expandrate)  # Use abs(growrate) to ensure positive change
#             else:
#                 expand += abs(incremental_expandrate)  # Use abs(growrate) to ensure positive change
#             output = torch.from_numpy(output)
#             out.append(output)

#         blurred = torch.stack(out, dim=0).reshape((-1, 1, mask.shape[-2], mask.shape[-1])).movedim(1, -1).expand(-1, -1, -1, 3)
#         if use_cuda:    
#             device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#             blurred = blurred.to(device)  # Move blurred tensor to the GPU

#         batch_size, height, width, channels = blurred.shape
#         if blur_radius != 0:
#             blurkernel_size = blur_radius * 2 + 1
#             blurkernel = gaussian_kernel(blurkernel_size, sigma, device=blurred.device).repeat(channels, 1, 1).unsqueeze(1)
#             blurred = blurred.permute(0, 3, 1, 2) # Torch wants (B, C, H, W) we use (B, H, W, C)
#             padded_image = F.pad(blurred, (blur_radius,blur_radius,blur_radius,blur_radius), 'reflect')
#             blurred = F.conv2d(padded_image, blurkernel, padding=blurkernel_size // 2, groups=channels)[:,:,blur_radius:-blur_radius, blur_radius:-blur_radius]
#             blurred = blurred.permute(0, 2, 3, 1)
#             blurred = blurred[:, :, :, 0]        
#             return (blurred, 1.0 - blurred,)
#         return (torch.stack(out, dim=0), 1.0 -torch.stack(out, dim=0),)
           
        
    

# class ColorToMask:
    
#     RETURN_TYPES = ("MASK",)
#     FUNCTION = "clip"
#     CATEGORY = "BDXNodes"

#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                  "images": ("IMAGE",),
#                  "invert": ("BOOLEAN", {"default": False}),
#                  "red": ("INT", {"default": 0,"min": 0, "max": 255, "step": 1}),
#                  "green": ("INT", {"default": 0,"min": 0, "max": 255, "step": 1}),
#                  "blue": ("INT", {"default": 0,"min": 0, "max": 255, "step": 1}),
#                  "threshold": ("INT", {"default": 10,"min": 0, "max": 255, "step": 1}),
#         },
#     } 

#     def clip(self, images, red, green, blue, threshold, invert):
#         color = np.array([red, green, blue])
#         images = 255. * images.cpu().numpy()
#         images = np.clip(images, 0, 255).astype(np.uint8)
#         images = [Image.fromarray(image) for image in images]
#         images = [np.array(image) for image in images]

#         black = [0, 0, 0]
#         white = [255, 255, 255]
#         if invert:
#              black, white = white, black

#         new_images = []
#         for image in images:
#             new_image = np.full_like(image, black)

#             color_distances = np.linalg.norm(image - color, axis=-1)
#             complement_indexes = color_distances <= threshold

#             new_image[complement_indexes] = white

#             new_images.append(new_image)

#         new_images = np.array(new_images).astype(np.float32) / 255.0
#         new_images = torch.from_numpy(new_images).permute(3, 0, 1, 2)
#         return new_images
      
# class ConditioningMultiCombine:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 "inputcount": ("INT", {"default": 2, "min": 2, "max": 20, "step": 1}),
#                 "conditioning_1": ("CONDITIONING", ),
#                 "conditioning_2": ("CONDITIONING", ),
#             },
        
#     }

#     RETURN_TYPES = ("CONDITIONING", "INT")
#     RETURN_NAMES = ("combined", "inputcount")
#     FUNCTION = "combine"
#     CATEGORY = "BDXNodes"

#     def combine(self, inputcount, **kwargs):
#         cond_combine_node = nodes.ConditioningCombine()
#         cond = kwargs["conditioning_1"]
#         for c in range(1, inputcount):
#             new_cond = kwargs[f"conditioning_{c + 1}"]
#             cond = cond_combine_node.combine(new_cond, cond)[0]
#         return (cond, inputcount,)

# def append_helper(t, mask, c, set_area_to_bounds, strength):
#         n = [t[0], t[1].copy()]
#         _, h, w = mask.shape
#         n[1]['mask'] = mask
#         n[1]['set_area_to_bounds'] = set_area_to_bounds
#         n[1]['mask_strength'] = strength
#         c.append(n)  

# class ConditioningSetMaskAndCombine:
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "positive_1": ("CONDITIONING", ),
#                 "negative_1": ("CONDITIONING", ),
#                 "positive_2": ("CONDITIONING", ),
#                 "negative_2": ("CONDITIONING", ),
#                 "mask_1": ("MASK", ),
#                 "mask_2": ("MASK", ),
#                 "mask_1_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_2_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "set_cond_area": (["default", "mask bounds"],),
#             }
#         }

#     RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
#     RETURN_NAMES = ("combined_positive", "combined_negative",)
#     FUNCTION = "append"
#     CATEGORY = "BDXNodes"

#     def append(self, positive_1, negative_1, positive_2, negative_2, mask_1, mask_2, set_cond_area, mask_1_strength, mask_2_strength):
#         c = []
#         c2 = []
#         set_area_to_bounds = False
#         if set_cond_area != "default":
#             set_area_to_bounds = True
#         if len(mask_1.shape) < 3:
#             mask_1 = mask_1.unsqueeze(0)
#         if len(mask_2.shape) < 3:
#             mask_2 = mask_2.unsqueeze(0)
#         for t in positive_1:
#             append_helper(t, mask_1, c, set_area_to_bounds, mask_1_strength)
#         for t in positive_2:
#             append_helper(t, mask_2, c, set_area_to_bounds, mask_2_strength)
#         for t in negative_1:
#             append_helper(t, mask_1, c2, set_area_to_bounds, mask_1_strength)
#         for t in negative_2:
#             append_helper(t, mask_2, c2, set_area_to_bounds, mask_2_strength)
#         return (c, c2)

# class ConditioningSetMaskAndCombine3:
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "positive_1": ("CONDITIONING", ),
#                 "negative_1": ("CONDITIONING", ),
#                 "positive_2": ("CONDITIONING", ),
#                 "negative_2": ("CONDITIONING", ),
#                 "positive_3": ("CONDITIONING", ),
#                 "negative_3": ("CONDITIONING", ),
#                 "mask_1": ("MASK", ),
#                 "mask_2": ("MASK", ),
#                 "mask_3": ("MASK", ),
#                 "mask_1_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_2_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_3_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "set_cond_area": (["default", "mask bounds"],),
#             }
#         }

#     RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
#     RETURN_NAMES = ("combined_positive", "combined_negative",)
#     FUNCTION = "append"
#     CATEGORY = "BDXNodes"

#     def append(self, positive_1, negative_1, positive_2, positive_3, negative_2, negative_3, mask_1, mask_2, mask_3, set_cond_area, mask_1_strength, mask_2_strength, mask_3_strength):
#         c = []
#         c2 = []
#         set_area_to_bounds = False
#         if set_cond_area != "default":
#             set_area_to_bounds = True
#         if len(mask_1.shape) < 3:
#             mask_1 = mask_1.unsqueeze(0)
#         if len(mask_2.shape) < 3:
#             mask_2 = mask_2.unsqueeze(0)
#         if len(mask_3.shape) < 3:
#             mask_3 = mask_3.unsqueeze(0)
#         for t in positive_1:
#             append_helper(t, mask_1, c, set_area_to_bounds, mask_1_strength)
#         for t in positive_2:
#             append_helper(t, mask_2, c, set_area_to_bounds, mask_2_strength)
#         for t in positive_3:
#             append_helper(t, mask_3, c, set_area_to_bounds, mask_3_strength)
#         for t in negative_1:
#             append_helper(t, mask_1, c2, set_area_to_bounds, mask_1_strength)
#         for t in negative_2:
#             append_helper(t, mask_2, c2, set_area_to_bounds, mask_2_strength)
#         for t in negative_3:
#             append_helper(t, mask_3, c2, set_area_to_bounds, mask_3_strength)
#         return (c, c2)

# class ConditioningSetMaskAndCombine4:
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "positive_1": ("CONDITIONING", ),
#                 "negative_1": ("CONDITIONING", ),
#                 "positive_2": ("CONDITIONING", ),
#                 "negative_2": ("CONDITIONING", ),
#                 "positive_3": ("CONDITIONING", ),
#                 "negative_3": ("CONDITIONING", ),
#                 "positive_4": ("CONDITIONING", ),
#                 "negative_4": ("CONDITIONING", ),
#                 "mask_1": ("MASK", ),
#                 "mask_2": ("MASK", ),
#                 "mask_3": ("MASK", ),
#                 "mask_4": ("MASK", ),
#                 "mask_1_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_2_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_3_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_4_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "set_cond_area": (["default", "mask bounds"],),
#             }
#         }

#     RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
#     RETURN_NAMES = ("combined_positive", "combined_negative",)
#     FUNCTION = "append"
#     CATEGORY = "BDXNodes"

#     def append(self, positive_1, negative_1, positive_2, positive_3, positive_4, negative_2, negative_3, negative_4, mask_1, mask_2, mask_3, mask_4, set_cond_area, mask_1_strength, mask_2_strength, mask_3_strength, mask_4_strength):
#         c = []
#         c2 = []
#         set_area_to_bounds = False
#         if set_cond_area != "default":
#             set_area_to_bounds = True
#         if len(mask_1.shape) < 3:
#             mask_1 = mask_1.unsqueeze(0)
#         if len(mask_2.shape) < 3:
#             mask_2 = mask_2.unsqueeze(0)
#         if len(mask_3.shape) < 3:
#             mask_3 = mask_3.unsqueeze(0)
#         if len(mask_4.shape) < 3:
#             mask_4 = mask_4.unsqueeze(0)
#         for t in positive_1:
#             append_helper(t, mask_1, c, set_area_to_bounds, mask_1_strength)
#         for t in positive_2:
#             append_helper(t, mask_2, c, set_area_to_bounds, mask_2_strength)
#         for t in positive_3:
#             append_helper(t, mask_3, c, set_area_to_bounds, mask_3_strength)
#         for t in positive_4:
#             append_helper(t, mask_4, c, set_area_to_bounds, mask_4_strength)
#         for t in negative_1:
#             append_helper(t, mask_1, c2, set_area_to_bounds, mask_1_strength)
#         for t in negative_2:
#             append_helper(t, mask_2, c2, set_area_to_bounds, mask_2_strength)
#         for t in negative_3:
#             append_helper(t, mask_3, c2, set_area_to_bounds, mask_3_strength)
#         for t in negative_4:
#             append_helper(t, mask_4, c2, set_area_to_bounds, mask_4_strength)
#         return (c, c2)

# class ConditioningSetMaskAndCombine5:
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "positive_1": ("CONDITIONING", ),
#                 "negative_1": ("CONDITIONING", ),
#                 "positive_2": ("CONDITIONING", ),
#                 "negative_2": ("CONDITIONING", ),
#                 "positive_3": ("CONDITIONING", ),
#                 "negative_3": ("CONDITIONING", ),
#                 "positive_4": ("CONDITIONING", ),
#                 "negative_4": ("CONDITIONING", ),
#                 "positive_5": ("CONDITIONING", ),
#                 "negative_5": ("CONDITIONING", ),
#                 "mask_1": ("MASK", ),
#                 "mask_2": ("MASK", ),
#                 "mask_3": ("MASK", ),
#                 "mask_4": ("MASK", ),
#                 "mask_5": ("MASK", ),
#                 "mask_1_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_2_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_3_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_4_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "mask_5_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
#                 "set_cond_area": (["default", "mask bounds"],),
#             }
#         }

#     RETURN_TYPES = ("CONDITIONING","CONDITIONING",)
#     RETURN_NAMES = ("combined_positive", "combined_negative",)
#     FUNCTION = "append"
#     CATEGORY = "BDXNodes"

#     def append(self, positive_1, negative_1, positive_2, positive_3, positive_4, positive_5, negative_2, negative_3, negative_4, negative_5, mask_1, mask_2, mask_3, mask_4, mask_5, set_cond_area, mask_1_strength, mask_2_strength, mask_3_strength, mask_4_strength, mask_5_strength):
#         c = []
#         c2 = []
#         set_area_to_bounds = False
#         if set_cond_area != "default":
#             set_area_to_bounds = True
#         if len(mask_1.shape) < 3:
#             mask_1 = mask_1.unsqueeze(0)
#         if len(mask_2.shape) < 3:
#             mask_2 = mask_2.unsqueeze(0)
#         if len(mask_3.shape) < 3:
#             mask_3 = mask_3.unsqueeze(0)
#         if len(mask_4.shape) < 3:
#             mask_4 = mask_4.unsqueeze(0)
#         if len(mask_5.shape) < 3:
#             mask_5 = mask_5.unsqueeze(0)
#         for t in positive_1:
#             append_helper(t, mask_1, c, set_area_to_bounds, mask_1_strength)
#         for t in positive_2:
#             append_helper(t, mask_2, c, set_area_to_bounds, mask_2_strength)
#         for t in positive_3:
#             append_helper(t, mask_3, c, set_area_to_bounds, mask_3_strength)
#         for t in positive_4:
#             append_helper(t, mask_4, c, set_area_to_bounds, mask_4_strength)
#         for t in positive_5:
#             append_helper(t, mask_5, c, set_area_to_bounds, mask_5_strength)
#         for t in negative_1:
#             append_helper(t, mask_1, c2, set_area_to_bounds, mask_1_strength)
#         for t in negative_2:
#             append_helper(t, mask_2, c2, set_area_to_bounds, mask_2_strength)
#         for t in negative_3:
#             append_helper(t, mask_3, c2, set_area_to_bounds, mask_3_strength)
#         for t in negative_4:
#             append_helper(t, mask_4, c2, set_area_to_bounds, mask_4_strength)
#         for t in negative_5:
#             append_helper(t, mask_5, c2, set_area_to_bounds, mask_5_strength)
#         return (c, c2)
    
# class VRAM_Debug:
    
#     @classmethod
    
#     def INPUT_TYPES(s):
#       return {
#         "required": {
# 			  "model": ("MODEL",),
#               "empty_cuda_cache": ("BOOLEAN", {"default": False}),
# 		  },
#         "optional": {
#             "clip_vision": ("CLIP_VISION", ),
#         }
# 	  }
#     RETURN_TYPES = ("MODEL", "INT", "INT",)
#     RETURN_NAMES = ("model", "freemem_before", "freemem_after")
#     FUNCTION = "VRAMdebug"
#     CATEGORY = "BDXNodes"

#     def VRAMdebug(self, model, empty_cuda_cache, clip_vision=None):
#         freemem_before = comfy.model_management.get_free_memory()
#         print(freemem_before)
#         if empty_cuda_cache:
#             torch.cuda.empty_cache()
#             torch.cuda.ipc_collect()
#         if clip_vision is not None:
#             print("unloading clip_vision_clone")
#             comfy.model_management.unload_model_clones(clip_vision.patcher)
#         freemem_after = comfy.model_management.get_free_memory()
#         print(freemem_after)
#         return (model, freemem_before, freemem_after)
    
# class SomethingToString:
#     @classmethod
    
#     def INPUT_TYPES(s):
#      return {
#         "required": {
#         "input": ("*", {"forceinput": True, "default": ""}),
#     },
#     }
#     RETURN_TYPES = ("STRING",)
#     FUNCTION = "stringify"
#     CATEGORY = "BDXNodes"

#     def stringify(self, input):
#         if isinstance(input, (int, float, bool)):   
#             stringified = str(input)
#             print(stringified)
#         else:
#             return
#         return (stringified,)

# from nodes import EmptyLatentImage

# class EmptyLatentImagePresets:
#     @classmethod
#     def INPUT_TYPES(cls):  
#         return {
#         "required": {
#             "dimensions": (
#             [   '768 x 512',
#                 '960 x 512',
#                 '1024 x 512',
#                 '1536 x 640',
#                 '1536 x 640',
#                 '1344 x 768',
#                 '1216 x 832',
#                 '1152 x 896',
#                 '1024 x 1024',
#             ],
#             {
#             "default": '1024 x 1024'
#              }),
           
#             "invert": ("BOOLEAN", {"default": False}),
#             "batch_size": ("INT", {
#             "default": 1,
#             "min": 1,
#             "max": 4096
#             }),
#         },
#         }

#     RETURN_TYPES = ("LATENT", "INT", "INT")
#     RETURN_NAMES = ("Latent", "Width", "Height")
#     FUNCTION = "generate"
#     CATEGORY = "BDXNodes"

#     def generate(self, dimensions, invert, batch_size):
#         result = [x.strip() for x in dimensions.split('x')]
        
#         if invert:
#             width = int(result[1].split(' ')[0])
#             height = int(result[0])
#         else:
#             width = int(result[0])
#             height = int(result[1].split(' ')[0])
#         latent = EmptyLatentImage().generate(width, height, batch_size)[0]

#         return (latent, int(width), int(height),)

# #https://github.com/hahnec/color-matcher/
# from color_matcher import ColorMatcher
# from color_matcher.normalizer import Normalizer

# class ColorMatch:
#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "image_ref": ("IMAGE",),
#                 "image_target": ("IMAGE",),
#                 "method": (
#             [   
#                 'mkl',
#                 'hm', 
#                 'reinhard', 
#                 'mvgd', 
#                 'hm-mvgd-hm', 
#                 'hm-mkl-hm',
#             ], {
#                "default": 'mkl'
#             }),
                
#             },
#         }
    
#     CATEGORY = "BDXNodes"

#     RETURN_TYPES = ("IMAGE",)
#     RETURN_NAMES = ("image",)
#     FUNCTION = "colormatch"
    
#     def colormatch(self, image_ref, image_target, method):
#         cm = ColorMatcher()
#         batch_size = image_target.size(0)
#         out = []
#         images_target = image_target.squeeze()
#         images_ref = image_ref.squeeze()

#         image_ref_np = images_ref.numpy()
#         images_target_np = images_target.numpy()

#         if image_ref.size(0) > 1 and image_ref.size(0) != batch_size:
#             raise ValueError("ColorMatch: Use either single reference image or a matching batch of reference images.")

#         for i in range(batch_size):
#             image_target_np = images_target_np if batch_size == 1 else images_target[i].numpy()
#             image_ref_np_i = image_ref_np if image_ref.size(0) == 1 else images_ref[i].numpy()
#             try:
#                 image_result = cm.transfer(src=image_target_np, ref=image_ref_np_i, method=method)
#             except BaseException as e:
#                 print(f"Error occurred during transfer: {e}")
#                 break
#             out.append(torch.from_numpy(image_result))
#         return (torch.stack(out, dim=0).to(torch.float32), )


NODE_CLASS_MAPPINGS = {
    "BDXTestInt": BDXTestInt,
    # "ConditioningMultiCombine": ConditioningMultiCombine,
    # "ConditioningSetMaskAndCombine": ConditioningSetMaskAndCombine,
    # "ConditioningSetMaskAndCombine3": ConditioningSetMaskAndCombine3,
    # "ConditioningSetMaskAndCombine4": ConditioningSetMaskAndCombine4,
    # "ConditioningSetMaskAndCombine5": ConditioningSetMaskAndCombine5,
    # "GrowMaskWithBlur": GrowMaskWithBlur,
    # "ColorToMask": ColorToMask,
    # "CreateGradientMask": CreateGradientMask,
    # "CreateTextMask": CreateTextMask,
    # "CreateAudioMask": CreateAudioMask,
    # "CreateFadeMask": CreateFadeMask,
    # "CreateFluidMask" :CreateFluidMask,
    # "VRAM_Debug" : VRAM_Debug,
    # "SomethingToString" : SomethingToString,
    # "CrossFadeImages": CrossFadeImages,
    # "EmptyLatentImagePresets": EmptyLatentImagePresets,
    # "ColorMatch": ColorMatch,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "BDXTestInt": "Test INT Constant (BDX)",
}