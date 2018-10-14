# Sony MDR-XB300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.0; 25 1.8; 28 0.2; 31 -1.1; 34 -2.2; 37 -3.2; 41 -4.3; 45 -5.1; 49 -5.9; 54 -6.5; 60 -6.9; 66 -6.9; 72 -6.8; 79 -7.2; 87 -7.8; 96 -8.2; 106 -8.3; 116 -8.1; 128 -8.0; 141 -7.7; 155 -7.2; 170 -6.8; 187 -6.6; 206 -6.1; 227 -5.3; 249 -4.3; 274 -3.8; 302 -2.9; 332 -2.0; 365 -0.9; 402 -0.0; 442 1.1; 486 1.8; 535 2.5; 588 3.5; 647 3.9; 712 4.3; 783 4.1; 861 2.7; 947 0.8; 1042 -0.5; 1146 -1.2; 1261 -2.0; 1387 -3.3; 1526 -3.9; 1678 -4.2; 1846 -5.0; 2031 -5.7; 2234 -6.1; 2457 -5.4; 2703 -3.7; 2973 -1.3; 3270 0.9; 3597 2.9; 3957 4.5; 4353 5.3; 4788 6.0; 5267 6.0; 5793 5.7; 6373 0.7; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.1  | 6.1 dB  |
| Peaking | 73 Hz   | 0.71 | -7.1 dB |
| Peaking | 162 Hz  | 1.32 | -5.0 dB |
| Peaking | 2174 Hz | 1.91 | -7.4 dB |
| Peaking | 4654 Hz | 1.77 | 7.2 dB  |
| Peaking | 73 Hz   | 6.91 | 0.9 dB  |
| Peaking | 274 Hz  | 2.12 | -1.8 dB |
| Peaking | 690 Hz  | 1.29 | 5.3 dB  |
| Peaking | 1303 Hz | 1.88 | -2.7 dB |
| Peaking | 8475 Hz | 2.9  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)