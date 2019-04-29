# Sony MH755
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.1; 25 -9.9; 28 -9.7; 31 -9.4; 34 -9.1; 37 -8.9; 41 -8.5; 45 -8.1; 49 -7.9; 54 -7.6; 60 -7.2; 66 -7.0; 72 -6.8; 79 -6.6; 87 -6.4; 96 -6.3; 106 -6.2; 116 -6.1; 128 -5.9; 141 -5.8; 155 -5.6; 170 -5.4; 187 -5.1; 206 -4.9; 227 -4.6; 249 -4.3; 274 -4.1; 302 -3.8; 332 -3.4; 365 -3.0; 402 -2.8; 442 -2.6; 486 -2.3; 535 -2.1; 588 -1.9; 647 -1.6; 712 -1.4; 783 -1.1; 861 -1.0; 947 -1.1; 1042 -1.6; 1146 -2.3; 1261 -2.9; 1387 -3.0; 1526 -2.8; 1678 -2.5; 1846 -2.2; 2031 -1.8; 2234 -1.4; 2457 -1.4; 2703 -2.1; 2973 -2.7; 3270 -2.9; 3597 -2.7; 3957 -2.2; 4353 -1.7; 4788 -1.2; 5267 -0.8; 5793 -0.5; 6373 -0.9; 7010 -1.4; 7711 -2.2; 8482 -2.5; 9330 -2.5; 10263 -2.5; 11289 -2.5; 12418 -2.7; 13660 -11.8; 15026 -20.8; 16529 -23.0; 18182 -19.6; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.26 | -7.9 dB  |
| Peaking | 149 Hz   | 0.72 | -2.1 dB  |
| Peaking | 767 Hz   | 1.67 | 1.7 dB   |
| Peaking | 11195 Hz | 0.44 | 17.4 dB  |
| Peaking | 16031 Hz | 0.51 | -32.8 dB |
| Peaking | 1361 Hz  | 5.46 | -0.9 dB  |
| Peaking | 5748 Hz  | 2.74 | 1.8 dB   |
| Peaking | 9058 Hz  | 1.62 | -1.8 dB  |
| Peaking | 12576 Hz | 4.11 | 4.3 dB   |
| Peaking | 14423 Hz | 4.82 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 16000 Hz | 1.41 | -24.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MH755/Sony%20MH755.png)