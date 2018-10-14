# California Headphone Lorado

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.6; 41 4.5; 45 3.3; 49 2.4; 54 1.5; 60 0.4; 66 -0.3; 72 -0.5; 79 -0.9; 87 -2.2; 96 -2.8; 106 -2.3; 116 -2.4; 128 -3.0; 141 -3.2; 155 -3.2; 170 -2.7; 187 -3.3; 206 -3.7; 227 -3.2; 249 -2.8; 274 -2.1; 302 -1.3; 332 -0.6; 365 -0.2; 402 0.0; 442 0.2; 486 0.2; 535 0.4; 588 0.8; 647 0.9; 712 0.8; 783 1.0; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.9; 1526 -2.0; 1678 -3.2; 1846 -2.9; 2031 -1.9; 2234 -0.1; 2457 1.8; 2703 3.7; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 -1.9; 11289 -0.1; 12418 0.0; 13660 -1.3; 15026 -0.3; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `California Headphone Lorado ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.9  | 6.9 dB  |
| Peaking | 138 Hz   | 0.74 | -3.8 dB |
| Peaking | 1816 Hz  | 2.32 | -5.0 dB |
| Peaking | 3501 Hz  | 1.31 | 6.9 dB  |
| Peaking | 5952 Hz  | 4.27 | 4.5 dB  |
| Peaking | 17 Hz    | 1.95 | 1.0 dB  |
| Peaking | 230 Hz   | 3.72 | -1.4 dB |
| Peaking | 571 Hz   | 1.13 | 1.2 dB  |
| Peaking | 10129 Hz | 3.26 | -2.1 dB |
| Peaking | 16520 Hz | 2.15 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/California%20Headphone%20Lorado/California%20Headphone%20Lorado.png)