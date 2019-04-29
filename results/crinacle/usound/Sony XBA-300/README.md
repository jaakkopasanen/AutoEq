# Sony XBA-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.6; 25 -2.9; 28 -3.2; 31 -3.5; 34 -3.7; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.6; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.5; 96 -6.9; 106 -7.2; 116 -7.4; 128 -7.6; 141 -7.7; 155 -7.8; 170 -7.8; 187 -7.7; 206 -7.5; 227 -7.3; 249 -6.9; 274 -6.6; 302 -6.2; 332 -5.8; 365 -5.4; 402 -5.0; 442 -4.5; 486 -3.9; 535 -3.4; 588 -2.9; 647 -2.3; 712 -1.7; 783 -1.1; 861 -0.7; 947 -0.5; 1042 -0.8; 1146 -1.5; 1261 -2.3; 1387 -2.8; 1526 -2.9; 1678 -2.9; 1846 -2.9; 2031 -3.4; 2234 -4.3; 2457 -5.9; 2703 -7.6; 2973 -8.4; 3270 -8.5; 3597 -8.2; 3957 -8.9; 4353 -9.0; 4788 -6.1; 5267 -3.7; 5793 -2.3; 6373 -1.7; 7010 -3.8; 7711 -8.1; 8482 -10.2; 9330 -9.1; 10263 -8.5; 11289 -9.6; 12418 -9.0; 13660 -5.6; 15026 -5.2; 16529 -8.1; 18182 -12.9; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 987 Hz   | 1.16 | 4.9 dB  |
| Peaking | 3379 Hz  | 2.57 | -4.2 dB |
| Peaking | 10477 Hz | 1.96 | -4.4 dB |
| Peaking | 18140 Hz | 2.27 | -6.1 dB |
| Peaking | 19640 Hz | 1.56 | -7.2 dB |
| Peaking | 18 Hz    | 0.66 | 3.0 dB  |
| Peaking | 151 Hz   | 0.85 | -3.0 dB |
| Peaking | 4340 Hz  | 4.67 | -4.2 dB |
| Peaking | 6477 Hz  | 1.58 | 5.8 dB  |
| Peaking | 8096 Hz  | 3.44 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20XBA-300/Sony%20XBA-300.png)