# Shure SRH240A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.6; 60 -2.5; 66 -3.4; 72 -4.1; 79 -4.7; 87 -5.4; 96 -5.8; 106 -6.1; 116 -6.4; 128 -6.5; 141 -6.4; 155 -6.2; 170 -5.8; 187 -5.1; 206 -4.6; 227 -4.1; 249 -3.9; 274 -4.1; 302 -4.8; 332 -6.1; 365 -6.6; 402 -7.3; 442 -8.6; 486 -9.7; 535 -10.2; 588 -10.3; 647 -9.9; 712 -9.4; 783 -8.8; 861 -8.4; 947 -8.1; 1042 -7.8; 1146 -7.7; 1261 -7.8; 1387 -8.3; 1526 -8.7; 1678 -9.0; 1846 -9.1; 2031 -8.5; 2234 -7.2; 2457 -6.1; 2703 -5.8; 2973 -6.3; 3270 -6.9; 3597 -6.5; 3957 -5.7; 4353 -4.8; 4788 -3.6; 5267 -1.7; 5793 -0.8; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -9.9; 11289 -11.3; 12418 -8.4; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -7.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH240A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH240A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.46 | 7.2 dB  |
| Peaking | 253 Hz   | 1.02 | 8.3 dB  |
| Peaking | 276 Hz   | 0.3  | -6.2 dB |
| Peaking | 5737 Hz  | 2.49 | 6.1 dB  |
| Peaking | 11021 Hz | 3.16 | -5.3 dB |
| Peaking | 582 Hz   | 2.24 | -2.0 dB |
| Peaking | 1203 Hz  | 0.61 | 2.5 dB  |
| Peaking | 1911 Hz  | 1.12 | -4.0 dB |
| Peaking | 2483 Hz  | 3.14 | 2.7 dB  |
| Peaking | 17649 Hz | 3.87 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SRH240A/Shure%20SRH240A.png)