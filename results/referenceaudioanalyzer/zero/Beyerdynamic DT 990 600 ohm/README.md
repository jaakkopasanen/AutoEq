# Beyerdynamic DT 990 600 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -2.0; 34 -2.7; 37 -3.3; 41 -3.9; 45 -4.5; 49 -5.0; 54 -5.5; 60 -6.0; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.6; 96 -8.2; 106 -8.6; 116 -8.7; 128 -8.7; 141 -8.5; 155 -8.2; 170 -8.0; 187 -7.7; 206 -7.5; 227 -7.2; 249 -6.9; 274 -6.5; 302 -6.1; 332 -5.6; 365 -5.1; 402 -4.6; 442 -3.9; 486 -3.2; 535 -2.7; 588 -2.4; 647 -2.0; 712 -1.9; 783 -2.1; 861 -2.7; 947 -3.4; 1042 -4.1; 1146 -4.6; 1261 -4.9; 1387 -4.9; 1526 -4.8; 1678 -4.5; 1846 -4.2; 2031 -3.9; 2234 -3.8; 2457 -3.5; 2703 -3.5; 2973 -3.8; 3270 -4.7; 3597 -5.9; 3957 -6.5; 4353 -6.2; 4788 -6.5; 5267 -9.4; 5793 -11.5; 6373 -11.6; 7010 -12.5; 7711 -15.8; 8482 -18.1; 9330 -17.9; 10263 -16.4; 11289 -15.6; 12418 -15.5; 13660 -14.9; 15026 -13.1; 16529 -10.1; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 600 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 600 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.79 | 6.2 dB   |
| Peaking | 124 Hz   | 0.88 | -2.7 dB  |
| Peaking | 634 Hz   | 1.2  | 4.5 dB   |
| Peaking | 3771 Hz  | 0.56 | 5.9 dB   |
| Peaking | 9216 Hz  | 0.57 | -13.1 dB |
| Peaking | 3688 Hz  | 1.92 | 1.5 dB   |
| Peaking | 3701 Hz  | 4.26 | -2.8 dB  |
| Peaking | 14628 Hz | 2.1  | -2.4 dB  |
| Peaking | 17591 Hz | 0.43 | 1.0 dB   |
| Peaking | 18255 Hz | 2.38 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -12.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20990%20600%20ohm/Beyerdynamic%20DT%20990%20600%20ohm.png)