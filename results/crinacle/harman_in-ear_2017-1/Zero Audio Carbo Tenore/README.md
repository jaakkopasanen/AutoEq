# Zero Audio Carbo Tenore
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.2; 28 -10.3; 31 -10.2; 34 -10.2; 37 -10.1; 41 -10.1; 45 -10.0; 49 -10.0; 54 -9.9; 60 -9.8; 66 -9.7; 72 -9.7; 79 -9.7; 87 -9.7; 96 -9.7; 106 -9.7; 116 -9.7; 128 -9.5; 141 -9.4; 155 -9.3; 170 -9.0; 187 -8.7; 206 -8.4; 227 -8.0; 249 -7.8; 274 -7.8; 302 -7.5; 332 -7.0; 365 -6.5; 402 -6.2; 442 -5.9; 486 -5.6; 535 -5.4; 588 -5.1; 647 -4.9; 712 -4.7; 783 -4.5; 861 -4.4; 947 -4.7; 1042 -5.5; 1146 -6.5; 1261 -7.2; 1387 -7.1; 1526 -7.1; 1678 -7.3; 1846 -7.7; 2031 -8.3; 2234 -8.8; 2457 -8.6; 2703 -6.8; 2973 -4.4; 3270 -2.2; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -2.8; 5793 -6.5; 6373 -9.3; 7010 -6.5; 7711 -6.1; 8482 -7.1; 9330 -9.4; 10263 -6.7; 11289 -6.4; 12418 -6.4; 13660 -18.3; 15026 -31.2; 16529 -32.0; 18182 -28.6; 20000 -31.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zero Audio Carbo Tenore GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zero Audio Carbo Tenore ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.1  | -3.7 dB  |
| Peaking | 516 Hz   | 1.25 | 0.6 dB   |
| Peaking | 1907 Hz  | 1.43 | -5.9 dB  |
| Peaking | 8840 Hz  | 0.18 | 23.5 dB  |
| Peaking | 16535 Hz | 0.29 | -43.9 dB |
| Peaking | 2491 Hz  | 4.22 | -3.5 dB  |
| Peaking | 4632 Hz  | 1.32 | 6.8 dB   |
| Peaking | 6191 Hz  | 1.72 | -8.6 dB  |
| Peaking | 12481 Hz | 2.97 | 9.8 dB   |
| Peaking | 14749 Hz | 3.33 | -8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 16000 Hz | 1.41 | -32.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Zero%20Audio%20Carbo%20Tenore/Zero%20Audio%20Carbo%20Tenore.png)