# Evaluación y validación de modelos de Aprendizaje automático

# Este módulo trata sobre cómo evaluar el rendimiento de los modelos en datos no observados,
# comenzando con las métricas de evaluación clave para la clasificación y la regresión.
# También explorará el ajuste de hiperparámetros para optimizar los modelos y evitar
# el sobreajuste mediante la validación cruzada. Se introducirán técnicas especiales,
# como la regularización en la regresión lineal, para manejar el sobreajuste debido a valores atípicos.
# Los ejercicios prácticos en Python le guiarán a través del ajuste fino de modelos y
# la validación cruzada para la evaluación fiable de modelos.

#IBM Data Science Professional Certificate

#For: Data science careers
#Covers: Data cleaning, analysis, and predictive modeling
#Tools Python, SQL, Pandas, Numpy

#IBM AI Engineering Path

#For: Data science careers, ML Engineers, software developers
#Covers: How to build, train and deploy ML models
#Tools Python, SciPy, Keras, PyTorch, TensorFlow


# Explain machine learning
# Machine learning:  Teach a computer how to learn from data,
#identify patterns and make predictions

# - uses algorithms to learn from data
# - Requires feature engineering

# Deep Learning: Use computational methods for learning
# Does not rely on a fixed algorithm

# - uses multi-layered neural networks to learn from data
# - Automatically extracts features from big data


================================================================================================
SUPERVISED LEARNING
Models train on labelaed data

UNSUPERVISED LEARNING
Learning works without labels

SEMI-SUPERVISED LEARNING
Learning works iteratively

REINFORMENT
Learning learns from feedback


================================================================================================
MACHINE LEARNING TECHNIQUES

Classification predict class or category of a case

Regression/estimation predicts continuos values

clustering groups similar data

Association find items or events that co-occur

Anomaly detaction discovers abnormal and unsual cases

Sequence mining predicts next event

Dimension reduction reduces size of data

Recommendation systems associate peoples preferences


================================================================================================
CLYCLE OF LIFE

1. Problem definition
2. Data collection - ETL
3. Data preparation - ETL
4. Model development and evaluation
5. Model deployment


WAYS OF MODEL DEVELOPMENT
================================================================================================
Data Scientist vs. AI Engineer

For years, data science was considered the "sexiest job," but the rise of AI engineering, 
especially in the generative AI era, has introduced new distinctions. Isaac Key, a former data scientist
now AI engineer at IBM, explains four main differences: use cases, data, models, and processes.

Use Cases

Data Scientist: Focuses on
descriptive (exploratory analysis, clustering) and
predictive (regression, classification) analytics. They are storytellers who analyze past data to explain or predict outcomes.

AI Engineer: Works on
prescriptive (decision optimization, recommendation engines) and
generative (intelligent assistants, chatbots) use cases, building AI systems to transform business processes.

Data

Data Scientist: Primarily uses structured/tabular data,
often in the hundreds to thousands of records,
requiring heavy cleaning and preprocessing.

AI Engineer: Mainly uses unstructured
data (text, images, audio, video).
Generative AI models like LLMs are trained on billions or trillions of tokens.

Models

Data Scientist: Uses many specialized machine learning models tailored to specific
datasets (regression, clustering, etc.), generally small, fast, and narrow in scope.

AI Engineer: Relies on foundation models, large and generalizable across tasks, but requiring massive compute resources and long training times.

Processes

Data Scientist: Workflow = define use case → collect/clean data → train/validate model → deploy for
prediction (with techniques like feature engineering and hyperparameter tuning).

AI Engineer: Workflow = define use case → use pre-trained foundation
model (thanks to AI democratization via open-source platforms like Hugging Face) → interact via prompt engineering → fine-tune or 
augment with frameworks (PEFT, RAG, chaining prompts, autonomous agents) → integrate into larger systems or applications.


================================================================================================

Tools for Machine Learning
Importance of Data

Data = raw facts, figures, or information used to gain insights, inform decisions, and power AI.

Central to all machine learning algorithms, as it fuels pattern discovery and predictions.

Machine Learning Tools

Provide functionalities across the ML pipeline: preprocessing, building, evaluating, optimizing, and deploying models.

Examples:

Pandas → data manipulation & analysis.

Scikit-learn → classical ML algorithms (regression, classification, clustering).

Programming Languages for ML

Python: most popular (rich libraries, easy model development).

R: strong in statistics and data exploration.

Julia: high-performance computing.

Scala: scalable, big data pipelines.

Java: scalable ML apps in production.

JavaScript: runs ML models in browsers.

Categories of ML Tools

Data Processing & Analytics

PostgreSQL, Hadoop, Spark, Kafka

Pandas, NumPy

Data Visualization

Matplotlib, Seaborn, ggplot2 (R), Tableau

Machine Learning

NumPy, Pandas, SciPy, Scikit-learn

Deep Learning

TensorFlow, Keras, Theano, PyTorch

Computer Vision

OpenCV, Scikit-Image, TorchVision

Natural Language Processing (NLP)

NLTK, TextBlob, Stanza

Generative AI

Hugging Face Transformers, ChatGPT, DALL·E, PyTorch (GANs & Transformers)

Conclusion

Data is the core fuel of machine learning.

Tools simplify complex tasks, support pipelines, and enable analytics, visualization, ML, deep learning, computer vision, NLP, and generative AI.

Popular languages: Python, R, Julia, Scala, Java, JavaScript.

================================================================================================

Scikit-Learn Machine Learning Ecosystem
Machine Learning Ecosystem

The ML ecosystem = interconnected tools, libraries, frameworks, platforms, and processes for developing, deploying, and monitoring ML models.

Covers stages: data collection, preprocessing, model training, evaluation, deployment, and monitoring.

Python provides one of the most widely used ML ecosystems with libraries like NumPy, Pandas, SciPy, Matplotlib, and Scikit-learn.

Key Libraries

NumPy: foundational support with efficient numerical computations on multidimensional arrays.

Pandas: data analysis, cleaning, and visualization using DataFrames.

SciPy: scientific computing (optimization, integration, regression, etc.).

Matplotlib: customizable data visualization tools.

Scikit-learn: built on NumPy, SciPy, and Matplotlib; core library for classical ML models.

Scikit-learn Features

Free, open-source ML library in Python.

Supports classification, regression, clustering, and dimensionality reduction.

Benefits:

Excellent documentation and large community support.

Easy to implement ML models with just a few lines of code.

Includes preprocessing (cleaning, scaling, feature selection/extraction), 
train/test splitting, model fitting, hyperparameter tuning (cross-validation), prediction, evaluation, and model export.

Example Workflow (Scikit-learn)

Preprocessing: scale data (standardization).

Train/test split: easily divide data (e.g., 33% test).

Model setup: instantiate a classifier (e.g., Support Vector Classifier with parameters γ and C).

Training: fit model to training data.

Prediction: use test data to generate predictions.

Evaluation: measure accuracy with metrics like a confusion matrix.

Model saving: export trained model (e.g., as a pickle file).

Conclusion

The ML ecosystem provides the foundation for end-to-end model development.

Scikit-learn is a powerful, user-friendly library that integrates preprocessing, training, evaluation,
and deployment into a seamless workflow, making it central to the Python ML ecosystem.


================================================================================================

La Inteligencia artificial (IA) simula la cognición humana, mientras que el Aprendizaje 
automático (AM) utiliza algoritmos y requiere ingeniería de características para aprender de los datos.

El aprendizaje automático incluye diferentes tipos de modelos: aprendizaje supervisado, 
que utiliza datos etiquetados para hacer predicciones; aprendizaje no supervisado, que 
encuentra patrones en datos no etiquetados; y aprendizaje semisupervisado, que se entrena en un pequeño subconjunto de datos etiquetados.

Los factores clave para elegir una técnica de aprendizaje automático son el tipo de 
problema que hay que resolver, los datos disponibles, los recursos disponibles y el resultado deseado.

Las técnicas de aprendizaje automático incluyen la Detección de anomalías para identificar 
casos inusuales como el fraude, la Clasificación para categorizar nuevos datos, la Regresión
 para predecir valores continuos y el Clustering para agrupar puntos de datos similares sin etiquetas.

Las herramientas de aprendizaje automático admiten canalizaciones con módulos para el 
preprocesamiento de datos, la creación de modelos, la evaluación, la optimización y la implantación.

R se utiliza habitualmente en el aprendizaje automático para el análisis estadístico y la 
exploración de datos, mientras que Python ofrece una amplia gama de bibliotecas para diferentes 
tareas de aprendizaje automático. Otros lenguajes de programación utilizados en ML son Julia, Scala, Java y JavaScript, cada uno adaptado a aplicaciones específicas como la computación de alto rendimiento y los modelos de ML basados en web.

Herramientas de Visualización de datos como Matplotlib y Seaborn crean gráficos personalizables, 
ggplot2 permite construir gráficos en capas, y Tableau proporciona cuadros de mando de datos interactivos.

Las bibliotecas de Python más utilizadas en el aprendizaje automático son NumPy para cálculos numéricos, 
Pandas para análisis y preparación de datos, SciPy para cálculo científico y Scikit-learn para crear modelos de aprendizaje automático tradicionales.

Los marcos de aprendizaje profundo como TensorFlow, Keras, Theano y PyTorch permiten diseñar, entrenar y probar 
redes neuronales utilizadas en áreas como la visión por ordenador y el Procesamiento de lenguaje natural.

Las herramientas de visión por ordenador permiten aplicaciones como la detección de objetos, la clasificación 
de imágenes y el reconocimiento facial, mientras que las herramientas de procesamiento de lenguaje natural (NLP) 
como NLTK, TextBlob y Stanza facilitan el procesamiento de textos, el análisis de sentimientos y el análisis sintáctico del lenguaje.

Las herramientas de IA generativa utilizan la inteligencia artificial para crear nuevos contenidos, como texto, 
imágenes, música y otros medios, a partir de datos o instrucciones.

Scikit-learn proporciona una serie de funciones, como la clasificación, la regresión, la agrupación, 
el preprocesamiento de datos, la evaluación de modelos y la exportación de modelos para su uso en producción.

El ecosistema de Aprendizaje automático incluye una red de herramientas, marcos de trabajo, bibliotecas, 
plataformas y procesos que apoyan colectivamente el desarrollo y la gestión de modelos de aprendizaje automático.