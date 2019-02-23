# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.1; 25 -3.5; 28 -3.9; 31 -4.3; 34 -4.6; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.8; 60 -6.1; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.3; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.3; 141 -8.5; 155 -8.8; 170 -9.0; 187 -9.3; 206 -9.7; 227 -9.9; 249 -9.9; 274 -9.7; 302 -9.6; 332 -9.3; 365 -9.1; 402 -8.9; 442 -8.7; 486 -8.5; 535 -8.0; 588 -7.4; 647 -6.7; 712 -6.2; 783 -5.6; 861 -4.9; 947 -4.1; 1042 -2.9; 1146 -1.6; 1261 -0.5; 1387 -1.1; 1526 -2.3; 1678 -3.6; 1846 -4.5; 2031 -5.8; 2234 -6.5; 2457 -4.7; 2703 -1.9; 2973 -0.8; 3270 -1.6; 3597 -2.5; 3957 -4.0; 4353 -5.3; 4788 -6.2; 5267 -8.7; 5793 -9.7; 6373 -7.2; 7010 -7.3; 7711 -7.3; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -7.6; 13660 -6.1; 15026 -6.1; 16529 -8.8; 18182 -12.6; 20000 -11.6
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
| Peaking | 15 Hz    | 0.59 | 4.2 dB  |
| Peaking | 247 Hz   | 0.53 | -3.8 dB |
| Peaking | 1247 Hz  | 2.12 | 6.1 dB  |
| Peaking | 3084 Hz  | 3.8  | 5.6 dB  |
| Peaking | 18950 Hz | 1.04 | -7.6 dB |
| Peaking | 2217 Hz  | 4.76 | -3.6 dB |
| Peaking | 2338 Hz  | 2.18 | 1.7 dB  |
| Peaking | 3953 Hz  | 3.52 | 1.2 dB  |
| Peaking | 5649 Hz  | 3.94 | -4.0 dB |
| Peaking | 15140 Hz | 3.95 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712/AKG%20K712.png)