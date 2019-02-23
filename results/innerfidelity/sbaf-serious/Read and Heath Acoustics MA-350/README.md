# Read and Heath Acoustics MA-350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.2; 23 -13.2; 25 -13.1; 28 -13.0; 31 -12.9; 34 -12.8; 37 -12.7; 41 -12.6; 45 -12.4; 49 -12.3; 54 -12.2; 60 -12.1; 66 -12.0; 72 -11.9; 79 -11.9; 87 -11.8; 96 -11.8; 106 -11.5; 116 -11.2; 128 -11.0; 141 -10.7; 155 -10.4; 170 -10.0; 187 -9.5; 206 -9.1; 227 -8.4; 249 -7.9; 274 -7.3; 302 -6.7; 332 -6.1; 365 -5.5; 402 -4.9; 442 -4.3; 486 -4.0; 535 -3.7; 588 -3.2; 647 -3.1; 712 -3.0; 783 -2.7; 861 -3.0; 947 -3.0; 1042 -3.0; 1146 -3.0; 1261 -3.0; 1387 -3.2; 1526 -3.3; 1678 -3.2; 1846 -2.7; 2031 -1.9; 2234 -1.4; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -1.1; 3597 -2.2; 3957 -4.0; 4353 -7.2; 4788 -10.5; 5267 -11.8; 5793 -6.6; 6373 -1.4; 7010 -2.0; 7711 -4.3; 8482 -4.5; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read and Heath Acoustics MA-350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read and Heath Acoustics MA-350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.18 | -8.4 dB  |
| Peaking | 150 Hz  | 0.79 | -3.1 dB  |
| Peaking | 4274 Hz | 0.48 | 22.1 dB  |
| Peaking | 4985 Hz | 0.87 | -29.4 dB |
| Peaking | 6528 Hz | 4.03 | 7.4 dB   |
| Peaking | 605 Hz  | 1.85 | 0.9 dB   |
| Peaking | 1577 Hz | 1.96 | -1.4 dB  |
| Peaking | 2692 Hz | 3.04 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20and%20Heath%20Acoustics%20MA-350/Read%20and%20Heath%20Acoustics%20MA-350.png)