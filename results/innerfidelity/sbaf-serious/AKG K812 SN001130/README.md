# AKG K812 sn001130

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 21 0.0; 23 1.2; 25 1.0; 28 0.7; 31 0.4; 34 0.2; 37 0.0; 41 -0.2; 45 -0.3; 49 -0.4; 54 -0.5; 60 -0.8; 66 -1.1; 72 -1.3; 79 -1.6; 87 -2.1; 96 -2.6; 106 -2.9; 116 -3.1; 128 -3.6; 141 -3.8; 155 -4.0; 170 -3.8; 187 -4.1; 206 -4.0; 227 -4.1; 249 -3.9; 274 -3.9; 302 -3.8; 332 -3.8; 365 -3.6; 402 -3.4; 442 -3.1; 486 -3.0; 535 -2.7; 588 -2.2; 647 -1.9; 712 -1.7; 783 -1.1; 861 -0.8; 947 -0.3; 1042 -0.0; 1146 0.2; 1261 0.5; 1387 -0.3; 1526 -0.4; 1678 -1.0; 1846 0.1; 2031 0.8; 2234 0.0; 2457 2.3; 2703 0.7; 2973 -1.9; 3270 -3.1; 3597 -4.3; 3957 -3.2; 4353 -0.0; 4788 0.7; 5267 -4.0; 5793 -8.0; 6373 -6.3; 7010 -1.4; 7711 -2.7; 8482 -4.3; 9330 -3.8; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.6; 18182 -3.6; 20000 -6.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.9dB` and instead set Global volume in the UI for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn001130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.6dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 11 Hz    |  0.56 | 2.3 dB  |
| Peaking | 214 Hz   |  0.47 | -4.3 dB |
| Peaking | 3572 Hz  |  5.92 | -4.4 dB |
| Peaking | 6006 Hz  |  5.15 | -9.2 dB |
| Peaking | 19770 Hz |  1.27 | -6.4 dB |
| Peaking | 2503 Hz  | 10.62 | 3.3 dB  |
| Peaking | 6883 Hz  |  7.96 | 2.4 dB  |
| Peaking | 8974 Hz  |  2.09 | -6.1 dB |
| Peaking | 10095 Hz |  0.64 | 1.7 dB  |
| Peaking | 10443 Hz |  3.67 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn001130/AKG%20K812%20sn001130.png)