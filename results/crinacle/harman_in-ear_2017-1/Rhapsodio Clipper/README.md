# Rhapsodio Clipper
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.1; 25 -11.3; 28 -11.6; 31 -11.7; 34 -11.9; 37 -12.0; 41 -12.1; 45 -12.2; 49 -12.3; 54 -12.4; 60 -12.5; 66 -12.6; 72 -12.7; 79 -12.8; 87 -13.0; 96 -13.2; 106 -13.3; 116 -13.3; 128 -13.3; 141 -13.2; 155 -13.1; 170 -12.8; 187 -12.5; 206 -12.1; 227 -11.7; 249 -11.2; 274 -10.7; 302 -10.0; 332 -9.3; 365 -8.6; 402 -7.9; 442 -7.3; 486 -6.6; 535 -5.9; 588 -5.3; 647 -4.5; 712 -3.8; 783 -3.2; 861 -2.5; 947 -1.8; 1042 -1.8; 1146 -2.7; 1261 -3.0; 1387 -3.1; 1526 -2.8; 1678 -2.6; 1846 -2.5; 2031 -2.6; 2234 -2.8; 2457 -3.6; 2703 -4.5; 2973 -4.6; 3270 -3.9; 3597 -3.7; 3957 -4.4; 4353 -7.1; 4788 -10.8; 5267 -8.0; 5793 -2.3; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -7.6; 15026 -10.8; 16529 -15.7; 18182 -18.2; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rhapsodio Clipper GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rhapsodio Clipper ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.44 | -6.0 dB  |
| Peaking | 130 Hz   | 1.12 | -4.8 dB  |
| Peaking | 239 Hz   | 1.95 | -3.5 dB  |
| Peaking | 6381 Hz  | 6.14 | 6.5 dB   |
| Peaking | 18021 Hz | 1.28 | -13.8 dB |
| Peaking | 942 Hz   | 1.91 | 4.0 dB   |
| Peaking | 1894 Hz  | 1.48 | 3.2 dB   |
| Peaking | 3671 Hz  | 3.57 | 2.0 dB   |
| Peaking | 4825 Hz  | 6.75 | -6.5 dB  |
| Peaking | 12243 Hz | 3.08 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Rhapsodio%20Clipper/Rhapsodio%20Clipper.png)