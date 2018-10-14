# Stax SR-X Mk3 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.2; 34 4.8; 37 4.4; 41 4.1; 45 3.8; 49 3.7; 54 3.5; 60 3.4; 66 3.2; 72 3.0; 79 2.7; 87 2.4; 96 2.1; 106 1.8; 116 1.7; 128 1.5; 141 1.3; 155 1.1; 170 1.0; 187 1.0; 206 0.8; 227 0.9; 249 0.9; 274 0.9; 302 0.9; 332 0.9; 365 1.0; 402 1.0; 442 1.0; 486 0.8; 535 0.4; 588 1.2; 647 0.9; 712 0.6; 783 0.7; 861 0.4; 947 0.0; 1042 0.1; 1146 0.2; 1261 0.0; 1387 0.6; 1526 0.8; 1678 1.2; 1846 2.1; 2031 2.0; 2234 1.5; 2457 0.5; 2703 -0.7; 2973 -1.8; 3270 -2.3; 3597 -3.1; 3957 -3.8; 4353 -3.3; 4788 -0.6; 5267 1.0; 5793 0.4; 6373 -1.2; 7010 -2.3; 7711 -2.3; 8482 -2.7; 9330 -1.6; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-X Mk3 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.28 | 5.6 dB  |
| Peaking | 63 Hz   | 0.07 | 0.8 dB  |
| Peaking | 1980 Hz | 3.29 | 2.4 dB  |
| Peaking | 3775 Hz | 2.93 | -4.0 dB |
| Peaking | 8125 Hz | 3.47 | -2.9 dB |
| Peaking | 2383 Hz | 5.55 | 0.1 dB  |
| Peaking | 2966 Hz | 5.6  | -1.4 dB |
| Peaking | 4387 Hz | 5.15 | -3.3 dB |
| Peaking | 5042 Hz | 1.64 | 2.9 dB  |
| Peaking | 6632 Hz | 3.67 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-X%20Mk3%20Pro/Stax%20SR-X%20Mk3%20Pro.png)