# Denon AH-D7200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -8.0; 25 -8.3; 28 -8.8; 31 -9.0; 34 -9.1; 37 -9.1; 41 -9.1; 45 -9.1; 49 -9.0; 54 -8.8; 60 -8.7; 66 -8.7; 72 -8.7; 79 -8.8; 87 -9.0; 96 -9.3; 106 -9.7; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.8; 170 -10.9; 187 -10.9; 206 -10.8; 227 -10.8; 249 -10.6; 274 -10.1; 302 -9.7; 332 -9.2; 365 -8.5; 402 -8.1; 442 -7.9; 486 -7.9; 535 -8.2; 588 -8.6; 647 -8.9; 712 -8.8; 783 -8.6; 861 -8.7; 947 -8.6; 1042 -8.4; 1146 -8.0; 1261 -7.4; 1387 -6.4; 1526 -5.1; 1678 -3.8; 1846 -2.5; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -0.8; 3270 -0.7; 3597 -1.2; 3957 -1.7; 4353 -2.2; 4788 -4.2; 5267 -5.9; 5793 -7.5; 6373 -7.9; 7010 -7.1; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.6; 12418 -6.7; 13660 -6.5; 15026 -9.0; 16529 -14.4; 18182 -16.1; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.87 | -2.3 dB  |
| Peaking | 181 Hz   | 0.72 | -4.4 dB  |
| Peaking | 993 Hz   | 1.06 | -3.2 dB  |
| Peaking | 2563 Hz  | 1.01 | 7.2 dB   |
| Peaking | 17971 Hz | 1.24 | -10.8 dB |
| Peaking | 2047 Hz  | 5.31 | 0.8 dB   |
| Peaking | 2698 Hz  | 3.77 | -1.2 dB  |
| Peaking | 4131 Hz  | 2.34 | 2.0 dB   |
| Peaking | 5965 Hz  | 2.95 | -3.1 dB  |
| Peaking | 13751 Hz | 4.14 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Denon%20AH-D7200/Denon%20AH-D7200.png)