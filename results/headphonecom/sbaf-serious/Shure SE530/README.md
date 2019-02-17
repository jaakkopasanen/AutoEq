# Shure SE530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.7; 25 -3.8; 28 -3.9; 31 -4.0; 34 -4.1; 37 -4.2; 41 -4.4; 45 -4.7; 49 -4.8; 54 -5.1; 60 -5.6; 66 -5.8; 72 -6.1; 79 -6.6; 87 -7.0; 96 -7.3; 106 -7.5; 116 -7.8; 128 -8.1; 141 -8.4; 155 -8.6; 170 -8.8; 187 -8.9; 206 -9.0; 227 -9.0; 249 -9.1; 274 -9.1; 302 -8.7; 332 -8.6; 365 -8.3; 402 -8.1; 442 -8.0; 486 -7.9; 535 -7.5; 588 -7.2; 647 -6.8; 712 -6.4; 783 -6.2; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.7; 1526 -8.3; 1678 -8.9; 1846 -9.3; 2031 -9.6; 2234 -9.0; 2457 -7.4; 2703 -5.6; 2973 -4.1; 3270 -2.4; 3597 -1.1; 3957 -1.1; 4353 -2.2; 4788 -2.2; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.56 | 2.9 dB  |
| Peaking | 207 Hz  | 0.68 | -2.8 dB |
| Peaking | 2011 Hz | 2.1  | -4.1 dB |
| Peaking | 3658 Hz | 2    | 5.6 dB  |
| Peaking | 5818 Hz | 3.19 | 5.7 dB  |
| Peaking | 848 Hz  | 2.97 | 0.9 dB  |
| Peaking | 1534 Hz | 6.82 | -0.6 dB |
| Peaking | 8229 Hz | 4.5  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE530/Shure%20SE530.png)