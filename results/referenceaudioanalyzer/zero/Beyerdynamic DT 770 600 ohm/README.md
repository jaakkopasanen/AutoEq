# Beyerdynamic DT 770 600 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.4; 54 -2.1; 60 -2.0; 66 -1.5; 72 -1.3; 79 -1.6; 87 -2.4; 96 -3.3; 106 -3.9; 116 -3.9; 128 -3.8; 141 -3.3; 155 -2.9; 170 -2.9; 187 -2.9; 206 -3.3; 227 -4.5; 249 -6.0; 274 -7.4; 302 -8.3; 332 -8.5; 365 -8.3; 402 -7.9; 442 -7.5; 486 -7.5; 535 -7.4; 588 -7.1; 647 -6.6; 712 -6.1; 783 -5.8; 861 -5.8; 947 -5.7; 1042 -5.4; 1146 -5.1; 1261 -4.9; 1387 -4.6; 1526 -4.2; 1678 -3.8; 1846 -3.5; 2031 -3.5; 2234 -3.9; 2457 -4.4; 2703 -4.4; 2973 -3.3; 3270 -1.6; 3597 -1.6; 3957 -4.2; 4353 -6.8; 4788 -8.5; 5267 -9.6; 5793 -11.2; 6373 -12.8; 7010 -14.1; 7711 -15.8; 8482 -17.4; 9330 -17.8; 10263 -16.8; 11289 -15.4; 12418 -15.2; 13660 -15.4; 15026 -14.1; 16529 -10.9; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 600 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.66 | 6.3 dB   |
| Peaking | 76 Hz    | 1.83 | 3.0 dB   |
| Peaking | 171 Hz   | 2.92 | 3.5 dB   |
| Peaking | 3522 Hz  | 0.73 | 9.7 dB   |
| Peaking | 8611 Hz  | 0.44 | -13.1 dB |
| Peaking | 357 Hz   | 2.14 | -2.6 dB  |
| Peaking | 2299 Hz  | 1.1  | 1.8 dB   |
| Peaking | 2553 Hz  | 3.32 | -3.4 dB  |
| Peaking | 14830 Hz | 2.8  | -2.2 dB  |
| Peaking | 18619 Hz | 0.98 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.3 dB   |
| Peaking | 125 Hz   | 1.41 | 2.9 dB   |
| Peaking | 250 Hz   | 1.41 | 0.3 dB   |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -13.3 dB |
| Peaking | 16000 Hz | 1.41 | -7.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20770%20600%20ohm/Beyerdynamic%20DT%20770%20600%20ohm.png)