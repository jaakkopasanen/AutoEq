# AKG K81DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.6; 28 5.0; 31 4.5; 34 3.9; 37 3.5; 41 3.0; 45 2.7; 49 2.4; 54 1.9; 60 1.2; 66 0.8; 72 0.6; 79 0.2; 87 -0.2; 96 0.3; 106 -0.0; 116 -1.1; 128 -2.1; 141 -2.8; 155 -2.8; 170 -2.6; 187 -2.7; 206 -1.5; 227 -1.0; 249 -0.5; 274 -0.7; 302 -0.5; 332 -0.1; 365 1.5; 402 2.2; 442 2.3; 486 2.1; 535 1.8; 588 1.8; 647 1.5; 712 1.0; 783 1.0; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -1.1; 1526 -1.8; 1678 -2.3; 1846 -2.5; 2031 -2.0; 2234 -1.5; 2457 0.5; 2703 1.8; 2973 3.3; 3270 3.7; 3597 3.2; 3957 2.8; 4353 2.0; 4788 2.8; 5267 3.4; 5793 1.7; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.6; 16529 -2.2; 18182 -1.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.7  | 6.0 dB   |
| Peaking | 160 Hz   | 1.66 | -3.5 dB  |
| Peaking | 1707 Hz  | 0.97 | -10.8 dB |
| Peaking | 1889 Hz  | 0.44 | 8.2 dB   |
| Peaking | 6445 Hz  | 9.13 | 3.3 dB   |
| Peaking | 450 Hz   | 1.86 | 3.0 dB   |
| Peaking | 486 Hz   | 0.77 | -1.5 dB  |
| Peaking | 3177 Hz  | 5.69 | 1.6 dB   |
| Peaking | 8672 Hz  | 2.94 | -1.2 dB  |
| Peaking | 17098 Hz | 2.23 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K81DJ/AKG%20K81DJ.png)