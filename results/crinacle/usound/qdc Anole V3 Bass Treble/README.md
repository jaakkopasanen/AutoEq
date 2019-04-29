# qdc Anole V3 Bass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -10.0; 28 -10.1; 31 -10.2; 34 -10.3; 37 -10.4; 41 -10.5; 45 -10.6; 49 -10.7; 54 -10.8; 60 -10.9; 66 -11.1; 72 -11.3; 79 -11.6; 87 -11.8; 96 -12.1; 106 -12.3; 116 -12.5; 128 -12.6; 141 -12.6; 155 -12.8; 170 -12.6; 187 -12.6; 206 -12.4; 227 -12.1; 249 -11.8; 274 -11.4; 302 -11.0; 332 -10.6; 365 -10.1; 402 -9.6; 442 -9.1; 486 -8.4; 535 -7.8; 588 -7.0; 647 -6.2; 712 -5.4; 783 -4.4; 861 -3.6; 947 -3.0; 1042 -2.6; 1146 -2.7; 1261 -2.8; 1387 -2.6; 1526 -2.0; 1678 -1.1; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.9; 2703 -1.9; 2973 -1.9; 3270 -1.1; 3597 -0.5; 3957 -1.0; 4353 -2.0; 4788 -1.3; 5267 -2.1; 5793 -5.4; 6373 -8.5; 7010 -9.7; 7711 -11.5; 8482 -11.3; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 Bass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 Bass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.62 | -2.5 dB |
| Peaking | 199 Hz  | 0.31 | -6.7 dB |
| Peaking | 2129 Hz | 0.25 | 6.4 dB  |
| Peaking | 5006 Hz | 3.84 | 2.6 dB  |
| Peaking | 7540 Hz | 1.72 | -8.8 dB |
| Peaking | 976 Hz  | 1.98 | 2.2 dB  |
| Peaking | 1315 Hz | 0.95 | -2.5 dB |
| Peaking | 1944 Hz | 1.53 | 2.3 dB  |
| Peaking | 2957 Hz | 2.08 | -1.7 dB |
| Peaking | 3551 Hz | 4.54 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V3%20Bass%20Treble/qdc%20Anole%20V3%20Bass%20Treble.png)