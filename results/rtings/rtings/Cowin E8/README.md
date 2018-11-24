# Cowin E8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.7; 34 5.3; 37 4.8; 41 4.1; 45 3.4; 49 2.8; 54 2.2; 60 1.6; 66 0.9; 72 0.3; 79 -0.2; 87 -0.8; 96 -1.3; 106 -1.8; 116 -2.1; 128 -2.4; 141 -2.4; 155 -2.4; 170 -2.2; 187 -1.8; 206 -1.3; 227 -0.8; 249 -0.4; 274 0.6; 302 0.9; 332 1.0; 365 1.2; 402 1.3; 442 1.3; 486 1.3; 535 1.2; 588 0.9; 647 0.5; 712 0.5; 783 3.2; 861 5.8; 947 2.0; 1042 0.1; 1146 2.0; 1261 4.4; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.8; 5267 -2.1; 5793 -1.9; 6373 2.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.77 | 6.4 dB   |
| Peaking | 128 Hz  | 1.31 | -3.2 dB  |
| Peaking | 1813 Hz | 0.84 | 6.0 dB   |
| Peaking | 3383 Hz | 2.6  | 3.6 dB   |
| Peaking | 4430 Hz | 6.95 | 4.1 dB   |
| Peaking | 371 Hz  | 2.57 | 1.2 dB   |
| Peaking | 856 Hz  | 8.67 | 4.8 dB   |
| Peaking | 1026 Hz | 6.13 | -3.8 dB  |
| Peaking | 5523 Hz | 7.22 | -10.0 dB |
| Peaking | 5659 Hz | 2.37 | 3.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Cowin%20E8/Cowin%20E8.png)