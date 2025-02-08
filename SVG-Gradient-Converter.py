import xml.etree.ElementTree as ET
import os
import argparse

def convert_svg_color_to_gradient(svg_path, output_path, color1, color2):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', namespace['svg'])
    
    # Define a linear gradient
    defs = root.find('svg:defs', namespace)
    if defs is None:
        defs = ET.Element('defs')
        root.insert(0, defs)
    
    gradient_id = 'gradient1'
    linear_gradient = ET.Element('linearGradient', {
        'id': gradient_id,
        'x1': '0%', 'y1': '0%', 'x2': '100%', 'y2': '100%'
    })
    
    stop1 = ET.Element('stop', {'offset': '0%', 'style': f'stop-color:{color1}; stop-opacity:1'})
    stop2 = ET.Element('stop', {'offset': '100%', 'style': f'stop-color:{color2}; stop-opacity:1'})
    
    linear_gradient.append(stop1)
    linear_gradient.append(stop2)
    defs.append(linear_gradient)
    
    # Replace solid color fills with gradient
    for elem in root.findall('.//*[@fill]', namespace):
        elem.set('fill', f'url(#{gradient_id})')
    
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

def process_folder(source_folder, destination_folder, color1, color2):
    if not os.path.exists(source_folder):
        print("Error: Source folder does not exist.")
        return
    
    os.makedirs(destination_folder, exist_ok=True)
    
    print("Processing SVG files...")
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".svg"):
            input_path = os.path.join(source_folder, file_name)
            output_path = os.path.join(destination_folder, file_name)
            convert_svg_color_to_gradient(input_path, output_path, color1, color2)
            print(f"Converted: {file_name}")
    print("Processing completed.")

def main():
    print("""
    SVG Gradient Converter
    -----------------------
    This tool converts solid color fills in SVG files to gradient fills.
    
    Usage:
      1. Run the application and provide parameters when prompted.
      2. Alternatively, run the application with command-line arguments:
         SVG-Gradient-Converter.exe <source_folder> <destination_folder> <color1> <color2>
      
    Example:
      SVG-Gradient-Converter.exe ./input ./output #FF0000 #0000FF
      (This will convert SVGs from input to output using a red-to-blue gradient.)
          
      For More Information Visit the 
      https://github.com/NSTechBytes/SVG-Gradient-Converter
    """)
    
    parser = argparse.ArgumentParser(description="Convert solid SVG colors to gradients.")
    parser.add_argument("source", nargs='?', help="Path to the source folder containing SVG files")
    parser.add_argument("destination", nargs='?', help="Path to the destination folder for processed SVG files")
    parser.add_argument("color1", nargs='?', help="Start color for the gradient (e.g., #FF0000)")
    parser.add_argument("color2", nargs='?', help="End color for the gradient (e.g., #0000FF)")
    
    args = parser.parse_args()
    
    if not args.source:
        args.source = input("Enter source folder path: ")
    if not args.destination:
        args.destination = input("Enter destination folder path: ")
    if not args.color1:
        args.color1 = input("Enter start gradient color (e.g., #FF0000): ")
    if not args.color2:
        args.color2 = input("Enter end gradient color (e.g., #0000FF): ")
    
    print("Starting conversion...")
    process_folder(args.source, args.destination, args.color1, args.color2)
    print("All files converted successfully!")

if __name__ == "__main__":
    main()
