# Grado SR225

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.7; 54 4.6; 60 3.3; 66 2.3; 72 1.4; 79 0.7; 87 0.1; 96 -0.4; 106 -0.8; 116 -1.1; 128 -1.1; 141 -1.1; 155 -1.1; 170 -1.1; 187 -1.0; 206 -1.0; 227 -0.8; 249 -0.7; 274 -0.7; 302 -0.6; 332 -0.1; 365 0.3; 402 0.4; 442 0.2; 486 0.4; 535 0.5; 588 0.5; 647 0.7; 712 0.7; 783 0.6; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.9; 1526 -3.1; 1678 -4.1; 1846 -4.8; 2031 -5.3; 2234 -5.5; 2457 -4.8; 2703 -4.6; 2973 -4.3; 3270 -4.2; 3597 -5.3; 3957 -9.3; 4353 -10.9; 4788 -8.3; 5267 -7.4; 5793 -8.2; 6373 -5.8; 7010 -2.4; 7711 -1.9; 8482 -5.8; 9330 -11.3; 10263 -11.3; 11289 -6.3; 12418 -3.2; 13660 -3.6; 15026 -3.4; 16529 -0.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.33 | 7.9 dB   |
| Peaking | 101 Hz   | 0.69 | -6.2 dB  |
| Peaking | 2033 Hz  | 2.06 | -4.8 dB  |
| Peaking | 4479 Hz  | 1.86 | -9.7 dB  |
| Peaking | 9980 Hz  | 2.9  | -11.9 dB |
| Peaking | 720 Hz   | 1.76 | 1.1 dB   |
| Peaking | 4930 Hz  | 6.18 | 3.0 dB   |
| Peaking | 5912 Hz  | 2.16 | -2.9 dB  |
| Peaking | 7433 Hz  | 5.53 | 4.5 dB   |
| Peaking | 14607 Hz | 4.77 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR225/Grado%20SR225.png)