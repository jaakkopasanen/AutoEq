# Shure SRH1440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.7; 96 -1.2; 106 -1.7; 116 -2.1; 128 -2.7; 141 -3.2; 155 -3.7; 170 -3.8; 187 -4.1; 206 -4.3; 227 -4.4; 249 -4.6; 274 -4.6; 302 -4.8; 332 -4.7; 365 -4.5; 402 -4.5; 442 -4.5; 486 -4.3; 535 -4.3; 588 -4.3; 647 -3.6; 712 -3.7; 783 -4.1; 861 -4.4; 947 -4.9; 1042 -5.3; 1146 -5.5; 1261 -6.1; 1387 -6.8; 1526 -8.1; 1678 -9.5; 1846 -10.4; 2031 -10.8; 2234 -11.3; 2457 -11.3; 2703 -11.2; 2973 -11.8; 3270 -11.6; 3597 -11.6; 3957 -11.4; 4353 -10.8; 4788 -9.0; 5267 -7.6; 5793 -5.9; 6373 -7.0; 7010 -5.3; 7711 -6.2; 8482 -8.7; 9330 -12.3; 10263 -11.2; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.31 | 6.5 dB  |
| Peaking | 890 Hz  | 0.7  | 4.2 dB  |
| Peaking | 3305 Hz | 0.47 | -8.1 dB |
| Peaking | 7074 Hz | 0.76 | 6.6 dB  |
| Peaking | 9515 Hz | 3.25 | -8.8 dB |
| Peaking | 85 Hz   | 4.68 | 0.8 dB  |
| Peaking | 1908 Hz | 3.38 | -1.0 dB |
| Peaking | 2699 Hz | 0.69 | 0.6 dB  |
| Peaking | 4146 Hz | 5    | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 3.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)