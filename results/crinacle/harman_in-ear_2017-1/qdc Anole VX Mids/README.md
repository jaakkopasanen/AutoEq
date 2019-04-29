# qdc Anole VX Mids
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.3; 28 -6.6; 31 -6.9; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.6; 49 -7.8; 54 -7.9; 60 -8.1; 66 -8.3; 72 -8.5; 79 -8.7; 87 -8.9; 96 -9.1; 106 -9.2; 116 -9.3; 128 -9.4; 141 -9.4; 155 -9.2; 170 -9.1; 187 -8.9; 206 -8.7; 227 -8.4; 249 -8.1; 274 -7.8; 302 -7.5; 332 -7.1; 365 -6.8; 402 -6.7; 442 -6.6; 486 -6.5; 535 -6.6; 588 -6.8; 647 -7.1; 712 -7.6; 783 -8.1; 861 -8.8; 947 -9.6; 1042 -10.4; 1146 -10.9; 1261 -10.9; 1387 -10.2; 1526 -9.1; 1678 -8.0; 1846 -7.0; 2031 -6.0; 2234 -4.9; 2457 -3.8; 2703 -2.6; 2973 -1.9; 3270 -1.4; 3597 -1.8; 3957 -3.3; 4353 -5.1; 4788 -2.5; 5267 -0.5; 5793 -0.7; 6373 -5.2; 7010 -7.3; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -14.9; 15026 -24.0; 16529 -28.5; 18182 -26.7; 20000 -18.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX Mids GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX Mids ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 138 Hz   | 0.55 | -3.2 dB  |
| Peaking | 1290 Hz  | 0.7  | -13.9 dB |
| Peaking | 3280 Hz  | 0.19 | 13.0 dB  |
| Peaking | 12192 Hz | 1.62 | 11.9 dB  |
| Peaking | 16316 Hz | 0.39 | -27.9 dB |
| Peaking | 19 Hz    | 1.83 | 1.2 dB   |
| Peaking | 4393 Hz  | 4.96 | -5.3 dB  |
| Peaking | 5556 Hz  | 2.36 | 3.5 dB   |
| Peaking | 5640 Hz  | 1.25 | 1.8 dB   |
| Peaking | 6757 Hz  | 3.62 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -25.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20VX%20Mids/qdc%20Anole%20VX%20Mids.png)