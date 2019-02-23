# Grado SR125i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.2; 72 -2.3; 79 -3.2; 87 -4.1; 96 -4.7; 106 -5.1; 116 -5.3; 128 -5.4; 141 -5.3; 155 -5.2; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.5; 249 -4.3; 274 -3.8; 302 -3.8; 332 -4.7; 365 -4.2; 402 -4.1; 442 -4.0; 486 -3.9; 535 -3.7; 588 -3.7; 647 -3.6; 712 -3.6; 783 -3.6; 861 -3.8; 947 -4.1; 1042 -4.4; 1146 -4.7; 1261 -5.2; 1387 -6.2; 1526 -7.4; 1678 -8.4; 1846 -9.4; 2031 -10.0; 2234 -10.6; 2457 -9.5; 2703 -8.4; 2973 -7.0; 3270 -5.9; 3597 -5.8; 3957 -6.1; 4353 -6.4; 4788 -9.6; 5267 -9.9; 5793 -11.5; 6373 -10.4; 7010 -10.9; 7711 -10.4; 8482 -13.0; 9330 -14.5; 10263 -9.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.62 | 6.8 dB  |
| Peaking | 2033 Hz  | 1.45 | -7.3 dB |
| Peaking | 3536 Hz  | 0.1  | 4.3 dB  |
| Peaking | 7957 Hz  | 0.84 | -9.9 dB |
| Peaking | 20043 Hz | 1.29 | -6.8 dB |
| Peaking | 3656 Hz  | 4.04 | 1.2 dB  |
| Peaking | 5540 Hz  | 8.02 | -3.0 dB |
| Peaking | 7706 Hz  | 3.49 | 4.2 dB  |
| Peaking | 9370 Hz  | 2.33 | -5.8 dB |
| Peaking | 10933 Hz | 3.34 | 5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)