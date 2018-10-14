# Westone UM1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.5; 54 5.0; 60 4.5; 66 4.0; 72 3.5; 79 3.0; 87 2.4; 96 2.0; 106 1.5; 116 1.2; 128 0.8; 141 0.5; 155 0.2; 170 0.0; 187 -0.1; 206 -0.3; 227 -0.3; 249 -0.4; 274 -0.4; 302 -0.4; 332 -0.3; 365 -0.2; 402 -0.1; 442 0.2; 486 0.1; 535 0.2; 588 0.6; 647 0.7; 712 0.7; 783 0.8; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.7; 1387 -1.2; 1526 -1.6; 1678 -1.6; 1846 -1.1; 2031 -0.2; 2234 0.8; 2457 2.5; 2703 4.0; 2973 5.8; 3270 6.0; 3597 6.0; 3957 5.6; 4353 5.4; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.63 | 6.7 dB  |
| Peaking | 773 Hz  | 2.59 | 1.0 dB  |
| Peaking | 1742 Hz | 1.41 | -3.0 dB |
| Peaking | 3282 Hz | 1.45 | 6.5 dB  |
| Peaking | 5589 Hz | 2.64 | 5.1 dB  |
| Peaking | 21 Hz   | 0.34 | 1.9 dB  |
| Peaking | 31 Hz   | 1.44 | -2.4 dB |
| Peaking | 197 Hz  | 0.98 | -0.9 dB |
| Peaking | 6564 Hz | 7.15 | 2.3 dB  |
| Peaking | 7851 Hz | 2.22 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM1/Westone%20UM1.png)