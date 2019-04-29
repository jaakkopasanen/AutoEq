# Dita Audio Truth
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.6; 28 -7.9; 31 -8.1; 34 -8.3; 37 -8.4; 41 -8.6; 45 -8.7; 49 -8.8; 54 -8.9; 60 -9.0; 66 -9.2; 72 -9.4; 79 -9.6; 87 -9.8; 96 -10.1; 106 -10.3; 116 -10.6; 128 -10.7; 141 -10.9; 155 -11.1; 170 -11.1; 187 -11.0; 206 -11.0; 227 -11.2; 249 -11.1; 274 -10.9; 302 -10.7; 332 -10.3; 365 -10.0; 402 -9.7; 442 -9.5; 486 -9.1; 535 -8.7; 588 -8.2; 647 -7.7; 712 -7.1; 783 -6.5; 861 -5.9; 947 -5.5; 1042 -5.4; 1146 -5.5; 1261 -5.7; 1387 -5.2; 1526 -4.3; 1678 -2.9; 1846 -1.2; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.4; 3957 -3.1; 4353 -4.9; 4788 -6.9; 5267 -8.6; 5793 -7.6; 6373 -5.0; 7010 -4.2; 7711 -6.4; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.9; 13660 -17.6; 15026 -23.2; 16529 -26.0; 18182 -27.3; 20000 -24.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Truth GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Truth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 98 Hz    | 0.32 | -2.4 dB  |
| Peaking | 254 Hz   | 0.55 | -3.1 dB  |
| Peaking | 2694 Hz  | 0.77 | 10.3 dB  |
| Peaking | 11041 Hz | 0.61 | 20.8 dB  |
| Peaking | 16403 Hz | 0.23 | -29.7 dB |
| Peaking | 1362 Hz  | 4.76 | -1.5 dB  |
| Peaking | 2999 Hz  | 0.26 | 0.4 dB   |
| Peaking | 5311 Hz  | 4    | -3.5 dB  |
| Peaking | 6789 Hz  | 3.87 | 4.1 dB   |
| Peaking | 8524 Hz  | 2.59 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -25.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Audio%20Truth/Dita%20Audio%20Truth.png)