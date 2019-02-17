# Skullcandy Crusher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.3; 34 -1.9; 37 -2.3; 41 -2.7; 45 -2.9; 49 -3.1; 54 -3.5; 60 -3.7; 66 -3.4; 72 -3.1; 79 -2.8; 87 -2.7; 96 -2.8; 106 -3.1; 116 -3.4; 128 -3.5; 141 -3.4; 155 -3.2; 170 -2.9; 187 -2.6; 206 -2.3; 227 -1.9; 249 -1.8; 274 -1.7; 302 -2.1; 332 -2.5; 365 -3.2; 402 -4.3; 442 -5.6; 486 -6.7; 535 -7.5; 588 -8.0; 647 -8.2; 712 -7.6; 783 -6.2; 861 -6.1; 947 -6.6; 1042 -6.2; 1146 -5.2; 1261 -3.8; 1387 -2.4; 1526 -2.0; 1678 -2.0; 1846 -2.3; 2031 -2.1; 2234 -1.4; 2457 -0.5; 2703 -0.7; 2973 -0.9; 3270 -0.9; 3597 -1.3; 3957 -2.7; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.1  | 4.8 dB  |
| Peaking | 255 Hz  | 1.68 | 4.3 dB  |
| Peaking | 1544 Hz | 3.24 | 3.4 dB  |
| Peaking | 2746 Hz | 1.46 | 5.6 dB  |
| Peaking | 5454 Hz | 2.29 | 5.8 dB  |
| Peaking | 35 Hz   | 0.37 | 2.2 dB  |
| Peaking | 50 Hz   | 1.13 | -3.1 dB |
| Peaking | 359 Hz  | 4.5  | 1.5 dB  |
| Peaking | 599 Hz  | 2.29 | -2.7 dB |
| Peaking | 8309 Hz | 4.29 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Crusher/Skullcandy%20Crusher.png)