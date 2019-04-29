# Stax SR-L700 #2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.9; 66 -3.3; 72 -3.5; 79 -3.7; 87 -4.3; 96 -4.5; 106 -4.6; 116 -5.1; 128 -5.3; 141 -5.5; 155 -5.6; 170 -5.8; 187 -5.9; 206 -5.9; 227 -6.1; 249 -6.2; 274 -6.4; 302 -6.6; 332 -6.6; 365 -6.9; 402 -7.0; 442 -7.3; 486 -7.4; 535 -7.5; 588 -7.9; 647 -8.1; 712 -8.4; 783 -8.8; 861 -8.7; 947 -9.5; 1042 -9.7; 1146 -10.0; 1261 -9.7; 1387 -9.1; 1526 -7.8; 1678 -6.7; 1846 -5.2; 2031 -4.9; 2234 -4.2; 2457 -4.9; 2703 -4.9; 2973 -4.4; 3270 -3.3; 3597 -3.6; 3957 -2.8; 4353 -1.9; 4788 -2.3; 5267 -5.3; 5793 -8.7; 6373 -8.0; 7010 -7.0; 7711 -7.0; 8482 -8.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -12.6; 15026 -11.8; 16529 -9.4; 18182 -11.5; 20000 -16.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.55 | 6.6 dB  |
| Peaking | 1260 Hz  | 0.87 | -5.2 dB |
| Peaking | 2057 Hz  | 1.06 | 4.6 dB  |
| Peaking | 4311 Hz  | 3.52 | 4.8 dB  |
| Peaking | 20807 Hz | 0.14 | -7.2 dB |
| Peaking | 4943 Hz  | 6.85 | 2.0 dB  |
| Peaking | 5831 Hz  | 4.97 | -3.0 dB |
| Peaking | 11423 Hz | 5.17 | 2.7 dB  |
| Peaking | 19986 Hz | 3.87 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stax%20SR-L700%20#2/Stax%20SR-L700%20#2.png)