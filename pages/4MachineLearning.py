import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

if "df" in st.session_state:

    model_selected = st.selectbox("Select a model", ["Logistic Regression", "Random Forest"])

    if "feature_selected_df" in st.session_state:
        st.subheader("Original dataset:")
        st.write(st.session_state.df)
        st.subheader("Selected features:")
        st.write(st.session_state.feature_selected_df)

        X = st.session_state.df.drop(columns=[st.session_state.target_column])
        y = st.session_state.df[st.session_state.target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        X_selected = st.session_state.feature_selected_df.drop(columns=[st.session_state.target_column])
        y_selected = st.session_state.feature_selected_df[st.session_state.target_column]
        X_train_selected, X_test_selected, y_train_selected, y_test_selected = train_test_split(X_selected, y_selected, test_size=0.2, random_state=42)

        if model_selected == "Logistic Regression":
            st.header("Logistic Regression Model")
            k = st.slider("Max iterations", 100, 1000, 100, 100)
            model = LogisticRegression(max_iter=k)
            model.fit(X_train, y_train)
            st.write(f"Model used {model.n_iter_} iterations to converge.")
        
        if model_selected == "Random Forest":
            st.header("Random Forest Model")
            l = st.slider("Number of estimators", 100, 1000, 100, 100)
            model = RandomForestClassifier(n_estimators=l)
            model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        st.write("Original features:")
        st.write("Accuracy:", accuracy_score(y_test, y_pred))
        st.write("F1 score:", f1_score(y_test, y_pred))
        st.write("ROC AUC score:", roc_auc_score(y_test, y_pred))
        
        if model_selected == "Logistic Regression":
            model_selected = LogisticRegression(max_iter=k)
            model_selected.fit(X_train_selected, y_train_selected)
            st.write(f"Model used {model_selected.n_iter_} iterations to converge.")

        if model_selected == "Random Forest":
            model_selected = RandomForestClassifier(n_estimators=l)
            model_selected.fit(X_train_selected, y_train_selected)

        y_pred_selected = model_selected.predict(X_test_selected)
        st.write("Selected features:")
        st.write("Accuracy:", accuracy_score(y_test_selected, y_pred_selected))
        st.write("F1 score:", f1_score(y_test_selected, y_pred_selected))
        st.write("ROC AUC score:", roc_auc_score(y_test_selected, y_pred_selected))
        
    else:
        st.error("Please select features in the Feature Selection page.")
else:
    st.error("Please upload a dataset in the Home page.")


    