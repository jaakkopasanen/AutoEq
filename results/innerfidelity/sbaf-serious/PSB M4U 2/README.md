# PSB M4U 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 0.0; 25 -1.1; 28 -1.6; 31 -1.1; 34 -0.4; 37 0.2; 41 0.8; 45 1.2; 49 1.5; 54 1.8; 60 1.9; 66 2.0; 72 2.2; 79 2.4; 87 2.1; 96 1.0; 106 0.2; 116 0.1; 128 0.1; 141 0.0; 155 0.1; 170 0.4; 187 0.0; 206 0.3; 227 0.7; 249 1.0; 274 1.5; 302 2.0; 332 2.5; 365 2.8; 402 3.2; 442 3.9; 486 3.6; 535 3.5; 588 3.4; 647 3.3; 712 2.8; 783 2.3; 861 1.5; 947 0.7; 1042 -0.3; 1146 -0.7; 1261 -1.4; 1387 -2.6; 1526 -3.6; 1678 -3.7; 1846 -3.0; 2031 -2.0; 2234 -1.4; 2457 -0.3; 2703 0.6; 2973 1.0; 3270 0.4; 3597 -0.2; 3957 0.0; 4353 1.0; 4788 1.7; 5267 3.4; 5793 5.3; 6373 4.3; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -0.2; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 2.06 | 2.5 dB  |
| Peaking | 527 Hz  | 0.99 | 4.1 dB  |
| Peaking | 1615 Hz | 1.68 | -4.3 dB |
| Peaking | 2813 Hz | 4.68 | 1.6 dB  |
| Peaking | 5889 Hz | 3.47 | 5.6 dB  |
| Peaking | 16 Hz   | 0.63 | 4.4 dB  |
| Peaking | 26 Hz   | 2.07 | -4.7 dB |
| Peaking | 136 Hz  | 1.49 | -0.7 dB |
| Peaking | 781 Hz  | 5.98 | 0.4 dB  |
| Peaking | 8739 Hz | 5.63 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202/PSB%20M4U%202.png)