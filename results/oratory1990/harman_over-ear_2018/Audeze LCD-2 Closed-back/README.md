# Audeze LCD-2 Closed-back
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.4; 25 -4.6; 28 -4.7; 31 -4.9; 34 -5.0; 37 -5.2; 41 -5.4; 45 -5.6; 49 -5.9; 54 -6.0; 60 -6.3; 66 -6.5; 72 -6.7; 79 -6.9; 87 -7.1; 96 -7.5; 106 -7.8; 116 -8.1; 128 -8.3; 141 -8.5; 155 -8.5; 170 -8.7; 187 -8.6; 206 -8.5; 227 -8.3; 249 -7.9; 274 -7.4; 302 -6.5; 332 -5.7; 365 -5.0; 402 -5.0; 442 -5.3; 486 -5.6; 535 -5.8; 588 -5.9; 647 -5.8; 712 -5.7; 783 -5.5; 861 -5.9; 947 -6.2; 1042 -6.8; 1146 -7.1; 1261 -7.0; 1387 -7.9; 1526 -8.9; 1678 -8.8; 1846 -9.1; 2031 -9.4; 2234 -8.3; 2457 -7.9; 2703 -6.0; 2973 -3.8; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -3.9; 5267 -5.7; 5793 -9.7; 6373 -10.6; 7010 -11.2; 7711 -10.2; 8482 -6.5; 9330 -6.5; 10263 -6.9; 11289 -13.1; 12418 -12.9; 13660 -10.1; 15026 -9.1; 16529 -10.8; 18182 -16.9; 20000 -27.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Closed-back GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Closed-back ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.79 | 2.3 dB   |
| Peaking | 2104 Hz  | 1.54 | -4.9 dB  |
| Peaking | 3832 Hz  | 1.35 | 8.6 dB   |
| Peaking | 6370 Hz  | 2.17 | -6.6 dB  |
| Peaking | 20024 Hz | 0.71 | -21.1 dB |
| Peaking | 205 Hz   | 0.84 | -3.3 dB  |
| Peaking | 370 Hz   | 0.97 | 2.8 dB   |
| Peaking | 9886 Hz  | 2.82 | 4.8 dB   |
| Peaking | 11617 Hz | 2.46 | -7.5 dB  |
| Peaking | 15621 Hz | 1.73 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Closed-back/Audeze%20LCD-2%20Closed-back.png)