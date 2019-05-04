# Denon AH-GC20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -16.2; 25 -16.4; 28 -16.5; 31 -16.6; 34 -16.5; 37 -16.5; 41 -16.4; 45 -16.3; 49 -16.1; 54 -16.0; 60 -15.7; 66 -15.4; 72 -15.1; 79 -14.7; 87 -14.4; 96 -14.0; 106 -13.5; 116 -13.1; 128 -12.6; 141 -12.1; 155 -11.5; 170 -10.9; 187 -10.3; 206 -9.7; 227 -9.2; 249 -8.8; 274 -8.8; 302 -9.0; 332 -9.3; 365 -9.9; 402 -10.9; 442 -11.7; 486 -11.6; 535 -10.2; 588 -8.9; 647 -7.9; 712 -7.5; 783 -7.5; 861 -7.8; 947 -7.8; 1042 -6.5; 1146 -4.4; 1261 -2.5; 1387 -1.1; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -4.5; 2973 -4.8; 3270 -1.0; 3597 -6.2; 3957 -10.2; 4353 -5.8; 4788 -7.1; 5267 -5.2; 5793 -4.2; 6373 -8.4; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-GC20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-GC20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 36 Hz   |  0.27 | -10.2 dB |
| Peaking | 471 Hz  |  2.11 | -4.5 dB  |
| Peaking | 1457 Hz |  3.62 | 4.0 dB   |
| Peaking | 2150 Hz |  1.44 | 5.9 dB   |
| Peaking | 3894 Hz | 10.69 | -5.7 dB  |
| Peaking | 619 Hz  |  0.41 | 0.3 dB   |
| Peaking | 946 Hz  |  3.55 | -2.2 dB  |
| Peaking | 1216 Hz |  6.31 | 1.1 dB   |
| Peaking | 2829 Hz | 11.11 | -3.5 dB  |
| Peaking | 3283 Hz | 11.28 | 4.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Denon%20AH-GC20/Denon%20AH-GC20.png)