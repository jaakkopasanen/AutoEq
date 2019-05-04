# Denon AHGC20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -16.1; 25 -16.2; 28 -16.4; 31 -16.4; 34 -16.4; 37 -16.4; 41 -16.3; 45 -16.2; 49 -16.0; 54 -15.9; 60 -15.6; 66 -15.3; 72 -15.0; 79 -14.6; 87 -14.2; 96 -13.8; 106 -13.4; 116 -12.9; 128 -12.5; 141 -11.9; 155 -11.4; 170 -10.8; 187 -10.2; 206 -9.6; 227 -9.1; 249 -8.8; 274 -8.7; 302 -9.0; 332 -9.3; 365 -10.0; 402 -10.9; 442 -11.7; 486 -11.7; 535 -10.2; 588 -8.4; 647 -7.0; 712 -6.7; 783 -7.3; 861 -8.0; 947 -8.1; 1042 -6.7; 1146 -4.6; 1261 -2.7; 1387 -1.3; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -5.2; 2973 -4.9; 3270 -0.7; 3597 -6.2; 3957 -9.9; 4353 -5.4; 4788 -7.5; 5267 -5.6; 5793 -4.2; 6373 -7.8; 7010 -5.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AHGC20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AHGC20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 36 Hz   |  0.26 | -10.0 dB |
| Peaking | 460 Hz  |  2.82 | -5.0 dB  |
| Peaking | 958 Hz  |  3.53 | -3.5 dB  |
| Peaking | 1563 Hz |  1.36 | 6.3 dB   |
| Peaking | 2296 Hz |  3.89 | 3.6 dB   |
| Peaking | 671 Hz  |  9.29 | 0.8 dB   |
| Peaking | 2829 Hz | 10.52 | -3.5 dB  |
| Peaking | 3299 Hz |  6.28 | 5.7 dB   |
| Peaking | 3819 Hz |  7.78 | -6.0 dB  |
| Peaking | 5667 Hz | 12.76 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Denon%20AHGC20/Denon%20AHGC20.png)