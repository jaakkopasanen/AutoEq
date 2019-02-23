# Audeze iSine10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.2; 25 -4.2; 28 -4.2; 31 -4.2; 34 -4.2; 37 -4.3; 41 -4.3; 45 -4.4; 49 -4.4; 54 -4.5; 60 -4.7; 66 -4.9; 72 -5.1; 79 -5.4; 87 -5.7; 96 -6.1; 106 -6.5; 116 -6.9; 128 -7.2; 141 -7.5; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.3; 227 -8.4; 249 -8.5; 274 -8.4; 302 -8.4; 332 -8.3; 365 -8.3; 402 -8.5; 442 -8.7; 486 -8.9; 535 -9.1; 588 -9.4; 647 -9.9; 712 -10.3; 783 -10.8; 861 -11.5; 947 -12.0; 1042 -12.6; 1146 -13.0; 1261 -13.2; 1387 -13.7; 1526 -12.9; 1678 -10.4; 1846 -7.3; 2031 -4.2; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -3.1; 7010 -6.1; 7711 -6.2; 8482 -6.8; 9330 -9.0; 10263 -10.4; 11289 -8.9; 12418 -8.5; 13660 -9.9; 15026 -8.6; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.6  | 2.7 dB   |
| Peaking | 1434 Hz  | 0.45 | -27.1 dB |
| Peaking | 2333 Hz  | 0.32 | 24.5 dB  |
| Peaking | 9781 Hz  | 1.34 | -7.5 dB  |
| Peaking | 14057 Hz | 1.86 | -4.5 dB  |
| Peaking | 430 Hz   | 2.63 | 0.6 dB   |
| Peaking | 2315 Hz  | 5.13 | 1.4 dB   |
| Peaking | 3402 Hz  | 1.09 | -1.1 dB  |
| Peaking | 6133 Hz  | 1.76 | 3.3 dB   |
| Peaking | 6890 Hz  | 4.35 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -8.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20iSine10/Audeze%20iSine10.png)