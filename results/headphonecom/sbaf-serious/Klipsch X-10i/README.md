# Klipsch X-10i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.8; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.4; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.6; 79 -9.7; 87 -10.0; 96 -10.4; 106 -10.4; 116 -10.6; 128 -10.7; 141 -11.0; 155 -11.0; 170 -11.0; 187 -11.0; 206 -10.8; 227 -10.7; 249 -10.5; 274 -10.2; 302 -9.9; 332 -9.5; 365 -9.0; 402 -8.6; 442 -8.3; 486 -7.9; 535 -7.4; 588 -6.9; 647 -6.4; 712 -6.1; 783 -5.9; 861 -5.8; 947 -6.0; 1042 -6.3; 1146 -6.6; 1261 -7.0; 1387 -7.5; 1526 -8.0; 1678 -8.0; 1846 -7.7; 2031 -7.5; 2234 -7.4; 2457 -7.3; 2703 -7.5; 2973 -6.9; 3270 -3.8; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X-10i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X-10i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 71 Hz   | 0.47 | -2.2 dB |
| Peaking | 161 Hz  | 0.95 | -3.0 dB |
| Peaking | 293 Hz  | 1.61 | -1.9 dB |
| Peaking | 2562 Hz | 1.29 | -3.9 dB |
| Peaking | 4345 Hz | 1.21 | 8.2 dB  |
| Peaking | 826 Hz  | 2.61 | 1.2 dB  |
| Peaking | 1535 Hz | 4.96 | -1.1 dB |
| Peaking | 4628 Hz | 6.12 | -1.4 dB |
| Peaking | 6381 Hz | 2.44 | 4.3 dB  |
| Peaking | 7543 Hz | 1.85 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20X-10i/Klipsch%20X-10i.png)