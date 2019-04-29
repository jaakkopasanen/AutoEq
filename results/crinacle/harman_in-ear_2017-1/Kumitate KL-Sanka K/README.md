# Kumitate KL-Sanka K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.4; 25 -8.6; 28 -8.7; 31 -8.9; 34 -9.0; 37 -9.2; 41 -9.3; 45 -9.4; 49 -9.6; 54 -9.7; 60 -10.0; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.1; 96 -11.5; 106 -11.7; 116 -11.9; 128 -12.0; 141 -12.1; 155 -12.1; 170 -11.9; 187 -11.7; 206 -11.3; 227 -10.8; 249 -10.2; 274 -9.6; 302 -9.0; 332 -8.2; 365 -7.5; 402 -6.9; 442 -6.4; 486 -5.9; 535 -5.3; 588 -4.8; 647 -4.3; 712 -3.7; 783 -3.2; 861 -2.8; 947 -2.6; 1042 -2.7; 1146 -3.0; 1261 -3.2; 1387 -3.0; 1526 -2.2; 1678 -1.3; 1846 -1.4; 2031 -2.6; 2234 -3.8; 2457 -3.4; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -3.9; 4788 -6.3; 5267 -5.7; 5793 -5.3; 6373 -8.1; 7010 -12.2; 7711 -12.1; 8482 -14.5; 9330 -17.5; 10263 -13.6; 11289 -6.7; 12418 -6.5; 13660 -17.3; 15026 -31.7; 16529 -31.1; 18182 -15.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sanka K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sanka K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 136 Hz   | 0.41 | -5.9 dB  |
| Peaking | 2443 Hz  | 0.22 | 5.6 dB   |
| Peaking | 9092 Hz  | 1.59 | -10.2 dB |
| Peaking | 11951 Hz | 2.69 | 14.2 dB  |
| Peaking | 15643 Hz | 1.54 | -31.6 dB |
| Peaking | 1303 Hz  | 5.38 | -1.5 dB  |
| Peaking | 2314 Hz  | 4.88 | -3.2 dB  |
| Peaking | 3609 Hz  | 1.64 | 2.9 dB   |
| Peaking | 4705 Hz  | 5.55 | -3.5 dB  |
| Peaking | 16811 Hz | 5.67 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Sanka%20K/Kumitate%20KL-Sanka%20K.png)