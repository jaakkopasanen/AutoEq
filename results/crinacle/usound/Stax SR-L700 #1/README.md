# Stax SR-L700 #1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.4; 66 -3.1; 72 -3.4; 79 -3.7; 87 -4.3; 96 -4.6; 106 -4.8; 116 -5.0; 128 -5.5; 141 -5.7; 155 -5.7; 170 -5.7; 187 -5.9; 206 -6.0; 227 -6.0; 249 -6.1; 274 -6.3; 302 -6.5; 332 -6.7; 365 -7.1; 402 -7.5; 442 -7.6; 486 -7.4; 535 -7.4; 588 -7.8; 647 -8.1; 712 -8.6; 783 -8.9; 861 -8.9; 947 -9.8; 1042 -10.0; 1146 -10.3; 1261 -10.2; 1387 -9.3; 1526 -8.1; 1678 -7.0; 1846 -5.8; 2031 -5.3; 2234 -4.8; 2457 -5.4; 2703 -5.6; 2973 -4.8; 3270 -2.5; 3597 -1.7; 3957 -0.6; 4353 -0.5; 4788 -2.6; 5267 -6.0; 5793 -8.7; 6373 -7.3; 7010 -6.2; 7711 -6.4; 8482 -8.5; 9330 -9.5; 10263 -6.9; 11289 -6.5; 12418 -6.6; 13660 -10.0; 15026 -10.6; 16529 -11.1; 18182 -14.2; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.56 | 6.6 dB  |
| Peaking | 1372 Hz  | 0.76 | -5.5 dB |
| Peaking | 1975 Hz  | 1.48 | 5.1 dB  |
| Peaking | 3965 Hz  | 2.75 | 7.2 dB  |
| Peaking | 19552 Hz | 0.45 | -8.8 dB |
| Peaking | 90 Hz    | 4.1  | -0.4 dB |
| Peaking | 4639 Hz  | 8.53 | 2.0 dB  |
| Peaking | 5779 Hz  | 7.21 | -3.3 dB |
| Peaking | 9138 Hz  | 6.48 | -3.0 dB |
| Peaking | 11480 Hz | 3.17 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stax%20SR-L700%20#1/Stax%20SR-L700%20#1.png)