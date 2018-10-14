# Superlux HD 681

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.8; 31 3.8; 34 3.0; 37 2.3; 41 1.6; 45 1.0; 49 0.6; 54 0.1; 60 -0.3; 66 -0.3; 72 -0.2; 79 -0.5; 87 -0.5; 96 -0.4; 106 -0.9; 116 -1.3; 128 -1.7; 141 -1.9; 155 -2.0; 170 -1.7; 187 -1.1; 206 -0.6; 227 -1.2; 249 -1.3; 274 -1.1; 302 -0.9; 332 -0.7; 365 -0.5; 402 -0.4; 442 -0.2; 486 -0.3; 535 -0.3; 588 -0.0; 647 1.0; 712 0.4; 783 0.5; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.7; 1261 -1.5; 1387 -2.5; 1526 -3.6; 1678 -4.1; 1846 -5.0; 2031 -5.7; 2234 -6.3; 2457 -5.8; 2703 -5.0; 2973 -4.1; 3270 -3.0; 3597 -1.5; 3957 -0.3; 4353 -2.4; 4788 -4.6; 5267 -4.5; 5793 -4.5; 6373 -2.6; 7010 -1.9; 7711 -7.2; 8482 -10.2; 9330 -9.8; 10263 -7.5; 11289 -1.5; 12418 0.0; 13660 -1.0; 15026 -3.0; 16529 -0.1; 18182 0.0; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.4  | 6.4 dB   |
| Peaking | 148 Hz   | 1    | -1.9 dB  |
| Peaking | 2191 Hz  | 1.64 | -6.4 dB  |
| Peaking | 5289 Hz  | 4.22 | -3.6 dB  |
| Peaking | 8956 Hz  | 2.78 | -11.1 dB |
| Peaking | 764 Hz   | 2.49 | 1.2 dB   |
| Peaking | 11754 Hz | 8.52 | 2.1 dB   |
| Peaking | 13120 Hz | 5.55 | 1.7 dB   |
| Peaking | 14753 Hz | 4.67 | -3.0 dB  |
| Peaking | 19911 Hz | 5.07 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)