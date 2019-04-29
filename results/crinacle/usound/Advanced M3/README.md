# Advanced M3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.6; 25 -12.6; 28 -12.7; 31 -12.7; 34 -12.8; 37 -12.8; 41 -12.9; 45 -12.9; 49 -13.0; 54 -13.1; 60 -13.1; 66 -13.2; 72 -13.4; 79 -13.5; 87 -13.6; 96 -13.8; 106 -13.9; 116 -13.8; 128 -13.7; 141 -13.7; 155 -13.5; 170 -13.2; 187 -12.8; 206 -12.5; 227 -12.0; 249 -11.5; 274 -10.9; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.4; 442 -7.7; 486 -7.0; 535 -6.3; 588 -5.6; 647 -4.9; 712 -4.1; 783 -3.3; 861 -2.7; 947 -2.3; 1042 -2.5; 1146 -2.8; 1261 -3.4; 1387 -3.8; 1526 -3.7; 1678 -3.5; 1846 -3.4; 2031 -3.6; 2234 -4.1; 2457 -4.9; 2703 -5.3; 2973 -4.8; 3270 -4.0; 3597 -3.7; 3957 -4.2; 4353 -5.5; 4788 -5.1; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -8.0; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.6; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.42 | -4.6 dB |
| Peaking | 144 Hz  | 0.32 | -7.2 dB |
| Peaking | 929 Hz  | 0.5  | 5.0 dB  |
| Peaking | 5927 Hz | 3.93 | 6.3 dB  |
| Peaking | 964 Hz  | 2.18 | 2.4 dB  |
| Peaking | 1006 Hz | 1.19 | -1.8 dB |
| Peaking | 4111 Hz | 2.13 | 2.5 dB  |
| Peaking | 4540 Hz | 4.85 | -3.2 dB |
| Peaking | 8496 Hz | 5.23 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20M3/Advanced%20M3.png)