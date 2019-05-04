# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.1; 25 -3.4; 28 -3.9; 31 -4.2; 34 -4.5; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.8; 60 -6.0; 66 -6.3; 72 -6.6; 79 -6.9; 87 -7.3; 96 -7.6; 106 -7.9; 116 -8.1; 128 -8.2; 141 -8.4; 155 -8.7; 170 -9.0; 187 -9.3; 206 -9.6; 227 -9.8; 249 -9.8; 274 -9.7; 302 -9.5; 332 -9.3; 365 -9.1; 402 -8.9; 442 -8.7; 486 -8.4; 535 -8.0; 588 -7.3; 647 -6.7; 712 -6.2; 783 -5.5; 861 -4.9; 947 -4.0; 1042 -2.9; 1146 -1.6; 1261 -0.5; 1387 -1.0; 1526 -2.3; 1678 -3.6; 1846 -4.5; 2031 -5.8; 2234 -6.5; 2457 -4.7; 2703 -1.9; 2973 -0.8; 3270 -1.6; 3597 -2.5; 3957 -4.0; 4353 -5.2; 4788 -6.2; 5267 -8.6; 5793 -9.6; 6373 -7.3; 7010 -7.2; 7711 -7.3; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.1; 12418 -7.6; 13660 -6.1; 15026 -6.0; 16529 -8.8; 18182 -12.6; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.65 | 3.8 dB  |
| Peaking | 248 Hz   | 0.53 | -3.8 dB |
| Peaking | 1247 Hz  | 2.12 | 6.1 dB  |
| Peaking | 3087 Hz  | 3.8  | 5.6 dB  |
| Peaking | 18950 Hz | 1.04 | -7.6 dB |
| Peaking | 2218 Hz  | 4.69 | -3.7 dB |
| Peaking | 2333 Hz  | 2.19 | 1.7 dB  |
| Peaking | 3970 Hz  | 3.46 | 1.2 dB  |
| Peaking | 5613 Hz  | 3.79 | -4.0 dB |
| Peaking | 15200 Hz | 3.94 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712/AKG%20K712.png)