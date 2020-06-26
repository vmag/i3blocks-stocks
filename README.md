# i3blocks-stocks
---

## Example

To display S&P Futures on the i3bar, add this configuration to i3blocks.conf

```bash[SPY]
command=python3 get_stocks.py https://www.investing.com/indices/us-spx-500-futures 
interval=60
align=center
markup=pango
separator_block_width=20
```
