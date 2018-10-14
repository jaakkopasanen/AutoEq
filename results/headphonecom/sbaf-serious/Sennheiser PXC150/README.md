# Sennheiser PXC150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.7; 60 4.1; 66 2.7; 72 1.5; 79 0.8; 87 1.0; 96 1.5; 106 1.0; 116 0.4; 128 0.1; 141 0.1; 155 0.3; 170 1.0; 187 1.2; 206 1.1; 227 1.1; 249 1.2; 274 1.6; 302 1.7; 332 2.1; 365 2.3; 402 2.4; 442 2.5; 486 2.6; 535 2.8; 588 2.6; 647 2.4; 712 2.1; 783 1.7; 861 1.1; 947 0.4; 1042 -0.4; 1146 -1.1; 1261 -2.0; 1387 -2.5; 1526 -3.9; 1678 -4.8; 1846 -5.3; 2031 -5.3; 2234 -3.2; 2457 -1.6; 2703 0.1; 2973 1.6; 3270 3.2; 3597 4.6; 3957 4.1; 4353 0.2; 4788 -0.1; 5267 1.5; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -3.9; 9330 -6.8; 10263 -6.0; 11289 -1.5; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.67 | 6.7 dB  |
| Peaking | 1852 Hz | 2.49 | -6.2 dB |
| Peaking | 3551 Hz | 3.86 | 5.4 dB  |
| Peaking | 6253 Hz | 4.21 | 6.9 dB  |
| Peaking | 9538 Hz | 3.49 | -8.0 dB |
| Peaking | 52 Hz   | 4.23 | 1.7 dB  |
| Peaking | 75 Hz   | 3.87 | -1.8 dB |
| Peaking | 130 Hz  | 4.1  | -1.1 dB |
| Peaking | 480 Hz  | 1.03 | 2.9 dB  |
| Peaking | 4628 Hz | 8.91 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC150/Sennheiser%20PXC150.png)