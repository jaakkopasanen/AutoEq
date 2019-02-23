# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.9; 25 -5.0; 28 -5.0; 31 -5.1; 34 -5.2; 37 -5.4; 41 -5.5; 45 -5.6; 49 -5.8; 54 -6.0; 60 -6.3; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.5; 96 -7.8; 106 -8.1; 116 -8.3; 128 -8.4; 141 -8.7; 155 -8.9; 170 -9.1; 187 -9.0; 206 -9.1; 227 -9.1; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.5; 365 -8.3; 402 -8.1; 442 -8.1; 486 -8.0; 535 -7.8; 588 -7.6; 647 -7.4; 712 -7.5; 783 -7.7; 861 -8.1; 947 -8.7; 1042 -9.6; 1146 -10.3; 1261 -11.2; 1387 -12.3; 1526 -13.4; 1678 -13.9; 1846 -13.5; 2031 -11.9; 2234 -9.4; 2457 -6.2; 2703 -3.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -2.9; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.59 | 1.7 dB   |
| Peaking | 188 Hz  | 0.62 | -2.7 dB  |
| Peaking | 1777 Hz | 1.31 | -10.0 dB |
| Peaking | 3181 Hz | 1.38 | 9.2 dB   |
| Peaking | 5873 Hz | 3.59 | 5.2 dB   |
| Peaking | 724 Hz  | 4.08 | 0.6 dB   |
| Peaking | 6587 Hz | 8.59 | 1.8 dB   |
| Peaking | 7909 Hz | 2.38 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE315/Shure%20SE315.png)