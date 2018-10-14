# Audeze LCD-X sn7454971

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.9; 28 3.6; 31 2.9; 34 2.2; 37 2.0; 41 2.2; 45 2.2; 49 1.9; 54 1.5; 60 1.2; 66 1.2; 72 1.0; 79 0.8; 87 0.4; 96 0.1; 106 -0.1; 116 -0.2; 128 -0.6; 141 -0.8; 155 -1.0; 170 -1.1; 187 -1.3; 206 -1.4; 227 -1.4; 249 -1.3; 274 -1.2; 302 -1.2; 332 -0.9; 365 -0.8; 402 -0.9; 442 -0.3; 486 -0.8; 535 -0.8; 588 -0.3; 647 -0.1; 712 -0.1; 783 0.2; 861 0.1; 947 -0.1; 1042 0.2; 1146 0.1; 1261 -0.0; 1387 -0.6; 1526 -0.9; 1678 -1.2; 1846 -1.1; 2031 -1.3; 2234 -0.7; 2457 0.9; 2703 2.5; 2973 4.0; 3270 5.1; 3597 4.3; 3957 1.3; 4353 4.7; 4788 5.9; 5267 5.8; 5793 5.3; 6373 3.3; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -1.9; 20000 -3.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sn7454971 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  1.36 | 3.4 dB  |
| Peaking | 50 Hz    |  0.54 | 1.5 dB  |
| Peaking | 202 Hz   |  0.59 | -1.6 dB |
| Peaking | 3234 Hz  |  4.55 | 4.7 dB  |
| Peaking | 5231 Hz  |  2.58 | 6.4 dB  |
| Peaking | 27 Hz    |  1.51 | 0.4 dB  |
| Peaking | 1877 Hz  |  1.76 | -4.0 dB |
| Peaking | 1942 Hz  |  1.04 | 2.2 dB  |
| Peaking | 6721 Hz  | 11.11 | 0.8 dB  |
| Peaking | 19737 Hz |  1.59 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sn7454971/Audeze%20LCD-X%20sn7454971.png)