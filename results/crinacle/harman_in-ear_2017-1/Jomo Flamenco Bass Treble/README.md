# Jomo Flamenco Bass Treble
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.3; 25 -3.7; 28 -4.2; 31 -4.6; 34 -5.0; 37 -5.2; 41 -5.6; 45 -5.9; 49 -6.2; 54 -6.5; 60 -6.8; 66 -7.2; 72 -7.6; 79 -7.9; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.6; 128 -9.8; 141 -10.1; 155 -10.3; 170 -10.4; 187 -10.5; 206 -10.5; 227 -10.3; 249 -10.2; 274 -9.9; 302 -9.6; 332 -9.2; 365 -8.7; 402 -8.3; 442 -7.8; 486 -7.2; 535 -6.5; 588 -5.8; 647 -5.1; 712 -4.2; 783 -3.3; 861 -2.4; 947 -1.9; 1042 -1.8; 1146 -2.1; 1261 -2.5; 1387 -2.7; 1526 -2.7; 1678 -2.9; 1846 -3.4; 2031 -4.0; 2234 -3.9; 2457 -2.8; 2703 -1.3; 2973 -0.5; 3270 -1.0; 3597 -1.9; 3957 -2.4; 4353 -3.4; 4788 -5.6; 5267 -7.9; 5793 -7.8; 6373 -6.9; 7010 -7.1; 7711 -6.4; 8482 -5.7; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -8.7; 15026 -19.9; 16529 -23.6; 18182 -19.3; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco Bass Treble GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco Bass Treble ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.55 | 4.0 dB   |
| Peaking | 201 Hz   | 0.44 | -5.0 dB  |
| Peaking | 1002 Hz  | 0.98 | 4.8 dB   |
| Peaking | 3135 Hz  | 2.28 | 5.2 dB   |
| Peaking | 16972 Hz | 1.42 | -19.7 dB |
| Peaking | 1632 Hz  | 9.32 | 0.6 dB   |
| Peaking | 4317 Hz  | 4.13 | 2.3 dB   |
| Peaking | 5373 Hz  | 2.62 | -3.3 dB  |
| Peaking | 13107 Hz | 1.47 | 6.7 dB   |
| Peaking | 15072 Hz | 2.74 | -9.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -17.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Flamenco%20Bass%20Treble/Jomo%20Flamenco%20Bass%20Treble.png)