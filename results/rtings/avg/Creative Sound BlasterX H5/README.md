# Creative Sound BlasterX H5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -1.5; 23 -1.2; 25 -1.0; 28 -1.0; 31 -1.0; 34 -1.0; 37 -0.7; 41 -0.2; 45 0.0; 49 -0.0; 54 -0.6; 60 -1.6; 66 -2.6; 72 -3.5; 79 -4.4; 87 -5.2; 96 -6.0; 106 -6.7; 116 -7.3; 128 -7.8; 141 -8.2; 155 -8.6; 170 -8.8; 187 -9.0; 206 -9.2; 227 -9.3; 249 -9.4; 274 -9.4; 302 -8.7; 332 -8.8; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.3; 535 -6.6; 588 -5.9; 647 -5.0; 712 -3.9; 783 -2.7; 861 -1.5; 947 -0.4; 1042 0.2; 1146 0.6; 1261 0.7; 1387 0.4; 1526 -0.3; 1678 -1.2; 1846 -2.6; 2031 -4.5; 2234 -5.7; 2457 -6.2; 2703 -6.9; 2973 -7.4; 3270 -8.4; 3597 -7.3; 3957 -2.5; 4353 -0.5; 4788 0.3; 5267 -4.8; 5793 -6.7; 6373 -6.0; 7010 -6.9; 7711 -7.3; 8482 -6.8; 9330 -6.6; 10263 -4.7; 11289 -1.5; 12418 -1.1; 13660 -3.9; 15026 -3.5; 16529 -0.7; 18182 -2.5; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Sound BlasterX H5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Sound BlasterX H5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 173 Hz   | 0.65 | -8.6 dB  |
| Peaking | 419 Hz   | 1.24 | -5.2 dB  |
| Peaking | 2895 Hz  | 2.16 | -7.8 dB  |
| Peaking | 7878 Hz  | 1.42 | -7.5 dB  |
| Peaking | 20124 Hz | 1.95 | -10.7 dB |
| Peaking | 1229 Hz  | 1.32 | 5.9 dB   |
| Peaking | 1364 Hz  | 0.61 | -3.5 dB  |
| Peaking | 4727 Hz  | 4.08 | 5.2 dB   |
| Peaking | 5517 Hz  | 6.92 | -4.7 dB  |
| Peaking | 23162 Hz | 1.88 | -0.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Creative%20Sound%20BlasterX%20H5/Creative%20Sound%20BlasterX%20H5.png)