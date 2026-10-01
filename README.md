# Scale

محاسبهٔ میانگین، واریانس و انحراف معیار برای یک آرایه از اعداد.

## توابع

### `loc(nums)`
میانگین آرایه را برمی‌گرداند:

```
loc = Σx / n
```

```python
loc(np.array([1, 4, 8, 9, 0]))   # 4.4
```

### `variance(nums_array)`
واریانس **جمعیت** را برمی‌گرداند (تقسیم بر `n`، نه `n-1`):

```
variance = Σ(x − mean)² / n
```

```python
variance(np.array([1, 4, 8, 9, 0]))   # 12.64
```

### `scale(v)`
انحراف معیار را از روی مقدار واریانس برمی‌گرداند:

```
scale = √v
```

```python
scale(12.64)   # 3.555...
```

## مثال

```python
import numpy as np
from Scale import loc, variance, scale

arry = np.array([1, 4, 8, 9, 0])

v = variance(arry)
print(loc(arry))     # 4.4
print(v)             # 12.64
print(scale(v))      # 3.555...
```

## اجرا

```bash
python Scale.py
```

## پیش‌نیاز

```bash
pip install numpy
```

## نکات

- واریانس به‌صورت **جمعیت** محاسبه می‌شود، نه نمونه.
- `loc` و `variance` ورودی numpy array می‌گیرند (چون از `.sum()` استفاده می‌کنند).
- `scale` از روی مقدار واریانس حساب می‌شود، نه مستقیم از داده‌ها.
- اگر آرایه خالی باشد، در `loc` و `variance` تقسیم بر صفر رخ می‌دهد.

## فرمول‌ها

```
mean     = Σx / n
variance = Σ(x − mean)² / n
std      = √variance
```
