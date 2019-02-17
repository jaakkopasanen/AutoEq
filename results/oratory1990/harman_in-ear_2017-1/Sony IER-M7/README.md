# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.0; 25 -8.2; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.2; 66 -9.3; 72 -9.5; 79 -9.7; 87 -9.9; 96 -10.0; 106 -10.2; 116 -10.4; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.4; 187 -10.3; 206 -10.1; 227 -10.0; 249 -9.8; 274 -9.5; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.3; 442 -8.1; 486 -7.8; 535 -7.4; 588 -7.1; 647 -6.9; 712 -6.6; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -6.9; 1387 -6.6; 1526 -6.2; 1678 -5.8; 1846 -5.2; 2031 -4.6; 2234 -3.8; 2457 -2.8; 2703 -1.7; 2973 -1.0; 3270 -1.8; 3597 -2.6; 3957 -1.4; 4353 -1.4; 4788 -2.0; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -8.7; 10263 -10.7; 11289 -12.5; 12418 -13.5; 13660 -15.4; 15026 -20.7; 16529 -25.9; 18182 -24.5; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.3  | -1.8 dB  |
| Peaking | 177 Hz   | 0.56 | -3.1 dB  |
| Peaking | 2872 Hz  | 2.06 | 4.2 dB   |
| Peaking | 5754 Hz  | 1.17 | 7.4 dB   |
| Peaking | 17272 Hz | 0.69 | -21.0 dB |
| Peaking | 864 Hz   | 1.63 | 1.7 dB   |
| Peaking | 1182 Hz  | 0.85 | -1.7 dB  |
| Peaking | 1860 Hz  | 1.34 | 0.9 dB   |
| Peaking | 13402 Hz | 4.78 | 1.5 dB   |
| Peaking | 15671 Hz | 4.96 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -25.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20IER-M7/Sony%20IER-M7.png)