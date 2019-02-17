# Phiaton PS 210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.2; 34 -2.6; 37 -3.0; 41 -3.5; 45 -4.0; 49 -4.4; 54 -4.9; 60 -5.4; 66 -5.9; 72 -6.4; 79 -6.9; 87 -7.4; 96 -8.0; 106 -8.2; 116 -8.5; 128 -9.0; 141 -9.4; 155 -9.6; 170 -9.8; 187 -9.8; 206 -10.0; 227 -10.1; 249 -10.1; 274 -10.1; 302 -10.1; 332 -10.0; 365 -9.8; 402 -10.0; 442 -10.5; 486 -9.9; 535 -9.7; 588 -9.6; 647 -9.5; 712 -9.1; 783 -8.3; 861 -7.5; 947 -6.9; 1042 -6.3; 1146 -5.8; 1261 -5.8; 1387 -6.3; 1526 -7.4; 1678 -8.6; 1846 -9.9; 2031 -11.1; 2234 -11.9; 2457 -9.9; 2703 -6.7; 2973 -3.1; 3270 -0.9; 3597 -0.6; 3957 -2.8; 4353 -6.8; 4788 -6.3; 5267 -5.8; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  0.53 | 6.1 dB  |
| Peaking | 249 Hz   |  0.44 | -4.0 dB |
| Peaking | 2201 Hz  |  3.36 | -6.3 dB |
| Peaking | 3369 Hz  |  3.59 | 7.3 dB  |
| Peaking | 6304 Hz  |  5.73 | 6.1 dB  |
| Peaking | 660 Hz   |  1.63 | -1.7 dB |
| Peaking | 1334 Hz  |  1.02 | 3.2 dB  |
| Peaking | 1716 Hz  |  2.05 | -3.0 dB |
| Peaking | 4514 Hz  | 10.7  | -2.7 dB |
| Peaking | 22050 Hz |  1.71 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20210/Phiaton%20PS%20210.png)