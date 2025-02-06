import streamlit as st
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from sklearn.preprocessing import StandardScaler

scoring_func = st.selectbox("Select a scoring function", ["ANOVA F-statistic", "mutual_info_classif"])

if "df" in st.session_state:
        
    st.write("Dataset preview:")
    st.write(st.session_state.df.head())
        
    st.write("Select the target column:")
    st.session_state.target_column = st.selectbox('Select the target column', st.session_state.df.columns.tolist())
        
    feature_columns = st.session_state.df.drop(columns=[st.session_state.target_column]).columns.tolist()

    if len(feature_columns) > 0:
        X = st.session_state.df[feature_columns]
        y = st.session_state.df[st.session_state.target_column]

        st.write("Select the number of features to keep:")
        k = st.slider('Number of features (k)', min_value=1, max_value=X.shape[1], value=4)

        if scoring_func == "ANOVA F-statistic":
            selector = SelectKBest(score_func=f_classif, k=k)
            X_selected = selector.fit_transform(X, y)
        else:
            selector = SelectKBest(score_func=mutual_info_classif, k=k)
            X_selected = selector.fit_transform(X, y)

        feature_columns_names = selector.get_feature_names_out(feature_columns)
            
        st.write(f"Selected {k} features:")
        st.write(feature_columns_names)

        st.write("Transformed data with selected features:")
        df_selected = pd.DataFrame(X_selected, columns=feature_columns_names)
        df_selected[st.session_state.target_column] = y
        st.write(df_selected)
        if st.button("Save selected features"):
            st.session_state.feature_selected_df = df_selected
            st.success("Selected features have been saved.")
    else:
        st.warning("Cannot perform feature selection. The dataset has no features.")
            
else:
    st.info("Please upload a CSV file to get started.")