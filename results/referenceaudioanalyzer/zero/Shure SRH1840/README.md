# Shure SRH1840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.4; 41 -2.0; 45 -2.5; 49 -2.8; 54 -3.1; 60 -3.6; 66 -4.1; 72 -4.4; 79 -4.6; 87 -4.8; 96 -5.1; 106 -5.4; 116 -5.6; 128 -5.8; 141 -5.8; 155 -5.8; 170 -5.8; 187 -5.8; 206 -5.9; 227 -6.1; 249 -6.1; 274 -6.1; 302 -5.9; 332 -5.5; 365 -5.5; 402 -5.5; 442 -5.3; 486 -5.2; 535 -5.0; 588 -5.1; 647 -5.2; 712 -5.0; 783 -4.8; 861 -5.1; 947 -5.5; 1042 -5.6; 1146 -5.8; 1261 -5.8; 1387 -5.9; 1526 -6.1; 1678 -6.4; 1846 -7.0; 2031 -7.6; 2234 -8.3; 2457 -8.9; 2703 -9.5; 2973 -10.0; 3270 -10.5; 3597 -10.7; 3957 -10.7; 4353 -10.2; 4788 -9.3; 5267 -8.3; 5793 -6.6; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -8.3; 10263 -8.0; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.57 | 6.2 dB  |
| Peaking | 811 Hz  | 0.55 | 1.7 dB  |
| Peaking | 3623 Hz | 1    | -4.7 dB |
| Peaking | 6646 Hz | 4.41 | 5.5 dB  |
| Peaking | 9541 Hz | 4.48 | -1.8 dB |
| Peaking | 256 Hz  | 5.62 | -0.4 dB |
| Peaking | 1520 Hz | 1.55 | -0.7 dB |
| Peaking | 1572 Hz | 2.59 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SRH1840/Shure%20SRH1840.png)