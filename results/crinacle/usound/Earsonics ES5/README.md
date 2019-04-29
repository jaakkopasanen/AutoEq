# Earsonics ES5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.7; 28 -9.9; 31 -10.0; 34 -10.1; 37 -10.2; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.5; 60 -10.6; 66 -10.7; 72 -10.8; 79 -11.0; 87 -11.0; 96 -11.2; 106 -11.1; 116 -11.0; 128 -10.9; 141 -10.7; 155 -10.4; 170 -10.1; 187 -9.6; 206 -9.0; 227 -8.3; 249 -7.7; 274 -7.1; 302 -6.4; 332 -5.8; 365 -5.3; 402 -5.0; 442 -4.7; 486 -4.6; 535 -4.7; 588 -5.0; 647 -5.5; 712 -6.3; 783 -7.1; 861 -8.1; 947 -9.2; 1042 -10.4; 1146 -11.4; 1261 -11.9; 1387 -11.8; 1526 -11.1; 1678 -10.0; 1846 -8.4; 2031 -6.4; 2234 -4.1; 2457 -2.0; 2703 -0.7; 2973 -0.5; 3270 -1.2; 3597 -2.7; 3957 -1.8; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -6.8; 6373 -8.4; 7010 -5.8; 7711 -6.9; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.7; 16529 -8.5; 18182 -11.1; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 70 Hz    |  0.5  | -5.0 dB |
| Peaking | 1369 Hz  |  1.98 | -6.6 dB |
| Peaking | 2831 Hz  |  2.13 | 6.7 dB  |
| Peaking | 4644 Hz  |  3.84 | 6.0 dB  |
| Peaking | 18962 Hz |  1.03 | -5.4 dB |
| Peaking | 22 Hz    |  2.13 | -1.4 dB |
| Peaking | 170 Hz   |  1.7  | -1.6 dB |
| Peaking | 473 Hz   |  1.03 | 2.8 dB  |
| Peaking | 986 Hz   |  2.76 | -1.8 dB |
| Peaking | 6150 Hz  | 11.09 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Earsonics%20ES5/Earsonics%20ES5.png)