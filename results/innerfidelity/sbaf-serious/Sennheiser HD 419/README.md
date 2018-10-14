# Sennheiser HD 419

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.9; 23 -5.1; 25 -5.3; 28 -5.6; 31 -5.8; 34 -5.9; 37 -6.1; 41 -6.2; 45 -6.3; 49 -6.3; 54 -6.4; 60 -6.5; 66 -6.4; 72 -6.5; 79 -6.9; 87 -6.1; 96 -4.6; 106 -6.8; 116 -8.2; 128 -8.9; 141 -9.1; 155 -9.2; 170 -8.9; 187 -9.1; 206 -9.0; 227 -8.6; 249 -7.8; 274 -6.9; 302 -5.8; 332 -4.3; 365 -3.2; 402 -2.9; 442 -2.1; 486 -2.0; 535 -2.6; 588 -2.6; 647 -1.8; 712 -0.8; 783 -0.9; 861 -0.2; 947 0.1; 1042 0.0; 1146 -0.4; 1261 -0.2; 1387 -1.0; 1526 -1.5; 1678 -1.6; 1846 -1.4; 2031 -0.4; 2234 1.3; 2457 2.5; 2703 2.2; 2973 3.2; 3270 3.3; 3597 3.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.5; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.64 | -5.2 dB |
| Peaking | 65 Hz   | 1.43 | -3.0 dB |
| Peaking | 128 Hz  | 2.97 | -3.1 dB |
| Peaking | 203 Hz  | 0.89 | -8.4 dB |
| Peaking | 4698 Hz | 1.43 | 6.8 dB  |
| Peaking | 370 Hz  | 5.22 | 0.7 dB  |
| Peaking | 1787 Hz | 2.22 | -3.9 dB |
| Peaking | 2240 Hz | 1.21 | 2.4 dB  |
| Peaking | 6310 Hz | 3.79 | 5.1 dB  |
| Peaking | 6796 Hz | 1.33 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)