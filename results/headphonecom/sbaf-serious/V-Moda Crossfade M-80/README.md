# V-Moda Crossfade M-80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.2; 25 -4.6; 28 -5.2; 31 -5.7; 34 -6.1; 37 -6.4; 41 -6.7; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.7; 66 -7.9; 72 -7.9; 79 -7.8; 87 -8.0; 96 -8.2; 106 -8.0; 116 -7.9; 128 -8.1; 141 -8.2; 155 -8.1; 170 -8.0; 187 -7.9; 206 -7.7; 227 -8.0; 249 -8.1; 274 -7.1; 302 -6.1; 332 -5.7; 365 -5.0; 402 -4.3; 442 -3.7; 486 -2.7; 535 -1.7; 588 -1.1; 647 -1.2; 712 -1.6; 783 -2.3; 861 -3.3; 947 -4.5; 1042 -5.7; 1146 -7.0; 1261 -8.1; 1387 -8.6; 1526 -8.7; 1678 -8.2; 1846 -6.5; 2031 -5.1; 2234 -4.3; 2457 -3.8; 2703 -4.1; 2973 -5.1; 3270 -6.0; 3597 -5.5; 3957 -3.5; 4353 -3.2; 4788 -3.3; 5267 -0.9; 5793 -0.5; 6373 -1.3; 7010 -2.6; 7711 -4.8; 8482 -5.4; 9330 -5.8; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.77 | -2.5 dB |
| Peaking | 214 Hz  | 0.87 | -2.7 dB |
| Peaking | 616 Hz  | 1.3  | 4.8 dB  |
| Peaking | 1384 Hz | 2.28 | -4.7 dB |
| Peaking | 5716 Hz | 2.76 | 5.0 dB  |
| Peaking | 19 Hz   | 2.4  | 1.9 dB  |
| Peaking | 1701 Hz | 5.31 | -1.7 dB |
| Peaking | 2600 Hz | 1.31 | 1.7 dB  |
| Peaking | 3302 Hz | 5.11 | -2.6 dB |
| Peaking | 8923 Hz | 5.64 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20Crossfade%20M-80/V-Moda%20Crossfade%20M-80.png)