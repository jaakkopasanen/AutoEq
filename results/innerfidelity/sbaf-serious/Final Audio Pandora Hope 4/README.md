# Final Audio Pandora Hope 4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.5; 23 -3.6; 25 -3.7; 28 -3.7; 31 -3.6; 34 -3.5; 37 -3.4; 41 -3.1; 45 -2.7; 49 -2.3; 54 -2.2; 60 -2.8; 66 -3.4; 72 -3.8; 79 -3.7; 87 -3.0; 96 -2.1; 106 -0.8; 116 -1.4; 128 -3.5; 141 -3.4; 155 -2.3; 170 -1.3; 187 -2.4; 206 -2.3; 227 -2.1; 249 -2.4; 274 -2.1; 302 -1.7; 332 -1.3; 365 -1.3; 402 -0.9; 442 -0.7; 486 -0.7; 535 -0.6; 588 -0.0; 647 0.1; 712 -0.7; 783 -0.8; 861 -0.7; 947 -0.3; 1042 0.2; 1146 0.6; 1261 0.6; 1387 0.4; 1526 0.2; 1678 0.4; 1846 0.9; 2031 1.4; 2234 1.3; 2457 1.7; 2703 3.5; 2973 6.0; 3270 3.8; 3597 5.4; 3957 1.5; 4353 -0.5; 4788 1.6; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.4; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Pandora Hope 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.77 | -3.7 dB |
| Peaking | 74 Hz   | 3.27 | -2.5 dB |
| Peaking | 191 Hz  | 0.71 | -2.3 dB |
| Peaking | 3050 Hz | 2.96 | 5.6 dB  |
| Peaking | 5872 Hz | 3.96 | 6.6 dB  |
| Peaking | 109 Hz  | 7.63 | 1.7 dB  |
| Peaking | 131 Hz  | 7.98 | -1.8 dB |
| Peaking | 3679 Hz | 8.95 | 3.0 dB  |
| Peaking | 4206 Hz | 7.83 | -3.5 dB |
| Peaking | 9197 Hz | 6.35 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Pandora%20Hope%204/Final%20Audio%20Pandora%20Hope%204.png)