# Shure SRH1840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.2; 60 -1.6; 66 -2.0; 72 -2.2; 79 -2.0; 87 -2.6; 96 -3.5; 106 -4.1; 116 -4.6; 128 -5.1; 141 -5.5; 155 -5.9; 170 -6.1; 187 -6.4; 206 -6.6; 227 -6.6; 249 -6.7; 274 -6.8; 302 -6.7; 332 -6.7; 365 -6.5; 402 -6.6; 442 -6.4; 486 -6.2; 535 -6.0; 588 -5.8; 647 -5.8; 712 -5.6; 783 -5.1; 861 -6.0; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -7.0; 1387 -7.7; 1526 -8.6; 1678 -9.2; 1846 -10.5; 2031 -11.2; 2234 -11.6; 2457 -11.4; 2703 -11.3; 2973 -11.2; 3270 -10.9; 3597 -10.3; 3957 -9.8; 4353 -8.9; 4788 -7.6; 5267 -5.6; 5793 -6.2; 6373 -7.8; 7010 -6.0; 7711 -6.7; 8482 -10.0; 9330 -10.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.51 | 6.5 dB  |
| Peaking | 803 Hz   | 1.93 | 1.5 dB  |
| Peaking | 2508 Hz  | 1.17 | -5.5 dB |
| Peaking | 8965 Hz  | 7.31 | -5.0 dB |
| Peaking | 22049 Hz | 1.89 | 0.5 dB  |
| Peaking | 84 Hz    | 3.6  | 1.3 dB  |
| Peaking | 240 Hz   | 0.74 | -1.0 dB |
| Peaking | 474 Hz   | 0.63 | 0.4 dB  |
| Peaking | 3871 Hz  | 3.86 | -1.1 dB |
| Peaking | 5323 Hz  | 6.4  | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)