# Grado SR 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.4; 66 4.4; 72 3.3; 79 2.1; 87 1.1; 96 0.3; 106 -0.1; 116 -0.6; 128 -0.8; 141 -1.1; 155 -1.1; 170 -1.0; 187 -0.8; 206 -0.8; 227 -0.7; 249 -0.5; 274 -0.1; 302 -0.1; 332 0.1; 365 0.3; 402 0.4; 442 0.5; 486 0.6; 535 0.6; 588 0.7; 647 0.7; 712 0.7; 783 0.6; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.1; 1387 -2.0; 1526 -3.2; 1678 -4.1; 1846 -5.0; 2031 -5.9; 2234 -6.1; 2457 -5.6; 2703 -5.2; 2973 -4.5; 3270 -4.1; 3597 -5.6; 3957 -10.2; 4353 -6.4; 4788 -4.2; 5267 -4.5; 5793 -7.3; 6373 -3.6; 7010 -5.4; 7711 -7.3; 8482 -9.7; 9330 -10.9; 10263 -8.5; 11289 -2.9; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 35 Hz    |  0.88 | 7.2 dB   |
| Peaking | 2114 Hz  |  1.9  | -5.8 dB  |
| Peaking | 4037 Hz  |  2.61 | -7.3 dB  |
| Peaking | 8947 Hz  |  2.24 | -11.1 dB |
| Peaking | 20448 Hz |  3.85 | -7.1 dB  |
| Peaking | 62 Hz    |  2.89 | 2.6 dB   |
| Peaking | 133 Hz   |  0.88 | -1.8 dB  |
| Peaking | 644 Hz   |  1.14 | 1.1 dB   |
| Peaking | 5795 Hz  | 11.91 | -4.1 dB  |
| Peaking | 12546 Hz |  4.06 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR%2080/Grado%20SR%2080.png)