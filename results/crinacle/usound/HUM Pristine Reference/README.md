# HUM Pristine Reference
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.1; 28 -3.4; 31 -3.7; 34 -4.0; 37 -4.2; 41 -4.5; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.7; 72 -6.1; 79 -6.5; 87 -6.8; 96 -7.3; 106 -7.7; 116 -8.0; 128 -8.3; 141 -8.6; 155 -8.8; 170 -8.8; 187 -8.9; 206 -8.9; 227 -8.8; 249 -8.6; 274 -8.4; 302 -8.1; 332 -7.9; 365 -7.5; 402 -7.2; 442 -6.8; 486 -6.4; 535 -6.0; 588 -5.6; 647 -5.1; 712 -4.6; 783 -4.1; 861 -3.7; 947 -3.6; 1042 -4.0; 1146 -4.9; 1261 -6.0; 1387 -7.0; 1526 -7.8; 1678 -8.5; 1846 -9.3; 2031 -9.5; 2234 -8.8; 2457 -7.2; 2703 -5.2; 2973 -4.0; 3270 -3.8; 3597 -5.0; 3957 -6.4; 4353 -5.9; 4788 -6.4; 5267 -7.8; 5793 -4.5; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HUM Pristine Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HUM Pristine Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.27 | 3.8 dB  |
| Peaking | 184 Hz   | 0.6  | -3.3 dB |
| Peaking | 870 Hz   | 1.62 | 2.9 dB  |
| Peaking | 1866 Hz  | 2.82 | -4.2 dB |
| Peaking | 6442 Hz  | 7.44 | 6.1 dB  |
| Peaking | 1415 Hz  | 7.6  | -0.9 dB |
| Peaking | 2277 Hz  | 6.92 | -1.5 dB |
| Peaking | 3077 Hz  | 3.92 | 2.8 dB  |
| Peaking | 5218 Hz  | 8.58 | -2.6 dB |
| Peaking | 22050 Hz | 1.97 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/HUM%20Pristine%20Reference/HUM%20Pristine%20Reference.png)