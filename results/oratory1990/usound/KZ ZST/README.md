# KZ ZST

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.0; 23 -3.2; 25 -3.4; 28 -3.6; 31 -3.7; 34 -3.8; 37 -3.9; 41 -4.0; 45 -4.0; 49 -4.1; 54 -4.1; 60 -4.2; 66 -4.3; 72 -4.3; 79 -4.4; 87 -4.5; 96 -4.5; 106 -4.5; 116 -4.4; 128 -4.1; 141 -3.9; 155 -3.9; 170 -4.3; 187 -3.9; 206 -3.4; 227 -3.0; 249 -2.6; 274 -2.2; 302 -1.8; 332 -1.4; 365 -1.1; 402 -0.8; 442 -0.5; 486 -0.2; 535 0.1; 588 0.2; 647 0.4; 712 0.7; 783 0.7; 861 0.3; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.6; 1387 -2.3; 1526 -2.9; 1678 -3.8; 1846 -4.5; 2031 -4.7; 2234 -3.9; 2457 -2.9; 2703 -1.5; 2973 -1.3; 3270 -2.0; 3597 -1.1; 3957 3.2; 4353 6.0; 4788 4.1; 5267 -1.5; 5793 -1.4; 6373 -3.3; 7010 -4.8; 7711 -1.2; 8482 0.0; 9330 -0.0; 10263 -4.7; 11289 -8.9; 12418 -8.7; 13660 -7.2; 15026 -3.8; 16529 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 71 Hz    | 0.33 | -4.7 dB  |
| Peaking | 1978 Hz  | 1.89 | -4.9 dB  |
| Peaking | 4390 Hz  | 6.05 | 7.8 dB   |
| Peaking | 6732 Hz  | 6.74 | -4.9 dB  |
| Peaking | 12336 Hz | 2.27 | -10.0 dB |
| Peaking | 189 Hz   | 2.78 | -1.0 dB  |
| Peaking | 688 Hz   | 1.6  | 1.4 dB   |
| Peaking | 8798 Hz  | 3.05 | 5.2 dB   |
| Peaking | 9722 Hz  | 1.16 | -2.7 dB  |
| Peaking | 16736 Hz | 3.7  | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZST/KZ%20ZST.png)