# Monoprice M1060
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.8; 28 -1.0; 31 -1.2; 34 -1.3; 37 -1.4; 41 -1.6; 45 -1.8; 49 -2.1; 54 -2.4; 60 -2.7; 66 -3.0; 72 -3.2; 79 -3.4; 87 -3.8; 96 -4.1; 106 -4.5; 116 -4.8; 128 -5.2; 141 -5.5; 155 -5.8; 170 -6.0; 187 -6.1; 206 -6.2; 227 -6.2; 249 -6.0; 274 -5.5; 302 -4.8; 332 -4.2; 365 -3.9; 402 -3.7; 442 -3.8; 486 -4.3; 535 -4.7; 588 -5.1; 647 -5.4; 712 -5.6; 783 -5.5; 861 -4.8; 947 -4.3; 1042 -4.5; 1146 -4.9; 1261 -5.4; 1387 -5.5; 1526 -5.6; 1678 -6.2; 1846 -6.7; 2031 -6.4; 2234 -6.2; 2457 -6.1; 2703 -6.0; 2973 -5.9; 3270 -5.5; 3597 -4.8; 3957 -5.5; 4353 -6.5; 4788 -4.9; 5267 -3.6; 5793 -3.3; 6373 -1.1; 7010 -1.9; 7711 -4.1; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -4.6; 12418 -4.4; 13660 -4.4; 15026 -5.6; 16529 -11.8; 18182 -18.3; 20000 -24.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice M1060 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.65 | 3.6 dB   |
| Peaking | 45 Hz    | 0.91 | 1.4 dB   |
| Peaking | 187 Hz   | 1.34 | -2.1 dB  |
| Peaking | 13757 Hz | 0.73 | 6.4 dB   |
| Peaking | 19530 Hz | 0.44 | -19.2 dB |
| Peaking | 397 Hz   | 3.42 | 1.2 dB   |
| Peaking | 689 Hz   | 4.15 | -1.2 dB  |
| Peaking | 2074 Hz  | 1.3  | -2.2 dB  |
| Peaking | 4308 Hz  | 8.46 | -2.0 dB  |
| Peaking | 6544 Hz  | 5.56 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Monoprice%20M1060/Monoprice%20M1060.png)