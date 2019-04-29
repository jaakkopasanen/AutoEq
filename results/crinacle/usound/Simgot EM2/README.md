# Simgot EM2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.6; 25 -3.0; 28 -3.4; 31 -3.8; 34 -4.1; 37 -4.3; 41 -4.7; 45 -4.9; 49 -5.2; 54 -5.4; 60 -5.8; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.2; 96 -7.7; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.0; 249 -8.8; 274 -8.5; 302 -8.3; 332 -8.2; 365 -7.8; 402 -7.4; 442 -7.0; 486 -6.5; 535 -6.0; 588 -5.5; 647 -4.9; 712 -4.3; 783 -3.6; 861 -3.0; 947 -2.7; 1042 -2.8; 1146 -3.2; 1261 -3.8; 1387 -4.0; 1526 -3.9; 1678 -3.5; 1846 -3.1; 2031 -2.9; 2234 -2.8; 2457 -2.6; 2703 -1.7; 2973 -0.8; 3270 -0.5; 3597 -0.7; 3957 -1.2; 4353 -1.3; 4788 -1.6; 5267 -2.7; 5793 -3.9; 6373 -6.5; 7010 -6.7; 7711 -6.2; 8482 -5.9; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EM2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.48 | 3.6 dB  |
| Peaking | 189 Hz   | 0.49 | -4.3 dB |
| Peaking | 904 Hz   | 1.7  | 2.7 dB  |
| Peaking | 3798 Hz  | 0.86 | 4.8 dB  |
| Peaking | 6885 Hz  | 2.3  | -3.8 dB |
| Peaking | 5407 Hz  | 5.37 | 0.5 dB  |
| Peaking | 10100 Hz | 0.39 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Simgot%20EM2/Simgot%20EM2.png)