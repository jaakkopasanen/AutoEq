# Beyerdynamic DT 880 32 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.7; 31 5.2; 34 4.7; 37 4.3; 41 3.8; 45 3.4; 49 3.1; 54 2.7; 60 2.1; 66 1.8; 72 2.0; 79 1.7; 87 0.4; 96 -0.3; 106 -0.8; 116 -1.2; 128 -1.6; 141 -2.0; 155 -2.2; 170 -2.3; 187 -2.5; 206 -2.6; 227 -2.5; 249 -2.4; 274 -2.4; 302 -2.2; 332 -2.2; 365 -2.1; 402 -1.8; 442 -1.3; 486 -1.1; 535 -1.2; 588 -0.8; 647 -0.7; 712 -0.5; 783 -0.0; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.4; 1526 -0.2; 1678 -0.8; 1846 -1.3; 2031 -1.1; 2234 -1.1; 2457 -0.3; 2703 -1.1; 2973 -0.9; 3270 -0.8; 3597 -0.6; 3957 -0.7; 4353 -0.4; 4788 2.1; 5267 5.9; 5793 6.0; 6373 -0.1; 7010 -1.7; 7711 -2.5; 8482 -4.5; 9330 -4.3; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 32 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  0.53 | 6.1 dB  |
| Peaking | 76 Hz    |  4.13 | 1.3 dB  |
| Peaking | 192 Hz   |  0.54 | -2.9 dB |
| Peaking | 5507 Hz  |  5.49 | 7.6 dB  |
| Peaking | 8534 Hz  |  2.96 | -5.0 dB |
| Peaking | 1351 Hz  |  1.78 | 1.5 dB  |
| Peaking | 1784 Hz  |  2.1  | -1.6 dB |
| Peaking | 3921 Hz  |  1.22 | -1.1 dB |
| Peaking | 5010 Hz  | 10.05 | 2.3 dB  |
| Peaking | 10772 Hz |  5.67 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%2032%20Ohm/Beyerdynamic%20DT%20880%2032%20Ohm.png)