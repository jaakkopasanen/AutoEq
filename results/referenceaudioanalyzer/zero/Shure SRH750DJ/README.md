# Shure SRH750DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.7; 141 -1.2; 155 -1.3; 170 -1.5; 187 -1.5; 206 -1.5; 227 -1.4; 249 -1.2; 274 -1.8; 302 -2.9; 332 -3.8; 365 -4.9; 402 -5.9; 442 -6.7; 486 -7.2; 535 -7.7; 588 -8.3; 647 -8.8; 712 -8.9; 783 -8.6; 861 -8.0; 947 -7.4; 1042 -7.1; 1146 -7.3; 1261 -7.1; 1387 -7.2; 1526 -7.6; 1678 -8.4; 1846 -9.6; 2031 -10.9; 2234 -11.9; 2457 -12.4; 2703 -12.1; 2973 -11.2; 3270 -9.9; 3597 -8.5; 3957 -7.9; 4353 -7.4; 4788 -6.6; 5267 -6.1; 5793 -5.9; 6373 -5.5; 7010 -6.0; 7711 -9.0; 8482 -11.9; 9330 -12.6; 10263 -12.0; 11289 -12.7; 12418 -14.2; 13660 -12.8; 15026 -7.4; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.22 | 5.6 dB   |
| Peaking | 636 Hz   | 0.74 | -8.8 dB  |
| Peaking | 2035 Hz  | 0.05 | 7.5 dB   |
| Peaking | 2502 Hz  | 1.01 | -11.5 dB |
| Peaking | 11411 Hz | 0.75 | -13.7 dB |
| Peaking | 409 Hz   | 6.13 | -0.6 dB  |
| Peaking | 6711 Hz  | 4.53 | 2.0 dB   |
| Peaking | 8520 Hz  | 5.83 | -2.7 dB  |
| Peaking | 15597 Hz | 4.88 | 2.3 dB   |
| Peaking | 19095 Hz | 0.37 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH750DJ/Shure%20SRH750DJ.png)