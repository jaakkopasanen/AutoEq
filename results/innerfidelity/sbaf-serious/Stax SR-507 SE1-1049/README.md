# Stax SR-507 SE1-1049

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 4.4; 25 3.7; 28 3.0; 31 2.7; 34 2.6; 37 2.8; 41 3.1; 45 3.3; 49 3.5; 54 3.8; 60 3.9; 66 3.8; 72 3.6; 79 3.3; 87 3.0; 96 2.8; 106 2.4; 116 2.4; 128 2.1; 141 2.1; 155 1.9; 170 1.9; 187 1.8; 206 1.7; 227 1.9; 249 1.7; 274 1.8; 302 1.6; 332 1.6; 365 1.6; 402 1.6; 442 1.8; 486 1.6; 535 1.5; 588 1.5; 647 1.3; 712 0.9; 783 0.9; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.8; 1387 -2.6; 1526 -3.1; 1678 -3.1; 1846 -2.3; 2031 1.0; 2234 3.5; 2457 3.3; 2703 1.7; 2973 0.9; 3270 0.3; 3597 1.2; 3957 1.8; 4353 -0.1; 4788 -0.9; 5267 1.3; 5793 -0.4; 6373 1.4; 7010 2.4; 7711 0.3; 8482 -2.9; 9330 -4.3; 10263 -2.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-507 SE1-1049 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 10 Hz   |  0.14 | 3.6 dB  |
| Peaking | 691 Hz  |  0.06 | 1.6 dB  |
| Peaking | 1728 Hz |  1.3  | -6.1 dB |
| Peaking | 2264 Hz |  3.44 | 6.4 dB  |
| Peaking | 9268 Hz |  4.39 | -5.6 dB |
| Peaking | 36 Hz   |  2.84 | -1.0 dB |
| Peaking | 63 Hz   |  2.84 | 0.8 dB  |
| Peaking | 4109 Hz |  6.33 | 2.4 dB  |
| Peaking | 4473 Hz |  4.96 | -2.9 dB |
| Peaking | 6798 Hz | 10.63 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-507%20SE1-1049/Stax%20SR-507%20SE1-1049.png)