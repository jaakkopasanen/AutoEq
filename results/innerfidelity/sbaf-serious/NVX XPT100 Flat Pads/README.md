# NVX XPT100 Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.7; 28 5.2; 31 4.9; 34 4.5; 37 4.2; 41 3.9; 45 3.7; 49 3.6; 54 3.4; 60 3.0; 66 2.7; 72 2.4; 79 2.0; 87 1.6; 96 1.2; 106 1.1; 116 1.2; 128 1.2; 141 0.5; 155 -0.2; 170 0.6; 187 0.0; 206 0.0; 227 0.7; 249 2.0; 274 3.9; 302 5.0; 332 4.1; 365 3.0; 402 2.3; 442 1.9; 486 1.1; 535 0.9; 588 1.0; 647 0.9; 712 0.6; 783 0.9; 861 0.9; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.9; 1526 -3.1; 1678 -3.5; 1846 -4.2; 2031 -4.2; 2234 -3.9; 2457 -2.9; 2703 -2.6; 2973 -0.2; 3270 1.5; 3597 -1.0; 3957 -1.0; 4353 0.1; 4788 1.6; 5267 4.1; 5793 5.8; 6373 4.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.79 | 5.8 dB  |
| Peaking | 56 Hz   | 1.31 | 1.8 dB  |
| Peaking | 319 Hz  | 2.33 | 4.8 dB  |
| Peaking | 1971 Hz | 1.91 | -4.8 dB |
| Peaking | 5870 Hz | 3.45 | 6.2 dB  |
| Peaking | 203 Hz  | 4.41 | -1.3 dB |
| Peaking | 788 Hz  | 1.38 | 0.9 dB  |
| Peaking | 1492 Hz | 7.17 | -0.9 dB |
| Peaking | 3164 Hz | 7.15 | 5.5 dB  |
| Peaking | 3271 Hz | 2.66 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100%20Flat%20Pads/NVX%20XPT100%20Flat%20Pads.png)