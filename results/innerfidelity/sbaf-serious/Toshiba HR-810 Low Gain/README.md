# Toshiba HR-810 Low Gain

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.6; 106 4.4; 116 3.6; 128 2.4; 141 1.5; 155 0.8; 170 0.3; 187 -0.1; 206 -0.4; 227 -0.4; 249 -0.4; 274 -0.4; 302 -0.3; 332 -0.2; 365 0.0; 402 0.1; 442 0.4; 486 0.5; 535 0.6; 588 0.9; 647 0.9; 712 0.8; 783 0.9; 861 0.6; 947 0.1; 1042 0.2; 1146 1.0; 1261 -1.1; 1387 -2.8; 1526 -3.2; 1678 -3.8; 1846 -3.5; 2031 -3.4; 2234 -4.1; 2457 -2.9; 2703 -2.7; 2973 -1.0; 3270 0.2; 3597 1.1; 3957 2.2; 4353 2.8; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Toshiba HR-810 Low Gain ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.33 | 7.8 dB  |
| Peaking | 632 Hz  | 0.65 | 7.6 dB  |
| Peaking | 1076 Hz | 0.12 | -7.4 dB |
| Peaking | 1133 Hz | 4.7  | 3.2 dB  |
| Peaking | 5210 Hz | 1.09 | 11.3 dB |
| Peaking | 18 Hz   | 1.8  | 1.8 dB  |
| Peaking | 81 Hz   | 0.64 | -1.8 dB |
| Peaking | 89 Hz   | 1.9  | 2.8 dB  |
| Peaking | 6440 Hz | 6.45 | 1.9 dB  |
| Peaking | 7627 Hz | 4.05 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Toshiba%20HR-810%20Low%20Gain/Toshiba%20HR-810%20Low%20Gain.png)