# Shure SRH440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.7; 87 -2.5; 96 -3.7; 106 -4.5; 116 -4.7; 128 -5.0; 141 -5.1; 155 -5.4; 170 -4.8; 187 -5.0; 206 -4.9; 227 -4.7; 249 -4.9; 274 -5.4; 302 -5.8; 332 -6.2; 365 -7.0; 402 -7.0; 442 -6.9; 486 -6.9; 535 -6.9; 588 -6.9; 647 -6.9; 712 -6.9; 783 -6.8; 861 -6.9; 947 -6.7; 1042 -5.8; 1146 -6.3; 1261 -6.8; 1387 -7.5; 1526 -8.5; 1678 -9.2; 1846 -9.0; 2031 -7.8; 2234 -6.6; 2457 -5.2; 2703 -4.7; 2973 -4.3; 3270 -4.6; 3597 -5.2; 3957 -4.8; 4353 -5.9; 4788 -4.9; 5267 -0.9; 5793 -4.3; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -12.4; 10263 -12.9; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.47 | 6.7 dB  |
| Peaking | 1760 Hz | 2.78 | -3.3 dB |
| Peaking | 2825 Hz | 2.34 | 2.4 dB  |
| Peaking | 6162 Hz | 2.13 | 5.0 dB  |
| Peaking | 9725 Hz | 3.71 | -8.2 dB |
| Peaking | 38 Hz   | 2.79 | -0.8 dB |
| Peaking | 76 Hz   | 2.75 | 2.5 dB  |
| Peaking | 102 Hz  | 1.26 | -1.5 dB |
| Peaking | 237 Hz  | 1.72 | 1.4 dB  |
| Peaking | 409 Hz  | 1.46 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)