# ZMF Eikon

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -3.4; 23 -3.5; 25 -3.6; 28 -3.6; 31 -3.6; 34 -3.6; 37 -3.6; 41 -3.5; 45 -3.5; 49 -3.7; 54 -3.5; 60 -3.3; 66 -3.8; 72 -4.7; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.3; 116 -6.3; 128 -6.3; 141 -6.1; 155 -5.3; 170 -5.2; 187 -5.0; 206 -4.6; 227 -4.2; 249 -4.1; 274 -3.9; 302 -3.9; 332 -3.8; 365 -3.4; 402 -2.9; 442 -2.2; 486 -2.1; 535 -1.6; 588 -0.7; 647 -0.5; 712 -0.4; 783 -0.4; 861 -0.6; 947 -0.3; 1042 0.2; 1146 0.3; 1261 0.2; 1387 0.3; 1526 4.6; 1678 4.0; 1846 1.4; 2031 0.1; 2234 0.5; 2457 1.4; 2703 0.7; 2973 0.7; 3270 1.0; 3597 1.3; 3957 -1.1; 4353 -0.9; 4788 0.1; 5267 0.3; 5793 -3.5; 6373 4.6; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -1.9; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Eikon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.22 | -2.7 dB |
| Peaking | 129 Hz  | 0.45 | -6.0 dB |
| Peaking | 1597 Hz | 6.17 | 5.9 dB  |
| Peaking | 5905 Hz | 8.59 | -5.6 dB |
| Peaking | 6488 Hz | 7.09 | 6.6 dB  |
| Peaking | 361 Hz  | 3.84 | -0.9 dB |
| Peaking | 663 Hz  | 3.73 | 0.6 dB  |
| Peaking | 3736 Hz | 2.11 | 2.4 dB  |
| Peaking | 4076 Hz | 4.73 | -3.5 dB |
| Peaking | 9192 Hz | 8.88 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Eikon/ZMF%20Eikon.png)