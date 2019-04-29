# qdc Anole V3 Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.9; 25 -8.0; 28 -8.2; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.8; 45 -8.9; 49 -9.0; 54 -9.1; 60 -9.3; 66 -9.5; 72 -9.8; 79 -10.1; 87 -10.4; 96 -10.7; 106 -11.0; 116 -11.2; 128 -11.4; 141 -11.5; 155 -11.6; 170 -11.6; 187 -11.5; 206 -11.4; 227 -11.2; 249 -11.0; 274 -10.7; 302 -10.4; 332 -10.1; 365 -9.7; 402 -9.3; 442 -8.8; 486 -8.2; 535 -7.7; 588 -7.0; 647 -6.3; 712 -5.5; 783 -4.7; 861 -3.9; 947 -3.3; 1042 -3.0; 1146 -3.2; 1261 -3.4; 1387 -3.3; 1526 -2.7; 1678 -1.8; 1846 -0.9; 2031 -0.5; 2234 -0.6; 2457 -1.4; 2703 -2.3; 2973 -2.2; 3270 -1.4; 3597 -0.7; 3957 -1.2; 4353 -2.1; 4788 -1.5; 5267 -2.4; 5793 -5.5; 6373 -8.5; 7010 -9.6; 7711 -11.4; 8482 -12.0; 9330 -9.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 167 Hz   | 0.33 | -5.1 dB |
| Peaking | 945 Hz   | 1.19 | 3.7 dB  |
| Peaking | 1999 Hz  | 1.95 | 4.3 dB  |
| Peaking | 4259 Hz  | 1.02 | 5.7 dB  |
| Peaking | 7695 Hz  | 2.06 | -7.4 dB |
| Peaking | 26 Hz    | 1.73 | -0.8 dB |
| Peaking | 5177 Hz  | 9.33 | 1.3 dB  |
| Peaking | 6223 Hz  | 9    | -1.6 dB |
| Peaking | 10413 Hz | 6.46 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V3%20Treble/qdc%20Anole%20V3%20Treble.png)