# Noble Sage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.2; 28 -4.4; 31 -4.5; 34 -4.7; 37 -4.8; 41 -5.0; 45 -5.2; 49 -5.4; 54 -5.6; 60 -5.8; 66 -6.2; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.7; 106 -8.1; 116 -8.4; 128 -8.7; 141 -8.9; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.2; 227 -9.1; 249 -9.0; 274 -8.8; 302 -8.5; 332 -8.2; 365 -7.9; 402 -7.5; 442 -7.1; 486 -6.7; 535 -6.3; 588 -5.8; 647 -5.3; 712 -4.7; 783 -4.2; 861 -3.7; 947 -3.4; 1042 -3.6; 1146 -4.1; 1261 -4.7; 1387 -5.0; 1526 -5.0; 1678 -4.7; 1846 -4.3; 2031 -4.1; 2234 -3.9; 2457 -3.5; 2703 -2.7; 2973 -1.7; 3270 -0.9; 3597 -0.5; 3957 -1.0; 4353 -2.6; 4788 -4.6; 5267 -4.5; 5793 -3.0; 6373 -3.0; 7010 -6.1; 7711 -5.5; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Sage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Sage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.21 | 1.7 dB  |
| Peaking | 182 Hz   | 0.49 | -4.1 dB |
| Peaking | 891 Hz   | 1.73 | 2.5 dB  |
| Peaking | 3466 Hz  | 1.76 | 5.0 dB  |
| Peaking | 22050 Hz | 2.25 | 0.3 dB  |
| Peaking | 4129 Hz  | 6.12 | 0.9 dB  |
| Peaking | 4926 Hz  | 3.64 | -1.8 dB |
| Peaking | 6142 Hz  | 3.95 | 3.0 dB  |
| Peaking | 7090 Hz  | 5.33 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Sage/Noble%20Sage.png)