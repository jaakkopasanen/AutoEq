# Shure SRH940
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.4; 49 -2.0; 54 -2.6; 60 -3.1; 66 -3.5; 72 -3.4; 79 -2.7; 87 -1.8; 96 -1.3; 106 -2.6; 116 -3.5; 128 -3.8; 141 -4.4; 155 -5.1; 170 -5.5; 187 -7.2; 206 -8.0; 227 -8.3; 249 -8.5; 274 -8.3; 302 -8.0; 332 -9.2; 365 -8.4; 402 -7.8; 442 -7.3; 486 -6.9; 535 -6.4; 588 -5.6; 647 -5.2; 712 -4.9; 783 -4.4; 861 -4.4; 947 -4.6; 1042 -4.7; 1146 -4.8; 1261 -5.0; 1387 -5.7; 1526 -6.5; 1678 -7.3; 1846 -7.8; 2031 -7.8; 2234 -7.7; 2457 -6.7; 2703 -6.9; 2973 -6.5; 3270 -6.4; 3597 -6.8; 3957 -6.8; 4353 -7.3; 4788 -6.6; 5267 -4.7; 5793 -3.4; 6373 -3.6; 7010 -4.7; 7711 -8.1; 8482 -12.4; 9330 -14.2; 10263 -9.9; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -7.6; 16529 -6.5; 18182 -6.5; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH940 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.67 | 6.4 dB  |
| Peaking | 100 Hz  | 1.66 | 3.7 dB  |
| Peaking | 265 Hz  | 1.68 | -2.8 dB |
| Peaking | 6305 Hz | 3.28 | 4.4 dB  |
| Peaking | 9062 Hz | 3.7  | -8.9 dB |
| Peaking | 405 Hz  | 1.72 | -1.7 dB |
| Peaking | 1000 Hz | 0.59 | 2.6 dB  |
| Peaking | 1883 Hz | 1.74 | -3.0 dB |
| Peaking | 4443 Hz | 3.07 | -1.2 dB |
| Peaking | 5448 Hz | 9.77 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)