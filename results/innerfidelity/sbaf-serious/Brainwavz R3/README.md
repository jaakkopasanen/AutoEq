# Brainwavz R3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.7; 28 3.4; 31 3.2; 34 3.0; 37 2.8; 41 2.5; 45 2.3; 49 2.0; 54 1.7; 60 1.3; 66 0.9; 72 0.4; 79 0.0; 87 -0.5; 96 -1.0; 106 -1.3; 116 -1.7; 128 -2.0; 141 -2.4; 155 -2.6; 170 -2.8; 187 -2.8; 206 -3.0; 227 -2.9; 249 -3.0; 274 -2.8; 302 -2.7; 332 -2.6; 365 -2.3; 402 -2.1; 442 -1.7; 486 -1.5; 535 -1.2; 588 -0.7; 647 -0.4; 712 -0.2; 783 0.2; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 0.4; 1387 -0.6; 1526 -1.0; 1678 -1.6; 1846 -2.0; 2031 -2.0; 2234 -0.9; 2457 2.2; 2703 5.5; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.4; 4788 5.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz R3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.35 | 4.1 dB  |
| Peaking | 199 Hz   | 0.58 | -3.4 dB |
| Peaking | 2043 Hz  | 2.09 | -6.2 dB |
| Peaking | 3039 Hz  | 1.18 | 7.8 dB  |
| Peaking | 5714 Hz  | 3.16 | 4.7 dB  |
| Peaking | 807 Hz   | 2.96 | 0.7 dB  |
| Peaking | 1513 Hz  | 6.52 | -0.5 dB |
| Peaking | 6566 Hz  | 8.13 | 1.9 dB  |
| Peaking | 7723 Hz  | 3.6  | -1.4 dB |
| Peaking | 10020 Hz | 1.74 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20R3/Brainwavz%20R3.png)