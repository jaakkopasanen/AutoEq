# Klipsch Image S4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 -8.2; 23 -8.2; 25 -8.3; 28 -8.3; 31 -8.3; 34 -8.4; 37 -8.4; 41 -8.6; 45 -8.7; 49 -8.8; 54 -9.1; 60 -9.3; 66 -9.5; 72 -9.7; 79 -9.8; 87 -10.1; 96 -10.1; 106 -10.2; 116 -10.2; 128 -10.2; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.1; 227 -8.7; 249 -8.2; 274 -7.7; 302 -7.0; 332 -6.3; 365 -5.5; 402 -4.8; 442 -4.1; 486 -3.6; 535 -2.9; 588 -2.1; 647 -1.4; 712 -0.7; 783 -0.2; 861 0.1; 947 0.0; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -1.1; 1526 -1.8; 1678 -2.2; 1846 -2.3; 2031 -2.5; 2234 -2.6; 2457 -2.2; 2703 -1.5; 2973 -0.1; 3270 2.1; 3597 3.8; 3957 3.2; 4353 1.1; 4788 -0.5; 5267 -1.7; 5793 -3.4; 6373 -1.1; 7010 1.9; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -5.3; 15026 -6.5; 16529 -1.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.27 | -7.3 dB |
| Peaking | 112 Hz   | 0.56 | -6.3 dB |
| Peaking | 247 Hz   | 0.77 | -4.6 dB |
| Peaking | 3699 Hz  | 6.84 | 4.6 dB  |
| Peaking | 14682 Hz | 3.62 | -7.7 dB |
| Peaking | 904 Hz   | 1.94 | 1.6 dB  |
| Peaking | 2313 Hz  | 1.17 | -4.3 dB |
| Peaking | 3247 Hz  | 1.13 | 2.9 dB  |
| Peaking | 5850 Hz  | 3.58 | -4.6 dB |
| Peaking | 6877 Hz  | 4.76 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4/Klipsch%20Image%20S4.png)