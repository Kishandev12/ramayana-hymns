#!/usr/bin/env python3
"""
Ramayana Hymns - Easy Hymn Addition Script
This script helps you add new hymns to your website without coding!
"""

import json
import re
from datetime import datetime

def get_input(prompt, required=True):
    """Get input from user with validation"""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("⚠️  This field is required. Please try again.\n")

def select_kanda():
    """Let user select which Kanda"""
    kandas = [
        ('bala', 'Bala Kanda (Childhood)'),
        ('ayodhya', 'Ayodhya Kanda (Ayodhya)'),
        ('aranya', 'Aranya Kanda (Forest)'),
        ('kishkinda', 'Kishkinda Kanda (Kishkinda)'),
        ('sundara', 'Sundara Kanda (Beautiful)'),
        ('yuddha', 'Yuddha Kanda (War)'),
        ('uttara', 'Uttara Kanda (After)')
    ]
    
    print("\n📚 Select Kanda:")
    for i, (key, name) in enumerate(kandas, 1):
        print(f"  {i}. {name}")
    
    while True:
        choice = input("\nEnter number (1-7): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 7:
            return kandas[int(choice) - 1][0]
        print("⚠️  Please enter a number between 1 and 7")

def create_hymn():
    """Interactive hymn creation"""
    print("\n" + "="*60)
    print("🕉️  RAMAYANA HYMNS - ADD NEW HYMN")
    print("="*60)
    print("\nLet's add a new hymn! Answer the following questions:\n")
    
    hymn = {}
    
    # Basic Info
    hymn['kanda'] = select_kanda()
    print(f"\n✅ Selected: {hymn['kanda'].capitalize()} Kanda")
    
    hymn['title'] = get_input("\n📝 Hymn Title (e.g., 'Hanuman's Prayer'): ")
    hymn['subtitle'] = get_input("📍 Subtitle (e.g., 'Sarga 15'): ")
    hymn['preview'] = get_input("📄 Short Preview (1-2 sentences): ")
    
    print("\n" + "-"*60)
    print("Sanskrit Text (Press Enter twice when done):")
    print("-"*60)
    sanskrit_lines = []
    while True:
        line = input()
        if line:
            sanskrit_lines.append(line)
        elif sanskrit_lines:
            break
    hymn['sanskrit'] = '\\n'.join(sanskrit_lines)
    
    hymn['transliteration'] = get_input("\n🔤 Transliteration (Roman script): ")
    
    print("\n" + "-"*60)
    print("Translation (English):")
    print("-"*60)
    translation_lines = []
    while True:
        line = input()
        if line:
            translation_lines.append(line)
        elif translation_lines:
            break
    hymn['translation'] = ' '.join(translation_lines)
    
    hymn['context'] = get_input("\n📖 Context/Background: ")
    
    # Optional full content
    add_more = input("\n➕ Add detailed content? (y/n): ").lower()
    if add_more == 'y':
        print("\n" + "-"*60)
        print("Additional Content (HTML allowed, press Enter twice when done):")
        print("Example: <h2 class='section-title'>More Details</h2>")
        print("-"*60)
        content_lines = []
        while True:
            line = input()
            if line:
                content_lines.append(line)
            elif content_lines:
                break
        hymn['fullContent'] = '\\n'.join(content_lines)
    else:
        hymn['fullContent'] = ''
    
    return hymn

def escape_js_string(s):
    """Escape string for JavaScript"""
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    return s

def add_to_index_html(hymn):
    """Add hymn to index.html file"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the hymnsData array
        match = re.search(r'const hymnsData = \[(.*?)\];', content, re.DOTALL)
        if not match:
            print("❌ Error: Could not find hymnsData array in index.html")
            return False
        
        # Create new hymn object
        new_hymn = f"""
            {{
                kanda: '{hymn['kanda']}',
                title: '{escape_js_string(hymn['title'])}',
                subtitle: '{escape_js_string(hymn['subtitle'])}',
                preview: '{escape_js_string(hymn['preview'])}',
                sanskrit: '{escape_js_string(hymn['sanskrit'])}',
                transliteration: '{escape_js_string(hymn['transliteration'])}',
                translation: '{escape_js_string(hymn['translation'])}',
                context: '{escape_js_string(hymn['context'])}',
                fullContent: `{hymn['fullContent']}`
            }}"""
        
        # Insert before the closing bracket
        existing_data = match.group(1)
        new_data = existing_data.rstrip() + ',' + new_hymn + '\n        '
        
        new_content = content.replace(
            f'const hymnsData = [{existing_data}];',
            f'const hymnsData = [{new_data}];'
        )
        
        # Backup original
        with open('index.html.backup', 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Write new content
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function"""
    print("\n🙏 Welcome to Ramayana Hymns Addition Tool\n")
    
    while True:
        hymn = create_hymn()
        
        print("\n" + "="*60)
        print("📋 HYMN SUMMARY")
        print("="*60)
        print(f"Kanda: {hymn['kanda'].capitalize()}")
        print(f"Title: {hymn['title']}")
        print(f"Subtitle: {hymn['subtitle']}")
        print(f"Preview: {hymn['preview'][:60]}...")
        print("="*60)
        
        confirm = input("\n✅ Add this hymn to website? (y/n): ").lower()
        
        if confirm == 'y':
            print("\n⏳ Adding hymn to index.html...")
            if add_to_index_html(hymn):
                print("✅ Hymn added successfully!")
                print("📁 Backup saved as: index.html.backup")
                
                print("\n📤 Next steps:")
                print("1. Run: git add index.html")
                print("2. Run: git commit -m 'Added new hymn: " + hymn['title'] + "'")
                print("3. Run: git push")
                print("4. Wait 2-3 minutes and check your website!")
            else:
                print("❌ Failed to add hymn. Check errors above.")
        
        another = input("\n➕ Add another hymn? (y/n): ").lower()
        if another != 'y':
            break
    
    print("\n🙏 Thank you! Your hymns have been added.\n")

if __name__ == "__main__":
    main()
