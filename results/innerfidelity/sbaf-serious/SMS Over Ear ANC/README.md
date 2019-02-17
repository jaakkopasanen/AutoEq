# SMS Over Ear ANC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -2.0; 25 -3.9; 28 -7.2; 31 -9.5; 34 -10.5; 37 -10.7; 41 -10.4; 45 -9.8; 49 -9.3; 54 -8.8; 60 -8.3; 66 -8.0; 72 -7.6; 79 -7.4; 87 -7.1; 96 -6.9; 106 -6.6; 116 -6.2; 128 -5.9; 141 -5.7; 155 -5.4; 170 -5.0; 187 -4.6; 206 -4.2; 227 -3.9; 249 -3.6; 274 -3.3; 302 -2.9; 332 -2.7; 365 -2.4; 402 -2.2; 442 -1.7; 486 -1.1; 535 -0.8; 588 -0.5; 647 -0.8; 712 -1.5; 783 -2.3; 861 -3.9; 947 -5.5; 1042 -7.2; 1146 -8.5; 1261 -10.8; 1387 -14.2; 1526 -17.0; 1678 -18.4; 1846 -16.3; 2031 -13.2; 2234 -12.3; 2457 -10.2; 2703 -8.9; 2973 -6.3; 3270 -5.7; 3597 -5.0; 3957 -3.8; 4353 -1.2; 4788 -0.5; 5267 -1.1; 5793 -4.8; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Over Ear ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Over Ear ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 22 Hz   |  1.52 | 9.4 dB   |
| Peaking | 34 Hz   |  1.08 | -6.9 dB  |
| Peaking | 627 Hz  |  0.55 | 7.0 dB   |
| Peaking | 1630 Hz |  1.53 | -15.0 dB |
| Peaking | 4668 Hz |  1.82 | 6.7 dB   |
| Peaking | 26 Hz   |  1.58 | -0.8 dB  |
| Peaking | 208 Hz  |  4.1  | 0.4 dB   |
| Peaking | 5699 Hz | 10.05 | -3.5 dB  |
| Peaking | 6622 Hz |  2.62 | 3.6 dB   |
| Peaking | 7577 Hz |  2.21 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB   |
| Peaking | 250 Hz   | 1.41 | 1.8 dB   |
| Peaking | 500 Hz   | 1.41 | 6.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20Over%20Ear%20ANC/SMS%20Over%20Ear%20ANC.png)