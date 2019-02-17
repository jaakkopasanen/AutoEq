# Grado SR125i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.4; 37 -2.3; 41 -3.2; 45 -4.1; 49 -4.9; 54 -5.6; 60 -6.4; 66 -7.0; 72 -7.5; 79 -8.0; 87 -8.4; 96 -8.8; 106 -8.8; 116 -8.8; 128 -9.0; 141 -8.9; 155 -8.8; 170 -8.6; 187 -8.4; 206 -8.1; 227 -7.7; 249 -7.5; 274 -7.1; 302 -6.6; 332 -7.2; 365 -7.2; 402 -7.2; 442 -6.9; 486 -6.8; 535 -6.7; 588 -6.2; 647 -6.2; 712 -6.3; 783 -6.1; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -7.1; 1387 -8.0; 1526 -9.4; 1678 -10.1; 1846 -12.5; 2031 -16.6; 2234 -15.3; 2457 -12.4; 2703 -10.4; 2973 -8.4; 3270 -6.8; 3597 -8.4; 3957 -8.1; 4353 -6.3; 4788 -6.6; 5267 -7.4; 5793 -5.4; 6373 -5.1; 7010 -8.7; 7711 -10.1; 8482 -10.7; 9330 -10.0; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.86 | 6.7 dB   |
| Peaking | 108 Hz   | 0.73 | -3.1 dB  |
| Peaking | 2109 Hz  | 3.09 | -10.5 dB |
| Peaking | 8472 Hz  | 3.81 | -4.9 dB  |
| Peaking | 22050 Hz | 2.1  | -2.7 dB  |
| Peaking | 11 Hz    | 0.52 | 0.2 dB   |
| Peaking | 837 Hz   | 1.81 | 0.8 dB   |
| Peaking | 6199 Hz  | 6.88 | 3.2 dB   |
| Peaking | 7194 Hz  | 5.62 | -1.8 dB  |
| Peaking | 10728 Hz | 5.7  | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)