# PNY Midtown
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.8; 23 -16.8; 25 -16.8; 28 -16.8; 31 -16.8; 34 -16.7; 37 -16.7; 41 -16.6; 45 -16.6; 49 -16.6; 54 -16.6; 60 -16.6; 66 -16.6; 72 -16.7; 79 -16.7; 87 -16.8; 96 -16.8; 106 -16.7; 116 -16.4; 128 -16.3; 141 -16.1; 155 -15.8; 170 -15.4; 187 -14.9; 206 -14.5; 227 -14.0; 249 -13.5; 274 -12.9; 302 -12.3; 332 -11.7; 365 -11.0; 402 -10.4; 442 -9.6; 486 -9.1; 535 -8.6; 588 -7.7; 647 -7.3; 712 -6.8; 783 -6.3; 861 -6.3; 947 -6.6; 1042 -6.1; 1146 -6.0; 1261 -6.5; 1387 -7.1; 1526 -7.9; 1678 -8.9; 1846 -10.3; 2031 -10.9; 2234 -10.8; 2457 -10.0; 2703 -7.9; 2973 -4.8; 3270 -1.9; 3597 -0.5; 3957 -1.0; 4353 -3.4; 4788 -4.7; 5267 -6.7; 5793 -11.1; 6373 -14.7; 7010 -9.1; 7711 -6.2; 8482 -6.4; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PNY Midtown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Midtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.18 | -10.1 dB |
| Peaking | 180 Hz  |  0.65 | -4.6 dB  |
| Peaking | 2235 Hz |  2.25 | -6.1 dB  |
| Peaking | 3631 Hz |  2.12 | 7.4 dB   |
| Peaking | 6220 Hz |  5.64 | -9.9 dB  |
| Peaking | 385 Hz  |  1.79 | -0.9 dB  |
| Peaking | 911 Hz  |  1    | 1.3 dB   |
| Peaking | 1757 Hz |  4.21 | -1.3 dB  |
| Peaking | 7636 Hz | 10.85 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -8.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Midtown/PNY%20Midtown.png)