# Beyerdynamic T1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.6; 31 -2.2; 34 -2.6; 37 -3.0; 41 -3.4; 45 -3.8; 49 -4.2; 54 -4.6; 60 -4.9; 66 -5.2; 72 -5.4; 79 -5.9; 87 -6.3; 96 -6.5; 106 -6.4; 116 -6.2; 128 -6.3; 141 -6.5; 155 -6.3; 170 -6.2; 187 -6.4; 206 -6.5; 227 -6.4; 249 -6.2; 274 -6.2; 302 -6.2; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.4; 486 -4.9; 535 -4.9; 588 -4.9; 647 -4.7; 712 -4.4; 783 -4.2; 861 -4.0; 947 -3.6; 1042 -4.0; 1146 -4.5; 1261 -4.4; 1387 -3.7; 1526 -2.5; 1678 -2.0; 1846 -2.9; 2031 -3.6; 2234 -3.4; 2457 -2.7; 2703 -3.3; 2973 -4.7; 3270 -6.0; 3597 -7.0; 3957 -8.0; 4353 -8.5; 4788 -8.1; 5267 -7.5; 5793 -10.8; 6373 -14.4; 7010 -14.9; 7711 -15.6; 8482 -16.5; 9330 -16.4; 10263 -15.0; 11289 -12.4; 12418 -8.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.81 | 5.8 dB   |
| Peaking | 762 Hz   | 1.02 | 1.8 dB   |
| Peaking | 2052 Hz  | 1.03 | 4.2 dB   |
| Peaking | 5264 Hz  | 7.08 | 2.9 dB   |
| Peaking | 8175 Hz  | 1.11 | -10.8 dB |
| Peaking | 2088 Hz  | 7.76 | -1.3 dB  |
| Peaking | 2600 Hz  | 5.27 | 1.3 dB   |
| Peaking | 8142 Hz  | 3.16 | 2.9 dB   |
| Peaking | 10652 Hz | 1.01 | -4.5 dB  |
| Peaking | 13103 Hz | 1.31 | 5.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | 0.3 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20T1/Beyerdynamic%20T1.png)