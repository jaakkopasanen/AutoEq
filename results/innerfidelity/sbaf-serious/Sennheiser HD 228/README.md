# Sennheiser HD 228

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.5; 28 2.6; 31 1.8; 34 1.1; 37 0.6; 41 0.0; 45 -0.6; 49 -1.1; 54 -1.7; 60 -2.4; 66 -3.0; 72 -3.5; 79 -4.1; 87 -4.5; 96 -5.1; 106 -5.1; 116 -4.7; 128 -4.8; 141 -6.0; 155 -6.8; 170 -6.6; 187 -6.9; 206 -6.5; 227 -6.0; 249 -6.2; 274 -4.6; 302 -3.3; 332 -3.4; 365 -2.8; 402 -1.8; 442 -1.2; 486 -0.7; 535 -0.0; 588 0.6; 647 0.8; 712 0.7; 783 0.7; 861 0.3; 947 0.1; 1042 0.1; 1146 0.4; 1261 0.9; 1387 1.4; 1526 1.3; 1678 0.1; 1846 1.0; 2031 1.5; 2234 2.2; 2457 3.4; 2703 3.7; 2973 5.4; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.5; 4788 -1.0; 5267 -2.3; 5793 1.3; 6373 2.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -4.3; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.01 | 5.5 dB  |
| Peaking | 91 Hz    | 0.84 | -3.8 dB |
| Peaking | 203 Hz   | 1.21 | -5.9 dB |
| Peaking | 3344 Hz  | 1.81 | 6.6 dB  |
| Peaking | 18576 Hz | 2.57 | -4.9 dB |
| Peaking | 656 Hz   | 2.58 | 1.4 dB  |
| Peaking | 4268 Hz  | 6.64 | 4.0 dB  |
| Peaking | 5008 Hz  | 4.91 | -6.2 dB |
| Peaking | 6655 Hz  | 3.17 | 3.7 dB  |
| Peaking | 7760 Hz  | 3.21 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)