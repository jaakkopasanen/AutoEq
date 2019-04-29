# Stax SR-002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.0; 25 -2.1; 28 -2.2; 31 -2.3; 34 -2.4; 37 -2.5; 41 -2.7; 45 -2.8; 49 -3.0; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.2; 79 -4.6; 87 -5.0; 96 -5.5; 106 -6.0; 116 -6.4; 128 -6.8; 141 -7.3; 155 -7.6; 170 -7.9; 187 -8.1; 206 -8.3; 227 -8.7; 249 -8.9; 274 -9.1; 302 -9.2; 332 -9.5; 365 -9.7; 402 -10.1; 442 -10.4; 486 -10.8; 535 -11.3; 588 -11.9; 647 -12.2; 712 -11.8; 783 -9.8; 861 -6.8; 947 -4.7; 1042 -4.7; 1146 -6.3; 1261 -8.0; 1387 -9.7; 1526 -11.6; 1678 -12.1; 1846 -9.5; 2031 -7.7; 2234 -7.9; 2457 -6.0; 2703 -3.9; 2973 -3.0; 3270 -2.4; 3597 -2.5; 3957 -5.1; 4353 -6.1; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.5; 15026 -14.3; 16529 -15.2; 18182 -14.4; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.61 | 4.7 dB  |
| Peaking | 466 Hz   | 0.88 | -4.8 dB |
| Peaking | 1638 Hz  | 4.51 | -6.0 dB |
| Peaking | 3169 Hz  | 3.35 | 4.3 dB  |
| Peaking | 5560 Hz  | 3.16 | 6.8 dB  |
| Peaking | 192 Hz   | 1.56 | -1.0 dB |
| Peaking | 471 Hz   | 1.33 | 3.2 dB  |
| Peaking | 717 Hz   | 1.09 | -5.5 dB |
| Peaking | 954 Hz   | 2.7  | 7.4 dB  |
| Peaking | 18491 Hz | 0.63 | -9.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB   |
| Peaking | 62 Hz    | 1.41 | 2.5 dB   |
| Peaking | 125 Hz   | 1.41 | -0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -10.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stax%20SR-002/Stax%20SR-002.png)