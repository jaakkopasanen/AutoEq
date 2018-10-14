# Apple iPod Ear Buds sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 5.7; 170 4.3; 187 3.0; 206 1.9; 227 0.9; 249 0.1; 274 -0.5; 302 -0.8; 332 -0.9; 365 -0.7; 402 -0.4; 442 0.0; 486 0.1; 535 0.1; 588 0.3; 647 0.1; 712 -0.1; 783 0.1; 861 -0.0; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.0; 1387 -0.5; 1526 -1.0; 1678 -1.3; 1846 -1.2; 2031 -0.4; 2234 0.7; 2457 0.3; 2703 -2.2; 2973 -5.1; 3270 -4.4; 3597 -1.5; 3957 -0.5; 4353 -1.6; 4788 -1.9; 5267 -1.5; 5793 -2.6; 6373 -4.5; 7010 -2.8; 7711 -2.0; 8482 -2.2; 9330 -0.4; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.19 | 6.6 dB  |
| Peaking | 251 Hz  | 2.37 | -2.6 dB |
| Peaking | 355 Hz  | 1.04 | -3.2 dB |
| Peaking | 3080 Hz | 5.49 | -5.6 dB |
| Peaking | 6465 Hz | 2.36 | -3.9 dB |
| Peaking | 16 Hz   | 1.26 | 1.2 dB  |
| Peaking | 44 Hz   | 0.34 | -0.6 dB |
| Peaking | 142 Hz  | 3.46 | 1.4 dB  |
| Peaking | 1714 Hz | 2.83 | -1.4 dB |
| Peaking | 2324 Hz | 7.08 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds%20sample%20B/Apple%20iPod%20Ear%20Buds%20sample%20B.png)