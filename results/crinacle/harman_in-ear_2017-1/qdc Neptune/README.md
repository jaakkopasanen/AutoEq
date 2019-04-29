# qdc Neptune
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.8; 25 -5.9; 28 -6.0; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.5; 45 -6.7; 49 -6.9; 54 -7.1; 60 -7.3; 66 -7.5; 72 -7.9; 79 -8.2; 87 -8.6; 96 -9.0; 106 -9.3; 116 -9.7; 128 -9.9; 141 -10.2; 155 -10.4; 170 -10.5; 187 -10.5; 206 -10.5; 227 -10.5; 249 -10.4; 274 -10.2; 302 -9.9; 332 -9.5; 365 -9.2; 402 -8.9; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.4; 647 -7.0; 712 -6.5; 783 -5.9; 861 -5.5; 947 -5.3; 1042 -5.5; 1146 -6.0; 1261 -6.3; 1387 -6.3; 1526 -5.9; 1678 -5.3; 1846 -4.8; 2031 -4.3; 2234 -3.9; 2457 -3.8; 2703 -3.8; 2973 -3.1; 3270 -1.8; 3597 -0.9; 3957 -0.5; 4353 -1.4; 4788 -3.4; 5267 -4.4; 5793 -1.9; 6373 -0.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -9.8; 15026 -22.3; 16529 -17.8; 18182 -6.3; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Neptune GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Neptune ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 142 Hz   | 0.72 | -3.4 dB  |
| Peaking | 295 Hz   | 0.88 | -2.7 dB  |
| Peaking | 4262 Hz  | 0.79 | 4.7 dB   |
| Peaking | 12802 Hz | 3.35 | 5.5 dB   |
| Peaking | 15341 Hz | 2.26 | -19.5 dB |
| Peaking | 4053 Hz  | 2.26 | 4.2 dB   |
| Peaking | 5434 Hz  | 1.28 | -6.4 dB  |
| Peaking | 6216 Hz  | 3.73 | 7.9 dB   |
| Peaking | 10687 Hz | 2.42 | 1.2 dB   |
| Peaking | 16404 Hz | 9.83 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -13.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Neptune/qdc%20Neptune.png)