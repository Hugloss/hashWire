# Hashwire
HashWires are extremely efficient to create commitments via hash multichains. In hashwire a digit represent a value from the position in the hash multichain. The hash multichain has a hash chain per digitposition,  each of length 10. For example, an 8 digit number will require a hash multichain with 8 hash chains when transforming digit number with hashwire.
If the same digit appears in the same position across multiple partitions, only one commitment to that digit needs to be generated and can be reused.

For example, an 8 digit number will never require more than 80 SHA26 operations!
Think how it would be represented with a classic hash chain.

## Install
The source code is currently hosted on GitHub at:
https://github.com/Hugloss/hashWire

The latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/hashwire)

```sh
# PyPI
pip install hashwire
```

## License
[MIT](LICENSE)

## Example
```python
import hashwire as hw
h = hw.HashChains(13770)
print(h.mdp)
>>[13770, 13769, 13699, 12999, 9999]
```
```python
print(h.seeds)
>>['71e0e4f637bfe1ef668fae90435f2c254beb02471dcea1507b20e43237c7c891',
 'c3d05a2ffe810f20a2f75f140668bae8e934962d984a3e91df94412c9dcaecd4',
 '006ccb9fbf32d766dfc82c5b9ecf09ff670609b2eec5203c34b743bbec687a1f',
 'e25b065d21ea5b0089fba7de484df6ee3fa213054e780473183acc3c3ec92f36',
 'df0358ccf75d97eb690c4900b3af25277b786a6277c183bcc8ce0cf79419e6df']
```

```python
print(h.hash_chains)
>>
|    | 0             | 1             | 2             | 3             | 4             |
|---:|:--------------|:--------------|:--------------|:--------------|:--------------|
|  0 | b8621c2cf5... | 5419420325... | 5110c37435... | 97a3f53515... | 8d67f816fc... |
|  1 | 04086ee0ff... | c89832a67c... | cbd9c9d55d... | 68d14ee5c0... | 6d55ebd146... |
|  2 | 16acb11ba8... | 403587d2d8... | 328f66c316... | 0a5431e4b1... | d7dad3336f... |
|  3 | 4cca995753... | 7d14d3705b... | 21c4f0a677... | fd86ade7d5... | 601d828c7a... |
|  4 | b3095eb322... | f56751f8ce... | ff56251509... | cdd3c69966... | 8bfaff3bc0... |
|  5 | 49a97db1f7... | 82b37be23a... | 49ed8decaa... | 296aadc7c6... | 029af6b8c9... |
|  6 | caaa4def53... | 90461f8376... | cd7ee6056f... | 41f740a1b2... | 006129d74d... |
|  7 | bf83759942... | 489acd60ff... | 001d3e8d07... | 252d0446db... | de9ff13270... |
|  8 | 3252f34330... | 740a730d2c... | b7a8a1e9d3... | fe006a4bc2... | 9fe5a28d2f... |
|  9 | 272cdd532b... | 790b25ac7f... | 94ac568dae... | 99ed55b8b0... | f4372d2062... |
```
```python
print(h.commitments)
>>
|    | 13770         | 13769         | 13699         | 12999         | 9999          |
|---:|:--------------|:--------------|:--------------|:--------------|:--------------|
|    | 04086ee0ff... | 04086ee0ff... | 04086ee0ff... | 04086ee0ff... | 790b25ac7f... |
|    | 7d14d3705b... | 7d14d3705b... | 7d14d3705b... | 403587d2d8... | 94ac568dae... |
|    | 001d3e8d07... | 001d3e8d07... | cd7ee6056f... | 94ac568dae... | 99ed55b8b0... |
|    | 252d0446db... | 41f740a1b2... | 99ed55b8b0... | 99ed55b8b0... | f4372d2062... |
|    | 8d67f816fc... | f4372d2062... | f4372d2062... | f4372d2062... |               |
```
Another example is:
```python
import hashwire
hashwire.hash.mdp(13645)
>>[13645, 13639, 13599, 12999, 9999]
```
You can find more information in the `code examples`.

## Code examples
Examples how a sequence of digits can be presented with hashwire and how hash multichain is used.

Introduction to hashwire and hash chains is found here:

[Hashwire introduction](https://github.com/Hugloss/CryptoDetails/blob/main/Hashwire_01_basic.ipynb)

Example that generate the code above, when seed is known, is found here:
[Code in this readme file](https://github.com/Hugloss/CryptoDetails/blob/main/Hashwire_02_readme.ipynb)

Another example when seed is generated:
[Basic example](https://github.com/Hugloss/CryptoDetails/blob/main/Hashwire_03_lib.ipynb)