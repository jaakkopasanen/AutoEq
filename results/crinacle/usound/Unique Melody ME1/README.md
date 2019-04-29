# Unique Melody ME1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.2; 45 -1.6; 49 -2.0; 54 -2.4; 60 -2.9; 66 -3.5; 72 -4.0; 79 -4.5; 87 -5.1; 96 -5.7; 106 -6.2; 116 -6.7; 128 -7.2; 141 -7.7; 155 -8.1; 170 -8.4; 187 -8.7; 206 -9.0; 227 -9.2; 249 -9.4; 274 -9.6; 302 -9.8; 332 -9.9; 365 -10.2; 402 -10.4; 442 -10.6; 486 -10.8; 535 -11.1; 588 -11.3; 647 -11.6; 712 -11.8; 783 -11.8; 861 -11.7; 947 -11.3; 1042 -10.9; 1146 -10.6; 1261 -10.6; 1387 -10.3; 1526 -9.3; 1678 -7.3; 1846 -5.4; 2031 -3.5; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.9; 4353 -4.0; 4788 -0.6; 5267 -0.5; 5793 -0.6; 6373 -3.6; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody ME1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody ME1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.6  | 6.5 dB  |
| Peaking | 1153 Hz | 0.23 | -6.5 dB |
| Peaking | 2709 Hz | 1.08 | 11.9 dB |
| Peaking | 5408 Hz | 2.84 | 6.3 dB  |
| Peaking | 435 Hz  | 2.64 | 0.7 dB  |
| Peaking | 1440 Hz | 4.29 | -1.3 dB |
| Peaking | 2104 Hz | 2.61 | 1.5 dB  |
| Peaking | 3180 Hz | 1.5  | -1.5 dB |
| Peaking | 3550 Hz | 6.21 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | -6.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20ME1/Unique%20Melody%20ME1.png)