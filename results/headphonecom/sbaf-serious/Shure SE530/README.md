# Shure SE530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.2; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.8; 45 -5.0; 49 -5.1; 54 -5.5; 60 -5.9; 66 -6.2; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.6; 106 -7.9; 116 -8.1; 128 -8.4; 141 -8.7; 155 -8.9; 170 -9.1; 187 -9.3; 206 -9.3; 227 -9.4; 249 -9.4; 274 -9.4; 302 -9.1; 332 -8.9; 365 -8.6; 402 -8.4; 442 -8.3; 486 -8.3; 535 -7.8; 588 -7.5; 647 -7.2; 712 -6.8; 783 -6.6; 861 -6.5; 947 -6.7; 1042 -6.9; 1146 -7.1; 1261 -7.4; 1387 -8.0; 1526 -8.7; 1678 -9.3; 1846 -9.7; 2031 -9.9; 2234 -9.3; 2457 -7.7; 2703 -6.0; 2973 -4.4; 3270 -2.7; 3597 -1.4; 3957 -1.4; 4353 -2.5; 4788 -2.5; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.56 | 2.6 dB  |
| Peaking | 210 Hz  | 0.6  | -3.1 dB |
| Peaking | 2003 Hz | 1.92 | -4.3 dB |
| Peaking | 3646 Hz | 2.05 | 5.4 dB  |
| Peaking | 5844 Hz | 3.26 | 5.8 dB  |
| Peaking | 833 Hz  | 3.78 | 0.8 dB  |
| Peaking | 8210 Hz | 4.58 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE530/Shure%20SE530.png)