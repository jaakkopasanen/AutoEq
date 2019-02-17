# Read and Heath Acoustics MA-350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.2; 25 -13.2; 28 -13.1; 31 -12.9; 34 -12.8; 37 -12.7; 41 -12.6; 45 -12.5; 49 -12.4; 54 -12.2; 60 -12.1; 66 -12.1; 72 -11.9; 79 -11.9; 87 -11.9; 96 -11.8; 106 -11.6; 116 -11.2; 128 -11.0; 141 -10.7; 155 -10.5; 170 -10.0; 187 -9.5; 206 -9.1; 227 -8.5; 249 -8.0; 274 -7.4; 302 -6.8; 332 -6.2; 365 -5.5; 402 -5.0; 442 -4.3; 486 -4.1; 535 -3.7; 588 -3.2; 647 -3.1; 712 -3.0; 783 -2.8; 861 -3.0; 947 -3.0; 1042 -3.0; 1146 -3.1; 1261 -3.0; 1387 -3.2; 1526 -3.4; 1678 -3.3; 1846 -2.7; 2031 -2.0; 2234 -1.4; 2457 -0.9; 2703 -0.5; 2973 -0.6; 3270 -1.1; 3597 -2.2; 3957 -4.0; 4353 -7.2; 4788 -10.5; 5267 -11.9; 5793 -6.6; 6373 -1.5; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read and Heath Acoustics MA-350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read and Heath Acoustics MA-350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.19 | -9.9 dB  |
| Peaking | 157 Hz  | 0.71 | -4.0 dB  |
| Peaking | 3054 Hz | 1.57 | 3.8 dB   |
| Peaking | 5141 Hz | 2.53 | -11.2 dB |
| Peaking | 6572 Hz | 3.77 | 6.5 dB   |
| Peaking | 291 Hz  | 2.69 | -0.5 dB  |
| Peaking | 652 Hz  | 1.31 | 0.7 dB   |
| Peaking | 1578 Hz | 4.39 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20and%20Heath%20Acoustics%20MA-350/Read%20and%20Heath%20Acoustics%20MA-350.png)