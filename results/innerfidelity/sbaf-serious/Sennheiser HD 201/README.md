# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 5.8; 155 5.2; 170 4.9; 187 4.5; 206 4.4; 227 4.1; 249 3.4; 274 3.1; 302 2.6; 332 2.1; 365 1.6; 402 1.1; 442 0.7; 486 0.3; 535 0.4; 588 0.7; 647 0.8; 712 0.4; 783 -0.2; 861 -0.7; 947 -0.4; 1042 0.3; 1146 -0.1; 1261 0.2; 1387 -0.0; 1526 0.3; 1678 0.7; 1846 0.1; 2031 0.5; 2234 1.3; 2457 2.7; 2703 3.4; 2973 3.7; 3270 4.2; 3597 2.8; 3957 3.1; 4353 5.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.6; 9330 -3.8; 10263 -0.4; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.16 | 6.0 dB  |
| Peaking | 149 Hz  |  0.74 | 3.2 dB  |
| Peaking | 2870 Hz |  3.24 | 2.6 dB  |
| Peaking | 5425 Hz |  1.42 | 6.8 dB  |
| Peaking | 8830 Hz |  3.79 | -6.6 dB |
| Peaking | 268 Hz  |  3.05 | 0.4 dB  |
| Peaking | 472 Hz  |  4.73 | -0.7 dB |
| Peaking | 872 Hz  |  4.76 | -1.2 dB |
| Peaking | 4374 Hz | 12.13 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)