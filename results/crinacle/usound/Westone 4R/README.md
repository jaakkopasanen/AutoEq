# Westone 4R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.7; 25 -3.4; 28 -4.3; 31 -4.9; 34 -5.5; 37 -5.9; 41 -6.5; 45 -6.9; 49 -7.4; 54 -7.8; 60 -8.3; 66 -8.8; 72 -9.3; 79 -9.7; 87 -10.2; 96 -10.7; 106 -11.2; 116 -11.7; 128 -12.0; 141 -12.3; 155 -12.5; 170 -12.6; 187 -12.8; 206 -12.9; 227 -12.9; 249 -12.7; 274 -12.6; 302 -12.4; 332 -12.2; 365 -11.8; 402 -11.4; 442 -11.0; 486 -10.5; 535 -9.9; 588 -9.2; 647 -8.5; 712 -7.6; 783 -6.8; 861 -6.1; 947 -5.7; 1042 -5.8; 1146 -6.2; 1261 -6.6; 1387 -6.4; 1526 -5.6; 1678 -4.2; 1846 -2.7; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.0; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -6.4; 7711 -10.0; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.0; 18182 -11.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.92 | 5.7 dB  |
| Peaking | 208 Hz   | 0.41 | -6.7 dB |
| Peaking | 3864 Hz  | 0.52 | 7.0 dB  |
| Peaking | 7911 Hz  | 3.68 | -7.6 dB |
| Peaking | 17788 Hz | 1.84 | -6.0 dB |
| Peaking | 926 Hz   | 1.61 | 3.6 dB  |
| Peaking | 1640 Hz  | 0.67 | -4.8 dB |
| Peaking | 2082 Hz  | 1.67 | 5.4 dB  |
| Peaking | 6025 Hz  | 5.05 | 2.4 dB  |
| Peaking | 10993 Hz | 3.29 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%204R/Westone%204R.png)