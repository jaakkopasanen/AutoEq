# Beyerdynamic DT 150 250 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.7; 45 -2.5; 49 -3.0; 54 -3.5; 60 -4.3; 66 -4.9; 72 -5.3; 79 -5.9; 87 -6.7; 96 -7.5; 106 -8.1; 116 -8.3; 128 -8.6; 141 -8.5; 155 -8.3; 170 -8.0; 187 -7.9; 206 -7.9; 227 -7.6; 249 -7.0; 274 -6.0; 302 -4.8; 332 -3.8; 365 -3.1; 402 -3.0; 442 -3.5; 486 -4.3; 535 -5.2; 588 -5.8; 647 -6.1; 712 -6.3; 783 -6.1; 861 -5.9; 947 -5.6; 1042 -5.2; 1146 -4.8; 1261 -4.4; 1387 -4.1; 1526 -4.0; 1678 -4.1; 1846 -4.4; 2031 -4.6; 2234 -4.9; 2457 -5.1; 2703 -4.6; 2973 -3.6; 3270 -4.2; 3597 -7.4; 3957 -11.3; 4353 -13.5; 4788 -13.6; 5267 -11.8; 5793 -8.7; 6373 -5.1; 7010 -4.3; 7711 -6.3; 8482 -9.2; 9330 -12.3; 10263 -13.8; 11289 -13.3; 12418 -11.2; 13660 -9.0; 15026 -7.9; 16529 -7.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 150 250 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 150 250 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 1.25 | 7.0 dB   |
| Peaking | 393 Hz   | 3.41 | 3.8 dB   |
| Peaking | 4706 Hz  | 1.82 | -16.2 dB |
| Peaking | 6911 Hz  | 0.47 | 16.2 dB  |
| Peaking | 10121 Hz | 0.9  | -18.4 dB |
| Peaking | 55 Hz    | 1.67 | 1.5 dB   |
| Peaking | 132 Hz   | 1.21 | -2.6 dB  |
| Peaking | 2521 Hz  | 3.11 | -2.5 dB  |
| Peaking | 3107 Hz  | 1.96 | 3.1 dB   |
| Peaking | 3900 Hz  | 5.3  | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20150%20250%20ohm/Beyerdynamic%20DT%20150%20250%20ohm.png)