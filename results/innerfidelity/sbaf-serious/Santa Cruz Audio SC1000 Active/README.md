# Santa Cruz Audio SC1000 Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.6; 25 -1.7; 28 -1.9; 31 -2.0; 34 -2.2; 37 -2.4; 41 -2.6; 45 -2.7; 49 -2.8; 54 -3.0; 60 -3.4; 66 -3.8; 72 -4.2; 79 -4.5; 87 -4.8; 96 -5.2; 106 -5.5; 116 -5.7; 128 -6.1; 141 -6.4; 155 -6.5; 170 -6.7; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.8; 274 -6.9; 302 -6.8; 332 -6.8; 365 -6.8; 402 -6.7; 442 -6.4; 486 -6.4; 535 -6.4; 588 -6.0; 647 -6.0; 712 -6.3; 783 -6.2; 861 -6.6; 947 -7.0; 1042 -7.1; 1146 -7.1; 1261 -7.2; 1387 -7.8; 1526 -8.4; 1678 -8.8; 1846 -8.9; 2031 -8.9; 2234 -9.0; 2457 -9.0; 2703 -9.3; 2973 -8.5; 3270 -6.7; 3597 -5.0; 3957 -5.2; 4353 -7.9; 4788 -9.7; 5267 -5.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -8.6; 9330 -9.2; 10263 -7.2; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Santa Cruz Audio SC1000 Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.84 | 4.7 dB  |
| Peaking | 55 Hz   | 1.34 | 2.2 dB  |
| Peaking | 2111 Hz | 1.29 | -2.9 dB |
| Peaking | 6148 Hz | 4.63 | 7.1 dB  |
| Peaking | 9043 Hz | 4.59 | -3.5 dB |
| Peaking | 652 Hz  | 4.21 | 0.6 dB  |
| Peaking | 2860 Hz | 5.29 | -1.7 dB |
| Peaking | 3738 Hz | 3.14 | 3.3 dB  |
| Peaking | 4729 Hz | 4.41 | -5.0 dB |
| Peaking | 5517 Hz | 9.46 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Active/Santa%20Cruz%20Audio%20SC1000%20Active.png)