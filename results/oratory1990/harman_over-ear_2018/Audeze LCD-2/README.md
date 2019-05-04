# Audeze LCD-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.7; 25 -3.7; 28 -3.8; 31 -3.9; 34 -4.0; 37 -4.2; 41 -4.4; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.2; 66 -5.4; 72 -5.7; 79 -5.9; 87 -6.3; 96 -6.6; 106 -7.0; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.3; 170 -8.5; 187 -8.7; 206 -8.8; 227 -9.0; 249 -9.0; 274 -8.8; 302 -8.7; 332 -8.4; 365 -8.0; 402 -7.9; 442 -8.2; 486 -8.5; 535 -8.6; 588 -8.8; 647 -8.8; 712 -8.5; 783 -8.1; 861 -8.5; 947 -8.7; 1042 -8.4; 1146 -7.6; 1261 -6.9; 1387 -7.4; 1526 -7.5; 1678 -6.1; 1846 -5.1; 2031 -4.4; 2234 -4.6; 2457 -6.2; 2703 -6.4; 2973 -6.1; 3270 -4.7; 3597 -2.7; 3957 -1.0; 4353 -0.5; 4788 -1.7; 5267 -5.6; 5793 -7.4; 6373 -5.6; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.5; 12418 -10.4; 13660 -9.9; 15026 -10.5; 16529 -13.1; 18182 -15.0; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.34 | 2.8 dB   |
| Peaking | 206 Hz   | 0.74 | -2.5 dB  |
| Peaking | 732 Hz   | 1.2  | -2.0 dB  |
| Peaking | 4213 Hz  | 2.68 | 6.6 dB   |
| Peaking | 19481 Hz | 0.47 | -10.1 dB |
| Peaking | 2034 Hz  | 4.21 | 2.8 dB   |
| Peaking | 6078 Hz  | 0.22 | -0.7 dB  |
| Peaking | 6957 Hz  | 9.3  | 2.8 dB   |
| Peaking | 10506 Hz | 1.81 | 2.6 dB   |
| Peaking | 12144 Hz | 3.74 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2/Audeze%20LCD-2.png)