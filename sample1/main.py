import streamlit as st
import numpy as np
import pandas as pd

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

