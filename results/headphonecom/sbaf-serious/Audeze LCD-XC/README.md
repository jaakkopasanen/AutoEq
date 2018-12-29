# Audeze LCD-XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.7; 28 0.9; 31 0.9; 34 0.8; 37 0.8; 41 0.9; 45 1.0; 49 1.0; 54 0.4; 60 -0.5; 66 -0.8; 72 -1.0; 79 -1.2; 87 -1.4; 96 -1.6; 106 -1.8; 116 -1.8; 128 -2.0; 141 -2.1; 155 -2.1; 170 -2.2; 187 -2.3; 206 -2.1; 227 -1.8; 249 -1.3; 274 -0.6; 302 -0.8; 332 0.1; 365 1.2; 402 1.0; 442 1.1; 486 1.1; 535 1.8; 588 2.1; 647 2.5; 712 2.4; 783 1.8; 861 1.2; 947 0.4; 1042 -0.2; 1146 -0.9; 1261 -1.8; 1387 -2.9; 1526 -3.8; 1678 -4.2; 1846 -3.9; 2031 -2.8; 2234 -0.8; 2457 0.9; 2703 2.4; 2973 2.4; 3270 2.6; 3597 -0.5; 3957 -1.8; 4353 2.8; 4788 5.7; 5267 5.1; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -4.1; 15026 -5.4; 16529 -6.4; 18182 -7.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 683 Hz   |  1.92 | 3.1 dB  |
| Peaking | 1704 Hz  |  1.6  | -4.8 dB |
| Peaking | 2732 Hz  |  3.56 | 3.8 dB  |
| Peaking | 5664 Hz  |  2.44 | 6.9 dB  |
| Peaking | 17137 Hz |  1.23 | -7.7 dB |
| Peaking | 38 Hz    |  1.16 | 1.5 dB  |
| Peaking | 160 Hz   |  0.54 | -2.5 dB |
| Peaking | 389 Hz   |  1.65 | 1.7 dB  |
| Peaking | 3912 Hz  | 11.67 | -3.7 dB |
| Peaking | 11950 Hz |  6.38 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-XC/Audeze%20LCD-XC.png)