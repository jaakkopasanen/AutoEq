# V-Moda M-80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.6; 28 0.0; 31 -0.5; 34 -0.8; 37 -1.1; 41 -1.5; 45 -1.7; 49 -1.9; 54 -2.2; 60 -2.4; 66 -2.6; 72 -2.6; 79 -2.6; 87 -2.8; 96 -3.0; 106 -2.7; 116 -2.7; 128 -2.8; 141 -2.9; 155 -2.9; 170 -2.8; 187 -2.6; 206 -2.4; 227 -2.7; 249 -2.8; 274 -1.8; 302 -0.8; 332 -0.4; 365 0.2; 402 0.9; 442 1.5; 486 2.5; 535 3.6; 588 4.2; 647 4.0; 712 3.6; 783 2.9; 861 1.9; 947 0.7; 1042 -0.5; 1146 -1.7; 1261 -2.8; 1387 -3.3; 1526 -3.4; 1678 -3.0; 1846 -1.3; 2031 0.1; 2234 1.0; 2457 1.5; 2703 1.1; 2973 0.2; 3270 -0.8; 3597 -0.2; 3957 1.7; 4353 2.0; 4788 1.9; 5267 4.3; 5793 4.7; 6373 3.9; 7010 2.5; 7711 0.3; 8482 -0.3; 9330 -0.6; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.85 | -2.3 dB |
| Peaking | 210 Hz  | 0.81 | -2.7 dB |
| Peaking | 614 Hz  | 1.25 | 5.0 dB  |
| Peaking | 1379 Hz | 2.35 | -4.6 dB |
| Peaking | 5695 Hz | 2.73 | 5.1 dB  |
| Peaking | 19 Hz   | 2.16 | 2.1 dB  |
| Peaking | 1686 Hz | 5.17 | -1.7 dB |
| Peaking | 2526 Hz | 1.39 | 1.7 dB  |
| Peaking | 3336 Hz | 5.63 | -2.4 dB |
| Peaking | 8828 Hz | 5.15 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20M-80/V-Moda%20M-80.png)