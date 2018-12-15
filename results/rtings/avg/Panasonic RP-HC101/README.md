# Panasonic RP-HC101

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.1; 41 3.6; 45 2.4; 49 1.3; 54 0.2; 60 -0.7; 66 -1.5; 72 -1.9; 79 -2.3; 87 -2.7; 96 -3.1; 106 -3.4; 116 -3.7; 128 -4.0; 141 -4.1; 155 -4.2; 170 -4.3; 187 -4.2; 206 -4.1; 227 -3.9; 249 -3.9; 274 -4.1; 302 -4.2; 332 -4.5; 365 -5.5; 402 -6.3; 442 -6.9; 486 -7.0; 535 -6.5; 588 -5.7; 647 -4.7; 712 -3.6; 783 -2.4; 861 -1.3; 947 -0.4; 1042 0.2; 1146 0.4; 1261 0.2; 1387 -0.5; 1526 -1.4; 1678 -2.8; 1846 -3.7; 2031 -3.5; 2234 -1.6; 2457 0.7; 2703 2.5; 2973 2.7; 3270 2.4; 3597 3.1; 3957 5.2; 4353 6.0; 4788 6.0; 5267 5.7; 5793 3.9; 6373 0.7; 7010 -3.3; 7711 -6.1; 8482 -3.3; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -3.9; 16529 -7.4; 18182 -9.2; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC101 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC101 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.72 | 9.1 dB  |
| Peaking | 97 Hz   | 0.3  | -4.9 dB |
| Peaking | 491 Hz  | 1.54 | -5.8 dB |
| Peaking | 4734 Hz | 1.88 | 7.3 dB  |
| Peaking | 7623 Hz | 4.01 | -7.9 dB |
| Peaking | 1136 Hz | 2.52 | 2.0 dB  |
| Peaking | 1925 Hz | 2.42 | -4.3 dB |
| Peaking | 1990 Hz | 2.08 | -0.3 dB |
| Peaking | 2696 Hz | 3.44 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC101/Panasonic%20RP-HC101.png)