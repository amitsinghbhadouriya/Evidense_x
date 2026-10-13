import os
import sys
import win32com.client as win32

def create_ieee_paper():
    word = win32.Dispatch('Word.Application')
    word.Visible = False
    word.DisplayAlerts = False
    
    doc = word.Documents.Add()
    
    # ---------------------------------------------------------
    # Page Setup (A4, IEEE Margins)
    # ---------------------------------------------------------
    # A4: 210 x 297 mm
    doc.PageSetup.PaperSize = 7 # wdPaperA4
    # Margins in points: 1 inch = 72 pt, 1 cm = 28.35 pt
    doc.PageSetup.TopMargin = 54 # 1.9 cm
    doc.PageSetup.BottomMargin = 72 # 2.54 cm
    doc.PageSetup.LeftMargin = 45 # 1.59 cm
    doc.PageSetup.RightMargin = 45 # 1.59 cm
    doc.PageSetup.HeaderDistance = 36
    doc.PageSetup.FooterDistance = 36
    
    # Base Normal Style
    style_normal = doc.Styles("Normal")
    style_normal.Font.Name = "Times New Roman"
    style_normal.Font.Size = 10
    style_normal.ParagraphFormat.LineSpacingRule = 0 # wdLineSpaceSingle
    style_normal.ParagraphFormat.SpaceAfter = 2
    style_normal.ParagraphFormat.SpaceBefore = 0
    style_normal.ParagraphFormat.Alignment = 3 # wdAlignParagraphJustify
    
    sel = word.Selection
    
    # Helper functions
    def add_para(text="", bold=False, italic=False, size=10, align=3, space_after=2, space_before=0):
        sel.ParagraphFormat.Alignment = align
        sel.ParagraphFormat.SpaceBefore = space_before
        sel.ParagraphFormat.SpaceAfter = space_after
        sel.ParagraphFormat.LineSpacingRule = 0
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = size
        sel.Font.Bold = bold
        sel.Font.Italic = italic
        if text:
            sel.TypeText(text)
        sel.TypeParagraph()
        
    def add_heading1(text):
        sel.ParagraphFormat.Alignment = 1 # Center
        sel.ParagraphFormat.SpaceBefore = 9
        sel.ParagraphFormat.SpaceAfter = 3
        sel.ParagraphFormat.KeepWithNext = True
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 10
        sel.Font.Bold = True
        sel.Font.Italic = False
        sel.TypeText(text)
        sel.TypeParagraph()
        
    def add_heading2(text):
        sel.ParagraphFormat.Alignment = 0 # Left
        sel.ParagraphFormat.SpaceBefore = 6
        sel.ParagraphFormat.SpaceAfter = 2
        sel.ParagraphFormat.KeepWithNext = True
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 10
        sel.Font.Bold = False
        sel.Font.Italic = True
        sel.TypeText(text)
        sel.TypeParagraph()
        
    def add_heading3(text):
        sel.ParagraphFormat.Alignment = 3 # Justify
        sel.ParagraphFormat.SpaceBefore = 4
        sel.ParagraphFormat.SpaceAfter = 2
        sel.ParagraphFormat.KeepWithNext = True
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 10
        sel.Font.Bold = False
        sel.Font.Italic = True
        sel.TypeText(text)
        
    # ---------------------------------------------------------
    # 1. Title and Header (Single Column)
    # ---------------------------------------------------------
    add_para("When Data Quality Defects Interact: Measuring the Impact of Missing Values and Duplicate Leakage on Machine Learning Evaluation",
             bold=True, size=22, align=1, space_after=8, space_before=0)
             
    # Authors
    add_para("Divya Bohare, Amit Singh Bhadouriya, Vani Sharma, Sunidhi Shrivastava",
             bold=True, size=11, align=1, space_after=3, space_before=0)
    add_para("Department of Computer Science & Engineering, Amity School of Engineering and Technology\nAmity University Madhya Pradesh, Gwalior, India\nEmail: divyabohare7@gmail.com",
             bold=False, size=10, align=1, space_after=12, space_before=0)
             
    # ---------------------------------------------------------
    # 2. Section Break -> 2 Columns
    # ---------------------------------------------------------
    # Insert Continuous Section Break (type 3 = wdSectionContinuous)
    sel.InsertBreak(3)
    
    # Set current section to 2 columns
    sec2 = doc.Sections(2)
    sec2.PageSetup.TextColumns.SetCount(2)
    sec2.PageSetup.TextColumns.Spacing = 18 # 0.635 cm (0.25 inch)
    sec2.PageSetup.TextColumns.EvenlySpaced = True
    
    # ---------------------------------------------------------
    # 3. Abstract and Keywords
    # ---------------------------------------------------------
    sel.ParagraphFormat.Alignment = 3 # Justify
    sel.ParagraphFormat.SpaceBefore = 0
    sel.ParagraphFormat.SpaceAfter = 4
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    
    # Abstract bold italic run-in
    sel.Font.Bold = True
    sel.Font.Italic = True
    sel.TypeText("Abstract—")
    sel.Font.Bold = False
    sel.Font.Italic = True
    sel.TypeText("Reliable supervised machine learning evaluation relies on the fundamental assumption that training and test partitions are independent and identically distributed (i.i.d.). However, real-world data pipelines frequently suffer from co-occurring data quality defects. In particular, duplicate records crossing partition boundaries introduce test-to-training leakage, while feature missingness alters the information content of those observations. Although existing studies treat data leakage and missing values as separate operational challenges, their joint empirical interaction remains poorly understood. This study systematically investigates this interaction across three tabular benchmark datasets: Wine Quality—Red (N = 1,599), Wine Quality—White (N = 4,898), and a stratified 10,000-record subsample of Adult Census Income (N = 10,000). We evaluate three foundational classifiers—Logistic Regression, Decision Trees, and Random Forests—across four Missing Completely at Random (MCAR) feature-masking levels (0%, 10%, 20%, 30%) and four controlled test-to-training duplicate overlap levels (0%, 10%, 25%, 50%), alongside ordinary random splitting, across ten random experimental seeds (2,160 model evaluations). Our findings demonstrate that duplicate overlap produces severe, model-dependent performance inflation: at 50% overlap and 0% additional missingness, F1-scores were inflated by +0.142 to +0.202 for Decision Trees and +0.098 to +0.168 for Random Forests (p < 0.002, Wilcoxon signed-rank tests), eliminating 52.2% to 60.8% of apparent reference classification errors (Error-Reduction Illusion). In contrast, Logistic Regression exhibited negligible sensitivity (ΔF1 ≤ +0.006). Under ordinary random splitting, natural duplicate prevalence (15.0% in Red Wine and 19.1% in White Wine) caused statistically significant F1 inflation of +0.035 to +0.066 in tree models (p < 0.05), while producing no inflation in Adult (0.05% duplicates). Furthermore, ordinary least squares (OLS) interaction models reveal that missingness significantly amplifies tree-based duplicate leakage in higher-dimensional data (β_inter = +0.244, p < 10^-9 for Random Forest on Adult). Finally, a supplementary mechanism experiment shows that independently masking duplicate copies destroys the exact coordinate alignment required by trees, reducing the retained leakage effect to only 15.0%–32.3% at 30% missingness. We formulate rigorous, pipeline-level recommendations to audit duplicate structures and enforce leakage-safe partitioning in scientific and industrial workflows.")
    sel.TypeParagraph()
    
    # Keywords
    sel.ParagraphFormat.Alignment = 3
    sel.ParagraphFormat.SpaceBefore = 2
    sel.ParagraphFormat.SpaceAfter = 8
    sel.Font.Bold = True
    sel.Font.Italic = True
    sel.TypeText("Keywords—")
    sel.Font.Bold = False
    sel.Font.Italic = False
    sel.TypeText("Data quality, missing values, duplicate leakage, machine learning evaluation, data partitioning, error-reduction illusion.")
    sel.TypeParagraph()
    
    # ---------------------------------------------------------
    # 4. Section I: INTRODUCTION
    # ---------------------------------------------------------
    add_heading1("I.  INTRODUCTION")
    
    add_para("Supervised machine learning algorithms are increasingly deployed in mission-critical decision systems, including clinical risk assessment, automated credit underwriting, fraud detection, and predictive maintenance. The scientific and operational credibility of these models rests upon empirical evaluation: fitting candidate models on a designated training subset and assessing their generalisation performance on an independent, held-out test partition. The mathematical validity of this paradigm assumes that training and test samples are independently and identically distributed (i.i.d.) realizations drawn from a stationary data-generating distribution [1].")
    
    add_para("In practice, this independence assumption is routinely violated by data leakage—the unintended introduction of information from the test set (or downstream evaluation context) into the training pipeline [1], [5]. A prevalent yet insidious vector of data leakage is duplicate records. Repeated measurements, sensor logging anomalies, multi-source record aggregation, and customer retrials frequently inject identical or near-identical observations into tabular datasets. When a naive random split is applied to a dataset containing duplicate instances, identical feature-label tuples cross the train-test boundary. Consequently, an evaluation metric computed on the test partition ceases to measure generalisation to unseen observations; instead, it measures the capacity of the model to memorize and retrieve previously encountered points [1], [4].")
    
    add_para("Simultaneously, real-world tabular data suffer from another ubiquitous quality defect: missing values. Observational non-response, sensor failure, communication dropouts, and multi-modal integration gaps result in incomplete feature vectors [2], [3]. While a substantial body of literature has benchmarked imputation techniques across diverse missingness mechanisms [3], missing-data research has predominantly operated under the assumption of leak-free data partitioning. Conversely, data leakage studies have largely operated on complete, uncorrupted feature spaces [1].")
    
    add_para("In practical machine learning lifecycles, these two defects do not occur in isolated silos; they interact. Specifically: Does feature corruption attenuate the memorization advantage gained from duplicate leakage? Or conversely, does imputation provide an artificial anchor that preserves or even exacerbates the distortion of evaluation metrics? How does classifier inductive bias—ranging from linear hyperplanes to non-parametric recursive partitioning—modulate this vulnerability? And what is the empirical consequence of standard random train-test splitting when tabular datasets possess naturally occurring duplicates?")
    
    add_para("To address these foundational questions, this study conducts an exhaustive, multi-dataset, multi-model empirical investigation into the interaction between missing-value contamination and duplicate leakage. The main contributions are: (1) Quantifying the quantitative sensitivity of linear baselines and flexible tree models across controlled duplicate overlap levels (0% to 50%), establishing the Leakage Sensitivity Index (LSI) and Error-Reduction Illusion (ERI); (2) Assessing whether feature missingness moderates or amplifies duplicate leakage via OLS interaction models; (3) Auditing natural duplicate leakage in standard random splitting across contrasting datasets; (4) Disentangling feature identity from instance duplication via an independent-masking experiment; and (5) Delivering actionable, pipeline-level safeguards for robust machine learning workflows.")
    
    # ---------------------------------------------------------
    # 5. Section II: RELATED WORK AND RESEARCH GAP
    # ---------------------------------------------------------
    add_heading1("II.  RELATED WORK AND RESEARCH GAP")
    
    add_heading2("A. Data Quality in Machine Learning")
    add_para("Data quality is a multi-dimensional construct encompassing accuracy, completeness, consistency, timeliness, and uniqueness [4]. Mohammed et al. [4] investigated how data-quality dimensions (including missingness, label noise, and feature noise) degrade the performance of supervised learning algorithms on tabular benchmarks. Their findings indicated that algorithmic resilience varies markedly across architectures, with tree ensembles often exhibiting greater robustness to noise than linear or distance-based algorithms [6], [8]. However, their benchmarking evaluated models under conventional partitioning schemes, without explicitly modeling the confounding effects of cross-partition duplicate leakage.")
    
    add_heading2("B. Missing-Value Handling")
    add_para("Missing data theory categorizes missingness into Missing Completely at Random (MCAR), Missing at Random (MAR), and Missing Not at Random (MNAR) [16]. Emmanuel et al. [2] reviewed missing-data handling techniques, spanning listwise deletion, mean/median statistical imputation, k-nearest neighbors (KNN), and generative modeling [10]. Jäger et al. [3] benchmarked 14 imputation algorithms across multiple tabular datasets and missingness proportions, demonstrating that simple median/mode imputation remains a highly competitive and computationally efficient baseline, particularly when downstream models are decision-tree ensembles [6], [9]. Crucially, existing missingness benchmarks fit imputers strictly within clean train-test splits, leaving unaddressed how missingness behaves when identical observations reside on both sides of the evaluation split.")
    
    add_heading2("C. Data Leakage and Partitioning Strategies")
    add_para("The reproducibility crisis in machine learning has highlighted data leakage as one of the primary drivers of irreproducible claims [1]. Kapoor and Narayanan [1] surveyed over 300 papers across 17 fields, discovering widespread methodological leakage that led to severe performance overestimation. They categorized leakage into pre-split preprocessing leakage, feature leakage, and duplicate/distributional leakage [5], [19], [20]. Kaufman et al. [5] and scikit-learn guidelines [15] emphasized encapsulating preprocessing within training-only pipelines. However, the interaction between duplicate contamination across partitions and feature corruption within pipelines remains unexplored.")
    
    add_heading2("D. Research Gap and Research Questions")
    add_para("Although the literature addresses data quality, missing data, and leakage in isolation, their joint interaction represents an unmapped crossroad in empirical machine learning methodology. Specifically, does missingness obscure duplicate records and eliminate leakage, or does it amplify the vulnerability of evaluation metrics by degrading the true signal? This investigation resolves four formal research questions:")
    add_para("• RQ1: How does controlled duplicate overlap affect the F1-score across classifiers possessing distinct inductive biases (linear vs. single-tree vs. ensemble)?")
    add_para("• RQ2: Does increasing feature missingness systematically moderate (dampen or amplify) the magnitude of duplicate-leakage effects?")
    add_para("• RQ3: To what extent does ordinary random splitting inflate performance estimates on tabular datasets with varying degrees of natural duplicate prevalence?")
    add_para("• RQ4: Does duplicate leakage stem from the presence of repeated target-correlated instances, or does it strictly require the preservation of exact, multi-dimensional feature coordinates?")
    
    # ---------------------------------------------------------
    # 6. Section III: METHODOLOGY
    # ---------------------------------------------------------
    add_heading1("III.  METHODOLOGY")
    
    add_heading2("A. Research Design")
    add_para("We executed a controlled, full-factorial experimental design implemented in Python using scikit-learn [15], numpy, pandas, scipy, and statsmodels. The design encompasses: 3 benchmark datasets (Wine Quality—Red, Wine Quality—White, Adult Census Income subsample); 3 classification models (Logistic Regression, Decision Tree, Random Forest); 4 additional MCAR feature cell masking levels (0%, 10%, 20%, 30%); 4 controlled overlap conditions (0%, 10%, 25%, 50%); 1 natural ordinary random split condition; 1 supplementary independent-masking condition at 50% overlap; and 10 random seeds (0 to 9). In total, the experimental suite executes 2,160 fully trained and evaluated classification pipelines.")
    
    add_heading2("B. Datasets and Duplicate Auditing")
    add_para("We selected three open-access tabular benchmarks from the UCI Machine Learning Repository [11], [12] to reflect contrasting dimensionalities, feature typologies, and intrinsic duplicate structures (Table I).")
    
    # Table I insertion
    sel.ParagraphFormat.Alignment = 1 # Center
    sel.ParagraphFormat.SpaceBefore = 6
    sel.ParagraphFormat.SpaceAfter = 2
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    sel.Font.Bold = True
    sel.TypeText("TABLE I.  DATASET CHARACTERISTICS AND NATURAL DUPLICATE AUDIT")
    sel.TypeParagraph()
    
    # Insert Table I
    t1_range = sel.Range
    table1 = doc.Tables.Add(t1_range, 4, 6)
    table1.Rows.Alignment = 1 # Center
    t1_headers = ["Dataset", "Records", "Features", "Duplicates", "Target Class", "Pos. Ratio"]
    for j, h in enumerate(t1_headers):
        cell = table1.Cell(1, j+1)
        cell.Range.Text = h
        cell.Range.Font.Name = "Times New Roman"
        cell.Range.Font.Size = 8
        cell.Range.Font.Bold = True
        cell.Range.ParagraphFormat.Alignment = 1
        
    t1_rows = [
        ["Wine Red [11]", "1,599", "11 num", "240 (15.0%)", "Quality ≥ 6", "53.5%"],
        ["Wine White [11]", "4,898", "11 num", "937 (19.1%)", "Quality ≥ 6", "66.5%"],
        ["Adult Income [12]", "10,000", "6 num, 8 cat", "5 (0.05%)", "Income > 50K", "23.9%"]
    ]
    for i, row in enumerate(t1_rows):
        for j, val in enumerate(row):
            cell = table1.Cell(i+2, j+1)
            cell.Range.Text = val
            cell.Range.Font.Name = "Times New Roman"
            cell.Range.Font.Size = 8
            cell.Range.ParagraphFormat.Alignment = 1 if j > 0 else 0
            
    # Set table borders (horizontal only)
    table1.Borders.Enable = False
    table1.Borders(-1).LineStyle = 1 # Top border (wdBorderTop = -1)
    table1.Borders(-3).LineStyle = 1 # Bottom border (wdBorderBottom = -3)
    table1.Rows(1).Borders(-3).LineStyle = 1 # Header bottom border
    
    # Move selection past table
    sel.SetRange(table1.Range.End, table1.Range.End)
    sel.TypeParagraph()
    
    add_para("Wine Quality datasets comprise physicochemical measurements of Portuguese Vinho Verde wines [11]. The positive class is defined as sensory quality score ≥ 6. Adult Census Income is extracted from the 1994 US Census [12]; we used a 10,000-record stratified subsample (seed 26) with pre-existing missing entries preserved. Automated auditing verified zero contradictory duplicate rows (identical features with conflicting labels) across all datasets.")
    
    add_heading2("C. Missing-Value Injection and Pipeline Encapsulation")
    add_para("Feature missingness is injected under an MCAR mechanism at rates m ∈ {0.0, 0.10, 0.20, 0.30}. Target labels are never masked. To strictly prevent preprocessing leakage [5], all transformations are encapsulated in a scikit-learn Pipeline. Numerical columns undergo training-set median imputation followed by StandardScaler. Categorical columns undergo training-set mode imputation followed by OneHotEncoder. All parameters are fitted strictly on the training partition.")
    
    add_heading2("D. Reference and Leakage Partitioning Schemes")
    add_para("The reference split employs a stratified group-aware partitioner. Every unique record (feature tuple plus label) is assigned an indivisible group ID, ensuring that training and testing partitions share zero identical observations (0% overlap). Controlled overlap conditions (10%, 25%, 50%) select K = round(α · |X_test|) observations from the test set and append exact copies to the training partition, evaluating on the original test set. The ordinary random split condition applies stratified row-level splitting without grouping.")
    
    add_heading2("E. Supplementary Mechanism Experiment")
    add_para("Fixed at 50% overlap, the supplementary experiment compares exact duplicate copies against independently masked copies. In the exact condition, training copies share the identical mask pattern as their test counterparts. In the independent condition, training copies are drawn from unmasked records and corrupted independently with rate m. This isolates whether tree models benefit from general neighborhood density or strictly from exact coordinate matching.")
    
    add_heading2("F. Classification Models and Evaluation Metrics")
    add_para("We evaluate Logistic Regression (max_iter=2000), CART Decision Tree (unpruned), and Random Forest (100 trees, sqrt features). Primary metric is positive-class binary F1-score:")
    
    # Equation 1
    sel.ParagraphFormat.Alignment = 1 # Center
    sel.ParagraphFormat.SpaceBefore = 3
    sel.ParagraphFormat.SpaceAfter = 3
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    sel.TypeText("F1 = (2 · Precision · Recall) / (Precision + Recall)      (1)")
    sel.TypeParagraph()
    
    add_para("We derive F1 inflation (ΔF1 = F1_contaminated - F1_reference), Leakage Sensitivity Index (LSI = β_overlap × 0.10), and Error-Reduction Illusion (ERI):")
    
    # Equation 2
    sel.ParagraphFormat.Alignment = 1 # Center
    sel.ParagraphFormat.SpaceBefore = 3
    sel.ParagraphFormat.SpaceAfter = 3
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    sel.TypeText("ERI = [ ΔF1 / (1 - F1_reference) ] × 100%      (2)")
    sel.TypeParagraph()
    
    # ---------------------------------------------------------
    # 7. Section IV: RESULTS AND DISCUSSION
    # ---------------------------------------------------------
    add_heading1("IV.  RESULTS AND DISCUSSION")
    
    add_heading2("A. Effect of Controlled Duplicate Overlap (RQ1)")
    add_para("Controlled duplicate overlap produced massive, statistically significant F1 inflation in tree-based models, while leaving Logistic Regression largely unaffected (Table II).")
    
    # Table II insertion
    sel.ParagraphFormat.Alignment = 1 # Center
    sel.ParagraphFormat.SpaceBefore = 6
    sel.ParagraphFormat.SpaceAfter = 2
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    sel.Font.Bold = True
    sel.TypeText("TABLE II.  F1 PERFORMANCE AND INFLATION AT 50% OVERLAP (0% MISSINGNESS)")
    sel.TypeParagraph()
    
    t2_range = sel.Range
    table2 = doc.Tables.Add(t2_range, 10, 6)
    table2.Rows.Alignment = 1
    t2_headers = ["Dataset", "Model", "Ref F1", "50% Overlap", "ΔF1", "ERI (%)"]
    for j, h in enumerate(t2_headers):
        cell = table2.Cell(1, j+1)
        cell.Range.Text = h
        cell.Range.Font.Name = "Times New Roman"
        cell.Range.Font.Size = 8
        cell.Range.Font.Bold = True
        cell.Range.ParagraphFormat.Alignment = 1
        
    t2_data = [
        ["Wine Red", "Decision Tree", "0.697", "0.873", "+0.176**", "57.9%"],
        ["Wine Red", "Random Forest", "0.777", "0.913", "+0.136**", "60.8%"],
        ["Wine Red", "Logistic Reg.", "0.757", "0.763", "+0.006*", "2.6%"],
        ["Wine White", "Decision Tree", "0.766", "0.908", "+0.142**", "60.5%"],
        ["Wine White", "Random Forest", "0.834", "0.932", "+0.098**", "58.7%"],
        ["Wine White", "Logistic Reg.", "0.820", "0.820", "+0.0004", "0.3%"],
        ["Adult Income", "Decision Tree", "0.615", "0.817", "+0.202**", "52.5%"],
        ["Adult Income", "Random Forest", "0.679", "0.847", "+0.168**", "52.2%"],
        ["Adult Income", "Logistic Reg.", "0.665", "0.671", "+0.005**", "1.6%"]
    ]
    for i, row in enumerate(t2_data):
        for j, val in enumerate(row):
            cell = table2.Cell(i+2, j+1)
            cell.Range.Text = val
            cell.Range.Font.Name = "Times New Roman"
            cell.Range.Font.Size = 8
            cell.Range.ParagraphFormat.Alignment = 1 if j > 1 else 0
            
    table2.Borders.Enable = False
    table2.Borders(-1).LineStyle = 1
    table2.Borders(-3).LineStyle = 1
    table2.Rows(1).Borders(-3).LineStyle = 1
    
    sel.SetRange(table2.Range.End, table2.Range.End)
    sel.TypeParagraph()
    
    # Figure 1 insertion
    fig1_path = os.path.abspath(os.path.join("figures", "fig1_f1_inflation_by_overlap.png"))
    if os.path.exists(fig1_path):
        sel.ParagraphFormat.Alignment = 1
        sel.ParagraphFormat.SpaceBefore = 4
        sel.ParagraphFormat.SpaceAfter = 2
        pic = sel.InlineShapes.AddPicture(fig1_path)
        pic.Width = 240 # fit 1 column width
        pic.Height = 85
        sel.TypeParagraph()
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 8
        sel.Font.Italic = False
        sel.TypeText("Fig. 1.  F1-score inflation (ΔF1) across controlled duplicate overlap (0%, 10%, 25%, 50%) at 0% additional missingness with 95% confidence interval bands.")
        sel.TypeParagraph()
        
    add_para("As shown in Fig. 1, tree models exhibit a linear dose-response sensitivity to duplicate overlap. Decision Tree F1 increased by +0.142 to +0.202, while Random Forest F1 rose by +0.098 to +0.168. In contrast, Logistic Regression remained essentially unaffected (ΔF1 ≤ +0.006). The Error-Reduction Illusion reveals that 52% to 61% of residual classification errors appear to vanish purely from duplicate memorization.")
    
    add_para("This divergence stems from inductive bias: Decision trees recursively partition space into axis-aligned hyper-rectangles. A leaked test instance in training creates a pure leaf node matching the test label exactly, functioning as a nearest-neighbor hash lookup. Ensembles average these pure leaves across trees. Logistic regression optimizes a global hyper-plane; duplicating instances merely shifts sample weights slightly along the decision boundary without permitting localized memorization.")
    
    add_heading2("B. Interaction Between Missingness and Leakage (RQ2)")
    add_para("OLS regressions (Table III) demonstrate that the interaction between missingness and leakage is mediated by feature dimensionality.")
    
    # Table III insertion
    sel.ParagraphFormat.Alignment = 1
    sel.ParagraphFormat.SpaceBefore = 6
    sel.ParagraphFormat.SpaceAfter = 2
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    sel.Font.Bold = True
    sel.TypeText("TABLE III.  OLS INTERACTION MODELS (ΔF1 ~ OVERLAP × MISSINGNESS)")
    sel.TypeParagraph()
    
    t3_range = sel.Range
    table3 = doc.Tables.Add(t3_range, 5, 6)
    table3.Rows.Alignment = 1
    t3_headers = ["Dataset", "Model", "β_overlap", "β_missing", "β_inter", "p_inter"]
    for j, h in enumerate(t3_headers):
        cell = table3.Cell(1, j+1)
        cell.Range.Text = h
        cell.Range.Font.Name = "Times New Roman"
        cell.Range.Font.Size = 8
        cell.Range.Font.Bold = True
        cell.Range.ParagraphFormat.Alignment = 1
        
    t3_data = [
        ["Wine Red", "Pooled", "+0.203", "-0.013", "+0.044", "0.659"],
        ["Wine White", "Pooled", "+0.157", "-0.009", "-0.029", "0.682"],
        ["Adult Income", "Decision Tree", "+0.406", "-0.007", "+0.115", "0.0137*"],
        ["Adult Income", "Random Forest", "+0.337", "+0.009", "+0.244", "6.6e-10**"]
    ]
    for i, row in enumerate(t3_data):
        for j, val in enumerate(row):
            cell = table3.Cell(i+2, j+1)
            cell.Range.Text = val
            cell.Range.Font.Name = "Times New Roman"
            cell.Range.Font.Size = 8
            cell.Range.ParagraphFormat.Alignment = 1 if j > 1 else 0
            
    table3.Borders.Enable = False
    table3.Borders(-1).LineStyle = 1
    table3.Borders(-3).LineStyle = 1
    table3.Rows(1).Borders(-3).LineStyle = 1
    
    sel.SetRange(table3.Range.End, table3.Range.End)
    sel.TypeParagraph()
    
    # Figure 2 insertion
    fig2_path = os.path.abspath(os.path.join("figures", "fig2_missingness_interaction.png"))
    if os.path.exists(fig2_path):
        sel.ParagraphFormat.Alignment = 1
        sel.ParagraphFormat.SpaceBefore = 4
        sel.ParagraphFormat.SpaceAfter = 2
        pic2 = sel.InlineShapes.AddPicture(fig2_path)
        pic2.Width = 240
        pic2.Height = 85
        sel.TypeParagraph()
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 8
        sel.Font.Italic = False
        sel.TypeText("Fig. 2.  Interaction between MCAR missingness and duplicate leakage at 50% overlap across models.")
        sel.TypeParagraph()
        
    add_para("In the 11-feature Wine datasets, the interaction term is non-significant (p > 0.60), as median imputation preserves coordinate matching between paired copies. In Adult Census Income, missingness significantly amplifies duplicate leakage in tree models (β_inter = +0.244, p < 10^-9 for Random Forest; Fig. 2). As missingness degrades the reference baseline from 0.679 to 0.640, leaked duplicate test points act as imputed anchors that trees exploit, expanding net F1 inflation to +0.241 at 30% missingness.")
    
    add_heading2("C. Ordinary Random Splitting vs. Duplicate-Aware Splitting (RQ3)")
    add_para("Natural duplicate prevalence dictates the evaluation bias incurred by ordinary random splitting (Table IV and Fig. 3).")
    
    # Table IV insertion
    sel.ParagraphFormat.Alignment = 1
    sel.ParagraphFormat.SpaceBefore = 6
    sel.ParagraphFormat.SpaceAfter = 2
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 9
    sel.Font.Bold = True
    sel.TypeText("TABLE IV.  EVALUATION BIAS IN ORDINARY RANDOM SPLITTING (0% MISSINGNESS)")
    sel.TypeParagraph()
    
    t4_range = sel.Range
    table4 = doc.Tables.Add(t4_range, 4, 5)
    table4.Rows.Alignment = 1
    t4_headers = ["Dataset", "Natural Dups", "Decision Tree ΔF1", "Random Forest ΔF1", "Logistic Reg. ΔF1"]
    for j, h in enumerate(t4_headers):
        cell = table4.Cell(1, j+1)
        cell.Range.Text = h
        cell.Range.Font.Name = "Times New Roman"
        cell.Range.Font.Size = 8
        cell.Range.Font.Bold = True
        cell.Range.ParagraphFormat.Alignment = 1
        
    t4_data = [
        ["Wine Red", "15.0%", "+0.058 ± 0.021**", "+0.035 ± 0.012*", "-0.008 ± 0.018"],
        ["Wine White", "19.1%", "+0.066 ± 0.015**", "+0.047 ± 0.010**", "+0.005 ± 0.008"],
        ["Adult Income", "0.05%", "-0.002 ± 0.012", "-0.009 ± 0.014", "-0.009 ± 0.014"]
    ]
    for i, row in enumerate(t4_data):
        for j, val in enumerate(row):
            cell = table4.Cell(i+2, j+1)
            cell.Range.Text = val
            cell.Range.Font.Name = "Times New Roman"
            cell.Range.Font.Size = 8
            cell.Range.ParagraphFormat.Alignment = 1 if j > 0 else 0
            
    table4.Borders.Enable = False
    table4.Borders(-1).LineStyle = 1
    table4.Borders(-3).LineStyle = 1
    table4.Rows(1).Borders(-3).LineStyle = 1
    
    sel.SetRange(table4.Range.End, table4.Range.End)
    sel.TypeParagraph()
    
    # Figure 3 insertion
    fig3_path = os.path.abspath(os.path.join("figures", "fig3_ordinary_vs_duplicate_aware.png"))
    if os.path.exists(fig3_path):
        sel.ParagraphFormat.Alignment = 1
        sel.ParagraphFormat.SpaceBefore = 4
        sel.ParagraphFormat.SpaceAfter = 2
        pic3 = sel.InlineShapes.AddPicture(fig3_path)
        pic3.Width = 240
        pic3.Height = 85
        sel.TypeParagraph()
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 8
        sel.Font.Italic = False
        sel.TypeText("Fig. 3.  Evaluation bias of ordinary random splitting compared to duplicate-aware reference across missingness levels.")
        sel.TypeParagraph()
        
    add_para("In Adult, where natural duplicates constitute 0.05% of rows, ordinary random splitting introduces zero bias (p = 0.922). However, in Wine Red and White (15.0% and 19.1% duplicates), random splitting allows 21.4% and 27.6% of test records to have training twins, artificially inflating tree F1 by +0.035 to +0.066 (p < 0.05). Published studies using naive random splits on Wine Quality are systematically overestimating tree performance.")
    
    add_heading2("D. Exact Copies vs. Independently Masked Copies (RQ4)")
    add_para("The supplementary experiment decouples record presence from exact coordinate matching. At 0% missingness, independently masked copies retain 100% of exact-copy inflation. However, as missingness reaches 30%, retained leakage collapses to 19.5%–23.7% for Decision Trees and 15.0%–32.3% for Random Forests (Fig. 4).")
    
    # Figure 4 insertion
    fig4_path = os.path.abspath(os.path.join("figures", "fig4_exact_vs_independent_mask.png"))
    if os.path.exists(fig4_path):
        sel.ParagraphFormat.Alignment = 1
        sel.ParagraphFormat.SpaceBefore = 4
        sel.ParagraphFormat.SpaceAfter = 2
        pic4 = sel.InlineShapes.AddPicture(fig4_path)
        pic4.Width = 240
        pic4.Height = 85
        sel.TypeParagraph()
        sel.Font.Name = "Times New Roman"
        sel.Font.Size = 8
        sel.Font.Italic = False
        sel.TypeText("Fig. 4.  Leakage retention ratio of independently masked copies vs. exact copies across missingness rates.")
        sel.TypeParagraph()
        
    add_para("When masks are sampled independently, differing feature dropouts route the test twin down an alternative branch of the tree, destroying memorized leaf purity. This proves that duplicate leakage is driven by exact multi-dimensional coordinate identity rather than local density.")
    
    add_heading2("E. Practical Recommendations for ML Engineering")
    add_para("We prescribe four concrete safeguards: (1) Mandatory Raw Duplicate Auditing before any transformation; (2) Enforce Group-Aware Splitting (StratifiedGroupKFold) so identical records never cross partitions; (3) Encapsulate Imputers within Pipeline objects fitted strictly on training folds; and (4) Audit Model Ranking Disparities, recognizing that sudden tree leads over linear baselines are frequent symptoms of duplicate contamination.")
    
    # ---------------------------------------------------------
    # 8. Section V: THREATS TO VALIDITY
    # ---------------------------------------------------------
    add_heading1("V.  THREATS TO VALIDITY")
    add_para("Internal validity was protected by strict seed controls, non-parametric Wilcoxon testing, and leak-free pipeline encapsulation. External validity is bounded by our focus on three tabular benchmarks and three model architectures; future work should examine gradient-boosted trees and deep tabular architectures [7], [8]. Construct validity is bounded by our focus on MCAR missingness and exact duplicates; real-world environments may exhibit MAR/MNAR dynamics and near-duplicate entity fuzziness.")
    
    # ---------------------------------------------------------
    # 9. Section VI: CONCLUSION AND FUTURE WORK
    # ---------------------------------------------------------
    add_heading1("VI.  CONCLUSION AND FUTURE WORK")
    add_para("This study systematically examined the interaction between missing values and duplicate leakage across 2,160 model evaluations. We demonstrated that duplicate leakage is highly model-dependent: flexible tree architectures suffer massive F1 inflation (up to +0.202 at 50% overlap), while linear models remain essentially immune. Standard random splitting on datasets with moderate natural duplicates (15%–19%) introduces statistically significant inflation (+0.035 to +0.066). In higher-dimensional data, missingness amplifies leakage by degrading the true signal while preserving duplicate memorization. Future work should investigate non-random missingness (MAR/MNAR) and soft record linkage in streaming environments.")
    
    # ---------------------------------------------------------
    # 10. ACKNOWLEDGMENT
    # ---------------------------------------------------------
    add_heading1("ACKNOWLEDGMENT")
    add_para("The authors thank Amity University Madhya Pradesh, the IEEE Student Branch (ASET-AUMP), Amity Innovation Incubator, and the IEEE MP Section for organizing and supporting the Amity Researchothon 2026. We also acknowledge the UCI Machine Learning Repository.")
    
    # ---------------------------------------------------------
    # 11. REFERENCES (20 references, 10 from last 5 years, IEEE format)
    # ---------------------------------------------------------
    add_heading1("REFERENCES")
    
    sel.ParagraphFormat.Alignment = 3
    sel.ParagraphFormat.SpaceBefore = 1
    sel.ParagraphFormat.SpaceAfter = 2
    sel.ParagraphFormat.LeftIndent = 14
    sel.ParagraphFormat.FirstLineIndent = -14
    sel.Font.Name = "Times New Roman"
    sel.Font.Size = 8
    
    refs = [
        "[1] S. Kapoor and A. Narayanan, “Leakage and the reproducibility crisis in machine-learning-based science,” Patterns, vol. 4, no. 9, Art. no. 100804, Sep. 2023, doi: 10.1016/j.patter.2023.100804.",
        "[2] T. Emmanuel, T. Maupong, D. Mpoeleng, T. Semong, B. Mphago, and O. Tabona, “A survey on missing data in machine learning,” Journal of Big Data, vol. 8, Art. no. 140, Oct. 2021, doi: 10.1186/s40537-021-00516-9.",
        "[3] S. Jäger, A. Allhorn, and F. Bießmann, “A benchmark for data imputation methods,” Frontiers in Big Data, vol. 4, Art. no. 693674, Jul. 2021, doi: 10.3389/fdata.2021.693674.",
        "[4] S. Mohammed, K. D. M. S. R. B. Dissanayake, and A. Bifet, “The effects of data quality on machine learning performance on tabular data,” Information Systems, vol. 132, Art. no. 102549, Jan. 2025, doi: 10.1016/j.is.2025.102549.",
        "[5] S. Kaufman, S. Rosset, C. Perlich, and O. Stitelman, “Leakage in data mining: Formulation, detection, and avoidance,” ACM Trans. Knowl. Discov. Data, vol. 6, no. 4, Art. no. 15, Dec. 2012, doi: 10.1145/2382577.2382579.",
        "[6] L. Grinsztajn, E. Oyallon, and G. Varoquaux, “Why do tree-based models still outperform deep learning on typical tabular data?,” in Adv. Neural Inf. Process. Syst. (NeurIPS), vol. 35, Dec. 2022, pp. 507–520.",
        "[7] V. Borisov, T. Leemann, K. Seßler, J. Haug, M. Pawelczyk, and G. Kasneci, “Deep neural networks and tabular data: A survey,” IEEE Trans. Neural Netw. Learn. Syst., vol. 35, no. 6, pp. 7499–7518, Jun. 2024, doi: 10.1109/TNNLS.2022.3229161.",
        "[8] R. Shwartz-Ziv and A. Armon, “Tabular data: Deep learning is not all you need,” Information Fusion, vol. 81, pp. 84–90, May 2022, doi: 10.1016/j.inffus.2021.11.011.",
        "[9] Y. Zhang, T. R. Shah, D. S. Berman, and H. Rangwala, “Benchmarking missing value imputation approaches on tabular healthcare data,” Scientific Reports, vol. 14, Art. no. 23819, Oct. 2024, doi: 10.1038/s41598-024-75010-8.",
        "[10] J. Yoon, J. Jordon, and M. van der Schaar, “GAIN: Missing data imputation using Generative Adversarial Nets,” in Proc. 35th Int. Conf. Mach. Learn. (ICML), Jul. 2018, pp. 5689–5698.",
        "[11] P. Cortez, A. Cerdeira, F. Almeida, T. Matos, and J. Reis, “Modeling wine preferences by data mining from physicochemical properties,” Decision Support Systems, vol. 47, no. 4, pp. 547–553, Nov. 2009, doi: 10.1016/j.dss.2009.05.016.",
        "[12] R. Kohavi, “Scaling up the accuracy of naive-Bayes classifiers: A decision-tree hybrid,” in Proc. 2nd Int. Conf. Knowl. Discov. Data Min. (KDD), Portland, OR, USA, 1996, pp. 202–207.",
        "[13] L. Breiman, “Random forests,” Machine Learning, vol. 45, no. 1, pp. 5–32, Oct. 2001, doi: 10.1023/A:1010933404324.",
        "[14] J. R. Quinlan, “Induction of decision trees,” Machine Learning, vol. 1, no. 1, pp. 81–106, Mar. 1986, doi: 10.1007/BF00116251.",
        "[15] F. Pedregosa et al., “Scikit-learn: Machine learning in Python,” Journal of Machine Learning Research, vol. 12, pp. 2825–2830, Nov. 2011.",
        "[16] D. B. Rubin, “Inference and missing data,” Biometrika, vol. 63, no. 3, pp. 581–592, Dec. 1976, doi: 10.1093/biomet/63.3.581.",
        "[17] M. Fernandez-Delgado, E. Cernadas, S. Barro, and D. Amorim, “Do we need hundreds of classifiers to solve real world classification problems?,” Journal of Machine Learning Research, vol. 15, no. 1, pp. 3133–3181, Oct. 2014.",
        "[18] M. S. Santos, J. P. Abreu, P. J. Garcia-Laencina, A. Simao, and P. H. Vieira, “A new cluster-based oversampling method for improving survival prediction,” J. Biomed. Inform., vol. 58, pp. 49–59, Dec. 2015.",
        "[19] M. J. Er, S. Zhang, N. Ning, and J. Wu, “Adaptive Information Leakage Detection and Mitigation for Tabular Data,” IEEE Trans. Knowl. Data Eng., vol. 35, no. 8, pp. 8421–8434, Aug. 2023, doi: 10.1109/TKDE.2022.3204910.",
        "[20] A. S. More, D. P. Rana, and S. Kumar, “A review on data leakage detection and prevention techniques in cloud and machine learning environments,” IEEE Access, vol. 11, pp. 34912–34928, Apr. 2023, doi: 10.1109/ACCESS.2023.3264102."
    ]
    
    for r in refs:
        sel.TypeText(r)
        sel.TypeParagraph()
        
    # ---------------------------------------------------------
    # Save DOCX and Export PDF
    # ---------------------------------------------------------
    docx_path = os.path.abspath("Amity_Researchothon_Research_Paper.docx")
    pdf_path = os.path.abspath("Amity_Researchothon_Research_Paper.pdf")
    
    # Save as docx
    doc.SaveAs2(docx_path, 16) # 16 = wdFormatDocumentDefault
    print(f"Saved Word Document: {docx_path}")
    
    # Export as PDF (17 = wdExportFormatPDF)
    doc.ExportAsFixedFormat(pdf_path, 17)
    print(f"Saved IEEE PDF: {pdf_path}")
    
    # Check page count
    pages = doc.ComputeStatistics(2) # 2 = wdStatisticPages
    print(f"Total Page Count: {pages} pages (Guideline limit: maximum 6 pages)")
    
    doc.Close(False)
    word.Quit()
    
    return docx_path, pdf_path, pages

if __name__ == '__main__':
    create_ieee_paper()
