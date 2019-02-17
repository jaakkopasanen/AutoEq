# Shure SRH750DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -1.0; 41 -1.7; 45 -2.3; 49 -2.8; 54 -3.2; 60 -3.7; 66 -4.4; 72 -5.0; 79 -5.7; 87 -6.1; 96 -6.1; 106 -5.7; 116 -5.7; 128 -6.5; 141 -7.1; 155 -7.6; 170 -7.2; 187 -7.3; 206 -7.7; 227 -7.6; 249 -9.0; 274 -9.1; 302 -8.7; 332 -8.2; 365 -8.0; 402 -8.2; 442 -8.4; 486 -8.6; 535 -8.5; 588 -8.2; 647 -7.8; 712 -7.4; 783 -6.7; 861 -6.3; 947 -6.1; 1042 -6.7; 1146 -6.8; 1261 -6.6; 1387 -7.2; 1526 -8.4; 1678 -9.9; 1846 -12.0; 2031 -13.7; 2234 -14.4; 2457 -12.5; 2703 -10.3; 2973 -7.3; 3270 -5.5; 3597 -4.2; 3957 -4.6; 4353 -7.7; 4788 -4.8; 5267 -1.5; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -11.0; 9330 -12.1; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.71 | 6.4 dB  |
| Peaking | 303 Hz  | 0.79 | -2.3 dB |
| Peaking | 2160 Hz | 2.92 | -8.7 dB |
| Peaking | 6006 Hz | 2.09 | 6.5 dB  |
| Peaking | 8924 Hz | 4.27 | -7.8 dB |
| Peaking | 563 Hz  | 3.4  | -1.0 dB |
| Peaking | 922 Hz  | 2.57 | 1.1 dB  |
| Peaking | 2609 Hz | 5.39 | -1.8 dB |
| Peaking | 3655 Hz | 2.53 | 2.8 dB  |
| Peaking | 4406 Hz | 7.78 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)