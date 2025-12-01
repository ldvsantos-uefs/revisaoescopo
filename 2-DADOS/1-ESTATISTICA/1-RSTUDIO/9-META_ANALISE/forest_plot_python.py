# =============================================================================
# FOREST PLOT: META-ANALYSIS BY ALGORITHM (Python + matplotlib manual)
# Com agrupamentos organizados
# =============================================================================

import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 1. ALGORITHM DATA - Organizado por grupos (valores da meta-análise original)
# -----------------------------------------------------------------------------
# Estrutura: lista de linhas (grupo header ou dados)
# Random-Effects Model fica no final (padrão de forest plots)
rows = [
    {'type': 'group', 'label': 'Chemometrics'},
    {'type': 'data', 'label': 'PLS-DA', 'n': '8', 'acc': 0.93, 'ci_low': 0.89, 'ci_high': 0.95, 'weight': '5.4', 'is_summary': False},
    
    {'type': 'group', 'label': 'Ensemble'},
    {'type': 'data', 'label': 'Random Forest', 'n': '37', 'acc': 0.91, 'ci_low': 0.90, 'ci_high': 0.93, 'weight': '25.0', 'is_summary': False},
    {'type': 'data', 'label': 'XGBoost', 'n': '7', 'acc': 0.90, 'ci_low': 0.86, 'ci_high': 0.93, 'weight': '4.7', 'is_summary': False},
    {'type': 'data', 'label': 'Decision Tree', 'n': '2', 'acc': 0.81, 'ci_low': 0.69, 'ci_high': 0.89, 'weight': '1.4', 'is_summary': False},
    
    {'type': 'group', 'label': 'Kernel/Neural'},
    {'type': 'data', 'label': 'Neural Network', 'n': '32', 'acc': 0.91, 'ci_low': 0.89, 'ci_high': 0.93, 'weight': '21.6', 'is_summary': False},
    {'type': 'data', 'label': 'Deep Learning', 'n': '15', 'acc': 0.91, 'ci_low': 0.87, 'ci_high': 0.93, 'weight': '10.1', 'is_summary': False},
    {'type': 'data', 'label': 'SVM', 'n': '47', 'acc': 0.90, 'ci_low': 0.89, 'ci_high': 0.92, 'weight': '31.8', 'is_summary': False},
    
    {'type': 'group', 'label': 'Summary'},
    {'type': 'data', 'label': 'Random-Effects Model', 'n': '148', 'acc': 0.91, 'ci_low': 0.90, 'ci_high': 0.91, 'weight': '100.0', 'is_summary': True},
]

# -----------------------------------------------------------------------------
# 2. CREATE FIGURE WITH CUSTOM LAYOUT
# -----------------------------------------------------------------------------
# Contar total de linhas (grupos + dados)
n_total = len(rows)

fig, (ax_table, ax_forest) = plt.subplots(1, 2, figsize=(10, 6), 
                                           gridspec_kw={'width_ratios': [3, 2], 'wspace': 0.02})

# -----------------------------------------------------------------------------
# 3. CONFIGURAR EIXOS COM MESMO SISTEMA DE COORDENADAS
# -----------------------------------------------------------------------------
# Column positions (x) - em coordenadas de dados (0-1)
col_x = [0.02, 0.38, 0.48, 0.58, 0.85]
headers = ['Algorithm', 'n', 'Acc.', '95% CI', 'Weight']

# Configurar ax_table
ax_table.set_xlim(0, 1)
ax_table.set_ylim(-1, n_total)
ax_table.invert_yaxis()
ax_table.axis('off')

# Configurar ax_forest COM MESMO YLIM
ax_forest.set_xlim(0.68, 0.96)  # Começa em 0.68 para mostrar Decision Tree (81%, CI: 0.69-0.89)
ax_forest.set_ylim(-1, n_total)
ax_forest.invert_yaxis()

# Draw header com linhas superior e inferior
header_y = -0.5
# Linha superior do cabeçalho
ax_table.axhline(y=header_y - 0.35, xmin=0, xmax=1, color='black', linewidth=1)
for x, h in zip(col_x, headers):
    ax_table.text(x, header_y, h, fontsize=9, fontweight='bold', ha='left', va='center')
# Linha inferior do cabeçalho (mais próxima ao texto do header)
ax_table.axhline(y=header_y + 0.20, xmin=0, xmax=1, color='black', linewidth=1)

# Draw rows (grupos e dados)
for i, row in enumerate(rows):
    y_pos = i
    
    if row['type'] == 'group':
        # Group header - apenas na tabela, não no forest
        ax_table.text(col_x[0], y_pos, row['label'], fontsize=9, fontweight='bold', 
                      fontstyle='italic', ha='left', va='center', color='#333333')
    else:
        # Data row
        ci_str = f"[{row['ci_low']:.2f}, {row['ci_high']:.2f}]"
        acc_str = f"{row['acc']*100:.0f}%"
        
        fw = 'bold' if row['is_summary'] else 'normal'
        indent = '  ' if not row['is_summary'] else ''
        
        # Tabela
        ax_table.text(col_x[0], y_pos, indent + row['label'], fontsize=9, fontweight=fw, ha='left', va='center')
        ax_table.text(col_x[1], y_pos, row['n'], fontsize=9, fontweight=fw, ha='left', va='center')
        ax_table.text(col_x[2], y_pos, acc_str, fontsize=9, fontweight=fw, ha='left', va='center')
        ax_table.text(col_x[3], y_pos, ci_str, fontsize=9, fontweight=fw, ha='left', va='center')
        ax_table.text(col_x[4], y_pos, row['weight'], fontsize=9, fontweight=fw, ha='left', va='center')
        
        # Forest plot - mesma posição Y
        color = 'navy' if row['is_summary'] else 'darkblue'
        marker = 'D' if row['is_summary'] else 's'
        ms = 10 if row['is_summary'] else 8
        
        # CI line
        ax_forest.hlines(y=y_pos, xmin=row['ci_low'], xmax=row['ci_high'], colors=color, linewidth=1.5)
        # Point estimate
        ax_forest.scatter(row['acc'], y_pos, marker=marker, color=color, s=ms**2, zorder=5)

# Linha separadora entre SVM e Summary (antes do grupo Summary, índice 10)
# SVM está no índice 9, Summary group está no índice 10
separator_y = 9.5  # Entre SVM (9) e Summary (10)
ax_table.axhline(y=separator_y, xmin=0, xmax=1, color='black', linewidth=1)

# -----------------------------------------------------------------------------
# 4. FOREST PLOT FORMATTING
# -----------------------------------------------------------------------------
# Vertical reference line at overall effect
ax_forest.axvline(x=0.91, color='red', linestyle='--', linewidth=1, alpha=0.7)

# Format forest plot
ax_forest.set_xlabel('Pooled Accuracy', fontsize=10)
ax_forest.set_yticks([])
ax_forest.spines['left'].set_visible(False)
ax_forest.spines['right'].set_visible(False)
ax_forest.spines['top'].set_visible(False)
ax_forest.set_xticks([0.70, 0.75, 0.80, 0.85, 0.90, 0.95])
ax_forest.tick_params(axis='x', labelsize=9)
ax_forest.grid(axis='x', linestyle=':', alpha=0.5)

# Nota explicativa das abreviações
fig.text(0.02, 0.02, 'Note: Acc. = Accuracy; CI = Confidence Interval; n = number of studies; PLS-DA = Partial Least Squares Discriminant Analysis; SVM = Support Vector Machine.',
         fontsize=7, ha='left', va='bottom', style='italic', color='#555555')

# -----------------------------------------------------------------------------
# 5. SAVE
# -----------------------------------------------------------------------------
plt.savefig('forest_algoritmos_python_v2.png', dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.1)
plt.close()

print("✓ Forest plot saved: forest_algoritmos_python_v2.png")
