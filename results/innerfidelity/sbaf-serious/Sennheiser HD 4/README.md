# Sennheiser HD 4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.5; 31 4.8; 34 4.2; 37 3.6; 41 3.1; 45 2.7; 49 2.4; 54 2.0; 60 1.6; 66 1.2; 72 0.9; 79 0.5; 87 0.2; 96 -0.1; 106 -0.4; 116 -0.5; 128 -0.5; 141 -0.8; 155 -1.5; 170 -0.5; 187 -1.1; 206 -1.4; 227 -1.2; 249 -0.8; 274 -0.5; 302 -0.1; 332 0.3; 365 0.8; 402 1.0; 442 0.8; 486 0.3; 535 0.3; 588 0.6; 647 0.5; 712 0.3; 783 0.5; 861 0.3; 947 0.2; 1042 -0.0; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.4; 1678 -2.0; 1846 -1.8; 2031 -1.2; 2234 -0.6; 2457 0.9; 2703 2.6; 2973 4.3; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 1.7; 5267 1.1; 5793 3.7; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  1.47 | 6.1 dB  |
| Peaking | 43 Hz   |  1.98 | 1.8 dB  |
| Peaking | 1837 Hz |  2.19 | -2.9 dB |
| Peaking | 3597 Hz |  1.94 | 6.9 dB  |
| Peaking | 6353 Hz |  6.97 | 4.9 dB  |
| Peaking | 233 Hz  |  0.93 | -2.5 dB |
| Peaking | 340 Hz  |  0.93 | 2.0 dB  |
| Peaking | 4463 Hz |  8.83 | 2.8 dB  |
| Peaking | 4935 Hz | 11.15 | -4.0 dB |
| Peaking | 8437 Hz |  4.44 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%204/Sennheiser%20HD%204.png)