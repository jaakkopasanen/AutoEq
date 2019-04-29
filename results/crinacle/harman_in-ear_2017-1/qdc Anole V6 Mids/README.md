# qdc Anole V6 Mids
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.0; 25 -8.1; 28 -8.1; 31 -8.2; 34 -8.2; 37 -8.2; 41 -8.2; 45 -8.3; 49 -8.3; 54 -8.3; 60 -8.3; 66 -8.4; 72 -8.6; 79 -8.6; 87 -8.7; 96 -8.9; 106 -8.9; 116 -8.9; 128 -8.8; 141 -8.8; 155 -8.7; 170 -8.5; 187 -8.3; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.2; 302 -6.9; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.3; 486 -6.4; 535 -6.5; 588 -6.7; 647 -7.0; 712 -7.3; 783 -7.6; 861 -7.9; 947 -8.4; 1042 -9.0; 1146 -9.7; 1261 -10.2; 1387 -10.2; 1526 -9.8; 1678 -9.1; 1846 -8.3; 2031 -7.5; 2234 -6.6; 2457 -5.5; 2703 -4.4; 2973 -3.4; 3270 -3.0; 3597 -3.4; 3957 -4.7; 4353 -5.3; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -10.2; 10263 -6.7; 11289 -6.5; 12418 -7.2; 13660 -18.3; 15026 -29.0; 16529 -31.4; 18182 -29.4; 20000 -31.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 Mids GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 Mids ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1368 Hz  | 2.01 | -3.8 dB  |
| Peaking | 5872 Hz  | 0.24 | 28.4 dB  |
| Peaking | 8955 Hz  | 2.99 | -5.4 dB  |
| Peaking | 12149 Hz | 0.97 | 21.1 dB  |
| Peaking | 15200 Hz | 0.16 | -48.8 dB |
| Peaking | 39 Hz    | 0.51 | -1.7 dB  |
| Peaking | 123 Hz   | 1.29 | -1.9 dB  |
| Peaking | 3128 Hz  | 3.36 | 2.1 dB   |
| Peaking | 4350 Hz  | 3.87 | -4.3 dB  |
| Peaking | 5101 Hz  | 3.34 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 16000 Hz | 1.41 | -32.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V6%20Mids/qdc%20Anole%20V6%20Mids.png)