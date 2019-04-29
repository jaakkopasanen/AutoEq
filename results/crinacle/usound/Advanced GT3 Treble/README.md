# Advanced GT3 Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.2; 25 -5.3; 28 -5.3; 31 -5.3; 34 -5.2; 37 -5.2; 41 -5.1; 45 -5.1; 49 -5.1; 54 -5.1; 60 -5.1; 66 -5.3; 72 -5.4; 79 -5.5; 87 -5.6; 96 -5.8; 106 -6.1; 116 -6.3; 128 -6.4; 141 -6.6; 155 -6.7; 170 -6.7; 187 -6.7; 206 -6.6; 227 -6.5; 249 -6.4; 274 -6.1; 302 -5.9; 332 -5.6; 365 -5.3; 402 -4.9; 442 -4.6; 486 -4.1; 535 -3.7; 588 -3.2; 647 -2.7; 712 -2.1; 783 -1.4; 861 -0.9; 947 -0.6; 1042 -0.6; 1146 -1.1; 1261 -1.6; 1387 -1.7; 1526 -1.4; 1678 -0.9; 1846 -0.5; 2031 -0.5; 2234 -0.8; 2457 -1.8; 2703 -3.5; 2973 -5.8; 3270 -7.8; 3597 -8.0; 3957 -6.6; 4353 -5.5; 4788 -6.8; 5267 -9.3; 5793 -11.1; 6373 -8.6; 7010 -7.1; 7711 -10.1; 8482 -12.1; 9330 -7.5; 10263 -4.9; 11289 -4.9; 12418 -6.0; 13660 -10.3; 15026 -11.7; 16529 -11.9; 18182 -15.9; 20000 -24.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 908 Hz   | 1.87 | 3.7 dB   |
| Peaking | 2086 Hz  | 1.1  | 4.8 dB   |
| Peaking | 3293 Hz  | 3.8  | -4.6 dB  |
| Peaking | 6287 Hz  | 1.34 | -4.6 dB  |
| Peaking | 19830 Hz | 0.62 | -18.8 dB |
| Peaking | 174 Hz   | 0.92 | -2.0 dB  |
| Peaking | 7013 Hz  | 7.64 | 3.7 dB   |
| Peaking | 8431 Hz  | 3.53 | -6.3 dB  |
| Peaking | 10667 Hz | 1.6  | 4.5 dB   |
| Peaking | 14214 Hz | 3.12 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -9.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20GT3%20Treble/Advanced%20GT3%20Treble.png)