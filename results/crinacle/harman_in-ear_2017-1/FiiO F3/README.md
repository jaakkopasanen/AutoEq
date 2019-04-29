# FiiO F3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.1; 28 -8.5; 31 -8.7; 34 -8.9; 37 -9.1; 41 -9.3; 45 -9.5; 49 -9.7; 54 -9.9; 60 -10.1; 66 -10.3; 72 -10.6; 79 -10.9; 87 -11.2; 96 -11.5; 106 -11.7; 116 -11.9; 128 -12.0; 141 -12.0; 155 -12.0; 170 -12.0; 187 -11.8; 206 -11.5; 227 -11.2; 249 -10.9; 274 -10.5; 302 -10.0; 332 -9.5; 365 -9.0; 402 -8.6; 442 -8.2; 486 -7.7; 535 -7.3; 588 -6.9; 647 -6.6; 712 -6.2; 783 -5.9; 861 -5.8; 947 -5.9; 1042 -6.2; 1146 -6.7; 1261 -7.2; 1387 -7.3; 1526 -6.9; 1678 -6.3; 1846 -5.3; 2031 -3.9; 2234 -2.2; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.1; 6373 -5.3; 7010 -6.8; 7711 -8.7; 8482 -9.7; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.2; 15026 -24.5; 16529 -25.2; 18182 -23.2; 20000 -21.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.82 | -1.2 dB  |
| Peaking | 147 Hz   | 0.46 | -5.5 dB  |
| Peaking | 7984 Hz  | 2.24 | -12.1 dB |
| Peaking | 8837 Hz  | 0.41 | 18.9 dB  |
| Peaking | 16406 Hz | 0.49 | -28.5 dB |
| Peaking | 1544 Hz  | 1.28 | -6.9 dB  |
| Peaking | 2056 Hz  | 0.52 | 4.6 dB   |
| Peaking | 7854 Hz  | 8.28 | 2.4 dB   |
| Peaking | 10788 Hz | 0.33 | -2.3 dB  |
| Peaking | 12432 Hz | 4.15 | 6.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -22.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FiiO%20F3/FiiO%20F3.png)