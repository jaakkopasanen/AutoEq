# Daiso $2 earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.9; 28 -6.1; 31 -6.2; 34 -6.3; 37 -6.5; 41 -6.7; 45 -6.8; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.9; 72 -8.2; 79 -8.6; 87 -9.1; 96 -9.6; 106 -10.1; 116 -10.5; 128 -11.0; 141 -11.4; 155 -11.8; 170 -12.2; 187 -12.5; 206 -12.7; 227 -13.0; 249 -13.2; 274 -13.5; 302 -13.7; 332 -13.9; 365 -14.2; 402 -14.7; 442 -15.1; 486 -15.7; 535 -16.3; 588 -17.1; 647 -18.0; 712 -18.7; 783 -18.6; 861 -17.3; 947 -15.1; 1042 -12.5; 1146 -9.7; 1261 -8.9; 1387 -8.6; 1526 -5.3; 1678 -2.2; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.9; 5793 -5.7; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -16.1; 16529 -19.1; 18182 -17.5; 20000 -20.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Daiso $2 earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Daiso $2 earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 16 Hz    |  0.21 | 1.1 dB   |
| Peaking | 220 Hz   |  0.44 | -5.4 dB  |
| Peaking | 756 Hz   |  1    | -11.4 dB |
| Peaking | 2033 Hz  |  1.12 | 8.1 dB   |
| Peaking | 4243 Hz  |  1.56 | 5.1 dB   |
| Peaking | 409 Hz   |  3.2  | -0.1 dB  |
| Peaking | 6542 Hz  | 11.4  | 3.6 dB   |
| Peaking | 9215 Hz  |  0.54 | 5.9 dB   |
| Peaking | 12938 Hz |  2.04 | 8.2 dB   |
| Peaking | 17214 Hz |  0.27 | -14.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -8.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -8.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Daiso%20$2%20earphones/Daiso%20$2%20earphones.png)