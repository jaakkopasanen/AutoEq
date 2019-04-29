# qdc Anole VX Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.0; 28 -7.3; 31 -7.6; 34 -7.8; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.5; 54 -8.6; 60 -8.8; 66 -9.0; 72 -9.2; 79 -9.4; 87 -9.6; 96 -9.8; 106 -9.9; 116 -10.1; 128 -10.1; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.4; 227 -9.1; 249 -8.8; 274 -8.5; 302 -8.2; 332 -7.8; 365 -7.4; 402 -7.2; 442 -7.1; 486 -6.9; 535 -6.9; 588 -6.9; 647 -7.1; 712 -7.2; 783 -7.4; 861 -7.7; 947 -8.1; 1042 -8.7; 1146 -9.3; 1261 -9.5; 1387 -9.2; 1526 -8.4; 1678 -7.5; 1846 -6.6; 2031 -5.6; 2234 -4.4; 2457 -3.0; 2703 -1.9; 2973 -1.4; 3270 -1.1; 3597 -1.5; 3957 -3.0; 4353 -4.4; 4788 -1.6; 5267 -0.5; 5793 -0.6; 6373 -5.9; 7010 -8.5; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.8; 13660 -19.1; 15026 -28.0; 16529 -32.1; 18182 -29.7; 20000 -21.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 124 Hz   | 0.49 | -3.7 dB  |
| Peaking | 1372 Hz  | 0.96 | -7.7 dB  |
| Peaking | 4477 Hz  | 0.32 | 14.2 dB  |
| Peaking | 11732 Hz | 1.51 | 14.9 dB  |
| Peaking | 16101 Hz | 0.33 | -31.9 dB |
| Peaking | 4315 Hz  | 4.34 | -5.8 dB  |
| Peaking | 5094 Hz  | 1.78 | 4.7 dB   |
| Peaking | 5888 Hz  | 6.84 | 2.8 dB   |
| Peaking | 6903 Hz  | 2.54 | -5.4 dB  |
| Peaking | 8397 Hz  | 3.01 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 16000 Hz | 1.41 | -30.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20VX%20Treble/qdc%20Anole%20VX%20Treble.png)