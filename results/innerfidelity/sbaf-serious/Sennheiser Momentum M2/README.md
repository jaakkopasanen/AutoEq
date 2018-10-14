# Sennheiser Momentum M2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.3; 28 4.7; 31 4.2; 34 3.8; 37 3.5; 41 3.2; 45 2.8; 49 2.6; 54 2.3; 60 2.0; 66 1.7; 72 1.4; 79 1.3; 87 0.9; 96 0.7; 106 0.7; 116 0.7; 128 0.8; 141 1.0; 155 0.7; 170 1.2; 187 1.3; 206 1.4; 227 1.4; 249 2.2; 274 1.7; 302 1.2; 332 1.4; 365 1.2; 402 1.1; 442 1.1; 486 0.6; 535 0.2; 588 0.4; 647 0.3; 712 0.0; 783 0.0; 861 -0.0; 947 -0.2; 1042 -0.1; 1146 0.1; 1261 -0.6; 1387 -0.3; 1526 -1.6; 1678 -1.9; 1846 -2.3; 2031 -1.7; 2234 -0.4; 2457 1.3; 2703 2.5; 2973 4.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 2.5; 5267 3.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.49 | 6.1 dB  |
| Peaking | 266 Hz  | 1.12 | 1.7 dB  |
| Peaking | 1881 Hz | 2.11 | -3.5 dB |
| Peaking | 3557 Hz | 1.65 | 6.8 dB  |
| Peaking | 6060 Hz | 4.8  | 5.1 dB  |
| Peaking | 6706 Hz | 9.22 | 1.6 dB  |
| Peaking | 7910 Hz | 2.35 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2/Sennheiser%20Momentum%20M2.png)