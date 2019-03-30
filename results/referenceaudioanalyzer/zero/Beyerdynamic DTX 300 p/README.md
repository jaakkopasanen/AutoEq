# Beyerdynamic DTX 300 p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.7; 486 -1.3; 535 -2.2; 588 -3.3; 647 -4.8; 712 -6.6; 783 -8.4; 861 -10.3; 947 -11.8; 1042 -13.2; 1146 -14.1; 1261 -14.9; 1387 -15.3; 1526 -15.3; 1678 -15.1; 1846 -15.6; 2031 -16.0; 2234 -15.7; 2457 -14.9; 2703 -13.3; 2973 -11.3; 3270 -9.4; 3597 -8.1; 3957 -8.0; 4353 -10.1; 4788 -12.6; 5267 -14.0; 5793 -15.2; 6373 -17.0; 7010 -18.4; 7711 -17.1; 8482 -12.9; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DTX 300 p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 300 p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 51 Hz   | 0.1  | 6.0 dB   |
| Peaking | 472 Hz  | 0.96 | 4.1 dB   |
| Peaking | 1215 Hz | 0.94 | -9.4 dB  |
| Peaking | 2190 Hz | 2.22 | -6.0 dB  |
| Peaking | 6811 Hz | 2.14 | -12.3 dB |
| Peaking | 2715 Hz | 5.19 | -1.4 dB  |
| Peaking | 3850 Hz | 3.16 | 2.9 dB   |
| Peaking | 5054 Hz | 2.34 | -4.2 dB  |
| Peaking | 7965 Hz | 1.1  | 5.1 dB   |
| Peaking | 7967 Hz | 3.32 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.5 dB  |
| Peaking | 250 Hz   | 1.41 | 4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.4 dB |
| Peaking | 2000 Hz  | 1.41 | -8.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -9.0 dB |
| Peaking | 16000 Hz | 1.41 | 1.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DTX%20300%20p/Beyerdynamic%20DTX%20300%20p.png)