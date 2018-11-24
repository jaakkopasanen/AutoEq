# Sony WI-SP600N

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 -8.7; 23 -9.0; 25 -9.3; 28 -9.5; 31 -9.6; 34 -9.7; 37 -9.7; 41 -9.7; 45 -9.6; 49 -9.4; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.2; 79 -9.1; 87 -9.0; 96 -9.0; 106 -9.0; 116 -9.0; 128 -9.0; 141 -8.9; 155 -8.7; 170 -8.5; 187 -8.3; 206 -8.1; 227 -7.7; 249 -7.3; 274 -6.7; 302 -6.1; 332 -5.6; 365 -5.0; 402 -4.6; 442 -4.1; 486 -3.6; 535 -3.1; 588 -2.5; 647 -1.8; 712 -1.2; 783 -0.6; 861 -0.3; 947 -0.1; 1042 -0.1; 1146 -1.1; 1261 -2.2; 1387 -2.8; 1526 -2.9; 1678 -2.9; 1846 -2.9; 2031 -2.7; 2234 -1.9; 2457 -1.0; 2703 -0.7; 2973 -1.1; 3270 -1.7; 3597 -1.6; 3957 -0.5; 4353 0.5; 4788 1.6; 5267 2.8; 5793 0.9; 6373 -6.2; 7010 -1.3; 7711 0.3; 8482 0.0; 9330 -0.8; 10263 -9.0; 11289 -10.4; 12418 -3.7; 13660 0.0; 15026 0.0; 16529 -1.7; 18182 -6.4; 20000 -0.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP600N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP600N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.21 | -9.3 dB  |
| Peaking | 223 Hz   | 0.65 | -4.4 dB  |
| Peaking | 1754 Hz  | 1.99 | -3.0 dB  |
| Peaking | 10990 Hz | 4.83 | -12.4 dB |
| Peaking | 18257 Hz | 2.92 | -7.1 dB  |
| Peaking | 919 Hz   | 4.28 | 1.4 dB   |
| Peaking | 5488 Hz  | 4.19 | 5.4 dB   |
| Peaking | 6451 Hz  | 4.51 | -9.3 dB  |
| Peaking | 7313 Hz  | 3.41 | 3.8 dB   |
| Peaking | 14325 Hz | 3.69 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WI-SP600N/Sony%20WI-SP600N.png)