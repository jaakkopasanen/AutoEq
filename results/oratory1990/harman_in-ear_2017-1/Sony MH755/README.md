# Sony MH755
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -12.7; 25 -12.4; 28 -12.0; 31 -11.6; 34 -11.3; 37 -10.9; 41 -10.4; 45 -10.0; 49 -9.6; 54 -9.3; 60 -8.9; 66 -8.5; 72 -8.3; 79 -8.1; 87 -7.9; 96 -7.7; 106 -7.6; 116 -7.4; 128 -7.3; 141 -7.2; 155 -6.9; 170 -6.7; 187 -6.5; 206 -6.2; 227 -5.9; 249 -5.7; 274 -5.5; 302 -5.1; 332 -4.8; 365 -4.4; 402 -4.2; 442 -4.0; 486 -3.8; 535 -3.5; 588 -3.3; 647 -3.0; 712 -2.8; 783 -2.6; 861 -2.4; 947 -2.6; 1042 -3.0; 1146 -3.7; 1261 -4.3; 1387 -4.6; 1526 -4.4; 1678 -4.2; 1846 -3.9; 2031 -3.5; 2234 -3.1; 2457 -3.1; 2703 -3.9; 2973 -4.5; 3270 -4.5; 3597 -4.1; 3957 -3.5; 4353 -2.9; 4788 -2.3; 5267 -1.6; 5793 -0.8; 6373 -0.5; 7010 -1.6; 7711 -3.6; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -4.5; 13660 -14.6; 15026 -22.4; 16529 -23.2; 18182 -21.1; 20000 -17.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.28 | -9.4 dB  |
| Peaking | 149 Hz   | 0.73 | -2.0 dB  |
| Peaking | 762 Hz   | 1.98 | 1.6 dB   |
| Peaking | 10744 Hz | 0.37 | 20.5 dB  |
| Peaking | 15952 Hz | 0.37 | -33.8 dB |
| Peaking | 1404 Hz  | 5.01 | -1.1 dB  |
| Peaking | 3223 Hz  | 5.4  | -1.1 dB  |
| Peaking | 6059 Hz  | 2.38 | 3.6 dB   |
| Peaking | 11008 Hz | 0.72 | -3.4 dB  |
| Peaking | 12165 Hz | 3.42 | 6.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 16000 Hz | 1.41 | -24.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20MH755/Sony%20MH755.png)