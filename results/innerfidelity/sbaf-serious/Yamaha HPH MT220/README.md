# Yamaha HPH MT220

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.5; 28 1.0; 31 0.7; 34 0.5; 37 0.4; 41 0.3; 45 0.3; 49 0.3; 54 0.4; 60 0.4; 66 0.3; 72 0.3; 79 0.4; 87 0.4; 96 0.4; 106 0.8; 116 1.5; 128 2.1; 141 1.9; 155 1.0; 170 2.7; 187 2.1; 206 2.0; 227 2.3; 249 2.9; 274 3.5; 302 4.0; 332 3.8; 365 3.9; 402 3.9; 442 3.6; 486 2.8; 535 2.2; 588 1.8; 647 1.1; 712 0.5; 783 0.3; 861 -0.0; 947 -0.0; 1042 0.1; 1146 0.4; 1261 1.0; 1387 0.8; 1526 1.1; 1678 2.2; 1846 3.9; 2031 5.7; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.7; 4353 3.3; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HPH MT220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.83 | 2.7 dB  |
| Peaking | 160 Hz  | 1.17 | 1.5 dB  |
| Peaking | 353 Hz  | 1.46 | 4.0 dB  |
| Peaking | 2765 Hz | 1.27 | 6.5 dB  |
| Peaking | 5590 Hz | 2.68 | 5.3 dB  |
| Peaking | 1116 Hz | 1.37 | -1.0 dB |
| Peaking | 2064 Hz | 5.34 | 2.0 dB  |
| Peaking | 2769 Hz | 4.24 | -1.0 dB |
| Peaking | 3717 Hz | 7.52 | 1.5 dB  |
| Peaking | 8375 Hz | 3.83 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HPH%20MT220/Yamaha%20HPH%20MT220.png)