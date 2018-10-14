# Philips TX1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -9.0; 23 -9.0; 25 -9.0; 28 -8.9; 31 -8.8; 34 -8.7; 37 -8.6; 41 -8.6; 45 -8.5; 49 -8.4; 54 -8.4; 60 -8.3; 66 -8.3; 72 -8.3; 79 -8.3; 87 -8.3; 96 -8.3; 106 -8.1; 116 -7.9; 128 -7.7; 141 -7.5; 155 -7.1; 170 -6.7; 187 -6.3; 206 -5.9; 227 -5.3; 249 -4.8; 274 -4.3; 302 -3.7; 332 -3.2; 365 -2.6; 402 -2.1; 442 -1.5; 486 -1.1; 535 -0.6; 588 0.1; 647 0.3; 712 0.4; 783 0.7; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.3; 1678 -2.8; 1846 -2.8; 2031 -2.5; 2234 -1.8; 2457 -0.2; 2703 1.1; 2973 2.9; 3270 4.1; 3597 4.4; 3957 2.8; 4353 -0.6; 4788 -3.1; 5267 -4.1; 5793 -2.8; 6373 -0.9; 7010 0.5; 7711 0.3; 8482 -1.1; 9330 -1.7; 10263 -0.8; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.7dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.2  | -8.7 dB |
| Peaking | 158 Hz  | 0.75 | -3.8 dB |
| Peaking | 1879 Hz | 2.26 | -3.6 dB |
| Peaking | 3489 Hz | 2.26 | 5.9 dB  |
| Peaking | 5029 Hz | 3    | -5.6 dB |
| Peaking | 321 Hz  | 2.19 | -0.7 dB |
| Peaking | 735 Hz  | 1.48 | 1.4 dB  |
| Peaking | 1447 Hz | 4.1  | -0.8 dB |
| Peaking | 7260 Hz | 6.09 | 1.5 dB  |
| Peaking | 9165 Hz | 4.38 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX1/Philips%20TX1.png)