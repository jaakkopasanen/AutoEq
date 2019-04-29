# Sony MH755 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.3; 25 -11.1; 28 -10.7; 31 -10.3; 34 -9.9; 37 -9.6; 41 -9.1; 45 -8.7; 49 -8.3; 54 -7.9; 60 -7.5; 66 -7.2; 72 -6.9; 79 -6.7; 87 -6.5; 96 -6.4; 106 -6.3; 116 -6.1; 128 -6.0; 141 -5.9; 155 -5.6; 170 -5.4; 187 -5.1; 206 -4.9; 227 -4.6; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.4; 365 -3.1; 402 -2.9; 442 -2.6; 486 -2.4; 535 -2.2; 588 -1.9; 647 -1.7; 712 -1.5; 783 -1.2; 861 -1.2; 947 -1.2; 1042 -1.7; 1146 -2.4; 1261 -3.0; 1387 -3.3; 1526 -3.1; 1678 -2.9; 1846 -2.6; 2031 -2.3; 2234 -2.0; 2457 -1.9; 2703 -2.6; 2973 -3.3; 3270 -3.4; 3597 -3.2; 3957 -2.9; 4353 -2.7; 4788 -2.1; 5267 -1.4; 5793 -0.8; 6373 -0.5; 7010 -1.1; 7711 -2.5; 8482 -2.7; 9330 -2.7; 10263 -2.8; 11289 -2.8; 12418 -3.7; 13660 -13.6; 15026 -20.9; 16529 -23.4; 18182 -21.2; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.31 | -9.0 dB  |
| Peaking | 148 Hz   | 0.76 | -1.9 dB  |
| Peaking | 755 Hz   | 1.57 | 1.8 dB   |
| Peaking | 10750 Hz | 0.54 | 14.5 dB  |
| Peaking | 16184 Hz | 0.53 | -29.1 dB |
| Peaking | 1373 Hz  | 6.29 | -0.9 dB  |
| Peaking | 6329 Hz  | 2.09 | 3.8 dB   |
| Peaking | 7837 Hz  | 0.98 | -2.8 dB  |
| Peaking | 12263 Hz | 3.81 | 4.6 dB   |
| Peaking | 14183 Hz | 4.56 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 16000 Hz | 1.41 | -25.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MH755%20sample%202/Sony%20MH755%20sample%202.png)