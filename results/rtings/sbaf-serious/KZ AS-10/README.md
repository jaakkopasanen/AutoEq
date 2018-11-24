# KZ AS-10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.9; 28 -2.1; 31 -2.3; 34 -2.5; 37 -2.7; 41 -2.9; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.8; 66 -4.1; 72 -4.3; 79 -4.5; 87 -4.8; 96 -5.2; 106 -5.7; 116 -6.1; 128 -6.5; 141 -6.8; 155 -6.8; 170 -6.7; 187 -6.7; 206 -6.7; 227 -6.6; 249 -6.1; 274 -5.4; 302 -4.7; 332 -4.1; 365 -3.4; 402 -2.8; 442 -2.1; 486 -1.4; 535 -0.7; 588 -0.1; 647 0.5; 712 1.0; 783 1.0; 861 0.9; 947 0.5; 1042 -0.3; 1146 -1.0; 1261 -1.9; 1387 -2.8; 1526 -3.9; 1678 -4.7; 1846 -5.3; 2031 -6.0; 2234 -6.9; 2457 -7.1; 2703 -5.6; 2973 -3.1; 3270 -1.5; 3597 -1.9; 3957 -4.4; 4353 -2.1; 4788 -3.1; 5267 -6.3; 5793 -2.7; 6373 -0.0; 7010 1.6; 7711 0.3; 8482 0.0; 9330 -1.8; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 58 Hz   |  0.51 | -2.9 dB |
| Peaking | 145 Hz  |  1.09 | -4.7 dB |
| Peaking | 255 Hz  |  1.6  | -4.0 dB |
| Peaking | 2222 Hz |  1.68 | -7.2 dB |
| Peaking | 5260 Hz |  6.39 | -5.9 dB |
| Peaking | 794 Hz  |  2.34 | 2.1 dB  |
| Peaking | 1504 Hz |  4.46 | -1.4 dB |
| Peaking | 4020 Hz | 12.98 | -3.0 dB |
| Peaking | 6975 Hz |  5.45 | 2.3 dB  |
| Peaking | 9668 Hz |  8.66 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/KZ%20AS-10/KZ%20AS-10.png)