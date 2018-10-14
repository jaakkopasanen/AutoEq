# Sennheiser HD 229

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.7; 28 3.8; 31 3.0; 34 2.3; 37 1.7; 41 0.9; 45 0.3; 49 -0.3; 54 -0.9; 60 -1.5; 66 -2.0; 72 -2.5; 79 -2.9; 87 -3.5; 96 -3.9; 106 -4.1; 116 -4.0; 128 -3.9; 141 -3.8; 155 -4.3; 170 -3.7; 187 -3.4; 206 -2.7; 227 -2.4; 249 -2.7; 274 -1.9; 302 -0.6; 332 0.2; 365 0.6; 402 1.0; 442 1.3; 486 0.9; 535 1.0; 588 1.2; 647 1.2; 712 0.7; 783 0.7; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 0.2; 1387 0.3; 1526 1.0; 1678 -1.3; 1846 -1.1; 2031 -0.6; 2234 0.1; 2457 0.8; 2703 0.2; 2973 0.4; 3270 0.4; 3597 0.9; 3957 0.1; 4353 -1.3; 4788 -0.9; 5267 1.9; 5793 3.8; 6373 4.9; 7010 2.5; 7711 0.3; 8482 -2.7; 9330 -3.9; 10263 -0.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.17 | 6.3 dB  |
| Peaking | 97 Hz   | 1.12 | -3.9 dB |
| Peaking | 173 Hz  | 1.88 | -2.8 dB |
| Peaking | 6311 Hz | 4.23 | 5.5 dB  |
| Peaking | 9001 Hz | 5.48 | -4.9 dB |
| Peaking | 256 Hz  | 4.22 | -1.9 dB |
| Peaking | 455 Hz  | 0.95 | 1.6 dB  |
| Peaking | 1788 Hz | 6.78 | -1.8 dB |
| Peaking | 4330 Hz | 1.63 | 1.5 dB  |
| Peaking | 4514 Hz | 5.05 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20229/Sennheiser%20HD%20229.png)