# Audeze LCD-4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.7; 25 4.6; 28 4.4; 31 4.3; 34 4.2; 37 4.1; 41 4.0; 45 3.9; 49 3.8; 54 3.6; 60 3.4; 66 3.2; 72 3.0; 79 2.7; 87 2.4; 96 2.0; 106 1.8; 116 1.6; 128 1.3; 141 1.1; 155 0.9; 170 0.8; 187 0.7; 206 0.6; 227 0.7; 249 0.6; 274 0.5; 302 0.4; 332 0.3; 365 0.4; 402 0.3; 442 0.1; 486 -0.0; 535 0.0; 588 0.2; 647 0.1; 712 0.1; 783 0.2; 861 -0.0; 947 0.2; 1042 0.1; 1146 -0.2; 1261 -0.2; 1387 -0.5; 1526 -1.2; 1678 -1.1; 1846 -0.6; 2031 -0.4; 2234 -0.1; 2457 1.4; 2703 2.0; 2973 3.2; 3270 5.0; 3597 4.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.2; 6373 3.9; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -3.6; 20000 -7.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.58 | 4.2 dB  |
| Peaking | 59 Hz    | 0.66 | 2.4 dB  |
| Peaking | 279 Hz   | 1.71 | 0.2 dB  |
| Peaking | 1767 Hz  | 1.94 | -2.0 dB |
| Peaking | 4357 Hz  | 1.27 | 6.8 dB  |
| Peaking | 3240 Hz  | 7.27 | 1.4 dB  |
| Peaking | 4557 Hz  | 1.61 | -2.0 dB |
| Peaking | 6025 Hz  | 1.41 | 3.4 dB  |
| Peaking | 7873 Hz  | 1.98 | -2.8 dB |
| Peaking | 19664 Hz | 2    | -7.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-4/Audeze%20LCD-4.png)