# MyST IzoPhones 60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 4.8; 60 3.0; 66 1.7; 72 0.6; 79 -0.3; 87 -0.8; 96 -1.1; 106 -1.1; 116 -1.0; 128 -0.9; 141 -0.7; 155 -0.6; 170 -0.4; 187 -0.2; 206 -0.0; 227 0.2; 249 0.5; 274 0.9; 302 1.4; 332 1.3; 365 1.2; 402 1.0; 442 1.3; 486 0.9; 535 1.1; 588 1.7; 647 1.6; 712 1.3; 783 1.4; 861 0.8; 947 -0.0; 1042 0.3; 1146 0.1; 1261 -0.1; 1387 -0.5; 1526 -0.4; 1678 -0.3; 1846 1.4; 2031 2.7; 2234 2.8; 2457 4.0; 2703 4.1; 2973 2.5; 3270 1.7; 3597 0.5; 3957 -1.5; 4353 -3.8; 4788 -0.2; 5267 3.3; 5793 5.3; 6373 0.5; 7010 -3.9; 7711 -4.5; 8482 -6.8; 9330 -6.7; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -0.9; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST IzoPhones 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.1  | 7.2 dB  |
| Peaking | 2557 Hz  | 2.39 | 4.4 dB  |
| Peaking | 4321 Hz  | 6.42 | -4.9 dB |
| Peaking | 5707 Hz  | 5.01 | 6.7 dB  |
| Peaking | 8454 Hz  | 2.76 | -7.8 dB |
| Peaking | 52 Hz    | 2.58 | 3.8 dB  |
| Peaking | 87 Hz    | 0.54 | -2.4 dB |
| Peaking | 407 Hz   | 0.51 | 1.6 dB  |
| Peaking | 1452 Hz  | 2.97 | -1.6 dB |
| Peaking | 10962 Hz | 6.58 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MyST%20IzoPhones%2060/MyST%20IzoPhones%2060.png)