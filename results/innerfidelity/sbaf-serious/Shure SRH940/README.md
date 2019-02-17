# Shure SRH940
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.4; 41 -2.4; 45 -3.1; 49 -3.8; 54 -4.4; 60 -4.9; 66 -5.2; 72 -5.2; 79 -4.5; 87 -3.6; 96 -3.1; 106 -4.3; 116 -5.2; 128 -5.6; 141 -6.2; 155 -6.8; 170 -7.3; 187 -9.0; 206 -9.8; 227 -10.1; 249 -10.3; 274 -10.1; 302 -9.8; 332 -11.0; 365 -10.2; 402 -9.5; 442 -9.0; 486 -8.7; 535 -8.2; 588 -7.4; 647 -6.9; 712 -6.7; 783 -6.2; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.7; 1387 -7.5; 1526 -8.3; 1678 -9.1; 1846 -9.6; 2031 -9.6; 2234 -9.5; 2457 -8.5; 2703 -8.7; 2973 -8.3; 3270 -8.2; 3597 -8.6; 3957 -8.6; 4353 -9.1; 4788 -8.4; 5267 -6.5; 5793 -5.1; 6373 -5.4; 7010 -6.4; 7711 -9.9; 8482 -14.2; 9330 -16.0; 10263 -11.7; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -9.3; 16529 -6.5; 18182 -6.9; 20000 -11.9
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.94 | 6.5 dB   |
| Peaking | 98 Hz    | 2.55 | 3.1 dB   |
| Peaking | 285 Hz   | 1.13 | -4.4 dB  |
| Peaking | 2242 Hz  | 1.35 | -3.0 dB  |
| Peaking | 9152 Hz  | 4.02 | -10.6 dB |
| Peaking | 887 Hz   | 2.22 | 1.1 dB   |
| Peaking | 4464 Hz  | 3.66 | -2.1 dB  |
| Peaking | 6103 Hz  | 2.73 | 3.7 dB   |
| Peaking | 11629 Hz | 3.72 | 3.2 dB   |
| Peaking | 20355 Hz | 0.06 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)