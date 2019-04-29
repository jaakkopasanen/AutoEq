# Fischer Omega Spark
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -0.9; 72 -1.3; 79 -1.7; 87 -2.1; 96 -2.5; 106 -2.9; 116 -3.3; 128 -3.7; 141 -4.0; 155 -4.3; 170 -4.6; 187 -4.7; 206 -4.9; 227 -5.0; 249 -5.1; 274 -5.1; 302 -5.1; 332 -5.2; 365 -5.1; 402 -5.1; 442 -5.2; 486 -5.0; 535 -4.8; 588 -4.7; 647 -4.5; 712 -4.1; 783 -3.7; 861 -3.4; 947 -3.3; 1042 -3.5; 1146 -4.0; 1261 -4.5; 1387 -4.7; 1526 -4.3; 1678 -3.6; 1846 -2.9; 2031 -2.5; 2234 -2.6; 2457 -3.6; 2703 -4.6; 2973 -7.5; 3270 -7.9; 3597 -12.5; 3957 -15.1; 4353 -12.3; 4788 -10.6; 5267 -11.0; 5793 -13.5; 6373 -17.6; 7010 -17.4; 7711 -16.1; 8482 -14.8; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -9.8; 18182 -7.4; 20000 -6.5
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
| Peaking | 36 Hz    | 0.33 | 6.3 dB   |
| Peaking | 868 Hz   | 1.05 | 2.7 dB   |
| Peaking | 2164 Hz  | 1.94 | 4.3 dB   |
| Peaking | 3887 Hz  | 4.42 | -8.3 dB  |
| Peaking | 6947 Hz  | 2.16 | -12.1 dB |
| Peaking | 1354 Hz  | 8.27 | -0.5 dB  |
| Peaking | 8572 Hz  | 4.84 | -5.4 dB  |
| Peaking | 9736 Hz  | 1.9  | 3.6 dB   |
| Peaking | 16886 Hz | 3.04 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB |
| Peaking | 8000 Hz  | 1.41 | -7.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Fischer%20Omega%20Spark/Fischer%20Omega%20Spark.png)