# Nocs NS 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.3; 23 -15.2; 25 -15.2; 28 -15.0; 31 -14.9; 34 -14.8; 37 -14.6; 41 -14.4; 45 -14.3; 49 -14.2; 54 -14.0; 60 -13.9; 66 -13.8; 72 -13.6; 79 -13.5; 87 -13.4; 96 -13.4; 106 -13.0; 116 -12.7; 128 -12.4; 141 -12.1; 155 -11.7; 170 -11.3; 187 -10.8; 206 -10.3; 227 -9.7; 249 -9.1; 274 -8.5; 302 -7.8; 332 -7.2; 365 -6.6; 402 -6.0; 442 -5.2; 486 -4.7; 535 -4.2; 588 -3.5; 647 -3.0; 712 -2.8; 783 -2.4; 861 -2.5; 947 -2.7; 1042 -3.0; 1146 -3.5; 1261 -3.8; 1387 -4.4; 1526 -4.8; 1678 -5.3; 1846 -5.6; 2031 -6.1; 2234 -7.2; 2457 -7.1; 2703 -6.9; 2973 -4.9; 3270 -2.3; 3597 -0.5; 3957 -0.7; 4353 -2.7; 4788 -3.9; 5267 -5.0; 5793 -8.0; 6373 -10.7; 7010 -8.1; 7711 -6.1; 8482 -6.2; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.37 | -8.4 dB |
| Peaking | 118 Hz  | 0.53 | -4.9 dB |
| Peaking | 753 Hz  | 1.01 | 4.5 dB  |
| Peaking | 3826 Hz | 3.44 | 6.4 dB  |
| Peaking | 6308 Hz | 6.33 | -5.3 dB |
| Peaking | 1320 Hz | 1.94 | 0.7 dB  |
| Peaking | 2579 Hz | 2.01 | -2.3 dB |
| Peaking | 3270 Hz | 5.75 | 2.3 dB  |
| Peaking | 4965 Hz | 6.76 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.1 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS%20400/Nocs%20NS%20400.png)