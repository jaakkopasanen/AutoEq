# Creative Sound BlasterX H5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 -1.1; 23 -0.8; 25 -0.7; 28 -0.8; 31 -1.0; 34 -1.0; 37 -0.8; 41 -0.4; 45 -0.2; 49 -0.3; 54 -0.9; 60 -1.8; 66 -2.7; 72 -3.5; 79 -4.2; 87 -4.9; 96 -5.5; 106 -6.2; 116 -6.7; 128 -7.2; 141 -7.7; 155 -8.0; 170 -8.1; 187 -8.4; 206 -8.7; 227 -8.8; 249 -8.8; 274 -8.7; 302 -7.9; 332 -7.9; 365 -7.5; 402 -7.1; 442 -6.6; 486 -6.1; 535 -5.4; 588 -4.8; 647 -4.0; 712 -3.0; 783 -2.2; 861 -1.3; 947 -0.4; 1042 0.3; 1146 0.8; 1261 0.9; 1387 0.4; 1526 -0.7; 1678 -1.6; 1846 -2.5; 2031 -4.0; 2234 -5.2; 2457 -5.8; 2703 -6.1; 2973 -5.9; 3270 -5.8; 3597 -4.1; 3957 -0.1; 4353 0.8; 4788 1.9; 5267 -1.8; 5793 -2.8; 6373 -2.3; 7010 -3.8; 7711 -5.7; 8482 -7.4; 9330 -7.7; 10263 -3.5; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound BlasterX H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound BlasterX H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 123 Hz   | 1.03 | -2.9 dB |
| Peaking | 281 Hz   | 0.5  | -8.0 dB |
| Peaking | 1146 Hz  | 1.74 | 3.4 dB  |
| Peaking | 2623 Hz  | 1.9  | -6.5 dB |
| Peaking | 8681 Hz  | 2.91 | -8.4 dB |
| Peaking | 47 Hz    | 4.1  | 1.2 dB  |
| Peaking | 3377 Hz  | 7.51 | -3.2 dB |
| Peaking | 4814 Hz  | 2.86 | 6.3 dB  |
| Peaking | 5451 Hz  | 3.36 | -5.2 dB |
| Peaking | 11436 Hz | 6.25 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Creative%20Sound%20BlasterX%20H5/Creative%20Sound%20BlasterX%20H5.png)