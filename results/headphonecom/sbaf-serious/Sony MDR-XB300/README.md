# Sony MDR-XB300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 4.4; 25 3.3; 28 2.1; 31 0.9; 34 -0.1; 37 -1.1; 41 -2.4; 45 -3.5; 49 -4.3; 54 -4.9; 60 -4.9; 66 -5.2; 72 -6.2; 79 -7.0; 87 -7.5; 96 -7.8; 106 -7.8; 116 -7.6; 128 -7.2; 141 -6.9; 155 -7.0; 170 -7.1; 187 -7.0; 206 -6.7; 227 -5.5; 249 -3.7; 274 -3.9; 302 -3.2; 332 -2.1; 365 -1.0; 402 0.0; 442 1.0; 486 1.9; 535 2.5; 588 3.0; 647 3.5; 712 3.7; 783 3.6; 861 2.7; 947 0.9; 1042 -0.6; 1146 -1.6; 1261 -2.2; 1387 -3.7; 1526 -4.1; 1678 -4.3; 1846 -4.6; 2031 -4.8; 2234 -4.9; 2457 -4.1; 2703 -2.8; 2973 -0.8; 3270 1.2; 3597 3.1; 3957 4.0; 4353 4.4; 4788 6.0; 5267 6.0; 5793 5.5; 6373 0.9; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.95 | 7.3 dB  |
| Peaking | 52 Hz   | 1    | -4.0 dB |
| Peaking | 104 Hz  | 1.25 | -6.5 dB |
| Peaking | 195 Hz  | 1.99 | -5.4 dB |
| Peaking | 5012 Hz | 3    | 7.0 dB  |
| Peaking | 304 Hz  | 3.15 | -2.0 dB |
| Peaking | 727 Hz  | 1.05 | 6.9 dB  |
| Peaking | 2026 Hz | 0.48 | -6.9 dB |
| Peaking | 3609 Hz | 2.11 | 6.3 dB  |
| Peaking | 6183 Hz | 1.66 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)