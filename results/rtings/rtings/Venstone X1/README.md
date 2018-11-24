# Venstone X1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.9; 25 -3.3; 28 -3.9; 31 -4.3; 34 -4.7; 37 -5.1; 41 -5.5; 45 -5.9; 49 -6.3; 54 -6.7; 60 -7.2; 66 -7.6; 72 -8.0; 79 -8.4; 87 -8.9; 96 -9.3; 106 -9.8; 116 -10.3; 128 -10.6; 141 -10.9; 155 -10.9; 170 -10.9; 187 -10.8; 206 -10.6; 227 -10.2; 249 -9.9; 274 -9.8; 302 -9.6; 332 -9.3; 365 -8.7; 402 -7.9; 442 -7.0; 486 -5.9; 535 -4.6; 588 -3.5; 647 -2.6; 712 -1.9; 783 -1.7; 861 -1.1; 947 -0.4; 1042 0.3; 1146 1.0; 1261 2.0; 1387 3.0; 1526 4.3; 1678 5.5; 1846 5.9; 2031 4.9; 2234 2.9; 2457 1.1; 2703 1.0; 2973 1.3; 3270 1.0; 3597 0.1; 3957 -1.4; 4353 -2.8; 4788 -5.1; 5267 -8.5; 5793 -6.2; 6373 -1.9; 7010 0.7; 7711 -1.6; 8482 -5.2; 9330 -2.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.4; 16529 -3.7; 18182 -2.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venstone X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venstone X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 121 Hz   | 0.36 | -9.6 dB |
| Peaking | 318 Hz   | 0.94 | -4.0 dB |
| Peaking | 1733 Hz  | 1.65 | 6.5 dB  |
| Peaking | 5291 Hz  | 3.59 | -9.0 dB |
| Peaking | 17151 Hz | 2.37 | -4.3 dB |
| Peaking | 2483 Hz  | 9.81 | -1.3 dB |
| Peaking | 5856 Hz  | 5    | -1.3 dB |
| Peaking | 6978 Hz  | 4.94 | 2.7 dB  |
| Peaking | 8575 Hz  | 4.25 | -7.4 dB |
| Peaking | 8955 Hz  | 1.26 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Venstone%20X1/Venstone%20X1.png)