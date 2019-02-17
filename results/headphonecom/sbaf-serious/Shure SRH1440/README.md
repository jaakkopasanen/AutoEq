# Shure SRH1440
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.5; 87 -2.1; 96 -2.6; 106 -3.2; 116 -3.6; 128 -4.1; 141 -4.6; 155 -5.1; 170 -5.3; 187 -5.6; 206 -5.8; 227 -5.9; 249 -6.1; 274 -6.1; 302 -6.3; 332 -6.2; 365 -6.0; 402 -5.9; 442 -5.9; 486 -5.8; 535 -5.8; 588 -5.8; 647 -5.1; 712 -5.2; 783 -5.5; 861 -5.9; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -8.3; 1526 -9.6; 1678 -10.9; 1846 -11.8; 2031 -12.3; 2234 -12.7; 2457 -12.8; 2703 -12.7; 2973 -13.3; 3270 -13.0; 3597 -13.0; 3957 -12.9; 4353 -12.3; 4788 -10.5; 5267 -9.1; 5793 -7.4; 6373 -8.5; 7010 -6.7; 7711 -7.5; 8482 -10.2; 9330 -13.8; 10263 -12.7; 11289 -7.0; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.45 | 6.7 dB   |
| Peaking | 942 Hz  | 0.89 | 3.4 dB   |
| Peaking | 3392 Hz | 0.45 | -9.6 dB  |
| Peaking | 7447 Hz | 0.66 | 7.1 dB   |
| Peaking | 9544 Hz | 2.96 | -10.5 dB |
| Peaking | 41 Hz   | 2.36 | -0.8 dB  |
| Peaking | 70 Hz   | 3.61 | 1.0 dB   |
| Peaking | 1912 Hz | 3.53 | -0.9 dB  |
| Peaking | 2857 Hz | 0.68 | 0.5 dB   |
| Peaking | 4158 Hz | 4.93 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)