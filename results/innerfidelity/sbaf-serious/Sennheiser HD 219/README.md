# Sennheiser HD 219

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.6; 28 1.7; 31 0.9; 34 0.3; 37 -0.4; 41 -1.1; 45 -1.7; 49 -2.2; 54 -2.8; 60 -3.3; 66 -3.8; 72 -4.2; 79 -4.4; 87 -4.7; 96 -5.0; 106 -5.1; 116 -5.1; 128 -4.8; 141 -4.3; 155 -4.0; 170 -3.9; 187 -3.7; 206 -2.9; 227 -2.1; 249 -2.0; 274 -1.4; 302 -0.1; 332 1.0; 365 1.7; 402 1.9; 442 2.2; 486 1.9; 535 1.6; 588 1.5; 647 1.3; 712 1.6; 783 1.7; 861 0.9; 947 0.3; 1042 -0.1; 1146 -0.1; 1261 0.1; 1387 0.3; 1526 0.8; 1678 -0.5; 1846 -1.2; 2031 -0.7; 2234 -0.2; 2457 0.5; 2703 0.5; 2973 0.6; 3270 0.5; 3597 0.5; 3957 0.1; 4353 -1.7; 4788 -0.7; 5267 2.7; 5793 5.0; 6373 5.3; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -0.3; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.6  | 5.8 dB  |
| Peaking | 134 Hz  | 0.34 | -3.6 dB |
| Peaking | 235 Hz  | 0.19 | -3.1 dB |
| Peaking | 422 Hz  | 0.62 | 6.7 dB  |
| Peaking | 6127 Hz | 4.9  | 6.3 dB  |
| Peaking | 1581 Hz | 5.2  | 1.8 dB  |
| Peaking | 1770 Hz | 4.09 | -2.0 dB |
| Peaking | 4385 Hz | 1.08 | 1.6 dB  |
| Peaking | 4455 Hz | 4.85 | -4.0 dB |
| Peaking | 8552 Hz | 5.72 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)