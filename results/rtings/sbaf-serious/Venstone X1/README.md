# Venstone X1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.0; 23 -2.6; 25 -3.1; 28 -3.7; 31 -4.3; 34 -4.7; 37 -5.2; 41 -5.7; 45 -6.2; 49 -6.6; 54 -7.0; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.9; 106 -9.4; 116 -9.8; 128 -10.1; 141 -10.3; 155 -10.3; 170 -10.3; 187 -10.2; 206 -10.0; 227 -9.7; 249 -9.3; 274 -9.1; 302 -8.8; 332 -8.4; 365 -7.7; 402 -6.9; 442 -5.9; 486 -4.7; 535 -3.5; 588 -2.5; 647 -1.6; 712 -1.1; 783 -1.2; 861 -0.9; 947 -0.3; 1042 0.4; 1146 1.2; 1261 2.2; 1387 3.0; 1526 4.0; 1678 5.2; 1846 6.0; 2031 5.3; 2234 3.4; 2457 1.5; 2703 1.6; 2973 2.4; 3270 2.9; 3597 2.3; 3957 -0.2; 4353 -2.8; 4788 -5.3; 5267 -8.1; 5793 -4.8; 6373 0.6; 7010 2.4; 7711 -0.6; 8482 -4.8; 9330 -1.3; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -0.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venstone X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venstone X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 95 Hz    | 0.35 | -7.7 dB |
| Peaking | 264 Hz   | 0.69 | -5.2 dB |
| Peaking | 1801 Hz  | 1.27 | 5.8 dB  |
| Peaking | 5217 Hz  | 4.8  | -9.2 dB |
| Peaking | 21864 Hz | 1.72 | -1.8 dB |
| Peaking | 2516 Hz  | 5.82 | -2.3 dB |
| Peaking | 3546 Hz  | 2.48 | 3.4 dB  |
| Peaking | 4231 Hz  | 2.85 | -2.9 dB |
| Peaking | 6859 Hz  | 6.49 | 4.3 dB  |
| Peaking | 8546 Hz  | 6.94 | -5.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Venstone%20X1/Venstone%20X1.png)