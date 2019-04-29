# qdc Anole VX Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.8; 28 -6.2; 31 -6.4; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.1; 49 -7.3; 54 -7.5; 60 -7.7; 66 -7.8; 72 -8.0; 79 -8.2; 87 -8.5; 96 -8.6; 106 -8.8; 116 -8.9; 128 -9.0; 141 -8.9; 155 -8.8; 170 -8.7; 187 -8.5; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.3; 302 -7.1; 332 -6.8; 365 -6.5; 402 -6.4; 442 -6.3; 486 -6.2; 535 -6.2; 588 -6.3; 647 -6.4; 712 -6.6; 783 -6.7; 861 -7.0; 947 -7.4; 1042 -7.9; 1146 -8.6; 1261 -9.1; 1387 -9.0; 1526 -8.5; 1678 -7.7; 1846 -6.8; 2031 -6.1; 2234 -5.5; 2457 -4.7; 2703 -4.0; 2973 -3.7; 3270 -3.3; 3597 -3.5; 3957 -4.6; 4353 -5.5; 4788 -2.3; 5267 -0.5; 5793 -1.2; 6373 -7.4; 7010 -10.8; 7711 -10.3; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -10.2; 15026 -11.6; 16529 -13.2; 18182 -13.2; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 1335 Hz  | 2.06 | -3.0 dB |
| Peaking | 3024 Hz  | 1.86 | 3.2 dB  |
| Peaking | 5437 Hz  | 3.85 | 7.2 dB  |
| Peaking | 7096 Hz  | 4.82 | -6.2 dB |
| Peaking | 17540 Hz | 0.91 | -7.8 dB |
| Peaking | 18 Hz    | 1.99 | 1.6 dB  |
| Peaking | 97 Hz    | 0.94 | -2.0 dB |
| Peaking | 173 Hz   | 1.69 | -1.4 dB |
| Peaking | 12109 Hz | 1.86 | 2.6 dB  |
| Peaking | 13880 Hz | 2.2  | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20VX%20Treble/qdc%20Anole%20VX%20Treble.png)