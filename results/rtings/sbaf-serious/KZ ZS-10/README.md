# KZ ZS-10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.5; 28 1.1; 31 0.8; 34 0.5; 37 0.3; 41 0.0; 45 -0.2; 49 -0.4; 54 -0.7; 60 -1.2; 66 -1.5; 72 -1.8; 79 -2.1; 87 -2.4; 96 -2.9; 106 -3.5; 116 -4.1; 128 -4.6; 141 -5.0; 155 -5.2; 170 -5.3; 187 -5.5; 206 -5.5; 227 -5.4; 249 -5.0; 274 -4.5; 302 -3.9; 332 -3.4; 365 -2.8; 402 -2.2; 442 -1.7; 486 -1.0; 535 -0.3; 588 0.2; 647 0.8; 712 1.2; 783 1.3; 861 1.1; 947 0.6; 1042 -0.4; 1146 -1.3; 1261 -2.0; 1387 -2.9; 1526 -3.9; 1678 -4.8; 1846 -5.5; 2031 -6.3; 2234 -6.7; 2457 -6.2; 2703 -5.0; 2973 -4.1; 3270 -4.1; 3597 -4.7; 3957 -5.7; 4353 -3.3; 4788 1.6; 5267 0.9; 5793 -2.7; 6373 0.4; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -3.7; 10263 -4.1; 11289 -0.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  1.47 | 2.3 dB  |
| Peaking | 178 Hz   |  0.81 | -5.9 dB |
| Peaking | 2175 Hz  |  1.71 | -7.0 dB |
| Peaking | 3853 Hz  |  5.31 | -4.7 dB |
| Peaking | 22147 Hz |  1.79 | -2.3 dB |
| Peaking | 770 Hz   |  2.14 | 2.5 dB  |
| Peaking | 1482 Hz  |  3.27 | -1.3 dB |
| Peaking | 6817 Hz  | 12.25 | 3.8 dB  |
| Peaking | 9627 Hz  |  1.45 | 2.2 dB  |
| Peaking | 9850 Hz  |  3.89 | -7.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/KZ%20ZS-10/KZ%20ZS-10.png)