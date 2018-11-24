# KZ AS-10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.1; 28 -2.2; 31 -2.4; 34 -2.5; 37 -2.6; 41 -2.7; 45 -2.8; 49 -2.8; 54 -3.1; 60 -3.5; 66 -4.0; 72 -4.3; 79 -4.7; 87 -5.2; 96 -5.7; 106 -6.2; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.3; 206 -7.2; 227 -7.1; 249 -6.7; 274 -6.1; 302 -5.6; 332 -5.1; 365 -4.4; 402 -3.8; 442 -3.2; 486 -2.6; 535 -1.9; 588 -1.2; 647 -0.5; 712 0.1; 783 0.5; 861 0.7; 947 0.4; 1042 -0.4; 1146 -1.2; 1261 -2.2; 1387 -2.8; 1526 -3.5; 1678 -4.3; 1846 -5.3; 2031 -6.5; 2234 -7.4; 2457 -7.5; 2703 -6.4; 2973 -4.6; 3270 -4.1; 3597 -5.1; 3957 -6.8; 4353 -3.4; 4788 -4.7; 5267 -9.2; 5793 -6.6; 6373 -3.8; 7010 -1.3; 7711 0.3; 8482 0.0; 9330 -0.7; 10263 -2.4; 11289 -3.3; 12418 -5.4; 13660 -3.1; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 156 Hz   | 0.53 | -7.7 dB |
| Peaking | 2286 Hz  | 1.81 | -7.6 dB |
| Peaking | 3883 Hz  | 4.87 | -4.1 dB |
| Peaking | 5421 Hz  | 4.98 | -8.8 dB |
| Peaking | 12446 Hz | 3.51 | -5.8 dB |
| Peaking | 27 Hz    | 1.32 | -1.6 dB |
| Peaking | 333 Hz   | 1.73 | -0.9 dB |
| Peaking | 840 Hz   | 1.63 | 2.5 dB  |
| Peaking | 1398 Hz  | 2.24 | -1.4 dB |
| Peaking | 7881 Hz  | 6.9  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20AS-10/KZ%20AS-10.png)