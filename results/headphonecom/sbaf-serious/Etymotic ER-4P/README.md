# Etymotic ER-4P

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.7; 45 5.4; 49 5.1; 54 4.8; 60 4.4; 66 4.0; 72 3.7; 79 3.4; 87 2.9; 96 2.6; 106 2.3; 116 2.1; 128 1.8; 141 1.5; 155 1.3; 170 1.1; 187 1.0; 206 0.9; 227 0.8; 249 0.8; 274 0.8; 302 0.9; 332 1.1; 365 1.2; 402 1.3; 442 1.3; 486 1.3; 535 1.2; 588 1.5; 647 1.5; 712 1.5; 783 1.4; 861 1.0; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.9; 1387 -2.9; 1526 -3.9; 1678 -4.6; 1846 -4.8; 2031 -4.9; 2234 -4.6; 2457 -3.7; 2703 -2.0; 2973 0.5; 3270 3.3; 3597 5.2; 3957 4.9; 4353 3.6; 4788 3.6; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -3.3; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.4  | 6.2 dB   |
| Peaking | 899 Hz   | 0.64 | 5.7 dB   |
| Peaking | 2269 Hz  | 0.44 | -10.3 dB |
| Peaking | 3558 Hz  | 1.67 | 11.6 dB  |
| Peaking | 5866 Hz  | 2.21 | 8.2 dB   |
| Peaking | 384 Hz   | 5.51 | 0.3 dB   |
| Peaking | 7708 Hz  | 7.06 | -1.0 dB  |
| Peaking | 13603 Hz | 0.8  | 0.8 dB   |
| Peaking | 13867 Hz | 2.78 | 0.2 dB   |
| Peaking | 14900 Hz | 5.44 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4P/Etymotic%20ER-4P.png)