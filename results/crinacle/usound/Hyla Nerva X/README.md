# Hyla Nerva X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.9; 25 -8.1; 28 -8.3; 31 -8.5; 34 -8.6; 37 -8.8; 41 -8.9; 45 -9.0; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.5; 72 -9.8; 79 -10.0; 87 -10.2; 96 -10.5; 106 -10.7; 116 -10.8; 128 -11.0; 141 -11.1; 155 -11.2; 170 -11.1; 187 -11.1; 206 -10.9; 227 -10.8; 249 -10.6; 274 -10.4; 302 -10.3; 332 -10.0; 365 -9.8; 402 -9.6; 442 -9.3; 486 -9.0; 535 -8.7; 588 -8.4; 647 -8.0; 712 -7.5; 783 -7.1; 861 -6.7; 947 -6.6; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -8.6; 1526 -8.6; 1678 -7.3; 1846 -6.8; 2031 -7.0; 2234 -5.9; 2457 -4.2; 2703 -2.4; 2973 -1.2; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -3.8; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.5; 18182 -8.6; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla Nerva X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla Nerva X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 59 Hz    | 0.3  | -1.9 dB |
| Peaking | 207 Hz   | 0.48 | -3.6 dB |
| Peaking | 1621 Hz  | 1.74 | -3.0 dB |
| Peaking | 4078 Hz  | 0.88 | 7.6 dB  |
| Peaking | 19713 Hz | 0.04 | -1.3 dB |
| Peaking | 917 Hz   | 4.49 | 1.0 dB  |
| Peaking | 5597 Hz  | 4.07 | 2.1 dB  |
| Peaking | 5890 Hz  | 4.63 | 1.8 dB  |
| Peaking | 6560 Hz  | 1.65 | -2.2 dB |
| Peaking | 13731 Hz | 1.68 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hyla%20Nerva%20X/Hyla%20Nerva%20X.png)