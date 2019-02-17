# Beyerdynamic Custom One Pro switch position 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.6; 25 -7.0; 28 -7.5; 31 -7.8; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.2; 49 -7.8; 54 -7.0; 60 -5.7; 66 -5.3; 72 -5.4; 79 -3.9; 87 -1.6; 96 -0.7; 106 -2.1; 116 -3.5; 128 -5.4; 141 -7.2; 155 -7.5; 170 -7.7; 187 -10.2; 206 -10.3; 227 -10.1; 249 -10.0; 274 -10.0; 302 -9.7; 332 -9.4; 365 -9.1; 402 -8.8; 442 -8.5; 486 -8.4; 535 -8.2; 588 -7.8; 647 -7.6; 712 -7.7; 783 -6.6; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -6.4; 1261 -6.6; 1387 -7.2; 1526 -7.9; 1678 -8.7; 1846 -9.2; 2031 -9.2; 2234 -8.5; 2457 -6.5; 2703 -4.8; 2973 -3.0; 3270 -2.2; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Custom One Pro switch position 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro switch position 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 1.72 | -2.1 dB |
| Peaking | 98 Hz   | 2.07 | 7.1 dB  |
| Peaking | 234 Hz  | 0.77 | -4.1 dB |
| Peaking | 1986 Hz | 2.45 | -4.4 dB |
| Peaking | 4394 Hz | 1.13 | 7.0 dB  |
| Peaking | 1030 Hz | 1.87 | 1.0 dB  |
| Peaking | 2748 Hz | 0.2  | -0.5 dB |
| Peaking | 3069 Hz | 3.38 | 1.2 dB  |
| Peaking | 6265 Hz | 3.32 | 4.5 dB  |
| Peaking | 7414 Hz | 1.67 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%202/Beyerdynamic%20Custom%20One%20Pro%20switch%20position%202.png)