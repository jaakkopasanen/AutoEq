# Elysian Terminator
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -5.9; 28 -6.3; 31 -6.6; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.6; 49 -7.8; 54 -8.1; 60 -8.3; 66 -8.6; 72 -8.8; 79 -9.2; 87 -9.5; 96 -9.8; 106 -10.1; 116 -10.4; 128 -10.5; 141 -10.6; 155 -10.6; 170 -10.6; 187 -10.6; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.4; 442 -8.1; 486 -7.6; 535 -7.2; 588 -6.8; 647 -6.3; 712 -5.8; 783 -5.3; 861 -4.9; 947 -4.7; 1042 -5.0; 1146 -5.7; 1261 -6.5; 1387 -6.9; 1526 -7.0; 1678 -6.8; 1846 -6.6; 2031 -6.5; 2234 -6.3; 2457 -6.0; 2703 -5.8; 2973 -5.0; 3270 -3.2; 3597 -1.9; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.8; 5793 -2.2; 6373 -4.0; 7010 -6.6; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.2; 16529 -13.6; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Terminator GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Terminator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 96 Hz    | 0.94 | -1.3 dB |
| Peaking | 191 Hz   | 0.59 | -3.7 dB |
| Peaking | 862 Hz   | 2.49 | 2.3 dB  |
| Peaking | 4530 Hz  | 1.89 | 6.9 dB  |
| Peaking | 16283 Hz | 2.76 | -8.2 dB |
| Peaking | 18 Hz    | 2.06 | 1.7 dB  |
| Peaking | 3510 Hz  | 2.99 | 3.1 dB  |
| Peaking | 3726 Hz  | 1.01 | -2.2 dB |
| Peaking | 5715 Hz  | 2.97 | 2.2 dB  |
| Peaking | 7304 Hz  | 5.31 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -5.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Elysian%20Terminator/Elysian%20Terminator.png)