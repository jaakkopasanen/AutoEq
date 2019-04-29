# qdc Anole V6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.4; 25 -8.4; 28 -8.5; 31 -8.5; 34 -8.6; 37 -8.6; 41 -8.6; 45 -8.7; 49 -8.7; 54 -8.7; 60 -8.7; 66 -8.8; 72 -8.9; 79 -9.0; 87 -9.1; 96 -9.2; 106 -9.3; 116 -9.3; 128 -9.2; 141 -9.2; 155 -9.0; 170 -8.8; 187 -8.6; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.1; 332 -6.9; 365 -6.7; 402 -6.5; 442 -6.4; 486 -6.3; 535 -6.2; 588 -6.2; 647 -6.1; 712 -6.0; 783 -5.9; 861 -5.9; 947 -6.1; 1042 -6.6; 1146 -7.4; 1261 -8.4; 1387 -8.9; 1526 -8.9; 1678 -8.6; 1846 -8.1; 2031 -7.7; 2234 -7.3; 2457 -6.6; 2703 -5.7; 2973 -5.0; 3270 -4.8; 3597 -4.9; 3957 -5.3; 4353 -4.9; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.8; 7711 -7.9; 8482 -10.3; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.8; 15026 -12.9; 16529 -13.2; 18182 -14.2; 20000 -21.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.41 | -2.1 dB  |
| Peaking | 136 Hz   | 1.05 | -2.1 dB  |
| Peaking | 1529 Hz  | 2.82 | -2.8 dB  |
| Peaking | 5499 Hz  | 2.6  | 7.3 dB   |
| Peaking | 20328 Hz | 0.35 | -13.8 dB |
| Peaking | 715 Hz   | 1.77 | 0.8 dB   |
| Peaking | 3121 Hz  | 5.32 | 1.5 dB   |
| Peaking | 8435 Hz  | 6.06 | -4.5 dB  |
| Peaking | 11592 Hz | 2.69 | 2.6 dB   |
| Peaking | 18234 Hz | 4.6  | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -8.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Anole%20V6/qdc%20Anole%20V6.png)