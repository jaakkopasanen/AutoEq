# Beyerdynamic DT 831
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.0; 96 -1.8; 106 -2.4; 116 -2.9; 128 -3.3; 141 -3.4; 155 -3.4; 170 -3.1; 187 -2.8; 206 -2.9; 227 -3.2; 249 -3.4; 274 -3.4; 302 -3.5; 332 -3.7; 365 -3.7; 402 -3.6; 442 -3.6; 486 -3.8; 535 -4.0; 588 -4.3; 647 -4.6; 712 -5.0; 783 -5.0; 861 -4.8; 947 -4.7; 1042 -4.8; 1146 -5.1; 1261 -5.5; 1387 -6.0; 1526 -6.3; 1678 -6.5; 1846 -6.9; 2031 -7.7; 2234 -8.9; 2457 -9.9; 2703 -10.5; 2973 -10.1; 3270 -8.9; 3597 -7.5; 3957 -7.8; 4353 -10.9; 4788 -14.8; 5267 -16.7; 5793 -15.7; 6373 -11.5; 7010 -7.6; 7711 -8.5; 8482 -11.1; 9330 -12.8; 10263 -13.2; 11289 -12.9; 12418 -11.7; 13660 -10.1; 15026 -8.6; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 831 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 831 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.34 | 6.3 dB   |
| Peaking | 426 Hz   | 0.42 | 2.3 dB   |
| Peaking | 2609 Hz  | 2.86 | -4.0 dB  |
| Peaking | 5298 Hz  | 3.6  | -10.5 dB |
| Peaking | 10963 Hz | 1.44 | -6.9 dB  |
| Peaking | 79 Hz    | 4.33 | 0.9 dB   |
| Peaking | 125 Hz   | 3.84 | -0.9 dB  |
| Peaking | 3778 Hz  | 7.37 | 2.1 dB   |
| Peaking | 6860 Hz  | 1.48 | -2.4 dB  |
| Peaking | 7251 Hz  | 4.57 | 5.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.1 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20831/Beyerdynamic%20DT%20831.png)