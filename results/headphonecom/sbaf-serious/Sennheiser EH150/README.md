# Sennheiser EH150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 4.1; 535 2.1; 588 1.1; 647 0.5; 712 0.6; 783 0.2; 861 -0.0; 947 -0.1; 1042 0.0; 1146 0.2; 1261 0.2; 1387 0.0; 1526 0.0; 1678 0.3; 1846 1.3; 2031 2.2; 2234 3.4; 2457 4.7; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 1.4; 4788 2.5; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.23 | 6.2 dB  |
| Peaking | 229 Hz  | 1.07 | 3.5 dB  |
| Peaking | 401 Hz  | 2.79 | 4.0 dB  |
| Peaking | 3126 Hz | 1.81 | 6.6 dB  |
| Peaking | 5890 Hz | 3.83 | 5.8 dB  |
| Peaking | 2511 Hz | 1.42 | 5.2 dB  |
| Peaking | 3449 Hz | 0.58 | -5.8 dB |
| Peaking | 3860 Hz | 6.02 | 4.4 dB  |
| Peaking | 6098 Hz | 1.25 | 3.8 dB  |
| Peaking | 7805 Hz | 4.36 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH150/Sennheiser%20EH150.png)