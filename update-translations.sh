#!/bin/bash

# Script to update DuelPy translations
# Usage: ./update-translations.sh [command]
#   update    - Update existing translations
#   add LANG  - Add new language (e.g., ./update-translations.sh add es)
#   stats     - Show translation statistics
#   help      - Show this help

set -e

PROJECT_NAME="duelpy"
PO_DIR="po"
POT_FILE="$PO_DIR/$PROJECT_NAME.pot"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_help() {
    echo -e "${BLUE}=== DuelPy Translation Manager ===${NC}"
    echo -e ""
    echo -e "Usage: ./update-translations.sh [command]"
    echo -e ""
    echo -e "Commands:"
    echo -e "  ${GREEN}update${NC}         - Update template and all existing translations"
    echo -e "  ${GREEN}add LANG${NC}       - Add new language (e.g., add es, add pt_BR)"
    echo -e "  ${GREEN}stats${NC}          - Show translation statistics"
    echo -e "  ${GREEN}help${NC}           - Show this help"
    echo -e ""
    echo -e "Examples:"
    echo -e "  ./update-translations.sh update"
    echo -e "  ./update-translations.sh add es"
    echo -e "  ./update-translations.sh add pt_BR"
    echo -e "  ./update-translations.sh stats"
}

update_pot() {
    echo -e "${BLUE}Updating translation template (.pot)...${NC}"
    
    if [ ! -d "builddir" ]; then
        echo -e "${YELLOW}WARNING: builddir directory not found. Setting up...${NC}"
        meson setup builddir
    fi
    
    ninja -C builddir ${PROJECT_NAME}-pot
    
    if [ -f "$POT_FILE" ]; then
        echo -e "${GREEN}SUCCESS: Template updated: $POT_FILE${NC}"
    else
        echo -e "${RED}ERROR: .pot file not found!${NC}"
        exit 1
    fi
}

update_translations() {
    echo -e "${BLUE}Updating existing translations...${NC}"
    
    # Check if LINGUAS exists and has content
    if [ ! -f "$PO_DIR/LINGUAS" ]; then
        echo -e "${YELLOW}WARNING: LINGUAS file not found${NC}"
        return
    fi
    
    # Read languages from LINGUAS file (ignoring comments and empty lines)
    LANGUAGES=$(grep -v '^#' "$PO_DIR/LINGUAS" | grep -v '^$')
    
    if [ -z "$LANGUAGES" ]; then
        echo -e "${YELLOW}WARNING: No languages configured in LINGUAS${NC}"
        return
    fi
    
    for lang in $LANGUAGES; do
        PO_FILE="$PO_DIR/$lang.po"
        
        if [ -f "$PO_FILE" ]; then
            echo -e "${BLUE}  Updating $lang...${NC}"
            msgmerge -U "$PO_FILE" "$POT_FILE"
            echo -e "${GREEN}  SUCCESS: $lang updated${NC}"
        else
            echo -e "${YELLOW}  WARNING: $PO_FILE not found, skipping...${NC}"
        fi
    done
    
    echo -e "${GREEN}SUCCESS: All translations have been updated!${NC}"
}

add_language() {
    LANG=$1
    
    if [ -z "$LANG" ]; then
        echo -e "${RED}ERROR: Specify a language code${NC}"
        echo -e "Example: ./update-translations.sh add es"
        echo -e ""
        echo -e "Common codes:"
        echo -e "  pt_BR - Portuguese (Brazil)"
        echo -e "  es    - Spanish"
        echo -e "  fr    - French"
        echo -e "  de    - German"
        echo -e "  it    - Italian"
        echo -e "  ja    - Japanese"
        echo -e "  zh_CN - Chinese (Simplified)"
        exit 1
    fi
    
    PO_FILE="$PO_DIR/$LANG.po"
    
    # Check if already exists
    if [ -f "$PO_FILE" ]; then
        echo -e "${YELLOW}WARNING: $LANG already exists!${NC}"
        read -p "Do you want to overwrite? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${BLUE}Operation cancelled${NC}"
            exit 0
        fi
    fi
    
    echo -e "${BLUE}Adding language: $LANG${NC}"
    
    # Update POT first
    update_pot
    
    # Create .po file
    cd "$PO_DIR"
    msginit -i "${PROJECT_NAME}.pot" -o "$LANG.po" -l "$LANG" --no-translator
    cd ..
    
    # Add to LINGUAS if not exists
    if ! grep -q "^$LANG$" "$PO_DIR/LINGUAS"; then
        echo "$LANG" >> "$PO_DIR/LINGUAS"
        echo -e "${GREEN}SUCCESS: $LANG added to LINGUAS${NC}"
    fi
    
    echo -e "${GREEN}SUCCESS: Language $LANG created successfully!${NC}"
    echo -e "${YELLOW}NOTE: Now edit $PO_FILE to add translations${NC}"
    echo -e "${YELLOW}      You can use: Poedit, Gtranslator, or a text editor${NC}"
}

show_stats() {
    echo -e "${BLUE}Translation statistics:${NC}"
    echo -e ""
    
    if [ ! -f "$PO_DIR/LINGUAS" ]; then
        echo -e "${YELLOW}WARNING: No translations configured${NC}"
        return
    fi
    
    LANGUAGES=$(grep -v '^#' "$PO_DIR/LINGUAS" | grep -v '^$')
    
    if [ -z "$LANGUAGES" ]; then
        echo -e "${YELLOW}WARNING: No translations configured${NC}"
        return
    fi
    
    for lang in $LANGUAGES; do
        PO_FILE="$PO_DIR/$lang.po"
        
        if [ ! -f "$PO_FILE" ]; then
            echo -e "${RED}ERROR: $lang: file not found${NC}"
            continue
        fi
        
        # Get statistics
        STATS=$(msgfmt --statistics "$PO_FILE" 2>&1 || true)
        
        echo -e "${GREEN}$lang:${NC} $STATS"
    done
}

# Main command
case "${1:-help}" in
    update)
        update_pot
        update_translations
        ;;
    add)
        add_language "$2"
        ;;
    stats)
        show_stats
        ;;
    help|--help|-h)
        print_help
        ;;
    *)
        echo -e "${RED}ERROR: Unknown command: $1${NC}"
        echo -e ""
        print_help
        exit 1
        ;;
esac