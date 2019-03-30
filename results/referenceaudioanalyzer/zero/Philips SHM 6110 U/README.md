# Philips SHM 6110 U
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -2.1; 72 -2.9; 79 -3.7; 87 -4.3; 96 -4.8; 106 -5.1; 116 -5.3; 128 -5.4; 141 -5.4; 155 -5.2; 170 -5.1; 187 -4.9; 206 -4.7; 227 -4.5; 249 -4.2; 274 -4.0; 302 -3.8; 332 -3.8; 365 -3.8; 402 -3.5; 442 -3.2; 486 -3.1; 535 -3.0; 588 -2.8; 647 -2.8; 712 -2.5; 783 -2.4; 861 -2.0; 947 -1.7; 1042 -1.3; 1146 -1.0; 1261 -1.8; 1387 -5.2; 1526 -10.0; 1678 -13.6; 1846 -15.3; 2031 -15.5; 2234 -15.5; 2457 -16.2; 2703 -17.0; 2973 -16.7; 3270 -15.2; 3597 -13.3; 3957 -11.1; 4353 -8.9; 4788 -7.3; 5267 -6.2; 5793 -5.0; 6373 -3.8; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.2; 11289 -7.8; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHM 6110 U GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHM 6110 U ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.65 | 6.7 dB   |
| Peaking | 1134 Hz  | 0.52 | 21.0 dB  |
| Peaking | 2081 Hz  | 0.44 | -24.2 dB |
| Peaking | 6034 Hz  | 1.27 | 9.0 dB   |
| Peaking | 12544 Hz | 0.54 | 1.3 dB   |
| Peaking | 58 Hz    | 5.65 | 1.6 dB   |
| Peaking | 1318 Hz  | 3.59 | 4.7 dB   |
| Peaking | 1603 Hz  | 1.41 | -6.3 dB  |
| Peaking | 2264 Hz  | 1.2  | 6.0 dB   |
| Peaking | 2891 Hz  | 2.61 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 3.8 dB   |
| Peaking | 125 Hz   | 1.41 | -0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 1.9 dB   |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -11.9 dB |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHM%206110%20U/Philips%20SHM%206110%20U.png)