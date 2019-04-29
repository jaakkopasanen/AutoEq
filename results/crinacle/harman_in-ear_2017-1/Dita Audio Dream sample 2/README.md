# Dita Audio Dream sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.0; 25 -11.8; 28 -11.6; 31 -11.3; 34 -11.1; 37 -11.0; 41 -10.7; 45 -10.5; 49 -10.4; 54 -10.2; 60 -10.1; 66 -10.1; 72 -10.1; 79 -10.1; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.6; 128 -10.7; 141 -10.8; 155 -10.9; 170 -10.8; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.4; 274 -10.2; 302 -9.9; 332 -9.4; 365 -9.0; 402 -8.6; 442 -8.2; 486 -7.8; 535 -7.3; 588 -6.8; 647 -6.2; 712 -5.7; 783 -5.1; 861 -4.6; 947 -4.4; 1042 -4.4; 1146 -4.8; 1261 -5.1; 1387 -5.0; 1526 -4.5; 1678 -3.8; 1846 -2.9; 2031 -1.9; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.1; 3597 -2.5; 3957 -4.4; 4353 -6.7; 4788 -8.4; 5267 -6.8; 5793 -5.6; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -13.2; 10263 -13.0; 11289 -10.9; 12418 -10.3; 13660 -14.6; 15026 -21.3; 16529 -23.5; 18182 -20.7; 20000 -15.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dita Audio Dream sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dita Audio Dream sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.18 | -5.4 dB  |
| Peaking | 193 Hz   | 0.73 | -4.0 dB  |
| Peaking | 2543 Hz  | 1.08 | 6.4 dB   |
| Peaking | 16295 Hz | 0.98 | -15.1 dB |
| Peaking | 19242 Hz | 0.78 | -7.0 dB  |
| Peaking | 878 Hz   | 3.12 | 1.8 dB   |
| Peaking | 4780 Hz  | 4.58 | -4.0 dB  |
| Peaking | 6727 Hz  | 3.11 | 4.9 dB   |
| Peaking | 9585 Hz  | 3.51 | -5.2 dB  |
| Peaking | 12420 Hz | 4.32 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -21.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dita%20Audio%20Dream%20sample%202/Dita%20Audio%20Dream%20sample%202.png)