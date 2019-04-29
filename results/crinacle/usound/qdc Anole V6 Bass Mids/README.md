# qdc Anole V6 Bass Mids
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.0; 25 -8.1; 28 -8.1; 31 -8.2; 34 -8.2; 37 -8.2; 41 -8.2; 45 -8.2; 49 -8.3; 54 -8.2; 60 -8.2; 66 -8.3; 72 -8.4; 79 -8.5; 87 -8.6; 96 -8.7; 106 -8.7; 116 -8.7; 128 -8.6; 141 -8.5; 155 -8.4; 170 -8.1; 187 -7.9; 206 -7.6; 227 -7.3; 249 -6.9; 274 -6.6; 302 -6.3; 332 -6.1; 365 -5.8; 402 -5.7; 442 -5.6; 486 -5.7; 535 -5.8; 588 -5.9; 647 -6.2; 712 -6.4; 783 -6.6; 861 -6.9; 947 -7.3; 1042 -7.9; 1146 -8.7; 1261 -9.4; 1387 -9.7; 1526 -9.5; 1678 -8.8; 1846 -8.2; 2031 -7.7; 2234 -7.3; 2457 -6.9; 2703 -6.1; 2973 -5.3; 3270 -4.9; 3597 -4.9; 3957 -5.9; 4353 -6.1; 4788 -2.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -9.5; 9330 -8.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -12.2; 16529 -12.2; 18182 -12.8; 20000 -19.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 Bass Mids GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 Bass Mids ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 73 Hz    | 0.52 | -2.3 dB  |
| Peaking | 1435 Hz  | 2.11 | -3.5 dB  |
| Peaking | 3198 Hz  | 4.99 | 1.6 dB   |
| Peaking | 5702 Hz  | 2.97 | 7.3 dB   |
| Peaking | 20555 Hz | 0.31 | -11.4 dB |
| Peaking | 22 Hz    | 1.88 | -0.8 dB  |
| Peaking | 445 Hz   | 1.7  | 1.3 dB   |
| Peaking | 8790 Hz  | 5.68 | -4.6 dB  |
| Peaking | 9518 Hz  | 1.92 | 1.0 dB   |
| Peaking | 12226 Hz | 3.85 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V6%20Bass%20Mids/qdc%20Anole%20V6%20Bass%20Mids.png)