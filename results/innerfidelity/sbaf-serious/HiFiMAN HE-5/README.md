# HiFiMAN HE-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.0; 28 4.4; 31 3.9; 34 3.6; 37 3.4; 41 3.1; 45 2.9; 49 2.8; 54 3.0; 60 2.8; 66 2.2; 72 1.9; 79 1.7; 87 1.4; 96 1.1; 106 0.9; 116 0.7; 128 0.4; 141 0.1; 155 -0.2; 170 -0.3; 187 -0.4; 206 -0.7; 227 -0.8; 249 -1.0; 274 -0.9; 302 -0.9; 332 -0.8; 365 -0.9; 402 -1.3; 442 -0.9; 486 -0.7; 535 -1.1; 588 -0.9; 647 -0.8; 712 -0.5; 783 0.1; 861 -0.2; 947 -0.4; 1042 0.2; 1146 1.3; 1261 1.6; 1387 1.7; 1526 1.3; 1678 2.2; 1846 4.1; 2031 3.7; 2234 2.8; 2457 3.3; 2703 2.2; 2973 0.5; 3270 -0.4; 3597 -0.7; 3957 -1.2; 4353 -3.7; 4788 -2.4; 5267 0.4; 5793 -1.2; 6373 -4.0; 7010 -4.4; 7711 -4.4; 8482 -7.5; 9330 -9.4; 10263 -5.6; 11289 -2.5; 12418 -4.6; 13660 -6.8; 15026 -5.0; 16529 -0.8; 18182 -0.1; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 14 Hz    |  0.36 | 6.3 dB  |
| Peaking | 2082 Hz  |  1.73 | 4.3 dB  |
| Peaking | 4354 Hz  |  8.4  | -2.6 dB |
| Peaking | 9822 Hz  |  0.87 | -6.9 dB |
| Peaking | 20059 Hz |  3.94 | -4.5 dB |
| Peaking | 363 Hz   |  0.8  | -1.3 dB |
| Peaking | 5424 Hz  | 10.14 | 3.6 dB  |
| Peaking | 9279 Hz  |  5.6  | -4.0 dB |
| Peaking | 11201 Hz |  3.62 | 4.7 dB  |
| Peaking | 13955 Hz |  3.67 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)