# Phiaton MS 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.1; 54 4.2; 60 3.6; 66 3.1; 72 2.9; 79 2.9; 87 2.8; 96 2.5; 106 2.3; 116 2.2; 128 2.1; 141 2.1; 155 2.2; 170 2.3; 187 2.4; 206 2.8; 227 3.1; 249 3.1; 274 3.2; 302 3.1; 332 3.0; 365 3.2; 402 3.7; 442 3.6; 486 4.0; 535 4.4; 588 4.6; 647 4.7; 712 4.2; 783 3.0; 861 2.0; 947 0.8; 1042 -0.5; 1146 -1.7; 1261 -2.1; 1387 -2.1; 1526 -1.4; 1678 -0.9; 1846 -0.9; 2031 1.1; 2234 3.3; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.54 | 6.3 dB  |
| Peaking | 274 Hz  | 0.74 | 2.4 dB  |
| Peaking | 648 Hz  | 1.31 | 4.6 dB  |
| Peaking | 1422 Hz | 1.09 | -5.8 dB |
| Peaking | 3357 Hz | 0.74 | 7.8 dB  |
| Peaking | 1947 Hz | 5.91 | -1.4 dB |
| Peaking | 2466 Hz | 4.32 | 1.9 dB  |
| Peaking | 3484 Hz | 2.66 | -1.2 dB |
| Peaking | 6248 Hz | 2.2  | 5.5 dB  |
| Peaking | 7422 Hz | 1.47 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20MS%20300/Phiaton%20MS%20300.png)