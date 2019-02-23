# Stax SR-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -3.2; 96 -5.5; 106 -7.4; 116 -8.3; 128 -9.0; 141 -9.2; 155 -9.2; 170 -9.6; 187 -9.7; 206 -9.3; 227 -9.0; 249 -8.6; 274 -8.3; 302 -8.1; 332 -7.8; 365 -7.8; 402 -7.7; 442 -7.3; 486 -7.4; 535 -7.4; 588 -7.1; 647 -7.1; 712 -7.2; 783 -7.4; 861 -8.0; 947 -8.3; 1042 -8.6; 1146 -7.9; 1261 -7.2; 1387 -7.3; 1526 -8.3; 1678 -8.5; 1846 -8.1; 2031 -7.4; 2234 -7.2; 2457 -7.2; 2703 -7.2; 2973 -6.4; 3270 -5.1; 3597 -3.4; 3957 -2.0; 4353 -1.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -12.6; 10263 -10.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 78 Hz   | 0.37 | 17.6 dB  |
| Peaking | 124 Hz  | 0.51 | -17.1 dB |
| Peaking | 2879 Hz | 0.54 | -3.8 dB  |
| Peaking | 4887 Hz | 0.97 | 9.4 dB   |
| Peaking | 9495 Hz | 3.81 | -8.6 dB  |
| Peaking | 17 Hz   | 1.26 | 1.8 dB   |
| Peaking | 47 Hz   | 1.59 | -0.9 dB  |
| Peaking | 79 Hz   | 5.2  | 1.7 dB   |
| Peaking | 96 Hz   | 5.36 | -0.8 dB  |
| Peaking | 2152 Hz | 5.56 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 6.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-1/Stax%20SR-1.png)