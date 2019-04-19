# Fiio F3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.6; 25 -9.8; 28 -10.1; 31 -10.3; 34 -10.4; 37 -10.6; 41 -10.7; 45 -10.8; 49 -11.0; 54 -11.3; 60 -11.6; 66 -11.9; 72 -12.0; 79 -12.4; 87 -12.3; 96 -12.2; 106 -12.4; 116 -12.3; 128 -12.5; 141 -12.2; 155 -12.0; 170 -11.9; 187 -11.7; 206 -11.5; 227 -11.2; 249 -10.9; 274 -10.5; 302 -10.0; 332 -9.5; 365 -9.0; 402 -8.5; 442 -8.1; 486 -7.7; 535 -7.3; 588 -6.9; 647 -6.6; 712 -6.2; 783 -5.9; 861 -5.8; 947 -5.9; 1042 -6.2; 1146 -6.7; 1261 -7.2; 1387 -7.2; 1526 -6.9; 1678 -6.3; 1846 -5.3; 2031 -3.9; 2234 -2.2; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.2; 6373 -5.4; 7010 -6.8; 7711 -8.6; 8482 -9.2; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.2; 15026 -24.0; 16529 -25.0; 18182 -23.2; 20000 -18.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio F3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio F3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.4  | -2.8 dB  |
| Peaking | 101 Hz   | 0.65 | -3.8 dB  |
| Peaking | 226 Hz   | 0.87 | -2.9 dB  |
| Peaking | 3956 Hz  | 0.83 | 7.4 dB   |
| Peaking | 17422 Hz | 0.83 | -20.5 dB |
| Peaking | 1506 Hz  | 2.75 | -2.3 dB  |
| Peaking | 2470 Hz  | 4.96 | 2.2 dB   |
| Peaking | 7884 Hz  | 3.12 | -4.2 dB  |
| Peaking | 12529 Hz | 1.41 | 9.0 dB   |
| Peaking | 14708 Hz | 2.33 | -11.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -22.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Fiio%20F3/Fiio%20F3.png)