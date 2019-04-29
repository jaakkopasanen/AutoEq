# Sony XBA-A3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.4; 25 -2.8; 28 -3.2; 31 -3.6; 34 -3.8; 37 -4.1; 41 -4.4; 45 -4.7; 49 -5.0; 54 -5.3; 60 -5.6; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.5; 106 -8.0; 116 -8.2; 128 -8.4; 141 -8.6; 155 -8.6; 170 -8.6; 187 -8.5; 206 -8.4; 227 -8.0; 249 -7.7; 274 -7.3; 302 -6.8; 332 -6.4; 365 -5.9; 402 -5.5; 442 -5.0; 486 -4.6; 535 -4.2; 588 -3.8; 647 -3.4; 712 -3.0; 783 -2.5; 861 -2.1; 947 -2.0; 1042 -2.4; 1146 -3.2; 1261 -4.2; 1387 -4.8; 1526 -4.9; 1678 -4.6; 1846 -3.9; 2031 -3.0; 2234 -2.2; 2457 -1.5; 2703 -1.1; 2973 -1.2; 3270 -0.9; 3597 -0.6; 3957 -0.5; 4353 -3.0; 4788 -7.1; 5267 -7.2; 5793 -2.0; 6373 -4.8; 7010 -4.1; 7711 -4.3; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -6.8; 12418 -10.0; 13660 -10.4; 15026 -8.8; 16529 -8.1; 18182 -7.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.79 | 3.2 dB  |
| Peaking | 155 Hz   | 0.65 | -4.3 dB |
| Peaking | 819 Hz   | 1.69 | 2.8 dB  |
| Peaking | 3145 Hz  | 1.85 | 4.3 dB  |
| Peaking | 14237 Hz | 1.28 | -5.9 dB |
| Peaking | 1499 Hz  | 4.91 | -1.4 dB |
| Peaking | 4971 Hz  | 5.54 | -9.0 dB |
| Peaking | 5150 Hz  | 1.85 | 4.2 dB  |
| Peaking | 10111 Hz | 4.07 | 2.2 dB  |
| Peaking | 16854 Hz | 0.22 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20XBA-A3/Sony%20XBA-A3.png)