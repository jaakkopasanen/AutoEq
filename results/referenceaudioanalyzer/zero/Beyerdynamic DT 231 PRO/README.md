# Beyerdynamic DT 231 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.6; 37 -2.5; 41 -3.6; 45 -4.5; 49 -5.4; 54 -6.3; 60 -7.1; 66 -7.4; 72 -7.4; 79 -7.6; 87 -8.0; 96 -8.4; 106 -8.7; 116 -9.0; 128 -9.1; 141 -8.9; 155 -8.7; 170 -8.1; 187 -7.3; 206 -6.3; 227 -5.7; 249 -5.7; 274 -6.3; 302 -6.8; 332 -7.1; 365 -7.1; 402 -7.2; 442 -7.4; 486 -7.6; 535 -7.5; 588 -7.4; 647 -7.1; 712 -6.6; 783 -6.3; 861 -6.1; 947 -5.8; 1042 -5.4; 1146 -4.9; 1261 -4.0; 1387 -3.3; 1526 -4.8; 1678 -6.7; 1846 -7.2; 2031 -6.2; 2234 -4.4; 2457 -2.9; 2703 -2.4; 2973 -2.6; 3270 -2.5; 3597 -1.6; 3957 -0.8; 4353 -5.4; 4788 -10.4; 5267 -11.8; 5793 -10.5; 6373 -8.5; 7010 -7.7; 7711 -7.9; 8482 -8.0; 9330 -8.0; 10263 -8.5; 11289 -10.0; 12418 -11.2; 13660 -11.0; 15026 -9.1; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 231 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 231 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.89 | 7.0 dB  |
| Peaking | 2888 Hz  | 1.7  | 4.0 dB  |
| Peaking | 3963 Hz  | 4.06 | 6.7 dB  |
| Peaking | 5075 Hz  | 2.6  | -7.1 dB |
| Peaking | 12873 Hz | 1.66 | -5.1 dB |
| Peaking | 10 Hz    | 0.57 | 2.6 dB  |
| Peaking | 113 Hz   | 1.44 | -2.9 dB |
| Peaking | 524 Hz   | 2.35 | -1.3 dB |
| Peaking | 1408 Hz  | 2.21 | 3.4 dB  |
| Peaking | 1794 Hz  | 3.63 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20231%20PRO/Beyerdynamic%20DT%20231%20PRO.png)