# Sony IER-M9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.8; 28 -8.9; 31 -9.1; 34 -9.2; 37 -9.3; 41 -9.4; 45 -9.4; 49 -9.5; 54 -9.7; 60 -9.8; 66 -10.0; 72 -10.2; 79 -10.4; 87 -10.5; 96 -10.7; 106 -10.8; 116 -11.0; 128 -11.0; 141 -11.0; 155 -11.0; 170 -10.8; 187 -10.7; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.2; 486 -7.9; 535 -7.5; 588 -7.2; 647 -6.8; 712 -6.5; 783 -6.3; 861 -6.1; 947 -6.2; 1042 -6.5; 1146 -6.7; 1261 -6.7; 1387 -6.5; 1526 -6.0; 1678 -5.6; 1846 -5.1; 2031 -4.2; 2234 -3.0; 2457 -1.4; 2703 -0.5; 2973 -1.7; 3270 -4.2; 3597 -4.4; 3957 -3.3; 4353 -3.7; 4788 -3.7; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -10.3; 10263 -13.9; 11289 -13.9; 12418 -12.8; 13660 -17.8; 15026 -28.0; 16529 -32.8; 18182 -27.2; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 112 Hz   | 0.35 | -4.5 dB  |
| Peaking | 2631 Hz  | 2.44 | 5.8 dB   |
| Peaking | 6040 Hz  | 1.83 | 7.9 dB   |
| Peaking | 15732 Hz | 2.83 | -10.5 dB |
| Peaking | 17459 Hz | 0.76 | -22.9 dB |
| Peaking | 24 Hz    | 1.84 | -1.0 dB  |
| Peaking | 781 Hz   | 3.03 | 0.9 dB   |
| Peaking | 8639 Hz  | 5.64 | 2.9 dB   |
| Peaking | 10321 Hz | 2.19 | -3.1 dB  |
| Peaking | 12580 Hz | 4.37 | 4.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 16000 Hz | 1.41 | -33.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M9/Sony%20IER-M9.png)