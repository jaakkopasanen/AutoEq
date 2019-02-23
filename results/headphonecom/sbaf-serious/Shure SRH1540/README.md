# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.7; 25 -6.2; 28 -6.9; 31 -7.4; 34 -7.8; 37 -8.1; 41 -8.5; 45 -8.8; 49 -8.9; 54 -9.0; 60 -9.1; 66 -9.0; 72 -8.7; 79 -8.2; 87 -7.7; 96 -7.3; 106 -7.2; 116 -7.2; 128 -7.0; 141 -6.5; 155 -5.4; 170 -4.3; 187 -5.0; 206 -4.8; 227 -5.2; 249 -5.4; 274 -5.4; 302 -5.7; 332 -5.8; 365 -5.5; 402 -4.9; 442 -4.3; 486 -3.8; 535 -3.4; 588 -2.8; 647 -2.2; 712 -1.7; 783 -1.3; 861 -1.2; 947 -1.1; 1042 -1.4; 1146 -1.1; 1261 -1.1; 1387 -1.8; 1526 -2.8; 1678 -3.8; 1846 -4.5; 2031 -4.5; 2234 -3.7; 2457 -3.1; 2703 -2.1; 2973 -1.0; 3270 -1.4; 3597 -1.0; 3957 -1.9; 4353 -2.2; 4788 -1.9; 5267 -0.5; 5793 -2.9; 6373 -4.0; 7010 -2.2; 7711 -3.2; 8482 -3.9; 9330 -5.9; 10263 -4.0; 11289 -3.5; 12418 -3.5; 13660 -3.5; 15026 -3.5; 16529 -3.5; 18182 -3.5; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.78 | -4.6 dB |
| Peaking | 93 Hz   | 0.86 | -2.3 dB |
| Peaking | 331 Hz  | 1.93 | -2.2 dB |
| Peaking | 907 Hz  | 1.48 | 2.8 dB  |
| Peaking | 3724 Hz | 1.79 | 2.3 dB  |
| Peaking | 1311 Hz | 3.22 | 2.1 dB  |
| Peaking | 2287 Hz | 1.01 | -2.9 dB |
| Peaking | 2796 Hz | 2.29 | 3.2 dB  |
| Peaking | 5263 Hz | 9.39 | 2.8 dB  |
| Peaking | 9395 Hz | 7.48 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)