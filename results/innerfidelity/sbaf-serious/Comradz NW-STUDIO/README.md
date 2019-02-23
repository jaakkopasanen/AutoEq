# Comradz NW-STUDIO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.2; 535 -5.7; 588 -0.9; 647 -0.7; 712 -1.2; 783 -1.4; 861 -2.1; 947 -3.0; 1042 -4.2; 1146 -5.8; 1261 -8.1; 1387 -11.3; 1526 -14.9; 1678 -18.2; 1846 -21.0; 2031 -22.4; 2234 -22.7; 2457 -21.2; 2703 -19.5; 2973 -16.6; 3270 -12.8; 3597 -12.1; 3957 -13.0; 4353 -15.5; 4788 -16.8; 5267 -17.3; 5793 -19.0; 6373 -19.3; 7010 -18.1; 7711 -19.7; 8482 -22.6; 9330 -20.6; 10263 -12.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Comradz NW-STUDIO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 112 Hz  |  0.05 | 6.2 dB   |
| Peaking | 1145 Hz |  0.6  | 11.4 dB  |
| Peaking | 1775 Hz |  0.72 | -23.7 dB |
| Peaking | 2294 Hz |  3.02 | -6.3 dB  |
| Peaking | 7886 Hz |  1.61 | -12.9 dB |
| Peaking | 523 Hz  | 16.2  | -5.4 dB  |
| Peaking | 3561 Hz |  4.96 | 4.1 dB   |
| Peaking | 5581 Hz |  1.41 | -6.6 dB  |
| Peaking | 8965 Hz |  0.91 | 9.7 dB   |
| Peaking | 9134 Hz |  3.7  | -13.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 4.3 dB   |
| Peaking | 125 Hz   | 1.41 | 4.4 dB   |
| Peaking | 250 Hz   | 1.41 | 5.0 dB   |
| Peaking | 500 Hz   | 1.41 | 4.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -17.9 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -14.6 dB |
| Peaking | 16000 Hz | 1.41 | 2.7 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO/Comradz%20NW-STUDIO.png)