# AKG K601
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.1; 31 -1.5; 34 -1.8; 37 -2.1; 41 -2.5; 45 -2.8; 49 -3.0; 54 -3.3; 60 -3.7; 66 -4.0; 72 -2.9; 79 -3.3; 87 -4.5; 96 -4.3; 106 -5.0; 116 -5.4; 128 -5.8; 141 -6.1; 155 -6.4; 170 -6.4; 187 -6.7; 206 -6.7; 227 -6.7; 249 -6.6; 274 -6.6; 302 -6.5; 332 -6.2; 365 -6.1; 402 -6.0; 442 -5.9; 486 -5.8; 535 -5.8; 588 -5.6; 647 -5.1; 712 -5.2; 783 -5.1; 861 -5.2; 947 -5.7; 1042 -6.1; 1146 -6.4; 1261 -7.0; 1387 -7.7; 1526 -8.1; 1678 -8.0; 1846 -8.2; 2031 -7.6; 2234 -7.3; 2457 -7.4; 2703 -7.4; 2973 -7.0; 3270 -6.4; 3597 -6.6; 3957 -7.5; 4353 -7.9; 4788 -7.3; 5267 -5.6; 5793 -7.9; 6373 -8.3; 7010 -5.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.63 | 5.9 dB  |
| Peaking | 77 Hz   | 2.73 | 2.0 dB  |
| Peaking | 777 Hz  | 1.43 | 1.7 dB  |
| Peaking | 1655 Hz | 1.48 | -1.9 dB |
| Peaking | 4355 Hz | 6.01 | -1.4 dB |
| Peaking | 202 Hz  | 2.22 | -0.6 dB |
| Peaking | 5378 Hz | 7.96 | 2.0 dB  |
| Peaking | 6145 Hz | 5.87 | -3.7 dB |
| Peaking | 6868 Hz | 4.76 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K601/AKG%20K601.png)