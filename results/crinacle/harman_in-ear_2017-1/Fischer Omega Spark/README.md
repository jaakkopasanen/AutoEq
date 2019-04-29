# Fischer Omega Spark
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -0.9; 49 -1.1; 54 -1.4; 60 -1.7; 66 -2.0; 72 -2.4; 79 -2.8; 87 -3.2; 96 -3.6; 106 -4.0; 116 -4.5; 128 -4.9; 141 -5.2; 155 -5.5; 170 -5.8; 187 -5.9; 206 -6.0; 227 -6.2; 249 -6.2; 274 -6.3; 302 -6.2; 332 -6.1; 365 -6.0; 402 -5.9; 442 -6.0; 486 -5.7; 535 -5.5; 588 -5.3; 647 -5.1; 712 -4.8; 783 -4.4; 861 -4.1; 947 -4.0; 1042 -4.3; 1146 -4.7; 1261 -5.0; 1387 -4.8; 1526 -4.2; 1678 -3.5; 1846 -2.7; 2031 -1.9; 2234 -1.4; 2457 -1.9; 2703 -2.5; 2973 -5.2; 3270 -5.6; 3597 -10.6; 3957 -13.5; 4353 -11.2; 4788 -9.7; 5267 -10.1; 5793 -12.4; 6373 -16.1; 7010 -15.1; 7711 -13.1; 8482 -13.1; 9330 -10.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -21.9; 16529 -28.7; 18182 -23.4; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Omega Spark GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Omega Spark ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.46 | 6.3 dB   |
| Peaking | 3922 Hz  | 4.81 | -8.8 dB  |
| Peaking | 7073 Hz  | 1.13 | -17.5 dB |
| Peaking | 10866 Hz | 0.27 | 24.8 dB  |
| Peaking | 16480 Hz | 0.62 | -40.2 dB |
| Peaking | 1362 Hz  | 3.79 | -1.6 dB  |
| Peaking | 2294 Hz  | 3.2  | 2.2 dB   |
| Peaking | 7477 Hz  | 8.19 | 2.3 dB   |
| Peaking | 8805 Hz  | 7.5  | -3.0 dB  |
| Peaking | 15272 Hz | 8.56 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.6 dB   |
| Peaking | 125 Hz   | 1.41 | 1.0 dB   |
| Peaking | 250 Hz   | 1.41 | -0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 16000 Hz | 1.41 | -19.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Fischer%20Omega%20Spark/Fischer%20Omega%20Spark.png)