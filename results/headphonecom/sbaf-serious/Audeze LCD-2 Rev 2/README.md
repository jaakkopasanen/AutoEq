# Audeze LCD-2 Rev 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.5; 28 0.6; 31 0.6; 34 0.7; 37 0.6; 41 0.5; 45 0.5; 49 0.6; 54 0.6; 60 -0.5; 66 -0.8; 72 -0.9; 79 -1.1; 87 -1.1; 96 -1.5; 106 -1.8; 116 -2.0; 128 -2.2; 141 -2.4; 155 -2.8; 170 -2.9; 187 -3.3; 206 -3.3; 227 -3.3; 249 -3.0; 274 -3.1; 302 -3.0; 332 -2.5; 365 -2.1; 402 -2.2; 442 -2.3; 486 -2.4; 535 -2.4; 588 -2.4; 647 -2.4; 712 -2.3; 783 -2.3; 861 -2.0; 947 -0.8; 1042 0.2; 1146 1.4; 1261 0.6; 1387 -0.6; 1526 -1.9; 1678 -2.5; 1846 -1.4; 2031 -0.1; 2234 -0.9; 2457 -0.4; 2703 1.2; 2973 0.6; 3270 0.9; 3597 2.7; 3957 3.5; 4353 3.3; 4788 1.3; 5267 0.1; 5793 -0.2; 6373 0.3; 7010 1.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.5; 18182 -3.6; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Rev 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 214 Hz   |  0.7  | -3.3 dB |
| Peaking | 645 Hz   |  2.04 | -1.9 dB |
| Peaking | 1683 Hz  |  6.19 | -2.8 dB |
| Peaking | 4000 Hz  |  3.36 | 3.9 dB  |
| Peaking | 18781 Hz |  2.03 | -4.4 dB |
| Peaking | 36 Hz    |  1.39 | 1.0 dB  |
| Peaking | 1115 Hz  |  1.56 | -1.5 dB |
| Peaking | 1152 Hz  |  3.68 | 3.5 dB  |
| Peaking | 5561 Hz  |  5.47 | -0.8 dB |
| Peaking | 7074 Hz  | 10.17 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)