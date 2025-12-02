
# SafeWaterML: Predicting Water Safety with Random Forests




## 📌 Overview
This project aims to assess water safety by analyzing chemical and biological contaminants using machine learning. By leveraging correlation analysis and classification models, we identify key pollutants and predict whether a water sample is safe for consumption.
## ❓ Problem Statement
Contaminated water poses serious health risks. Traditional water testing methods are time-consuming and expensive. This project explores whether machine learning can accurately classify water samples as safe or unsafe based on measurable contaminants, enabling faster and scalable assessments.
## 📂 Dataset
The dataset contains 21 features representing various chemical elements and biological agents found in water samples:

Chemical contaminants: aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper, fluoride, lead, nitrates, nitrites, mercury, perchlorate, radium, selenium, silver, uranium

Biological agents: bacteria, viruses

Target variable: is_safe (binary indicator of water safety)

These features were used for correlation analysis and classification modeling.
## 🛠️ Tools & Technologies
Programming Language: Python

Libraries:

pandas, numpy for data manipulation

matplotlib, seaborn for visualization

scikit-learn for machine learning (RandomForestClassifier, classification_report)

Model: Random Forest Classifier

Evaluation Metrics: Precision, Recall, F1-score, Accuracy
## 🔍 Key insights
📊 Correlation Analysis
Negative correlations with safety: viruses (-0.097), nitrates (-0.072), uranium (-0.076), aluminium (-0.11), arsenic (-0.09), cadmium (-0.08)

Positive correlations with safety: silver (0.100), chloramine (0.09), perchlorate (0.076), copper (0.07)

These insights suggest that certain contaminants are strong indicators of water safety and can be prioritized in monitoring systems.

🤖 Model Performance
Using RandomForestClassifier:

Accuracy: 98%

Precision & Recall: ~97–99% for both classes

F1-score: 0.98 for both safe and unsafe classes

This demonstrates that the model is highly effective in distinguishing safe vs. unsafe water
## Conclusion
Machine learning, particularly Random Forest, can be a powerful tool for water safety classification. The model achieved high accuracy and revealed meaningful relationships between contaminants and safety. This approach can support environmental agencies and public health initiatives by enabling rapid, automated water quality assessments.
## Contributing
Contributions to this project are welcome! If you have ideas for improvements or additional insights, please open an issue or a pull request. Your contributions will be greatly appreciated.
## 📬 Contact Information
LinkedIn: kaushik-raghani

Email: kaushikraghani23@gmail.com
=======
