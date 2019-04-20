# Sony WI-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.5; 25 -9.7; 28 -9.8; 31 -9.9; 34 -9.9; 37 -9.9; 41 -9.8; 45 -9.8; 49 -9.8; 54 -9.8; 60 -9.8; 66 -9.9; 72 -10.0; 79 -10.1; 87 -10.3; 96 -10.3; 106 -10.2; 116 -10.1; 128 -10.7; 141 -11.2; 155 -11.2; 170 -11.0; 187 -10.7; 206 -10.4; 227 -10.1; 249 -9.8; 274 -9.6; 302 -9.2; 332 -8.8; 365 -8.3; 402 -7.8; 442 -7.3; 486 -6.9; 535 -6.6; 588 -6.3; 647 -5.7; 712 -4.8; 783 -4.0; 861 -3.7; 947 -4.1; 1042 -3.7; 1146 -3.1; 1261 -2.1; 1387 -1.4; 1526 -0.8; 1678 -0.5; 1846 -0.5; 2031 -0.8; 2234 -1.1; 2457 -2.1; 2703 -2.2; 2973 -1.5; 3270 -1.8; 3597 -3.0; 3957 -3.7; 4353 -2.6; 4788 -3.1; 5267 -5.2; 5793 -5.2; 6373 -3.3; 7010 -4.9; 7711 -7.9; 8482 -9.6; 9330 -9.5; 10263 -9.4; 11289 -9.8; 12418 -11.2; 13660 -17.0; 15026 -24.8; 16529 -26.0; 18182 -19.3; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.63 | -3.2 dB  |
| Peaking | 178 Hz   | 0.36 | -5.0 dB  |
| Peaking | 2598 Hz  | 0.27 | 5.4 dB   |
| Peaking | 12199 Hz | 2.11 | 6.1 dB   |
| Peaking | 15896 Hz | 0.73 | -22.9 dB |
| Peaking | 1046 Hz  | 4.9  | -1.0 dB  |
| Peaking | 1684 Hz  | 2.2  | 1.5 dB   |
| Peaking | 3222 Hz  | 0.64 | -0.7 dB  |
| Peaking | 6673 Hz  | 7.05 | 3.2 dB   |
| Peaking | 8340 Hz  | 6.3  | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -24.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20WI-1000X/Sony%20WI-1000X.png)