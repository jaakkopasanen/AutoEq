# Stax SR-L700 #3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -2.0; 66 -3.6; 72 -3.8; 79 -3.8; 87 -4.2; 96 -4.6; 106 -4.9; 116 -5.1; 128 -5.5; 141 -5.5; 155 -5.7; 170 -5.7; 187 -5.9; 206 -6.0; 227 -6.1; 249 -6.2; 274 -6.3; 302 -6.5; 332 -6.6; 365 -6.7; 402 -6.8; 442 -7.5; 486 -7.7; 535 -7.9; 588 -8.3; 647 -8.1; 712 -8.7; 783 -9.0; 861 -8.9; 947 -9.7; 1042 -9.7; 1146 -10.0; 1261 -9.6; 1387 -9.3; 1526 -8.4; 1678 -7.0; 1846 -5.6; 2031 -5.2; 2234 -4.6; 2457 -5.5; 2703 -5.4; 2973 -4.4; 3270 -2.3; 3597 -2.0; 3957 -1.2; 4353 -1.3; 4788 -2.7; 5267 -5.4; 5793 -8.1; 6373 -8.3; 7010 -6.6; 7711 -6.2; 8482 -8.4; 9330 -9.9; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -10.1; 16529 -11.8; 18182 -15.0; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.57 | 6.6 dB  |
| Peaking | 1027 Hz  | 1.09 | -3.7 dB |
| Peaking | 4331 Hz  | 1.25 | 7.7 dB  |
| Peaking | 5823 Hz  | 1.92 | -5.5 dB |
| Peaking | 18850 Hz | 0.69 | -9.2 dB |
| Peaking | 2095 Hz  | 2.43 | 4.4 dB  |
| Peaking | 2325 Hz  | 1.24 | -3.1 dB |
| Peaking | 3304 Hz  | 6.59 | 1.5 dB  |
| Peaking | 9189 Hz  | 3.73 | -6.7 dB |
| Peaking | 9485 Hz  | 1.43 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Stax%20SR-L700%20#3/Stax%20SR-L700%20#3.png)