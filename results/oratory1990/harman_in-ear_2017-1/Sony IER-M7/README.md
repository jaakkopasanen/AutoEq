# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.6; 25 -8.7; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.3; 45 -9.3; 49 -9.4; 54 -9.6; 60 -9.7; 66 -9.9; 72 -10.0; 79 -10.2; 87 -10.4; 96 -10.6; 106 -10.8; 116 -10.9; 128 -11.0; 141 -11.0; 155 -11.0; 170 -11.0; 187 -10.9; 206 -10.7; 227 -10.5; 249 -10.3; 274 -10.1; 302 -9.8; 332 -9.5; 365 -9.1; 402 -8.9; 442 -8.7; 486 -8.3; 535 -8.0; 588 -7.7; 647 -7.5; 712 -7.1; 783 -6.8; 861 -6.7; 947 -6.8; 1042 -7.1; 1146 -7.4; 1261 -7.4; 1387 -7.2; 1526 -6.8; 1678 -6.3; 1846 -5.8; 2031 -5.1; 2234 -4.4; 2457 -3.4; 2703 -2.3; 2973 -1.5; 3270 -2.4; 3597 -3.1; 3957 -2.0; 4353 -1.9; 4788 -2.5; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -9.3; 10263 -11.3; 11289 -13.1; 12418 -14.1; 13660 -16.0; 15026 -21.3; 16529 -26.5; 18182 -25.0; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.59 | -1.6 dB  |
| Peaking | 153 Hz   | 0.4  | -4.4 dB  |
| Peaking | 2901 Hz  | 2.38 | 4.0 dB   |
| Peaking | 5883 Hz  | 1.25 | 7.8 dB   |
| Peaking | 17273 Hz | 0.66 | -21.5 dB |
| Peaking | 840 Hz   | 2.17 | 0.7 dB   |
| Peaking | 1264 Hz  | 1.92 | -1.1 dB  |
| Peaking | 2164 Hz  | 3.15 | 0.4 dB   |
| Peaking | 13411 Hz | 4.93 | 1.6 dB   |
| Peaking | 15668 Hz | 4.98 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -26.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M7/Sony%20IER-M7.png)