# Audio Technica ATH-AD900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.9; 72 5.5; 79 5.3; 87 5.2; 96 4.3; 106 3.7; 116 3.2; 128 2.4; 141 1.8; 155 1.3; 170 1.2; 187 1.3; 206 1.5; 227 1.4; 249 1.1; 274 1.1; 302 1.0; 332 1.0; 365 0.9; 402 0.9; 442 1.0; 486 0.8; 535 0.8; 588 0.9; 647 0.8; 712 0.7; 783 0.9; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -1.9; 1526 -2.8; 1678 -2.8; 1846 -1.1; 2031 0.3; 2234 1.3; 2457 2.2; 2703 1.7; 2973 1.2; 3270 1.9; 3597 -0.4; 3957 -3.7; 4353 -5.3; 4788 -3.9; 5267 -0.7; 5793 0.7; 6373 2.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.39 | 6.5 dB  |
| Peaking | 1605 Hz | 1.52 | -7.8 dB |
| Peaking | 2040 Hz | 0.64 | 5.6 dB  |
| Peaking | 4334 Hz | 3.22 | -7.7 dB |
| Peaking | 6648 Hz | 6.16 | 3.0 dB  |
| Peaking | 31 Hz   | 0.19 | 1.8 dB  |
| Peaking | 38 Hz   | 0.94 | -2.3 dB |
| Peaking | 151 Hz  | 1.78 | -1.7 dB |
| Peaking | 8673 Hz | 3.3  | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)