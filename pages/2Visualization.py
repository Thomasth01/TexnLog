import streamlit as st
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import umap
import plotly.express as px

algorithm = st.selectbox("Select an algorithm", ["PCA","UMAP"])

if algorithm == "PCA":
    if "df" in st.session_state:
        
        st.write("Dataset preview:")
        st.write(st.session_state.df.head())

        st.write("Select the columns for PCA:")
        feature_columns = st.multiselect('Select feature columns', st.session_state.df.columns.tolist())
        
        if len(feature_columns) > 1:
            X = st.session_state.df[feature_columns]

            pca_2d = PCA(n_components=2)
            X_pca_2d = pca_2d.fit_transform(X)

            st.write("PCA 2D Visualization:")
            fig_2d, ax_2d = plt.subplots(figsize=(8, 6))
            ax_2d.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], edgecolor='k', s=100)
            ax_2d.set_title("PCA - 2D Projection", fontsize=16)
            ax_2d.set_xlabel('Principal Component 1', fontsize=14)
            ax_2d.set_ylabel('Principal Component 2', fontsize=14)
            st.pyplot(fig_2d)

            if len(feature_columns) < 3:

                st.info("Select three or more columns to visualize in 3D.")

            else:

                st.write("PCA 3D Visualization:")
                pca_3d = PCA(n_components=3)
                X_pca_3d = pca_3d.fit_transform(X)

                fig_3d = px.scatter_3d(
                    x=X_pca_3d[:, 0], y=X_pca_3d[:, 1], z=X_pca_3d[:, 2],
                    title="PCA - 3D Projection",
                    labels={'x': 'Principal Component 1', 'y': 'Principal Component 2', 'z': 'Principal Component 3'}
                )
                st.plotly_chart(fig_3d)

            st.write("Explained Variance Ratio:")
            st.write(pca_2d.explained_variance_ratio_)

        else:
            st.warning("Please select feature columns for PCA.")
    else:
        st.info("Please upload a CSV file to get started.")

elif algorithm == "UMAP":

    if "df" in st.session_state:
        
        st.write("Dataset preview:")
        st.write(st.session_state.df.head())

        st.write("Select the columns for UMAP:")
        feature_columns = st.multiselect('Select feature columns', st.session_state.df.columns.tolist())
        
        if len(feature_columns) > 1:
            # Extract features (X)
            X = st.session_state.df[feature_columns]

            umap_2d = umap.UMAP(n_components=2)
            X_umap_2d = umap_2d.fit_transform(X)

            st.write("UMAP 2D Visualization:")
            fig_2d, ax_2d = plt.subplots(figsize=(8, 6))
            ax_2d.scatter(X_umap_2d[:, 0], X_umap_2d[:, 1], edgecolor='k', s=100)
            ax_2d.set_title("UMAP - 2D Projection", fontsize=16)
            ax_2d.set_xlabel('UMAP Component 1', fontsize=14)
            ax_2d.set_ylabel('UMAP Component 2', fontsize=14)
            st.pyplot(fig_2d)

            st.write("UMAP 3D Visualization:")
            umap_3d = umap.UMAP(n_components=3)
            X_umap_3d = umap_3d.fit_transform(X)

            fig_3d = px.scatter_3d(
                x=X_umap_3d[:, 0], y=X_umap_3d[:, 1], z=X_umap_3d[:, 2],
                title="UMAP - 3D Projection",
                labels={'x': 'UMAP Component 1', 'y': 'UMAP Component 2', 'z': 'UMAP Component 3'}
            )
            st.plotly_chart(fig_3d)

        else:
            st.warning("Please select feature columns for UMAP.")
    else:
        st.info("Please upload a CSV file to get started.")

else:
    st.info("Please select an algorithm to proceed.")
