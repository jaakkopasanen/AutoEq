# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.7; 66 5.3; 72 4.4; 79 3.8; 87 3.6; 96 3.1; 106 2.7; 116 2.4; 128 2.1; 141 1.7; 155 1.6; 170 2.0; 187 2.2; 206 1.8; 227 1.8; 249 1.8; 274 1.8; 302 2.2; 332 2.6; 365 2.6; 402 2.7; 442 2.5; 486 2.4; 535 2.0; 588 2.0; 647 2.0; 712 1.6; 783 1.2; 861 0.8; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.5; 1387 -2.6; 1526 -3.5; 1678 -3.6; 1846 -4.6; 2031 -5.3; 2234 -5.4; 2457 -5.3; 2703 -4.1; 2973 -3.0; 3270 -1.5; 3597 0.3; 3957 -0.1; 4353 -1.8; 4788 -5.1; 5267 -2.8; 5793 -4.9; 6373 -1.8; 7010 -0.3; 7711 -6.6; 8482 -10.0; 9330 -9.4; 10263 -6.3; 11289 -0.5; 12418 0.0; 13660 -1.3; 15026 -1.7; 16529 0.0; 18182 0.0; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 35 Hz    |  0.45 | 6.5 dB   |
| Peaking | 464 Hz   |  0.73 | 2.5 dB   |
| Peaking | 1521 Hz  |  2.05 | -2.0 dB  |
| Peaking | 2245 Hz  |  1.75 | -5.2 dB  |
| Peaking | 8851 Hz  |  2.8  | -10.9 dB |
| Peaking | 3777 Hz  |  3.99 | 3.8 dB   |
| Peaking | 5077 Hz  |  1.67 | -3.6 dB  |
| Peaking | 6669 Hz  | 10.5  | 3.0 dB   |
| Peaking | 6969 Hz  | 10.03 | 3.5 dB   |
| Peaking | 19800 Hz |  4.95 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)