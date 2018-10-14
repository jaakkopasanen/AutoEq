# Yamaha HP1 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.5; 28 4.0; 31 3.5; 34 3.2; 37 2.9; 41 2.7; 45 2.5; 49 2.4; 54 2.1; 60 1.8; 66 1.5; 72 1.3; 79 1.0; 87 0.8; 96 0.4; 106 0.2; 116 0.1; 128 -0.3; 141 -0.6; 155 -0.8; 170 -0.9; 187 -1.0; 206 -1.1; 227 -1.1; 249 -1.2; 274 -0.9; 302 -0.9; 332 -0.8; 365 -0.7; 402 -0.8; 442 -0.6; 486 -0.7; 535 -0.7; 588 -0.3; 647 -0.4; 712 -0.5; 783 -0.1; 861 -0.1; 947 -0.0; 1042 0.3; 1146 1.0; 1261 2.2; 1387 2.5; 1526 2.4; 1678 3.2; 1846 3.3; 2031 2.1; 2234 0.3; 2457 1.7; 2703 0.8; 2973 3.4; 3270 5.2; 3597 5.9; 3957 5.1; 4353 3.5; 4788 4.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -1.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.19 | 5.1 dB  |
| Peaking | 50 Hz   |  1.91 | 1.6 dB  |
| Peaking | 1639 Hz |  2.56 | 3.1 dB  |
| Peaking | 3568 Hz |  3.28 | 5.4 dB  |
| Peaking | 5662 Hz |  2.81 | 6.2 dB  |
| Peaking | 208 Hz  |  1.41 | -1.1 dB |
| Peaking | 496 Hz  |  0.76 | -0.6 dB |
| Peaking | 1261 Hz |  6.99 | 1.2 dB  |
| Peaking | 2270 Hz | 10.11 | -1.0 dB |
| Peaking | 8246 Hz |  4.78 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1%20sample%201/Yamaha%20HP1%20sample%201.png)