# Yuin PK1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.9; 79 5.1; 87 4.4; 96 3.8; 106 3.4; 116 3.3; 128 3.1; 141 2.9; 155 2.7; 170 2.8; 187 2.6; 206 2.7; 227 2.5; 249 2.6; 274 2.6; 302 2.6; 332 2.6; 365 2.5; 402 2.3; 442 2.0; 486 1.7; 535 1.6; 588 1.5; 647 1.3; 712 1.1; 783 0.9; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.4; 1526 -2.4; 1678 -3.3; 1846 -4.0; 2031 -4.3; 2234 -4.0; 2457 -3.1; 2703 -1.4; 2973 0.4; 3270 1.9; 3597 2.4; 3957 1.0; 4353 -1.5; 4788 -2.6; 5267 -2.8; 5793 -3.1; 6373 -3.6; 7010 -2.5; 7711 -2.0; 8482 -2.0; 9330 -1.6; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.5; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin PK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.37 | 6.4 dB  |
| Peaking | 375 Hz   | 0.6  | 2.0 dB  |
| Peaking | 2045 Hz  | 1.55 | -4.8 dB |
| Peaking | 3475 Hz  | 2.55 | 5.3 dB  |
| Peaking | 5602 Hz  | 1.15 | -3.8 dB |
| Peaking | 40 Hz    | 2    | -0.4 dB |
| Peaking | 71 Hz    | 2.99 | 0.9 dB  |
| Peaking | 98 Hz    | 2.54 | -0.5 dB |
| Peaking | 9178 Hz  | 3.78 | -1.2 dB |
| Peaking | 10543 Hz | 2.11 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)