# Fiio FH3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -10.2; 25 -10.6; 28 -10.6; 31 -10.7; 34 -10.9; 37 -11.0; 41 -11.2; 45 -11.2; 49 -11.4; 54 -11.8; 60 -12.0; 66 -12.4; 72 -12.4; 79 -12.9; 87 -12.8; 96 -12.6; 106 -12.9; 116 -12.7; 128 -12.9; 141 -12.6; 155 -12.5; 170 -12.3; 187 -12.2; 206 -12.0; 227 -11.7; 249 -11.3; 274 -10.9; 302 -10.5; 332 -9.9; 365 -9.4; 402 -9.0; 442 -8.6; 486 -8.1; 535 -7.7; 588 -7.3; 647 -7.0; 712 -6.7; 783 -6.4; 861 -6.2; 947 -6.3; 1042 -6.7; 1146 -7.1; 1261 -7.6; 1387 -7.7; 1526 -7.4; 1678 -6.7; 1846 -5.8; 2031 -4.4; 2234 -2.7; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -2.6; 6373 -5.9; 7010 -7.3; 7711 -9.0; 8482 -9.6; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.7; 15026 -24.5; 16529 -25.5; 18182 -23.7; 20000 -19.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.34 | -3.5 dB  |
| Peaking | 158 Hz   | 0.47 | -4.7 dB  |
| Peaking | 3929 Hz  | 0.92 | 7.5 dB   |
| Peaking | 17437 Hz | 0.83 | -21.0 dB |
| Peaking | 1504 Hz  | 2.67 | -2.4 dB  |
| Peaking | 2514 Hz  | 4.96 | 2.3 dB   |
| Peaking | 7872 Hz  | 2.99 | -4.5 dB  |
| Peaking | 12452 Hz | 1.35 | 9.4 dB   |
| Peaking | 14746 Hz | 2.26 | -11.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20FH3/Fiio%20FH3.png)