# Beyerdynamic DT 770 80 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.7; 25 -7.3; 28 -8.1; 31 -8.9; 34 -9.6; 37 -10.2; 41 -10.9; 45 -11.4; 49 -11.8; 54 -12.1; 60 -12.1; 66 -11.6; 72 -10.6; 79 -9.3; 87 -8.4; 96 -8.3; 106 -8.3; 116 -8.6; 128 -8.8; 141 -8.2; 155 -7.2; 170 -5.6; 187 -3.5; 206 -2.0; 227 -1.9; 249 -2.8; 274 -3.8; 302 -4.6; 332 -5.2; 365 -5.4; 402 -5.5; 442 -5.4; 486 -5.4; 535 -5.4; 588 -5.5; 647 -5.9; 712 -6.3; 783 -6.7; 861 -6.5; 947 -5.9; 1042 -5.7; 1146 -5.7; 1261 -6.0; 1387 -6.5; 1526 -6.6; 1678 -6.3; 1846 -6.7; 2031 -7.4; 2234 -7.9; 2457 -7.5; 2703 -6.4; 2973 -4.8; 3270 -2.4; 3597 -0.5; 3957 -2.8; 4353 -7.6; 4788 -11.1; 5267 -13.0; 5793 -14.9; 6373 -15.8; 7010 -13.8; 7711 -9.2; 8482 -6.4; 9330 -6.4; 10263 -6.5; 11289 -9.0; 12418 -9.3; 13660 -6.7; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 80 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 80 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.86 | -5.5 dB  |
| Peaking | 226 Hz   | 2.3  | 5.3 dB   |
| Peaking | 3622 Hz  | 4.33 | 8.2 dB   |
| Peaking | 5979 Hz  | 2.17 | -10.1 dB |
| Peaking | 21307 Hz | 1.89 | -0.9 dB  |
| Peaking | 17 Hz    | 2    | 1.7 dB   |
| Peaking | 137 Hz   | 5.26 | -1.8 dB  |
| Peaking | 2269 Hz  | 5.55 | -1.7 dB  |
| Peaking | 8737 Hz  | 4.48 | 2.6 dB   |
| Peaking | 12014 Hz | 4.87 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20770%2080%20ohm/Beyerdynamic%20DT%20770%2080%20ohm.png)