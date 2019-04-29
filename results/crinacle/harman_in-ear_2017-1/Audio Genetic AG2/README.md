# Audio Genetic AG2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.3; 25 -5.6; 28 -5.9; 31 -6.2; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.3; 49 -7.5; 54 -7.7; 60 -7.9; 66 -8.3; 72 -8.7; 79 -9.1; 87 -9.5; 96 -10.0; 106 -10.3; 116 -10.8; 128 -11.1; 141 -11.4; 155 -11.6; 170 -11.8; 187 -11.9; 206 -11.9; 227 -11.9; 249 -11.9; 274 -11.7; 302 -11.5; 332 -11.2; 365 -10.9; 402 -10.6; 442 -10.3; 486 -10.0; 535 -9.5; 588 -9.0; 647 -8.6; 712 -8.0; 783 -7.4; 861 -7.0; 947 -6.8; 1042 -6.9; 1146 -7.2; 1261 -7.4; 1387 -7.3; 1526 -6.6; 1678 -5.6; 1846 -4.7; 2031 -3.4; 2234 -1.8; 2457 -0.9; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.6; 5793 -2.4; 6373 -2.5; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.2; 15026 -24.1; 16529 -26.8; 18182 -20.9; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Genetic AG2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Genetic AG2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.19 | 2.5 dB   |
| Peaking | 194 Hz   | 0.69 | -2.6 dB  |
| Peaking | 253 Hz   | 0.12 | -3.5 dB  |
| Peaking | 8964 Hz  | 0.19 | 10.6 dB  |
| Peaking | 16414 Hz | 0.76 | -30.2 dB |
| Peaking | 1513 Hz  | 1.56 | -4.8 dB  |
| Peaking | 1713 Hz  | 0.64 | 3.2 dB   |
| Peaking | 7895 Hz  | 2.35 | -3.5 dB  |
| Peaking | 13151 Hz | 2.49 | 7.4 dB   |
| Peaking | 14880 Hz | 3.77 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -21.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Genetic%20AG2/Audio%20Genetic%20AG2.png)