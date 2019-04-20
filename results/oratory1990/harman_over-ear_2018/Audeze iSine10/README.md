# Audeze iSine10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.1; 25 -4.1; 28 -4.1; 31 -4.1; 34 -4.1; 37 -4.2; 41 -4.2; 45 -4.3; 49 -4.4; 54 -4.5; 60 -4.6; 66 -4.8; 72 -5.0; 79 -5.3; 87 -5.6; 96 -6.0; 106 -6.4; 116 -6.8; 128 -7.1; 141 -7.4; 155 -7.7; 170 -7.9; 187 -8.1; 206 -8.2; 227 -8.3; 249 -8.4; 274 -8.3; 302 -8.3; 332 -8.2; 365 -8.2; 402 -8.4; 442 -8.6; 486 -8.8; 535 -9.0; 588 -9.3; 647 -9.8; 712 -10.3; 783 -10.9; 861 -11.6; 947 -12.2; 1042 -12.3; 1146 -12.2; 1261 -13.1; 1387 -13.7; 1526 -12.9; 1678 -10.3; 1846 -6.8; 2031 -3.7; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.7; 7010 -5.6; 7711 -6.2; 8482 -7.3; 9330 -10.0; 10263 -10.9; 11289 -9.0; 12418 -8.9; 13660 -10.3; 15026 -8.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.58 | 2.7 dB   |
| Peaking | 1432 Hz  | 0.46 | -26.9 dB |
| Peaking | 2309 Hz  | 0.31 | 24.3 dB  |
| Peaking | 9693 Hz  | 1.62 | -8.3 dB  |
| Peaking | 13973 Hz | 1.9  | -5.3 dB  |
| Peaking | 873 Hz   | 4.26 | -1.0 dB  |
| Peaking | 1858 Hz  | 0.29 | 0.3 dB   |
| Peaking | 3282 Hz  | 2.83 | -1.0 dB  |
| Peaking | 6060 Hz  | 3.31 | 2.5 dB   |
| Peaking | 6798 Hz  | 5.03 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -7.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20iSine10/Audeze%20iSine10.png)