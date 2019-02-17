# Tin Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.2; 34 -1.6; 37 -1.9; 41 -2.4; 45 -2.7; 49 -3.1; 54 -3.5; 60 -3.9; 66 -4.4; 72 -4.8; 79 -5.3; 87 -5.8; 96 -6.3; 106 -6.8; 116 -7.2; 128 -7.6; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.7; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.8; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.2; 535 -7.9; 588 -7.6; 647 -7.3; 712 -6.9; 783 -6.4; 861 -6.0; 947 -6.4; 1042 -6.2; 1146 -6.0; 1261 -5.9; 1387 -5.5; 1526 -4.9; 1678 -4.1; 1846 -3.2; 2031 -2.6; 2234 -2.5; 2457 -3.0; 2703 -4.0; 2973 -4.6; 3270 -4.5; 3597 -4.3; 3957 -4.3; 4353 -4.9; 4788 -6.7; 5267 -7.3; 5793 -4.6; 6373 -2.8; 7010 -4.6; 7711 -8.0; 8482 -7.8; 9330 -6.5; 10263 -6.5; 11289 -6.8; 12418 -8.6; 13660 -8.0; 15026 -8.2; 16529 -6.9; 18182 -6.5; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.64 | 6.0 dB  |
| Peaking | 59 Hz    | 1.14 | 1.2 dB  |
| Peaking | 242 Hz   | 0.52 | -2.6 dB |
| Peaking | 2183 Hz  | 1.34 | 4.0 dB  |
| Peaking | 6409 Hz  | 7.98 | 3.9 dB  |
| Peaking | 4335 Hz  | 3.35 | 2.4 dB  |
| Peaking | 4954 Hz  | 4.14 | -2.6 dB |
| Peaking | 13402 Hz | 1.44 | -1.9 dB |
| Peaking | 20031 Hz | 2.8  | -6.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Tin%20Audio%20T2/Tin%20Audio%20T2.png)