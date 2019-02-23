# Shure SE420
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.3; 25 -2.6; 28 -2.9; 31 -3.3; 34 -3.5; 37 -3.8; 41 -4.1; 45 -4.4; 49 -4.7; 54 -5.1; 60 -5.5; 66 -6.0; 72 -6.3; 79 -6.8; 87 -7.2; 96 -7.4; 106 -7.9; 116 -8.2; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.4; 227 -9.4; 249 -9.5; 274 -9.3; 302 -9.1; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.4; 486 -8.1; 535 -7.9; 588 -7.4; 647 -7.2; 712 -7.1; 783 -6.9; 861 -6.9; 947 -7.1; 1042 -7.4; 1146 -7.8; 1261 -8.1; 1387 -8.6; 1526 -9.2; 1678 -9.5; 1846 -9.6; 2031 -9.8; 2234 -9.9; 2457 -9.3; 2703 -8.0; 2973 -6.2; 3270 -4.2; 3597 -2.7; 3957 -2.4; 4353 -2.6; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE420 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.71 | 4.4 dB  |
| Peaking | 45 Hz   | 1.23 | 1.0 dB  |
| Peaking | 211 Hz  | 0.61 | -3.1 dB |
| Peaking | 2033 Hz | 1.5  | -4.4 dB |
| Peaking | 4948 Hz | 1.37 | 6.5 dB  |
| Peaking | 2612 Hz | 5.01 | -1.1 dB |
| Peaking | 3582 Hz | 2.82 | 2.0 dB  |
| Peaking | 4441 Hz | 4.5  | -2.1 dB |
| Peaking | 6395 Hz | 3.24 | 3.8 dB  |
| Peaking | 7421 Hz | 1.75 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE420/Shure%20SE420.png)