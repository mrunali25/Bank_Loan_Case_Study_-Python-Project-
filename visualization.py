# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_all_visualizations(df):
    """
    Plot all visualizations in a single pop-up window.
    """
    # Create a single Matplotlib figure
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Plot target distribution
    sns.countplot(x='TARGET', data=df, ax=axes[0])
    axes[0].set_title('Distribution of Loan Status')

    # Plot class imbalance pie chart
    class_counts = df['TARGET'].value_counts()
    class_ratios = class_counts / len(df)
    explode = (0.1, 0)  # Explode the first slice to highlight class imbalance
    colors = ['lightcoral', 'lightskyblue']
    axes[1].pie(class_ratios, labels=class_ratios.index, autopct='%1.1f%%', startangle=90, explode=explode, colors=colors)
    axes[1].set_title('Class Imbalance')

    # Convert Matplotlib plot to a Streamlit image
    image = fig_to_image(fig)
    plt.close(fig)  # Close the Matplotlib figure to free up memory

    return image

def fig_to_image(fig):
    """
    Convert Matplotlib figure to a Streamlit image.
    """
    import io
    import numpy as np
    from PIL import Image

    # Save Matplotlib figure to a buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    # Convert Matplotlib buffer to a PIL Image
    img = Image.open(buf)

    # Convert PIL Image to a NumPy array
    img_array = np.array(img)

    return img_array
