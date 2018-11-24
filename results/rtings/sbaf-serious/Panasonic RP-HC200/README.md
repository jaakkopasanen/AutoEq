# Panasonic RP-HC200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.6; 128 5.1; 141 5.0; 155 5.0; 170 5.0; 187 4.9; 206 5.1; 227 5.1; 249 5.2; 274 5.4; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 5.2; 588 4.1; 647 2.8; 712 1.4; 783 0.2; 861 -0.4; 947 -0.0; 1042 0.2; 1146 0.7; 1261 2.0; 1387 1.7; 1526 2.0; 1678 3.3; 1846 5.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.9; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.21 | 6.3 dB  |
| Peaking | 326 Hz   | 1.65 | 3.7 dB  |
| Peaking | 489 Hz   | 3.49 | 3.7 dB  |
| Peaking | 3894 Hz  | 0.61 | 6.9 dB  |
| Peaking | 8621 Hz  | 2.94 | -4.5 dB |
| Peaking | 936 Hz   | 2.63 | -2.3 dB |
| Peaking | 2067 Hz  | 3.81 | 2.3 dB  |
| Peaking | 3831 Hz  | 2.5  | -1.0 dB |
| Peaking | 6095 Hz  | 5.07 | 1.8 dB  |
| Peaking | 13038 Hz | 1.46 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Panasonic%20RP-HC200/Panasonic%20RP-HC200.png)