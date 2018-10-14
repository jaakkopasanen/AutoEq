# Thermaltake Isurus

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 21 -0.0; 23 -0.2; 25 -0.3; 28 -0.4; 31 -0.6; 34 -0.7; 37 -0.9; 41 -1.0; 45 -1.2; 49 -1.4; 54 -1.6; 60 -1.9; 66 -2.2; 72 -2.5; 79 -3.0; 87 -3.5; 96 -3.9; 106 -4.2; 116 -4.4; 128 -4.8; 141 -5.0; 155 -5.3; 170 -5.5; 187 -5.5; 206 -5.7; 227 -5.6; 249 -5.7; 274 -5.6; 302 -5.5; 332 -5.4; 365 -5.1; 402 -4.9; 442 -4.5; 486 -3.6; 535 -2.9; 588 -2.4; 647 -1.8; 712 -1.4; 783 -0.6; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.1; 1261 0.1; 1387 -0.3; 1526 -1.0; 1678 -1.4; 1846 -1.6; 2031 -1.6; 2234 -1.5; 2457 -0.8; 2703 -0.6; 2973 0.2; 3270 0.8; 3597 1.2; 3957 0.6; 4353 -1.4; 4788 -2.0; 5267 -2.8; 5793 -3.9; 6373 -4.9; 7010 -2.9; 7711 -1.6; 8482 -2.4; 9330 -3.3; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.9; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.4dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thermaltake Isurus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 159 Hz   | 0.59 | -5.0 dB |
| Peaking | 362 Hz   | 1.32 | -3.1 dB |
| Peaking | 1937 Hz  | 4.08 | -1.7 dB |
| Peaking | 6310 Hz  | 2.22 | -4.6 dB |
| Peaking | 21922 Hz | 2.16 | -0.9 dB |
| Peaking | 1004 Hz  | 3.04 | 0.9 dB  |
| Peaking | 3554 Hz  | 5.7  | 2.1 dB  |
| Peaking | 9255 Hz  | 4.98 | -4.2 dB |
| Peaking | 9547 Hz  | 1.88 | 1.4 dB  |
| Peaking | 22386 Hz | 1.55 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thermaltake%20Isurus/Thermaltake%20Isurus.png)