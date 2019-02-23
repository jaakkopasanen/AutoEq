# Skullcandy Crusher
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.9; 25 -3.2; 28 -4.9; 31 -6.3; 34 -7.5; 37 -8.5; 41 -9.4; 45 -10.1; 49 -10.4; 54 -10.5; 60 -10.8; 66 -10.8; 72 -10.5; 79 -10.1; 87 -9.5; 96 -8.3; 106 -9.1; 116 -9.7; 128 -10.5; 141 -10.2; 155 -10.6; 170 -10.1; 187 -10.6; 206 -10.7; 227 -10.8; 249 -10.9; 274 -10.8; 302 -10.9; 332 -10.5; 365 -10.1; 402 -9.9; 442 -9.9; 486 -9.9; 535 -10.2; 588 -10.0; 647 -9.9; 712 -9.9; 783 -9.3; 861 -9.0; 947 -7.8; 1042 -6.3; 1146 -4.4; 1261 -5.4; 1387 -5.8; 1526 -7.7; 1678 -8.9; 1846 -8.8; 2031 -9.1; 2234 -8.2; 2457 -8.2; 2703 -7.4; 2973 -6.6; 3270 -7.2; 3597 -6.8; 3957 -7.7; 4353 -8.5; 4788 -2.2; 5267 -0.6; 5793 -0.7; 6373 -1.2; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.56 | 7.6 dB  |
| Peaking | 50 Hz   | 1.06 | -4.3 dB |
| Peaking | 246 Hz  | 0.56 | -4.1 dB |
| Peaking | 654 Hz  | 2.42 | -2.0 dB |
| Peaking | 5747 Hz | 3.57 | 7.2 dB  |
| Peaking | 22 Hz   | 1.42 | 0.4 dB  |
| Peaking | 1221 Hz | 3.67 | 3.7 dB  |
| Peaking | 1870 Hz | 1.67 | -2.5 dB |
| Peaking | 4254 Hz | 7.85 | -4.3 dB |
| Peaking | 4932 Hz | 8.94 | 3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher/Skullcandy%20Crusher.png)