#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MODELAGEM PREDITIVA
Corpus: Machine Learning aplicado a Indicações Geográficas
Objetivo: Modelar relações preditivas entre características dos estudos
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import (mean_squared_error, r2_score, mean_absolute_error,
                             accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, classification_report)
import warnings
warnings.filterwarnings('ignore')

# Configuração
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# ============================================================================
# EXTRAÇÃO DE DADOS
# ============================================================================

def extrair_dados_modelagem(caminho_bib):
    """
    Extrai features para modelagem preditiva
    """
    with open(caminho_bib, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    entradas = re.split(r'\n\n% Score:', conteudo)
    dados = []
    
    for entrada in entradas[1:]:
        try:
            score_match = re.search(r'^([\d.]+)', entrada)
            score = float(score_match.group(1)) if score_match else 0
            
            ano_match = re.search(r'year = \{(\d{4})\}', entrada)
            ano = int(ano_match.group(1)) if ano_match else 0
            
            id_match = re.search(r'@ARTICLE\{([^,]+),', entrada)
            id_ref = id_match.group(1) if id_match else "Unknown"
            
            keywords_match = re.search(r'keywords = \{([^}]+)\}', entrada)
            keywords = keywords_match.group(1).lower() if keywords_match else ""
            
            abstract_match = re.search(r'abstract = \{([^}]+)\}', entrada)
            abstract = abstract_match.group(1).lower() if abstract_match else ""
            
            texto = f"{keywords} {abstract}".lower()
            
            # Features preditoras
            features = {
                'id': id_ref,
                'score': score,
                'ano': ano,
                'ano_normalizado': (ano - 2010) / 15,
                
                # Algoritmos (0/1)
                'rf': int(bool(re.search(r'random forest', texto))),
                'svm': int(bool(re.search(r'support vector machine|svm', texto))),
                'nn': int(bool(re.search(r'neural network|ann|deep learning|cnn', texto))),
                'knn': int(bool(re.search(r'k-nearest neighbor|knn', texto))),
                'plsda': int(bool(re.search(r'pls-da|partial least squares', texto))),
                
                # Instrumentos
                'nir': int(bool(re.search(r'nir|near.infrared', texto))),
                'gcms': int(bool(re.search(r'gc-ms|gas chromatography', texto))),
                'icpms': int(bool(re.search(r'icp-ms|inductively coupled', texto))),
                'nmr': int(bool(re.search(r'nmr|nuclear magnetic', texto))),
                'raman': int(bool(re.search(r'raman', texto))),
                'ftir': int(bool(re.search(r'ftir|fourier transform', texto))),
                
                # Produtos
                'wine': int(bool(re.search(r'wine|vinho', texto))),
                'tea': int(bool(re.search(r'\btea\b|chá', texto))),
                'meat': int(bool(re.search(r'meat|carne|lamb', texto))),
                'oil': int(bool(re.search(r'oil|olive|azeite', texto))),
                
                # Aplicações
                'authentication': int(bool(re.search(r'authentication', texto))),
                'traceability': int(bool(re.search(r'traceability', texto))),
                'fraud': int(bool(re.search(r'fraud|adulteration', texto))),
                'quality': int(bool(re.search(r'quality control', texto))),
                
                # Regiões
                'asia': int(bool(re.search(r'china|japan|korea', texto))),
                'europe': int(bool(re.search(r'italy|spain|france|portugal', texto))),
                'americas': int(bool(re.search(r'brazil|america|usa', texto))),
                
                # Técnicas avançadas
                'metabolomics': int(bool(re.search(r'metabolomics', texto))),
                'chemometrics': int(bool(re.search(r'chemometrics', texto))),
                'fingerprinting': int(bool(re.search(r'fingerprinting', texto))),
                'deep_learning': int(bool(re.search(r'deep learning', texto))),
                
                # Variáveis alvo
                'high_score': int(score >= 40),  # Classificação binária
                'validation_external': int(bool(re.search(r'external validation|cross.validation', texto))),
            }
            
            dados.append(features)
            
        except Exception as e:
            print(f"Erro: {e}")
            continue
    
    return pd.DataFrame(dados)

# ============================================================================
# MODELAGEM: REGRESSÃO (Predizer Score)
# ============================================================================

def executar_regressao(df):
    """
    Modelos de regressão para predizer score
    """
    # Preparar dados
    X = df.drop(['id', 'score', 'high_score', 'validation_external'], axis=1)
    y = df['score']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Padronizar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    resultados = {}
    
    # 1. Regressão Linear Simples
    lr = LinearRegression()
    lr.fit(X_train_scaled, y_train)
    y_pred_lr = lr.predict(X_test_scaled)
    
    resultados['Linear_Regression'] = {
        'modelo': lr,
        'y_pred': y_pred_lr,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_lr)),
        'mae': mean_absolute_error(y_test, y_pred_lr),
        'r2': r2_score(y_test, y_pred_lr),
        'cv_score': cross_val_score(lr, X_train_scaled, y_train, cv=5, scoring='r2').mean()
    }
    
    # 2. Ridge Regression
    ridge = Ridge(alpha=1.0)
    ridge.fit(X_train_scaled, y_train)
    y_pred_ridge = ridge.predict(X_test_scaled)
    
    resultados['Ridge'] = {
        'modelo': ridge,
        'y_pred': y_pred_ridge,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_ridge)),
        'mae': mean_absolute_error(y_test, y_pred_ridge),
        'r2': r2_score(y_test, y_pred_ridge),
        'cv_score': cross_val_score(ridge, X_train_scaled, y_train, cv=5, scoring='r2').mean()
    }
    
    # 3. Lasso Regression
    lasso = Lasso(alpha=0.5)
    lasso.fit(X_train_scaled, y_train)
    y_pred_lasso = lasso.predict(X_test_scaled)
    
    resultados['Lasso'] = {
        'modelo': lasso,
        'y_pred': y_pred_lasso,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_lasso)),
        'mae': mean_absolute_error(y_test, y_pred_lasso),
        'r2': r2_score(y_test, y_pred_lasso),
        'cv_score': cross_val_score(lasso, X_train_scaled, y_train, cv=5, scoring='r2').mean()
    }
    
    # 4. Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    
    resultados['Random_Forest'] = {
        'modelo': rf,
        'y_pred': y_pred_rf,
        'rmse': np.sqrt(mean_squared_error(y_test, y_pred_rf)),
        'mae': mean_absolute_error(y_test, y_pred_rf),
        'r2': r2_score(y_test, y_pred_rf),
        'cv_score': cross_val_score(rf, X_train, y_train, cv=5, scoring='r2').mean(),
        'feature_importance': pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
    }
    
    return resultados, X_test, y_test, scaler

# ============================================================================
# MODELAGEM: CLASSIFICAÇÃO (Predizer High Score)
# ============================================================================

def executar_classificacao(df):
    """
    Modelos de classificação para predizer high_score
    """
    # Preparar dados
    X = df.drop(['id', 'score', 'high_score', 'validation_external'], axis=1)
    y = df['high_score']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Padronizar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    resultados = {}
    
    # 1. Logistic Regression
    logreg = LogisticRegression(max_iter=1000, random_state=42)
    logreg.fit(X_train_scaled, y_train)
    y_pred_logreg = logreg.predict(X_test_scaled)
    
    resultados['Logistic_Regression'] = {
        'modelo': logreg,
        'y_pred': y_pred_logreg,
        'accuracy': accuracy_score(y_test, y_pred_logreg),
        'precision': precision_score(y_test, y_pred_logreg, zero_division=0),
        'recall': recall_score(y_test, y_pred_logreg, zero_division=0),
        'f1': f1_score(y_test, y_pred_logreg, zero_division=0),
        'cv_score': cross_val_score(logreg, X_train_scaled, y_train, cv=5, scoring='accuracy').mean(),
        'confusion_matrix': confusion_matrix(y_test, y_pred_logreg)
    }
    
    # 2. Random Forest Classifier
    rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_clf.fit(X_train, y_train)
    y_pred_rf = rf_clf.predict(X_test)
    
    resultados['Random_Forest'] = {
        'modelo': rf_clf,
        'y_pred': y_pred_rf,
        'accuracy': accuracy_score(y_test, y_pred_rf),
        'precision': precision_score(y_test, y_pred_rf, zero_division=0),
        'recall': recall_score(y_test, y_pred_rf, zero_division=0),
        'f1': f1_score(y_test, y_pred_rf, zero_division=0),
        'cv_score': cross_val_score(rf_clf, X_train, y_train, cv=5, scoring='accuracy').mean(),
        'confusion_matrix': confusion_matrix(y_test, y_pred_rf),
        'feature_importance': pd.Series(rf_clf.feature_importances_, index=X.columns).sort_values(ascending=False)
    }
    
    return resultados, X_test, y_test, scaler

# ============================================================================
# VISUALIZAÇÕES
# ============================================================================

def plot_regressao_resultados(resultados_reg, y_test, output_path):
    """
    Comparação de modelos de regressão
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    modelos = ['Linear_Regression', 'Ridge', 'Lasso', 'Random_Forest']
    
    for i, modelo in enumerate(modelos):
        ax = axes[i // 2, i % 2]
        
        y_pred = resultados_reg[modelo]['y_pred']
        r2 = resultados_reg[modelo]['r2']
        rmse = resultados_reg[modelo]['rmse']
        
        ax.scatter(y_test, y_pred, alpha=0.6, edgecolors='black')
        ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
                'r--', linewidth=2, label='Predição Perfeita')
        
        ax.set_xlabel('Score Real', fontsize=11)
        ax.set_ylabel('Score Predito', fontsize=11)
        ax.set_title(f'{modelo}\nR²={r2:.3f}, RMSE={rmse:.2f}', fontsize=12, fontweight='bold')
        ax.legend(fontsize=9)
        ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Gráfico de regressão salvo: {output_path}")

def plot_feature_importance(importances, titulo, output_path):
    """
    Importância de features
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    top_features = importances.head(15)
    
    ax.barh(range(len(top_features)), top_features.values, color='steelblue', alpha=0.8, edgecolor='black')
    ax.set_yticks(range(len(top_features)))
    ax.set_yticklabels(top_features.index)
    ax.set_xlabel('Importância', fontsize=12, fontweight='bold')
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Importância de features salva: {output_path}")

def plot_confusion_matrix(cm, titulo, output_path):
    """
    Matriz de confusão
    """
    fig, ax = plt.subplots(figsize=(8, 7))
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Low Score', 'High Score'],
                yticklabels=['Low Score', 'High Score'],
                cbar_kws={'label': 'Contagem'}, ax=ax)
    
    ax.set_xlabel('Predito', fontsize=12, fontweight='bold')
    ax.set_ylabel('Real', fontsize=12, fontweight='bold')
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Matriz de confusão salva: {output_path}")

def plot_metricas_comparacao(resultados_reg, resultados_clf, output_path):
    """
    Comparação de métricas entre modelos
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Regressão
    modelos_reg = list(resultados_reg.keys())
    r2_scores = [resultados_reg[m]['r2'] for m in modelos_reg]
    cv_scores_reg = [resultados_reg[m]['cv_score'] for m in modelos_reg]
    
    x_pos = np.arange(len(modelos_reg))
    width = 0.35
    
    axes[0].bar(x_pos - width/2, r2_scores, width, label='R² (Test)', alpha=0.8)
    axes[0].bar(x_pos + width/2, cv_scores_reg, width, label='R² (CV)', alpha=0.8)
    axes[0].set_xticks(x_pos)
    axes[0].set_xticklabels(modelos_reg, rotation=15, ha='right')
    axes[0].set_ylabel('R²', fontsize=12, fontweight='bold')
    axes[0].set_title('Desempenho: Modelos de Regressão', fontsize=13, fontweight='bold')
    axes[0].legend(fontsize=10)
    axes[0].grid(alpha=0.3, axis='y')
    
    # Classificação
    modelos_clf = list(resultados_clf.keys())
    acc_scores = [resultados_clf[m]['accuracy'] for m in modelos_clf]
    cv_scores_clf = [resultados_clf[m]['cv_score'] for m in modelos_clf]
    
    x_pos2 = np.arange(len(modelos_clf))
    
    axes[1].bar(x_pos2 - width/2, acc_scores, width, label='Accuracy (Test)', alpha=0.8)
    axes[1].bar(x_pos2 + width/2, cv_scores_clf, width, label='Accuracy (CV)', alpha=0.8)
    axes[1].set_xticks(x_pos2)
    axes[1].set_xticklabels(modelos_clf, rotation=15, ha='right')
    axes[1].set_ylabel('Accuracy', fontsize=12, fontweight='bold')
    axes[1].set_title('Desempenho: Modelos de Classificação', fontsize=13, fontweight='bold')
    axes[1].legend(fontsize=10)
    axes[1].grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Comparação de métricas salva: {output_path}")

# ============================================================================
# RELATÓRIO
# ============================================================================

def gerar_relatorio(df, resultados_reg, resultados_clf, output_path):
    """
    Relatório de modelagem preditiva
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("RELATÓRIO DE MODELAGEM PREDITIVA\n")
        f.write("Corpus: Machine Learning para Indicações Geográficas\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"Total de estudos: {len(df)}\n")
        f.write(f"Número de features: {len([c for c in df.columns if c not in ['id', 'score']])}\n\n")
        
        f.write("-"*80 + "\n")
        f.write("MODELOS DE REGRESSÃO (Predizer Score)\n")
        f.write("-"*80 + "\n")
        for modelo, res in resultados_reg.items():
            f.write(f"\n{modelo}:\n")
            f.write(f"  R²: {res['r2']:.4f}\n")
            f.write(f"  RMSE: {res['rmse']:.4f}\n")
            f.write(f"  MAE: {res['mae']:.4f}\n")
            f.write(f"  CV Score (R²): {res['cv_score']:.4f}\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("MODELOS DE CLASSIFICAÇÃO (Predizer High Score)\n")
        f.write("-"*80 + "\n")
        for modelo, res in resultados_clf.items():
            f.write(f"\n{modelo}:\n")
            f.write(f"  Accuracy: {res['accuracy']:.4f}\n")
            f.write(f"  Precision: {res['precision']:.4f}\n")
            f.write(f"  Recall: {res['recall']:.4f}\n")
            f.write(f"  F1-Score: {res['f1']:.4f}\n")
            f.write(f"  CV Score (Accuracy): {res['cv_score']:.4f}\n")
        
        f.write("\n" + "-"*80 + "\n")
        f.write("TOP 10 FEATURES IMPORTANTES (Random Forest - Regressão)\n")
        f.write("-"*80 + "\n")
        if 'feature_importance' in resultados_reg['Random_Forest']:
            for feat, imp in resultados_reg['Random_Forest']['feature_importance'].head(10).items():
                f.write(f"  {feat:25s}: {imp:.4f}\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("FIM DO RELATÓRIO\n")
        f.write("="*80 + "\n")
    
    print(f"✓ Relatório salvo: {output_path}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    """
    Função principal
    """
    print("\n" + "="*80)
    print("MODELAGEM PREDITIVA")
    print("Machine Learning para Indicações Geográficas")
    print("="*80 + "\n")
    
    caminho_bib = "../referencias_filtradas/referencias_ML_IG_filtradas.bib"
    output_dir = "."
    
    # 1. Extrair dados
    print("📚 Extraindo dados para modelagem...")
    df = extrair_dados_modelagem(caminho_bib)
    print(f"✓ Total de estudos: {len(df)}")
    
    # 2. Modelagem de Regressão
    print("\n📈 Executando modelos de regressão...")
    resultados_reg, X_test_reg, y_test_reg, scaler_reg = executar_regressao(df)
    print("✓ Modelos de regressão treinados")
    
    # 3. Modelagem de Classificação
    print("\n🎯 Executando modelos de classificação...")
    resultados_clf, X_test_clf, y_test_clf, scaler_clf = executar_classificacao(df)
    print("✓ Modelos de classificação treinados")
    
    # 4. Visualizações
    print("\n🎨 Gerando visualizações...")
    plot_regressao_resultados(resultados_reg, y_test_reg, f"{output_dir}/model_regressao_comparacao.png")
    
    if 'feature_importance' in resultados_reg['Random_Forest']:
        plot_feature_importance(
            resultados_reg['Random_Forest']['feature_importance'],
            'Importância de Features (Regressão - Random Forest)',
            f"{output_dir}/model_feature_importance_reg.png"
        )
    
    if 'feature_importance' in resultados_clf['Random_Forest']:
        plot_feature_importance(
            resultados_clf['Random_Forest']['feature_importance'],
            'Importância de Features (Classificação - Random Forest)',
            f"{output_dir}/model_feature_importance_clf.png"
        )
    
    plot_confusion_matrix(
        resultados_clf['Random_Forest']['confusion_matrix'],
        'Matriz de Confusão (Random Forest Classifier)',
        f"{output_dir}/model_confusion_matrix.png"
    )
    
    plot_metricas_comparacao(resultados_reg, resultados_clf, f"{output_dir}/model_metricas_comparacao.png")
    
    # 5. Relatório
    print("\n📝 Gerando relatório...")
    gerar_relatorio(df, resultados_reg, resultados_clf, f"{output_dir}/model_relatorio.txt")
    
    # 6. Salvar dados
    df.to_csv(f"{output_dir}/model_dados_completos.csv", index=False)
    print(f"\n✓ Dados salvos: model_dados_completos.csv")
    
    print("\n" + "="*80)
    print("✅ MODELAGEM PREDITIVA CONCLUÍDA COM SUCESSO!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
