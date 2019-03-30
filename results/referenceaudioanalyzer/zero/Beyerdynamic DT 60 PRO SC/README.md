# Beyerdynamic DT 60 PRO SC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.8; 28 -8.2; 31 -8.6; 34 -8.9; 37 -9.2; 41 -9.4; 45 -9.6; 49 -9.7; 54 -9.8; 60 -10.0; 66 -10.1; 72 -10.1; 79 -10.1; 87 -10.1; 96 -10.1; 106 -10.1; 116 -10.1; 128 -9.8; 141 -9.8; 155 -9.6; 170 -9.5; 187 -9.2; 206 -9.1; 227 -8.8; 249 -8.5; 274 -8.2; 302 -7.9; 332 -7.6; 365 -7.3; 402 -6.9; 442 -6.4; 486 -6.1; 535 -5.6; 588 -5.2; 647 -4.7; 712 -4.5; 783 -4.3; 861 -4.1; 947 -3.9; 1042 -3.6; 1146 -3.6; 1261 -3.6; 1387 -3.8; 1526 -4.2; 1678 -4.9; 1846 -5.8; 2031 -7.1; 2234 -8.9; 2457 -10.8; 2703 -12.3; 2973 -12.7; 3270 -12.3; 3597 -11.8; 3957 -11.3; 4353 -10.6; 4788 -8.9; 5267 -5.6; 5793 -1.2; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 60 PRO SC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 60 PRO SC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 92 Hz    | 0.3  | -4.3 dB  |
| Peaking | 1579 Hz  | 0.58 | 6.2 dB   |
| Peaking | 3021 Hz  | 0.83 | -10.8 dB |
| Peaking | 6150 Hz  | 3.3  | 9.1 dB   |
| Peaking | 15 Hz    | 1.4  | 1.0 dB   |
| Peaking | 2686 Hz  | 3.72 | -1.3 dB  |
| Peaking | 3153 Hz  | 1.44 | 1.0 dB   |
| Peaking | 4456 Hz  | 4.95 | -1.2 dB  |
| Peaking | 11314 Hz | 1.8  | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%2060%20PRO%20SC/Beyerdynamic%20DT%2060%20PRO%20SC.png)