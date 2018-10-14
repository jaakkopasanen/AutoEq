# Focal Elear with Utopia Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.5; 37 5.2; 41 4.9; 45 4.7; 49 4.5; 54 4.2; 60 3.9; 66 3.6; 72 3.3; 79 2.9; 87 2.4; 96 1.9; 106 1.7; 116 1.5; 128 1.2; 141 0.9; 155 0.7; 170 0.8; 187 0.7; 206 0.6; 227 0.8; 249 0.7; 274 0.9; 302 0.9; 332 1.0; 365 1.2; 402 1.2; 442 1.4; 486 1.4; 535 1.3; 588 1.6; 647 1.4; 712 1.2; 783 1.2; 861 0.7; 947 0.3; 1042 -0.0; 1146 -0.6; 1261 -1.2; 1387 -1.5; 1526 -1.5; 1678 -1.6; 1846 -0.7; 2031 0.9; 2234 2.2; 2457 2.8; 2703 3.1; 2973 3.5; 3270 4.1; 3597 4.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear with Utopia Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.62 | 5.8 dB  |
| Peaking | 62 Hz   | 1.01 | 1.8 dB  |
| Peaking | 558 Hz  | 0.79 | 1.4 dB  |
| Peaking | 1469 Hz | 2.18 | -2.9 dB |
| Peaking | 4428 Hz | 1.12 | 6.7 dB  |
| Peaking | 1765 Hz | 7.68 | -1.1 dB |
| Peaking | 2378 Hz | 3.24 | 1.2 dB  |
| Peaking | 4499 Hz | 3.87 | -0.5 dB |
| Peaking | 6320 Hz | 2.92 | 4.9 dB  |
| Peaking | 7290 Hz | 1.56 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Elear%20with%20Utopia%20Pads/Focal%20Elear%20with%20Utopia%20Pads.png)