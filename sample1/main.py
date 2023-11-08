import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit introduction")

# st.write("DataFrame")

df = pd.DataFrame({
    "First row": [1, 2, 3, 4],
    "Second row": [10, 20, 30, 40]
})

df1 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)
# st.write(df)
# st.table(df.style.highlight_max(axis=0))

# """
# # chapter
# ## second chapter
# ### third chapter

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

# st.line_chart(df1)
# st.area_chart(df1)
# st.bar_chart(df1)
# st.map(df2)

# st.write("Display image")

# if st.checkbox("Show image"):
#     img = Image.open("aircraft.jpg")
#     st.image(img, "aricraft", use_column_width=True)

# option = st.selectbox(
#     "Please select your favorite",
#     list(range(1, 11))
# )

# "Your favorite number is:", option

# st.write("Interactive Widgets")

# left_column, right_column = st.columns(2)

# button = left_column.button("Right button")
# if button:
#     right_column.write("This is right")

# expander = st.expander("Query")
# expander.write("Input your query")

# option = st.text_input("Please tell your hobby")


# condition = st.slider("How about you", 0, 100, 50)

# "Your hobby is ", option
# "Your condition is ", condition

st.write("Progress bar")
"Start"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)