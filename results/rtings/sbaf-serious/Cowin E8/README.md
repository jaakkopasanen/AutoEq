# Cowin E8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.7; 41 3.9; 45 3.1; 49 2.5; 54 1.9; 60 1.3; 66 0.7; 72 0.3; 79 -0.0; 87 -0.5; 96 -0.9; 106 -1.3; 116 -1.6; 128 -1.8; 141 -1.9; 155 -1.8; 170 -1.5; 187 -1.2; 206 -0.8; 227 -0.4; 249 0.1; 274 1.2; 302 1.7; 332 1.9; 365 2.2; 402 2.4; 442 2.5; 486 2.5; 535 2.3; 588 2.0; 647 1.5; 712 1.4; 783 3.6; 861 6.0; 947 2.1; 1042 0.1; 1146 2.2; 1261 4.7; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.7; 5267 -1.7; 5793 -0.5; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 26 Hz   |  1.4  | 6.9 dB  |
| Peaking | 441 Hz  |  1.93 | 2.2 dB  |
| Peaking | 1832 Hz |  0.87 | 5.9 dB  |
| Peaking | 3431 Hz |  2.21 | 3.6 dB  |
| Peaking | 4465 Hz |  6.6  | 3.7 dB  |
| Peaking | 138 Hz  |  1.67 | -2.4 dB |
| Peaking | 858 Hz  |  7.59 | 4.7 dB  |
| Peaking | 1026 Hz |  6.89 | -3.9 dB |
| Peaking | 5471 Hz | 10.62 | -6.1 dB |
| Peaking | 6457 Hz |  7.77 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Cowin%20E8/Cowin%20E8.png)