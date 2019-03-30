# Beyerdynamic DT 770 32 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.9; 60 -0.8; 66 -0.6; 72 -0.8; 79 -1.3; 87 -2.0; 96 -3.0; 106 -3.7; 116 -4.0; 128 -4.2; 141 -4.5; 155 -4.4; 170 -4.1; 187 -3.6; 206 -3.5; 227 -4.3; 249 -5.6; 274 -7.0; 302 -7.9; 332 -8.3; 365 -8.1; 402 -7.7; 442 -7.4; 486 -7.4; 535 -7.3; 588 -6.8; 647 -6.2; 712 -5.9; 783 -6.1; 861 -6.4; 947 -6.1; 1042 -5.6; 1146 -5.0; 1261 -4.6; 1387 -4.2; 1526 -3.5; 1678 -3.2; 1846 -3.4; 2031 -4.1; 2234 -5.0; 2457 -5.7; 2703 -5.8; 2973 -4.9; 3270 -3.0; 3597 -1.2; 3957 -1.8; 4353 -4.6; 4788 -7.1; 5267 -9.0; 5793 -10.9; 6373 -12.6; 7010 -14.2; 7711 -16.1; 8482 -17.3; 9330 -16.9; 10263 -15.0; 11289 -13.5; 12418 -12.9; 13660 -12.1; 15026 -10.6; 16529 -8.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 32 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 32 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.33 | 6.1 dB   |
| Peaking | 72 Hz    | 2.4  | 1.5 dB   |
| Peaking | 1657 Hz  | 2.06 | 3.7 dB   |
| Peaking | 3832 Hz  | 2.33 | 8.1 dB   |
| Peaking | 8852 Hz  | 0.76 | -10.7 dB |
| Peaking | 209 Hz   | 2.8  | 2.8 dB   |
| Peaking | 329 Hz   | 1.61 | -2.6 dB  |
| Peaking | 11060 Hz | 3.82 | 1.7 dB   |
| Peaking | 14726 Hz | 1.02 | -1.8 dB  |
| Peaking | 17340 Hz | 1.26 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 4.8 dB   |
| Peaking | 125 Hz   | 1.41 | 1.8 dB   |
| Peaking | 250 Hz   | 1.41 | 0.5 dB   |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -13.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20770%2032%20ohm/Beyerdynamic%20DT%20770%2032%20ohm.png)