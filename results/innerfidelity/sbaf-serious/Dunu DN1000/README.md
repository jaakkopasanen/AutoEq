# Dunu DN1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.2; 25 -4.2; 28 -4.1; 31 -4.1; 34 -4.1; 37 -4.1; 41 -4.1; 45 -4.1; 49 -4.2; 54 -4.2; 60 -4.3; 66 -4.4; 72 -4.5; 79 -4.6; 87 -4.8; 96 -4.9; 106 -4.8; 116 -4.7; 128 -4.7; 141 -4.6; 155 -4.5; 170 -4.2; 187 -4.0; 206 -3.7; 227 -3.3; 249 -3.0; 274 -2.7; 302 -2.3; 332 -2.0; 365 -1.6; 402 -1.3; 442 -0.9; 486 -0.7; 535 -0.4; 588 0.1; 647 0.2; 712 0.3; 783 0.6; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -0.9; 1526 -1.2; 1678 -1.2; 1846 -0.8; 2031 -0.2; 2234 0.5; 2457 1.7; 2703 2.4; 2973 3.7; 3270 5.7; 3597 6.0; 3957 5.6; 4353 0.4; 4788 -1.5; 5267 1.2; 5793 1.6; 6373 1.8; 7010 1.3; 7711 -1.1; 8482 -5.5; 9330 -8.2; 10263 -6.1; 11289 -0.4; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.19 | -3.9 dB |
| Peaking | 152 Hz   | 0.68 | -2.9 dB |
| Peaking | 3466 Hz  | 3.37 | 6.9 dB  |
| Peaking | 6685 Hz  | 4.1  | 2.9 dB  |
| Peaking | 9309 Hz  | 3.6  | -9.3 dB |
| Peaking | 742 Hz   | 2.24 | 1.0 dB  |
| Peaking | 1606 Hz  | 2.82 | -1.6 dB |
| Peaking | 4436 Hz  | 2.5  | 2.5 dB  |
| Peaking | 4609 Hz  | 6.52 | -5.6 dB |
| Peaking | 11719 Hz | 7.23 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN1000/Dunu%20DN1000.png)