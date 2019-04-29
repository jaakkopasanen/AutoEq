# Stax SR-L700 #3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -3.1; 66 -4.7; 72 -4.9; 79 -5.0; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.2; 128 -6.6; 141 -6.7; 155 -6.9; 170 -6.9; 187 -7.1; 206 -7.1; 227 -7.2; 249 -7.3; 274 -7.4; 302 -7.6; 332 -7.6; 365 -7.6; 402 -7.7; 442 -8.3; 486 -8.5; 535 -8.6; 588 -9.0; 647 -8.8; 712 -9.3; 783 -9.7; 861 -9.7; 947 -10.4; 1042 -10.5; 1146 -10.7; 1261 -10.1; 1387 -9.5; 1526 -8.3; 1678 -6.9; 1846 -5.4; 2031 -4.6; 2234 -3.4; 2457 -3.7; 2703 -3.3; 2973 -2.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.8; 5267 -4.5; 5793 -7.0; 6373 -6.7; 7010 -4.5; 7711 -6.2; 8482 -7.0; 9330 -10.8; 10263 -9.1; 11289 -6.5; 12418 -7.7; 13660 -17.9; 15026 -26.4; 16529 -30.6; 18182 -31.5; 20000 -25.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.86 | 7.0 dB   |
| Peaking | 1123 Hz  | 0.63 | -9.8 dB  |
| Peaking | 7670 Hz  | 0.12 | 12.4 dB  |
| Peaking | 15748 Hz | 2.54 | -10.4 dB |
| Peaking | 18202 Hz | 0.36 | -32.8 dB |
| Peaking | 4122 Hz  | 2.5  | 2.1 dB   |
| Peaking | 5889 Hz  | 4.36 | -4.7 dB  |
| Peaking | 9516 Hz  | 4.62 | -5.2 dB  |
| Peaking | 12087 Hz | 2.15 | 7.4 dB   |
| Peaking | 14183 Hz | 3.23 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB   |
| Peaking | 62 Hz    | 1.41 | 2.1 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -30.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stax%20SR-L700%20#3/Stax%20SR-L700%20#3.png)