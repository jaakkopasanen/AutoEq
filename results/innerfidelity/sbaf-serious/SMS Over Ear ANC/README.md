# SMS Over Ear ANC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -3.0; 25 -5.1; 28 -8.5; 31 -10.7; 34 -11.7; 37 -12.0; 41 -11.6; 45 -11.0; 49 -10.5; 54 -10.0; 60 -9.6; 66 -9.2; 72 -8.9; 79 -8.7; 87 -8.4; 96 -8.2; 106 -7.8; 116 -7.5; 128 -7.1; 141 -6.9; 155 -6.6; 170 -6.3; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.9; 274 -4.5; 302 -4.2; 332 -4.0; 365 -3.7; 402 -3.5; 442 -3.0; 486 -2.4; 535 -2.1; 588 -1.8; 647 -2.1; 712 -2.8; 783 -3.5; 861 -5.2; 947 -6.8; 1042 -8.5; 1146 -9.7; 1261 -12.1; 1387 -15.5; 1526 -18.3; 1678 -19.6; 1846 -17.6; 2031 -14.5; 2234 -13.6; 2457 -11.5; 2703 -10.2; 2973 -7.6; 3270 -7.0; 3597 -6.3; 3957 -5.1; 4353 -2.4; 4788 -0.5; 5267 -2.0; 5793 -6.1; 6373 -4.1; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Over Ear ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Over Ear ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 21 Hz   |  1.67 | 11.6 dB  |
| Peaking | 33 Hz   |  0.76 | -8.2 dB  |
| Peaking | 622 Hz  |  0.74 | 5.9 dB   |
| Peaking | 1641 Hz |  1.57 | -15.0 dB |
| Peaking | 4722 Hz |  2.72 | 6.9 dB   |
| Peaking | 2711 Hz |  2.86 | -0.9 dB  |
| Peaking | 3026 Hz |  6.19 | 2.0 dB   |
| Peaking | 5657 Hz | 13.48 | -2.8 dB  |
| Peaking | 6678 Hz |  6.28 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB   |
| Peaking | 500 Hz   | 1.41 | 5.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -12.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20Over%20Ear%20ANC/SMS%20Over%20Ear%20ANC.png)