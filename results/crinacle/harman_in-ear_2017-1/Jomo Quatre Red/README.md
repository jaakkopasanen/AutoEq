# Jomo Quatre Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -10.9; 25 -11.0; 28 -11.1; 31 -11.2; 34 -11.3; 37 -11.4; 41 -11.5; 45 -11.6; 49 -11.7; 54 -11.8; 60 -12.0; 66 -12.2; 72 -12.4; 79 -12.7; 87 -13.0; 96 -13.3; 106 -13.5; 116 -13.7; 128 -13.9; 141 -13.9; 155 -14.0; 170 -14.0; 187 -13.9; 206 -13.7; 227 -13.5; 249 -13.3; 274 -12.9; 302 -12.6; 332 -12.2; 365 -11.7; 402 -11.3; 442 -10.8; 486 -10.3; 535 -9.7; 588 -9.1; 647 -8.5; 712 -7.8; 783 -6.9; 861 -6.1; 947 -5.7; 1042 -5.6; 1146 -5.5; 1261 -5.1; 1387 -4.2; 1526 -3.2; 1678 -2.7; 1846 -2.6; 2031 -2.3; 2234 -1.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.5; 4788 -6.0; 5267 -5.0; 5793 -1.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -13.0; 16529 -17.5; 18182 -19.3; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.15 | -4.1 dB  |
| Peaking | 215 Hz   | 0.46 | -5.7 dB  |
| Peaking | 2704 Hz  | 0.74 | 6.3 dB   |
| Peaking | 6236 Hz  | 6.42 | 4.7 dB   |
| Peaking | 17852 Hz | 1.15 | -14.5 dB |
| Peaking | 883 Hz   | 5.49 | 0.9 dB   |
| Peaking | 4040 Hz  | 4.68 | 2.2 dB   |
| Peaking | 4844 Hz  | 6.75 | -3.9 dB  |
| Peaking | 13067 Hz | 2.4  | 3.5 dB   |
| Peaking | 15273 Hz | 2.17 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -11.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Quatre%20Red/Jomo%20Quatre%20Red.png)