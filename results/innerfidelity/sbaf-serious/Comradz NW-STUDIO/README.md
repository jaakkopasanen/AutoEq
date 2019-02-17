# Comradz NW-STUDIO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.6; 402 -1.2; 442 -1.6; 486 -3.6; 535 -8.7; 588 -3.8; 647 -3.6; 712 -4.2; 783 -4.3; 861 -5.0; 947 -5.9; 1042 -7.1; 1146 -8.7; 1261 -11.1; 1387 -14.2; 1526 -17.8; 1678 -21.1; 1846 -23.9; 2031 -25.3; 2234 -25.6; 2457 -24.1; 2703 -22.5; 2973 -19.6; 3270 -15.8; 3597 -15.0; 3957 -15.9; 4353 -18.4; 4788 -19.7; 5267 -20.2; 5793 -21.9; 6373 -22.3; 7010 -21.1; 7711 -22.6; 8482 -25.6; 9330 -23.5; 10263 -15.5; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Comradz NW-STUDIO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 88 Hz    | 0.06 | 6.1 dB   |
| Peaking | 2083 Hz  | 0.99 | -25.8 dB |
| Peaking | 3857 Hz  | 0.15 | 4.8 dB   |
| Peaking | 6073 Hz  | 1.3  | -12.8 dB |
| Peaking | 8828 Hz  | 2.96 | -16.7 dB |
| Peaking | 525 Hz   | 8.27 | -7.6 dB  |
| Peaking | 789 Hz   | 0.59 | 1.5 dB   |
| Peaking | 1615 Hz  | 4.21 | -2.9 dB  |
| Peaking | 9864 Hz  | 6.42 | -2.7 dB  |
| Peaking | 11449 Hz | 4.79 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.4 dB   |
| Peaking | 125 Hz   | 1.41 | 4.3 dB   |
| Peaking | 250 Hz   | 1.41 | 5.8 dB   |
| Peaking | 500 Hz   | 1.41 | 2.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -20.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -17.7 dB |
| Peaking | 16000 Hz | 1.41 | 3.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO/Comradz%20NW-STUDIO.png)