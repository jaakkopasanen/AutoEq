# Bowers & Wilkins P7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 0.3; 25 0.0; 28 -0.4; 31 -0.7; 34 -1.0; 37 -1.2; 41 -1.3; 45 -1.4; 49 -1.6; 54 -1.4; 60 -1.5; 66 -2.1; 72 -2.4; 79 -2.5; 87 -2.4; 96 -2.1; 106 -1.1; 116 -0.6; 128 -1.2; 141 -2.0; 155 -2.0; 170 -0.8; 187 -1.4; 206 -0.8; 227 -0.2; 249 0.5; 274 1.2; 302 1.7; 332 1.9; 365 2.1; 402 2.0; 442 2.2; 486 2.1; 535 2.0; 588 2.2; 647 2.0; 712 1.3; 783 0.6; 861 -0.0; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.5; 1387 -2.7; 1526 -3.6; 1678 -4.3; 1846 -4.3; 2031 -3.9; 2234 -3.2; 2457 -1.3; 2703 2.0; 2973 4.0; 3270 3.8; 3597 1.6; 3957 0.1; 4353 0.2; 4788 1.2; 5267 2.6; 5793 1.8; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 143 Hz  | 0.32 | -2.6 dB |
| Peaking | 412 Hz  | 0.64 | 4.1 dB  |
| Peaking | 1883 Hz | 1.28 | -5.5 dB |
| Peaking | 3013 Hz | 3.16 | 6.4 dB  |
| Peaking | 6423 Hz | 4.66 | 5.0 dB  |
| Peaking | 17 Hz   | 1.67 | 1.8 dB  |
| Peaking | 110 Hz  | 1.41 | -1.6 dB |
| Peaking | 112 Hz  | 3.48 | 2.9 dB  |
| Peaking | 5145 Hz | 5.88 | 3.0 dB  |
| Peaking | 5228 Hz | 1.8  | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)