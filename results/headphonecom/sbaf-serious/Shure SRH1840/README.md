# Shure SRH1840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.1; 72 -1.2; 79 -1.0; 87 -1.6; 96 -2.6; 106 -3.2; 116 -3.7; 128 -4.1; 141 -4.6; 155 -5.0; 170 -5.1; 187 -5.4; 206 -5.7; 227 -5.7; 249 -5.8; 274 -5.8; 302 -5.8; 332 -5.8; 365 -5.6; 402 -5.7; 442 -5.5; 486 -5.2; 535 -5.1; 588 -4.9; 647 -4.9; 712 -4.7; 783 -4.2; 861 -5.0; 947 -5.3; 1042 -5.6; 1146 -5.7; 1261 -6.1; 1387 -6.8; 1526 -7.7; 1678 -8.3; 1846 -9.5; 2031 -10.3; 2234 -10.6; 2457 -10.5; 2703 -10.4; 2973 -10.3; 3270 -9.9; 3597 -9.4; 3957 -8.9; 4353 -8.0; 4788 -6.6; 5267 -4.6; 5793 -5.2; 6373 -6.9; 7010 -5.1; 7711 -6.2; 8482 -9.1; 9330 -9.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.42 | 6.6 dB  |
| Peaking | 865 Hz  | 0.91 | 2.4 dB  |
| Peaking | 2503 Hz | 0.95 | -4.7 dB |
| Peaking | 5387 Hz | 4.01 | 3.2 dB  |
| Peaking | 8949 Hz | 8.39 | -4.1 dB |
| Peaking | 39 Hz   | 2.57 | -0.6 dB |
| Peaking | 81 Hz   | 4.17 | 1.1 dB  |
| Peaking | 184 Hz  | 1.42 | -0.5 dB |
| Peaking | 6287 Hz | 6.96 | -1.1 dB |
| Peaking | 7094 Hz | 6.9  | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)