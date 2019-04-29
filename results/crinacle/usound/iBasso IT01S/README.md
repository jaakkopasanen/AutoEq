# iBasso IT01S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.3; 25 -2.5; 28 -2.7; 31 -3.0; 34 -3.2; 37 -3.3; 41 -3.5; 45 -3.7; 49 -3.9; 54 -4.2; 60 -4.5; 66 -4.7; 72 -5.0; 79 -5.3; 87 -5.7; 96 -6.1; 106 -6.4; 116 -6.7; 128 -6.9; 141 -7.1; 155 -7.2; 170 -7.2; 187 -7.1; 206 -7.0; 227 -6.8; 249 -6.6; 274 -6.3; 302 -6.0; 332 -5.6; 365 -5.2; 402 -4.8; 442 -4.4; 486 -3.9; 535 -3.5; 588 -3.1; 647 -2.6; 712 -1.9; 783 -1.2; 861 -0.7; 947 -0.5; 1042 -0.7; 1146 -1.2; 1261 -1.9; 1387 -2.3; 1526 -2.5; 1678 -2.5; 1846 -2.6; 2031 -3.0; 2234 -3.7; 2457 -4.1; 2703 -3.8; 2973 -2.6; 3270 -1.4; 3597 -0.9; 3957 -1.3; 4353 -3.1; 4788 -6.9; 5267 -7.6; 5793 -3.4; 6373 -0.7; 7010 -2.2; 7711 -5.9; 8482 -4.0; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -4.2; 13660 -3.8; 15026 -3.8; 16529 -4.0; 18182 -4.4; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 176 Hz   | 0.68 | -3.6 dB |
| Peaking | 931 Hz   | 1.34 | 3.6 dB  |
| Peaking | 3808 Hz  | 3.03 | 3.8 dB  |
| Peaking | 5060 Hz  | 3.87 | -5.6 dB |
| Peaking | 6342 Hz  | 6.32 | 4.4 dB  |
| Peaking | 21 Hz    | 1.15 | 1.8 dB  |
| Peaking | 2482 Hz  | 5.59 | -1.4 dB |
| Peaking | 3646 Hz  | 0.44 | 0.3 dB  |
| Peaking | 7826 Hz  | 8.94 | -2.8 dB |
| Peaking | 17551 Hz | 2.94 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/iBasso%20IT01S/iBasso%20IT01S.png)