# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.1; 28 -8.4; 31 -8.6; 34 -8.8; 37 -8.9; 41 -9.1; 45 -9.2; 49 -9.3; 54 -9.5; 60 -9.7; 66 -9.8; 72 -10.0; 79 -10.3; 87 -10.5; 96 -10.7; 106 -11.0; 116 -11.1; 128 -11.1; 141 -11.2; 155 -11.2; 170 -11.1; 187 -11.1; 206 -11.0; 227 -10.8; 249 -10.6; 274 -10.4; 302 -10.1; 332 -9.7; 365 -9.4; 402 -9.2; 442 -8.9; 486 -8.6; 535 -8.2; 588 -7.9; 647 -7.5; 712 -7.1; 783 -6.6; 861 -6.3; 947 -6.3; 1042 -6.6; 1146 -7.1; 1261 -7.5; 1387 -7.4; 1526 -7.0; 1678 -6.5; 1846 -5.9; 2031 -5.1; 2234 -4.2; 2457 -3.2; 2703 -1.8; 2973 -0.5; 3270 -1.8; 3597 -3.6; 3957 -2.2; 4353 -1.7; 4788 -2.8; 5267 -2.1; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.7; 12418 -11.3; 13660 -17.1; 15026 -23.8; 16529 -28.8; 18182 -24.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 136 Hz   | 0.33 | -4.9 dB  |
| Peaking | 2929 Hz  | 2.57 | 5.2 dB   |
| Peaking | 5889 Hz  | 1.44 | 7.3 dB   |
| Peaking | 11087 Hz | 2.19 | 7.3 dB   |
| Peaking | 16565 Hz | 0.87 | -24.6 dB |
| Peaking | 30 Hz    | 2.19 | -0.6 dB  |
| Peaking | 913 Hz   | 2.21 | 1.4 dB   |
| Peaking | 1320 Hz  | 1.68 | -1.4 dB  |
| Peaking | 2155 Hz  | 2.83 | 0.5 dB   |
| Peaking | 14795 Hz | 5.37 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 16000 Hz | 1.41 | -25.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20IER-M7/Sony%20IER-M7.png)