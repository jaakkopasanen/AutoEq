# Sennheiser PX 200 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.7; 54 5.3; 60 4.9; 66 4.5; 72 4.2; 79 3.8; 87 3.6; 96 4.4; 106 4.3; 116 3.2; 128 2.9; 141 2.7; 155 2.1; 170 1.8; 187 1.5; 206 1.4; 227 1.9; 249 2.5; 274 2.2; 302 1.6; 332 1.8; 365 1.5; 402 1.2; 442 0.9; 486 0.7; 535 0.6; 588 0.8; 647 1.0; 712 0.5; 783 0.5; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -1.2; 1387 -2.3; 1526 -2.5; 1678 -1.9; 1846 -2.4; 2031 -2.1; 2234 -0.4; 2457 0.9; 2703 2.5; 2973 4.2; 3270 5.2; 3597 5.6; 3957 5.5; 4353 2.9; 4788 2.4; 5267 4.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.32 | 4.9 dB  |
| Peaking | 78 Hz   | 0.06 | 1.2 dB  |
| Peaking | 1722 Hz | 1.34 | -3.7 dB |
| Peaking | 3406 Hz | 1.95 | 6.2 dB  |
| Peaking | 5962 Hz | 4.04 | 5.8 dB  |
| Peaking | 85 Hz   | 2.92 | -0.8 dB |
| Peaking | 101 Hz  | 6.03 | 1.8 dB  |
| Peaking | 214 Hz  | 1.95 | -1.1 dB |
| Peaking | 248 Hz  | 3.5  | 1.6 dB  |
| Peaking | 8276 Hz | 4.52 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20200%20II/Sennheiser%20PX%20200%20II.png)