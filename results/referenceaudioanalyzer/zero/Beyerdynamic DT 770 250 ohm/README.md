# Beyerdynamic DT 770 250 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.3; 25 -14.5; 28 -14.7; 31 -14.8; 34 -14.8; 37 -14.8; 41 -14.7; 45 -14.4; 49 -14.0; 54 -13.1; 60 -11.8; 66 -10.4; 72 -9.1; 79 -7.7; 87 -7.6; 96 -9.0; 106 -10.5; 116 -11.1; 128 -10.8; 141 -10.0; 155 -8.7; 170 -6.8; 187 -4.2; 206 -1.8; 227 -0.6; 249 -0.8; 274 -1.8; 302 -2.9; 332 -3.6; 365 -4.0; 402 -4.1; 442 -4.3; 486 -4.2; 535 -4.1; 588 -4.4; 647 -4.8; 712 -5.4; 783 -5.6; 861 -5.1; 947 -4.7; 1042 -4.7; 1146 -4.7; 1261 -4.7; 1387 -4.6; 1526 -4.4; 1678 -4.4; 1846 -4.5; 2031 -5.1; 2234 -5.3; 2457 -4.8; 2703 -4.0; 2973 -2.9; 3270 -1.6; 3597 -0.5; 3957 -1.4; 4353 -4.6; 4788 -7.6; 5267 -10.6; 5793 -14.4; 6373 -15.9; 7010 -13.2; 7711 -8.3; 8482 -6.0; 9330 -6.6; 10263 -8.4; 11289 -10.7; 12418 -11.7; 13660 -9.4; 15026 -5.9; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.69 | -10.0 dB |
| Peaking | 142 Hz   | 1.63 | -8.4 dB  |
| Peaking | 208 Hz   | 1    | 7.6 dB   |
| Peaking | 6327 Hz  | 3.89 | -11.6 dB |
| Peaking | 20851 Hz | 2.02 | -3.8 dB  |
| Peaking | 82 Hz    | 7.73 | 2.3 dB   |
| Peaking | 1462 Hz  | 2.12 | 1.0 dB   |
| Peaking | 3647 Hz  | 2.6  | 6.1 dB   |
| Peaking | 5294 Hz  | 4.51 | -2.9 dB  |
| Peaking | 12249 Hz | 2.79 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | 5.7 dB   |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -6.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20770%20250%20ohm/Beyerdynamic%20DT%20770%20250%20ohm.png)