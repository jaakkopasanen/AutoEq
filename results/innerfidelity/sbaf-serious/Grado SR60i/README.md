# Grado SR60i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.1; 41 -2.0; 45 -2.8; 49 -3.6; 54 -4.4; 60 -5.1; 66 -5.6; 72 -6.1; 79 -6.4; 87 -6.9; 96 -7.3; 106 -7.3; 116 -7.4; 128 -7.5; 141 -7.5; 155 -7.4; 170 -7.2; 187 -7.1; 206 -7.0; 227 -6.5; 249 -6.3; 274 -6.2; 302 -6.0; 332 -6.0; 365 -5.8; 402 -5.6; 442 -5.4; 486 -5.4; 535 -5.3; 588 -4.9; 647 -4.8; 712 -4.9; 783 -4.7; 861 -5.0; 947 -5.1; 1042 -5.2; 1146 -5.3; 1261 -5.8; 1387 -6.7; 1526 -7.8; 1678 -8.6; 1846 -11.4; 2031 -15.0; 2234 -13.3; 2457 -10.3; 2703 -8.1; 2973 -6.4; 3270 -6.6; 3597 -6.3; 3957 -3.9; 4353 -3.7; 4788 -3.1; 5267 -4.7; 5793 -3.8; 6373 -2.8; 7010 -6.5; 7711 -6.7; 8482 -6.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.59 | 6.9 dB  |
| Peaking | 91 Hz   | 0.58 | -2.4 dB |
| Peaking | 775 Hz  | 0.53 | 1.9 dB  |
| Peaking | 2075 Hz | 3.09 | -9.6 dB |
| Peaking | 4809 Hz | 1.75 | 3.4 dB  |
| Peaking | 5469 Hz | 9.44 | -2.1 dB |
| Peaking | 6319 Hz | 5.12 | 3.6 dB  |
| Peaking | 6962 Hz | 5.05 | -2.2 dB |
| Peaking | 8715 Hz | 3.89 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR60i/Grado%20SR60i.png)