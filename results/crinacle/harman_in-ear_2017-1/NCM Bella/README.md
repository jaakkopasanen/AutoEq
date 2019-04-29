# NCM Bella
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.7; 25 -11.8; 28 -11.8; 31 -11.7; 34 -11.7; 37 -11.6; 41 -11.5; 45 -11.5; 49 -11.4; 54 -11.4; 60 -11.3; 66 -11.3; 72 -11.3; 79 -11.3; 87 -11.3; 96 -11.3; 106 -11.3; 116 -11.2; 128 -11.1; 141 -10.9; 155 -10.7; 170 -10.5; 187 -10.2; 206 -9.9; 227 -9.5; 249 -9.2; 274 -8.8; 302 -8.4; 332 -7.9; 365 -7.4; 402 -7.1; 442 -6.8; 486 -6.4; 535 -6.1; 588 -5.8; 647 -5.5; 712 -5.2; 783 -4.9; 861 -4.8; 947 -5.0; 1042 -5.6; 1146 -6.5; 1261 -7.3; 1387 -7.4; 1526 -6.4; 1678 -5.4; 1846 -5.5; 2031 -6.9; 2234 -6.2; 2457 -3.9; 2703 -1.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -6.2; 5267 -10.2; 5793 -8.1; 6373 -5.0; 7010 -4.6; 7711 -7.2; 8482 -8.4; 9330 -7.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -13.6; 15026 -23.8; 16529 -27.7; 18182 -25.9; 20000 -20.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NCM Bella GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NCM Bella ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.22 | -5.1 dB  |
| Peaking | 156 Hz   | 0.85 | -2.5 dB  |
| Peaking | 5428 Hz  | 5.39 | -8.5 dB  |
| Peaking | 9542 Hz  | 0.28 | 12.6 dB  |
| Peaking | 16920 Hz | 0.5  | -30.3 dB |
| Peaking | 1358 Hz  | 4.74 | -2.8 dB  |
| Peaking | 2135 Hz  | 3.94 | -4.2 dB  |
| Peaking | 3228 Hz  | 1.7  | 3.2 dB   |
| Peaking | 8306 Hz  | 3.45 | -4.1 dB  |
| Peaking | 12374 Hz | 4.53 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -24.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/NCM%20Bella/NCM%20Bella.png)