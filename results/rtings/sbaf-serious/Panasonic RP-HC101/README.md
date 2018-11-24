# Panasonic RP-HC101

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.0; 41 3.4; 45 2.1; 49 1.0; 54 -0.1; 60 -1.0; 66 -1.6; 72 -1.9; 79 -2.2; 87 -2.4; 96 -2.6; 106 -2.9; 116 -3.2; 128 -3.4; 141 -3.6; 155 -3.6; 170 -3.6; 187 -3.7; 206 -3.5; 227 -3.5; 249 -3.4; 274 -3.4; 302 -3.4; 332 -3.6; 365 -4.5; 402 -5.3; 442 -5.8; 486 -5.8; 535 -5.3; 588 -4.6; 647 -3.7; 712 -2.7; 783 -1.9; 861 -1.1; 947 -0.4; 1042 0.3; 1146 0.6; 1261 0.4; 1387 -0.5; 1526 -1.8; 1678 -3.2; 1846 -3.7; 2031 -3.1; 2234 -1.2; 2457 1.2; 2703 3.3; 2973 4.3; 3270 4.9; 3597 5.9; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.4; 7010 0.1; 7711 -3.6; 8482 -2.2; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.1; 18182 -1.6; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC101 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC101 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.79 | 8.8 dB  |
| Peaking | 93 Hz    | 0.32 | -4.3 dB |
| Peaking | 484 Hz   | 1.71 | -5.0 dB |
| Peaking | 1891 Hz  | 3.44 | -5.2 dB |
| Peaking | 4058 Hz  | 1.3  | 7.1 dB  |
| Peaking | 1129 Hz  | 4.76 | 1.5 dB  |
| Peaking | 6039 Hz  | 4.31 | 3.9 dB  |
| Peaking | 7786 Hz  | 4.23 | -5.9 dB |
| Peaking | 19702 Hz | 1.12 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Panasonic%20RP-HC101/Panasonic%20RP-HC101.png)