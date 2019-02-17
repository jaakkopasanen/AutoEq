# Shure SRH940
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.5; 34 -2.3; 37 -2.9; 41 -3.7; 45 -4.3; 49 -4.8; 54 -5.2; 60 -5.6; 66 -5.7; 72 -5.0; 79 -3.8; 87 -3.7; 96 -5.3; 106 -6.2; 116 -6.0; 128 -5.7; 141 -6.5; 155 -6.8; 170 -6.7; 187 -8.1; 206 -8.7; 227 -9.1; 249 -9.4; 274 -9.3; 302 -9.2; 332 -10.4; 365 -9.3; 402 -8.7; 442 -8.4; 486 -8.1; 535 -7.8; 588 -7.4; 647 -7.1; 712 -6.9; 783 -6.5; 861 -6.2; 947 -6.6; 1042 -6.4; 1146 -6.5; 1261 -6.8; 1387 -7.5; 1526 -8.1; 1678 -8.6; 1846 -8.5; 2031 -8.4; 2234 -8.2; 2457 -6.7; 2703 -6.9; 2973 -6.9; 3270 -7.4; 3597 -8.0; 3957 -9.0; 4353 -9.3; 4788 -8.6; 5267 -5.6; 5793 -3.4; 6373 -2.8; 7010 -4.0; 7711 -7.0; 8482 -13.8; 9330 -16.3; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -7.7; 15026 -9.7; 16529 -8.2; 18182 -10.0; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH940 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.28 | 7.6 dB   |
| Peaking | 304 Hz   | 1.23 | -3.5 dB  |
| Peaking | 4998 Hz  | 1.04 | -5.2 dB  |
| Peaking | 6261 Hz  | 1.91 | 9.0 dB   |
| Peaking | 9006 Hz  | 4.39 | -11.8 dB |
| Peaking | 59 Hz    | 2.11 | -1.4 dB  |
| Peaking | 83 Hz    | 5.17 | 2.5 dB   |
| Peaking | 1841 Hz  | 2.73 | -1.9 dB  |
| Peaking | 2804 Hz  | 3.22 | 1.4 dB   |
| Peaking | 10811 Hz | 7.98 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)