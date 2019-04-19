# Sennheiser HE1 Orpheus 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.3; 25 -5.5; 28 -5.6; 31 -5.5; 34 -5.2; 37 -5.0; 41 -5.2; 45 -6.0; 49 -6.6; 54 -6.5; 60 -5.7; 66 -5.3; 72 -5.5; 79 -5.7; 87 -6.0; 96 -6.0; 106 -5.8; 116 -5.8; 128 -5.8; 141 -5.8; 155 -5.7; 170 -5.7; 187 -5.6; 206 -5.5; 227 -5.5; 249 -5.6; 274 -5.6; 302 -5.6; 332 -5.5; 365 -5.3; 402 -5.1; 442 -4.8; 486 -4.8; 535 -5.0; 588 -5.1; 647 -5.0; 712 -4.7; 783 -4.6; 861 -5.0; 947 -5.4; 1042 -5.7; 1146 -5.4; 1261 -4.7; 1387 -3.3; 1526 -2.1; 1678 -2.3; 1846 -3.6; 2031 -3.8; 2234 -4.0; 2457 -4.0; 2703 -4.2; 2973 -3.3; 3270 -2.9; 3597 -1.9; 3957 -1.0; 4353 -0.5; 4788 -1.3; 5267 -2.8; 5793 -4.2; 6373 -5.7; 7010 -5.4; 7711 -5.2; 8482 -7.1; 9330 -9.3; 10263 -9.7; 11289 -8.7; 12418 -5.0; 13660 -4.7; 15026 -4.7; 16529 -5.5; 18182 -8.4; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HE1 Orpheus 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HE1 Orpheus 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 91 Hz    | 0.28 | -1.2 dB  |
| Peaking | 1101 Hz  | 3.23 | -1.4 dB  |
| Peaking | 1564 Hz  | 3.5  | 2.9 dB   |
| Peaking | 4235 Hz  | 2.38 | 4.5 dB   |
| Peaking | 9948 Hz  | 2.28 | -5.6 dB  |
| Peaking | 3225 Hz  | 4.74 | 0.2 dB   |
| Peaking | 14988 Hz | 1.34 | 1.7 dB   |
| Peaking | 20029 Hz | 1    | -11.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HE1%20Orpheus%202/Sennheiser%20HE1%20Orpheus%202.png)