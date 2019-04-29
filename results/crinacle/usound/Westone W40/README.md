# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.3; 25 -2.8; 28 -3.4; 31 -4.0; 34 -4.6; 37 -5.1; 41 -5.7; 45 -6.1; 49 -6.4; 54 -6.8; 60 -7.4; 66 -7.9; 72 -8.4; 79 -8.9; 87 -9.4; 96 -9.9; 106 -10.4; 116 -10.8; 128 -11.2; 141 -11.6; 155 -11.9; 170 -12.1; 187 -12.3; 206 -12.3; 227 -12.3; 249 -12.3; 274 -12.2; 302 -12.0; 332 -11.8; 365 -11.5; 402 -11.2; 442 -10.9; 486 -10.4; 535 -9.9; 588 -9.3; 647 -8.6; 712 -7.9; 783 -7.0; 861 -6.3; 947 -5.9; 1042 -6.0; 1146 -6.5; 1261 -7.0; 1387 -7.0; 1526 -6.3; 1678 -5.1; 1846 -3.6; 2031 -2.2; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.7; 3270 -0.9; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.0; 8482 -10.3; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.82 | 4.9 dB  |
| Peaking | 117 Hz   | 0.89 | -1.7 dB |
| Peaking | 262 Hz   | 0.51 | -5.5 dB |
| Peaking | 4048 Hz  | 0.6  | 7.0 dB  |
| Peaking | 8289 Hz  | 3.8  | -7.7 dB |
| Peaking | 924 Hz   | 2.25 | 2.0 dB  |
| Peaking | 1392 Hz  | 2.6  | -1.9 dB |
| Peaking | 2271 Hz  | 2.74 | 2.6 dB  |
| Peaking | 6234 Hz  | 3.64 | 2.5 dB  |
| Peaking | 10814 Hz | 0.05 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20W40/Westone%20W40.png)