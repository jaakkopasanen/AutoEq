# Shure SE846 Blue Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.4; 23 -4.4; 25 -4.4; 28 -4.4; 31 -4.4; 34 -4.4; 37 -4.4; 41 -4.4; 45 -4.3; 49 -4.3; 54 -4.3; 60 -4.4; 66 -4.4; 72 -4.4; 79 -4.4; 87 -4.4; 96 -4.3; 106 -4.2; 116 -4.1; 128 -4.0; 141 -3.9; 155 -3.7; 170 -3.5; 187 -3.3; 206 -3.1; 227 -2.8; 249 -2.6; 274 -2.4; 302 -2.0; 332 -1.7; 365 -1.5; 402 -1.2; 442 -1.1; 486 -0.9; 535 -0.6; 588 -0.4; 647 0.1; 712 0.3; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.6; 1387 -1.0; 1526 -1.5; 1678 -1.7; 1846 -1.4; 2031 -1.0; 2234 -0.1; 2457 1.6; 2703 4.2; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.2  | -4.6 dB |
| Peaking | 1921 Hz | 1.91 | -2.9 dB |
| Peaking | 3100 Hz | 2.11 | 5.8 dB  |
| Peaking | 4546 Hz | 2.27 | 4.5 dB  |
| Peaking | 6015 Hz | 4.07 | 4.4 dB  |
| Peaking | 763 Hz  | 2.38 | 0.9 dB  |
| Peaking | 1458 Hz | 5.58 | -0.5 dB |
| Peaking | 8248 Hz | 4.05 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Blue%20Filter/Shure%20SE846%20Blue%20Filter.png)