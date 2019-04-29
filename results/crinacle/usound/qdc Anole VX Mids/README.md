# qdc Anole VX Mids
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.9; 25 -5.1; 28 -5.5; 31 -5.7; 34 -5.9; 37 -6.1; 41 -6.2; 45 -6.4; 49 -6.6; 54 -6.8; 60 -6.9; 66 -7.1; 72 -7.3; 79 -7.5; 87 -7.7; 96 -7.9; 106 -8.0; 116 -8.2; 128 -8.2; 141 -8.2; 155 -8.1; 170 -8.0; 187 -7.8; 206 -7.6; 227 -7.3; 249 -7.0; 274 -6.7; 302 -6.4; 332 -6.2; 365 -5.9; 402 -5.8; 442 -5.8; 486 -5.8; 535 -5.9; 588 -6.1; 647 -6.5; 712 -6.9; 783 -7.4; 861 -8.1; 947 -8.8; 1042 -9.6; 1146 -10.2; 1261 -10.4; 1387 -10.1; 1526 -9.2; 1678 -8.2; 1846 -7.2; 2031 -6.6; 2234 -6.1; 2457 -5.5; 2703 -4.7; 2973 -4.2; 3270 -3.7; 3597 -3.8; 3957 -4.9; 4353 -6.3; 4788 -3.3; 5267 -0.5; 5793 -1.2; 6373 -6.7; 7010 -9.7; 7711 -8.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.6; 16529 -9.7; 18182 -10.2; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX Mids GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX Mids ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 1246 Hz  | 1.97 | -4.3 dB |
| Peaking | 3113 Hz  | 2.36 | 2.9 dB  |
| Peaking | 5444 Hz  | 4.38 | 7.1 dB  |
| Peaking | 7060 Hz  | 4.77 | -4.7 dB |
| Peaking | 17687 Hz | 1.44 | -4.3 dB |
| Peaking | 16 Hz    | 0.89 | 2.4 dB  |
| Peaking | 90 Hz    | 0.94 | -0.6 dB |
| Peaking | 143 Hz   | 0.94 | -1.5 dB |
| Peaking | 437 Hz   | 1.63 | 1.2 dB  |
| Peaking | 2205 Hz  | 3.74 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20VX%20Mids/qdc%20Anole%20VX%20Mids.png)