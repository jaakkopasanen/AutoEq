# Sennheiser HD 429

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.0; 25 -0.1; 28 -0.4; 31 -0.5; 34 -0.7; 37 -0.7; 41 -0.8; 45 -0.8; 49 -0.7; 54 -0.8; 60 -0.9; 66 -0.9; 72 -0.8; 79 -0.5; 87 0.1; 96 1.3; 106 0.7; 116 -1.2; 128 -2.3; 141 -2.4; 155 -2.1; 170 -2.2; 187 -2.5; 206 -2.4; 227 -2.1; 249 -1.6; 274 -1.0; 302 -0.2; 332 0.6; 365 0.5; 402 0.1; 442 -0.1; 486 -0.2; 535 -0.6; 588 -0.6; 647 -0.8; 712 -0.9; 783 -0.5; 861 -0.3; 947 -0.0; 1042 -0.0; 1146 -0.3; 1261 -0.1; 1387 -0.5; 1526 -0.8; 1678 -0.6; 1846 0.4; 2031 1.7; 2234 3.6; 2457 4.1; 2703 4.6; 2973 5.4; 3270 5.8; 3597 5.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.96 | -0.6 dB |
| Peaking | 99 Hz   | 4.6  | 3.1 dB  |
| Peaking | 157 Hz  | 1.08 | -2.7 dB |
| Peaking | 1547 Hz | 2.32 | -2.4 dB |
| Peaking | 3921 Hz | 0.87 | 6.7 dB  |
| Peaking | 342 Hz  | 5.39 | 1.4 dB  |
| Peaking | 679 Hz  | 2.84 | -1.0 dB |
| Peaking | 3694 Hz | 7.4  | -1.3 dB |
| Peaking | 6323 Hz | 2.52 | 4.8 dB  |
| Peaking | 7507 Hz | 1.67 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)