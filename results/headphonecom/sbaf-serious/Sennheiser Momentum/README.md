# Sennheiser Momentum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 3.1; 28 2.8; 31 2.6; 34 2.4; 37 2.3; 41 2.1; 45 1.9; 49 1.8; 54 1.6; 60 1.2; 66 1.1; 72 0.8; 79 0.4; 87 0.2; 96 0.0; 106 -0.2; 116 -0.1; 128 -0.1; 141 -0.3; 155 -1.0; 170 -0.8; 187 -1.0; 206 -1.2; 227 -1.1; 249 -1.0; 274 -0.4; 302 -0.3; 332 0.4; 365 1.2; 402 1.5; 442 1.6; 486 1.7; 535 1.6; 588 1.6; 647 1.2; 712 0.7; 783 0.5; 861 0.3; 947 0.1; 1042 0.0; 1146 0.2; 1261 -0.2; 1387 -1.0; 1526 -1.5; 1678 -1.4; 1846 -1.3; 2031 -0.3; 2234 1.3; 2457 3.3; 2703 5.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.34 | 3.4 dB  |
| Peaking | 47 Hz   | 2    | 1.4 dB  |
| Peaking | 504 Hz  | 2.39 | 1.9 dB  |
| Peaking | 1750 Hz | 1.94 | -4.1 dB |
| Peaking | 3748 Hz | 0.86 | 7.2 dB  |
| Peaking | 203 Hz  | 2    | -1.4 dB |
| Peaking | 2797 Hz | 5.87 | 1.5 dB  |
| Peaking | 3807 Hz | 2.56 | -1.0 dB |
| Peaking | 6264 Hz | 2.38 | 5.4 dB  |
| Peaking | 7365 Hz | 1.5  | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)