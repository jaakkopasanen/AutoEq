# Jomo Flamenco
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.7; 25 -4.1; 28 -4.7; 31 -5.1; 34 -5.4; 37 -5.7; 41 -6.1; 45 -6.4; 49 -6.7; 54 -7.0; 60 -7.4; 66 -7.8; 72 -8.1; 79 -8.5; 87 -9.0; 96 -9.5; 106 -9.9; 116 -10.3; 128 -10.6; 141 -10.9; 155 -11.1; 170 -11.2; 187 -11.4; 206 -11.4; 227 -11.4; 249 -11.2; 274 -11.1; 302 -10.9; 332 -10.5; 365 -10.1; 402 -9.7; 442 -9.3; 486 -8.8; 535 -8.2; 588 -7.5; 647 -6.8; 712 -6.0; 783 -5.1; 861 -4.3; 947 -3.8; 1042 -3.8; 1146 -4.3; 1261 -4.7; 1387 -4.8; 1526 -4.7; 1678 -4.7; 1846 -4.8; 2031 -5.2; 2234 -5.2; 2457 -4.4; 2703 -3.0; 2973 -2.3; 3270 -2.9; 3597 -3.7; 3957 -2.0; 4353 -0.5; 4788 -1.0; 5267 -5.3; 5793 -4.8; 6373 -3.9; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.3; 15026 -23.8; 16529 -27.2; 18182 -23.1; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.46 | 5.1 dB   |
| Peaking | 207 Hz   | 0.45 | -5.1 dB  |
| Peaking | 907 Hz   | 1.91 | 2.9 dB   |
| Peaking | 11228 Hz | 0.25 | 18.6 dB  |
| Peaking | 16379 Hz | 0.47 | -36.7 dB |
| Peaking | 4565 Hz  | 3.63 | 3.9 dB   |
| Peaking | 5382 Hz  | 7.01 | -3.7 dB  |
| Peaking | 8327 Hz  | 2.39 | -2.5 dB  |
| Peaking | 12822 Hz | 3.25 | 5.4 dB   |
| Peaking | 14724 Hz | 4.23 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco/Jomo%20Flamenco.png)