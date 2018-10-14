# Bloc Roc Galvanize S2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 1.3; 25 0.4; 28 -0.9; 31 -2.0; 34 -3.0; 37 -3.9; 41 -4.9; 45 -5.7; 49 -6.3; 54 -6.9; 60 -7.4; 66 -7.5; 72 -7.7; 79 -7.6; 87 -7.2; 96 -7.0; 106 -7.3; 116 -7.3; 128 -7.3; 141 -7.2; 155 -7.0; 170 -6.5; 187 -6.4; 206 -6.1; 227 -5.4; 249 -4.8; 274 -4.1; 302 -4.3; 332 -4.2; 365 -3.6; 402 -3.1; 442 -2.7; 486 -2.5; 535 -1.7; 588 -0.4; 647 0.7; 712 1.2; 783 1.2; 861 0.9; 947 0.3; 1042 -0.2; 1146 -1.0; 1261 -1.5; 1387 -2.8; 1526 -4.2; 1678 -5.0; 1846 -4.5; 2031 -4.1; 2234 -3.2; 2457 -1.7; 2703 0.0; 2973 1.4; 3270 1.0; 3597 3.2; 3957 3.5; 4353 2.7; 4788 -2.0; 5267 -1.9; 5793 -0.7; 6373 -0.5; 7010 0.1; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bloc Roc Galvanize S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.92 | 5.2 dB  |
| Peaking | 62 Hz   | 0.49 | -7.4 dB |
| Peaking | 199 Hz  | 0.8  | -3.8 dB |
| Peaking | 1787 Hz | 2.48 | -5.4 dB |
| Peaking | 3764 Hz | 4.73 | 4.5 dB  |
| Peaking | 478 Hz  | 1.68 | -1.9 dB |
| Peaking | 710 Hz  | 1.63 | 2.9 dB  |
| Peaking | 1422 Hz | 4.36 | -1.1 dB |
| Peaking | 4322 Hz | 8.27 | 3.0 dB  |
| Peaking | 4912 Hz | 4.07 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bloc%20Roc%20Galvanize%20S2/Bloc%20Roc%20Galvanize%20S2.png)