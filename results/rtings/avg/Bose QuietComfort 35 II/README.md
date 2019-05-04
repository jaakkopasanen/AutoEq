# Bose QuietComfort 35 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -6.8; 25 -6.4; 28 -6.0; 31 -5.9; 34 -5.8; 37 -5.9; 41 -6.0; 45 -6.0; 49 -6.0; 54 -6.0; 60 -5.9; 66 -5.8; 72 -5.7; 79 -5.6; 87 -5.5; 96 -5.5; 106 -5.4; 116 -5.4; 128 -5.4; 141 -5.3; 155 -5.2; 170 -5.1; 187 -4.9; 206 -4.7; 227 -4.5; 249 -4.3; 274 -4.2; 302 -4.1; 332 -3.9; 365 -3.7; 402 -3.6; 442 -3.6; 486 -3.6; 535 -3.4; 588 -3.2; 647 -3.0; 712 -2.7; 783 -2.4; 861 -2.0; 947 -2.0; 1042 -1.8; 1146 -1.3; 1261 -1.2; 1387 -1.7; 1526 -2.3; 1678 -3.9; 1846 -5.8; 2031 -7.3; 2234 -7.1; 2457 -5.7; 2703 -4.5; 2973 -3.4; 3270 -1.7; 3597 -4.4; 3957 -6.2; 4353 -4.7; 4788 -3.6; 5267 -0.5; 5793 -3.3; 6373 -6.8; 7010 -3.3; 7711 -3.3; 8482 -3.6; 9330 -3.6; 10263 -3.6; 11289 -3.6; 12418 -6.3; 13660 -6.7; 15026 -6.5; 16529 -4.4; 18182 -3.6; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 1.42 | -3.9 dB |
| Peaking | 63 Hz    | 0.33 | -2.1 dB |
| Peaking | 1335 Hz  | 0.92 | 3.1 dB  |
| Peaking | 2058 Hz  | 2.58 | -5.8 dB |
| Peaking | 14104 Hz | 2.01 | -3.6 dB |
| Peaking | 3331 Hz  | 5.64 | 4.0 dB  |
| Peaking | 3807 Hz  | 3.26 | -3.6 dB |
| Peaking | 5417 Hz  | 6.13 | 5.1 dB  |
| Peaking | 6238 Hz  | 5.4  | -5.4 dB |
| Peaking | 7107 Hz  | 3.18 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2035%20II/Bose%20QuietComfort%2035%20II.png)