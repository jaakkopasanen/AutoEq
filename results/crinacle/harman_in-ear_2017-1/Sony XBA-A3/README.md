# Sony XBA-A3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.4; 25 -5.8; 28 -6.3; 31 -6.6; 34 -6.9; 37 -7.1; 41 -7.5; 45 -7.7; 49 -8.0; 54 -8.3; 60 -8.7; 66 -9.0; 72 -9.4; 79 -9.7; 87 -10.1; 96 -10.5; 106 -11.0; 116 -11.3; 128 -11.4; 141 -11.6; 155 -11.7; 170 -11.7; 187 -11.6; 206 -11.5; 227 -11.1; 249 -10.8; 274 -10.3; 302 -9.8; 332 -9.2; 365 -8.7; 402 -8.2; 442 -7.7; 486 -7.3; 535 -6.8; 588 -6.3; 647 -5.9; 712 -5.5; 783 -5.1; 861 -4.8; 947 -4.7; 1042 -5.1; 1146 -5.9; 1261 -6.5; 1387 -6.8; 1526 -6.7; 1678 -6.3; 1846 -5.5; 2031 -4.4; 2234 -2.9; 2457 -1.6; 2703 -0.9; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -3.7; 4788 -8.1; 5267 -8.2; 5793 -2.8; 6373 -5.1; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.8; 11289 -10.1; 12418 -14.4; 13660 -21.2; 15026 -27.0; 16529 -28.8; 18182 -26.0; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 120 Hz   | 0.81 | -4.5 dB  |
| Peaking | 233 Hz   | 1.42 | -2.9 dB  |
| Peaking | 3165 Hz  | 1.37 | 7.9 dB   |
| Peaking | 9717 Hz  | 0.73 | 13.5 dB  |
| Peaking | 16032 Hz | 0.44 | -27.4 dB |
| Peaking | 19 Hz    | 2.36 | 1.8 dB   |
| Peaking | 885 Hz   | 2.02 | 2.1 dB   |
| Peaking | 1457 Hz  | 2.9  | -1.6 dB  |
| Peaking | 5062 Hz  | 7.65 | -5.6 dB  |
| Peaking | 5861 Hz  | 6.07 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 16000 Hz | 1.41 | -30.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20XBA-A3/Sony%20XBA-A3.png)