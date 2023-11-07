import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit introduction")

st.write("DataFrame")

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

"""
# chapter
## second chapter
### third chapter

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

# st.line_chart(df1)
# st.area_chart(df1)
# st.bar_chart(df1)
# st.map(df2)

st.write("Display image")
Image.open("aircraft.jpg")