# Sony MH755 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.6; 25 -7.6; 28 -7.6; 31 -7.6; 34 -7.6; 37 -7.5; 41 -7.3; 45 -7.1; 49 -6.9; 54 -6.8; 60 -6.6; 66 -6.4; 72 -6.3; 79 -6.3; 87 -6.2; 96 -6.1; 106 -6.1; 116 -5.9; 128 -5.8; 141 -5.7; 155 -5.5; 170 -5.3; 187 -5.0; 206 -4.8; 227 -4.5; 249 -4.2; 274 -4.0; 302 -3.6; 332 -3.2; 365 -2.9; 402 -2.6; 442 -2.4; 486 -2.2; 535 -1.9; 588 -1.7; 647 -1.4; 712 -1.2; 783 -0.9; 861 -0.8; 947 -0.9; 1042 -1.3; 1146 -2.0; 1261 -2.5; 1387 -2.6; 1526 -2.3; 1678 -1.9; 1846 -1.5; 2031 -1.0; 2234 -0.6; 2457 -0.5; 2703 -1.0; 2973 -1.7; 3270 -2.2; 3597 -2.1; 3957 -1.5; 4353 -0.9; 4788 -0.6; 5267 -0.5; 5793 -1.1; 6373 -3.1; 7010 -3.4; 7711 -1.9; 8482 -2.2; 9330 -2.2; 10263 -2.2; 11289 -2.2; 12418 -2.2; 13660 -8.2; 15026 -20.2; 16529 -23.6; 18182 -17.6; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.09 | -5.1 dB  |
| Peaking | 740 Hz   | 1.58 | 1.6 dB   |
| Peaking | 8274 Hz  | 0.42 | 6.3 dB   |
| Peaking | 12561 Hz | 1.57 | 11.9 dB  |
| Peaking | 15877 Hz | 0.66 | -28.3 dB |
| Peaking | 1385 Hz  | 3.78 | -1.1 dB  |
| Peaking | 2392 Hz  | 2.64 | 1.3 dB   |
| Peaking | 3390 Hz  | 2.53 | -1.7 dB  |
| Peaking | 6009 Hz  | 1.15 | 1.7 dB   |
| Peaking | 6633 Hz  | 5.15 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -22.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MH755%20sample%201/Sony%20MH755%20sample%201.png)