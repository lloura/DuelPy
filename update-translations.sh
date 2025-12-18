#!/bin/bash

# Script para atualizar traduções do DuelPy
# Uso: ./update-translations.sh [comando]
#   update    - Atualiza traduções existentes
#   add LANG  - Adiciona novo idioma (ex: ./update-translations.sh add es)
#   stats     - Mostra estatísticas de tradução
#   help      - Mostra esta ajuda

set -e

PROJECT_NAME="duelpy"
PO_DIR="po"
POT_FILE="$PO_DIR/$PROJECT_NAME.pot"

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_help() {
    echo -e "${BLUE}=== DuelPy Translation Manager ===${NC}"
    echo ""
    echo "Uso: ./update-translations.sh [comando]"
    echo ""
    echo "Comandos:"
    echo "  ${GREEN}update${NC}         - Atualiza o template e todas as traduções existentes"
    echo "  ${GREEN}add LANG${NC}       - Adiciona novo idioma (ex: add es, add pt_BR)"
    echo "  ${GREEN}stats${NC}          - Mostra estatísticas de tradução"
    echo "  ${GREEN}help${NC}           - Mostra esta ajuda"
    echo ""
    echo "Exemplos:"
    echo "  ./update-translations.sh update"
    echo "  ./update-translations.sh add es"
    echo "  ./update-translations.sh add pt_BR"
    echo "  ./update-translations.sh stats"
}

update_pot() {
    echo -e "${BLUE} Atualizando template de tradução (.pot)...${NC}"
    
    if [ ! -d "builddir" ]; then
        echo -e "${YELLOW}  Diretório builddir não encontrado. Configurando...${NC}"
        meson setup builddir
    fi
    
    ninja -C builddir ${PROJECT_NAME}-pot
    
    if [ -f "$POT_FILE" ]; then
        echo -e "${GREEN} Template atualizado: $POT_FILE${NC}"
    else
        echo -e "${RED} Erro: Arquivo .pot não encontrado!${NC}"
        exit 1
    fi
}

update_translations() {
    echo -e "${BLUE} Atualizando traduções existentes...${NC}"
    
    # Verificar se LINGUAS existe e tem conteúdo
    if [ ! -f "$PO_DIR/LINGUAS" ]; then
        echo -e "${YELLOW}  Arquivo LINGUAS não encontrado${NC}"
        return
    fi
    
    # Ler idiomas do arquivo LINGUAS (ignorando comentários e linhas vazias)
    LANGUAGES=$(grep -v '^#' "$PO_DIR/LINGUAS" | grep -v '^$')
    
    if [ -z "$LANGUAGES" ]; then
        echo -e "${YELLOW}  Nenhum idioma configurado em LINGUAS${NC}"
        return
    fi
    
    for lang in $LANGUAGES; do
        PO_FILE="$PO_DIR/$lang.po"
        
        if [ -f "$PO_FILE" ]; then
            echo -e "${BLUE}  Atualizando $lang...${NC}"
            msgmerge -U "$PO_FILE" "$POT_FILE"
            echo -e "${GREEN}   $lang atualizado${NC}"
        else
            echo -e "${YELLOW}    $PO_FILE não encontrado, pulando...${NC}"
        fi
    done
    
    echo -e "${GREEN} Todas as traduções foram atualizadas!${NC}"
}

add_language() {
    LANG=$1
    
    if [ -z "$LANG" ]; then
        echo -e "${RED} Erro: Especifique um código de idioma${NC}"
        echo "Exemplo: ./update-translations.sh add es"
        echo ""
        echo "Códigos comuns:"
        echo "  pt_BR - Português (Brasil)"
        echo "  es    - Espanhol"
        echo "  fr    - Francês"
        echo "  de    - Alemão"
        echo "  it    - Italiano"
        echo "  ja    - Japonês"
        echo "  zh_CN - Chinês (Simplificado)"
        exit 1
    fi
    
    PO_FILE="$PO_DIR/$LANG.po"
    
    # Verificar se já existe
    if [ -f "$PO_FILE" ]; then
        echo -e "${YELLOW}  $LANG já existe!${NC}"
        read -p "Deseja sobrescrever? (s/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Ss]$ ]]; then
            echo -e "${BLUE}Operação cancelada${NC}"
            exit 0
        fi
    fi
    
    echo -e "${BLUE}➕ Adicionando idioma: $LANG${NC}"
    
    # Atualizar POT primeiro
    update_pot
    
    # Criar arquivo .po
    cd "$PO_DIR"
    msginit -i "${PROJECT_NAME}.pot" -o "$LANG.po" -l "$LANG" --no-translator
    cd ..
    
    # Adicionar ao LINGUAS se não existir
    if ! grep -q "^$LANG$" "$PO_DIR/LINGUAS"; then
        echo "$LANG" >> "$PO_DIR/LINGUAS"
        echo -e "${GREEN} $LANG adicionado ao LINGUAS${NC}"
    fi
    
    echo -e "${GREEN} Idioma $LANG criado com sucesso!${NC}"
    echo -e "${YELLOW} Agora edite $PO_FILE para adicionar as traduções${NC}"
    echo -e "${YELLOW}   Você pode usar: Poedit, Gtranslator, ou um editor de texto${NC}"
}

show_stats() {
    echo -e "${BLUE} Estatísticas de tradução:${NC}"
    echo ""
    
    if [ ! -f "$PO_DIR/LINGUAS" ]; then
        echo -e "${YELLOW}  Nenhuma tradução configurada${NC}"
        return
    fi
    
    LANGUAGES=$(grep -v '^#' "$PO_DIR/LINGUAS" | grep -v '^$')
    
    if [ -z "$LANGUAGES" ]; then
        echo -e "${YELLOW}  Nenhuma tradução configurada${NC}"
        return
    fi
    
    for lang in $LANGUAGES; do
        PO_FILE="$PO_DIR/$lang.po"
        
        if [ ! -f "$PO_FILE" ]; then
            echo -e "${RED} $lang: arquivo não encontrado${NC}"
            continue
        fi
        
        # Obter estatísticas
        STATS=$(msgfmt --statistics "$PO_FILE" 2>&1 || true)
        
        echo -e "${GREEN}$lang:${NC} $STATS"
    done
}

# Comando principal
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
        echo -e "${RED} Comando desconhecido: $1${NC}"
        echo ""
        print_help
        exit 1
        ;;
esac
